import csv
from marshmallow import Schema, fields, validate
from app.adapter.http_request_log import HttpRequestLogAdapter
from app.lib.csv_writer import CsvWriter
from app.service.http_request_metric import HttpRequestMetric


class OrderedSchema(Schema):
    class Meta:
        ordered = True


class Log(Schema):
    timestamp = fields.Integer(required=True)
    url = fields.String(required=True)
    method = fields.String(
        required=True, validate=validate.OneOf(["PUT", "POST", "GET", "DELETE"])
    )
    response_code = fields.Integer(required=True)
    response_time = fields.Integer(required=True)


class Request(OrderedSchema):
    method = fields.String(
        required=True, validate=validate.OneOf(["PUT", "POST", "GET", "DELETE"])
    )
    url = fields.String(required=True)
    min_time = fields.Integer(required=True)
    max_time = fields.Integer(required=True)
    average_time = fields.Float(required=True)


class TopRequest(OrderedSchema):
    url = fields.String(required=True)
    method = fields.String(
        required=True, validate=validate.OneOf(["PUT", "POST", "GET", "DELETE"])
    )
    frequency = fields.Integer(required=True)


class Controller:
    def __init__(self):
        self.http_request_metric = HttpRequestMetric()
        self.csv_writer = CsvWriter()

    def _get_requests(self):
        logs = Log(many=True).load(list(csv.DictReader(open("log.csv"))))
        logs = [HttpRequestLogAdapter.get_log(log) for log in logs]
        return self.http_request_metric.get_requests(logs)

    def get_all_requests(self):
        requests = self._get_requests()
        requests = Request(many=True).dump(vars(request) for request in requests)
        self.csv_writer.write(requests)

    def get_top_requests(self):
        limit = 5
        requests = self._get_requests()
        requests.sort(reverse=True, key=lambda request: request.frequency)
        requests = requests[0:limit]
        requests = TopRequest(many=True).dump(vars(request) for request in requests)
        self.csv_writer.write(requests)


Controller().get_top_requests()
print()
Controller().get_all_requests()
