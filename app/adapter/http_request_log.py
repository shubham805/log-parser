import random

from app.entity.http_request_log import HttpRequestLog, HttpRequestLogBody


class HttpRequestLogAdapter:
    @classmethod
    def get_log(cls, log: dict) -> HttpRequestLog:
        return HttpRequestLog(
            random.randint(1, 1000),
            HttpRequestLogBody(
                log['timestamp'], log['url'], log['method'],
                log['response_code'], log['response_time']
            )
        )
