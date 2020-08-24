import re


class Url:
    @staticmethod
    def mask_path_param(url: str) -> str:
        return re.sub("\d+", "{id}", url)
