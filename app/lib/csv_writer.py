from typing import List


class CsvWriter:
    def _write_header(self, dict_row: dict):
        row = ""
        for key, value in dict_row.items():
            row = row + "{:<25}".format(key)
        print(row)

    def _write_row(self, dict_row: dict):
        row = ""
        for key, value in dict_row.items():
            row = row + "{:<25}".format(value)
        print(row)

    def write(self, data: List[dict]) -> None:
        if len(data) == 0:
            return
        self._write_header(data[0])
        for row in data:
            self._write_row(row)
