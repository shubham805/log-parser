from app.entity.entity import Entity


class LogBody(object):
    def __init__(self, timestamp: int):
        self.timestamp = timestamp


class Log(Entity):
    def __init__(self, log_id: int, body: LogBody):
        super(Log, self).__init__(log_id)
        self.body = body
