from typing import List
from app.entity.http_request import HttpRequest
from app.entity.http_request_log import HttpRequestLog
from app.lib.stat import average
from app.lib.url import Url


def _get_key(masked_url, method):
    return masked_url + method


class HttpRequestMetric:

    def __init__(self):
        self.min_reducer = ResponseTimeReducer(min)
        self.max_reducer = ResponseTimeReducer(max)
        self.average_reducer = ResponseTimeReducer(average)
        self.frequency_reducer = ResponseTimeReducer(len)

    def get_requests(self, logs: List[HttpRequestLog]) -> List[HttpRequest]:
        requests: dict = {}
        for log in logs:
            masked_url = Url.mask_path_param(log.body.url)
            method = log.body.method
            key = _get_key(masked_url, method)
            if requests.get(key) is None:
                requests[key] = HttpRequest(
                    masked_url, method, 0, 0, 0, 0, []
                )
            requests[key].logs.append(log)
        for _, value in requests.items():
            value.min_time = self.min_reducer.reduce(value.logs)
            value.max_time = self.max_reducer.reduce(value.logs)
            value.average_time = self.average_reducer.reduce(value.logs)
            value.frequency = self.frequency_reducer.reduce(value.logs)
        return list(requests.values())


class ResponseTimeReducer:
    def __init__(self, fun):
        self.fun = fun

    def reduce(self, logs: List[HttpRequestLog]):
        return self.fun([log.body.response_time for log in logs])
