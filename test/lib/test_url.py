import unittest

from app.lib.url import Url


class UrlTest(unittest.TestCase):
    def test_mask_path_param(self):
        self.assertEqual(
            Url.mask_path_param("/books/1/page/10"),
            "/books/{id}/page/{id}"
        )