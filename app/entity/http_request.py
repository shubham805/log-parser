from typing import List

from app.entity.http_request_log import HttpRequestLog


class HttpRequest(object):
    def __init__(self, url: str, method: str, frequency: int,
                 min_time: int, max_time: int, average_time: float,
                 logs: List[HttpRequestLog]):
        self.url = url
        self.method = method.upper()
        self.frequency = frequency
        self.min_time = min_time
        self.max_time = max_time
        self.average_time = average_time
        if logs is None:
            logs = []
        self.logs = logs
