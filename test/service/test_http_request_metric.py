import unittest

from app.entity.http_request_log import HttpRequestLog, HttpRequestLogBody
from app.service.http_request_metric import HttpRequestMetric


class HttpRequestMetricTest(unittest.TestCase):
    def setUp(self) -> None:
        self.metric = HttpRequestMetric()

    def test_get(self):
        logs = [
            HttpRequestLog(
                1, HttpRequestLogBody(
                    12, "/books/1/pages/2", 'PUT', 201, 214
                )
            ),
            HttpRequestLog(
                2, HttpRequestLogBody(
                    12, "/books/2/pages/3", 'PUT', 201, 124
                )
            ),
            HttpRequestLog(
                9, HttpRequestLogBody(
                    12, "/books/4/pages/4", 'PUT', 201, 169
                )
            ),
            HttpRequestLog(
                3, HttpRequestLogBody(
                    12, "/books/1/pages/2", 'GET', 200, 214
                )
            ),
            HttpRequestLog(
                4, HttpRequestLogBody(
                    12, "/books/2/pages/3", 'GET', 200, 212
                )
            ),
            HttpRequestLog(
                5, HttpRequestLogBody(
                    12, "/books/2", 'GET', 200, 212
                )
            ),
            HttpRequestLog(
                6, HttpRequestLogBody(
                    12, "/books/3", 'GET', 200, 434
                )
            ),
            HttpRequestLog(
                7, HttpRequestLogBody(
                    12, "/books/2", 'PUT', 201, 245
                )
            ),
            HttpRequestLog(
                8, HttpRequestLogBody(
                    12, "/books/3", 'PUT', 201, 145
                )
            ),
            HttpRequestLog(
                10, HttpRequestLogBody(
                    12, "/books", 'GET', 201, 145
                )
            )
        ]
        requests = self.metric.get_requests(logs)
        self.assertEqual(len(requests), 5)
