from typing import List

from app.entity.log import LogBody, Log


class HttpRequestLogBody(LogBody):
    def __init__(self, timestamp: int, url: str, method: str, code: int, response_time: int):
        super(HttpRequestLogBody, self).__init__(timestamp)
        self.url = url
        self.method = method
        self.code = code
        self.response_time = response_time


class HttpRequestLog(Log):
    def __init__(self, log_id: int, body: HttpRequestLogBody):
        super(HttpRequestLog, self).__init__(log_id, body)
