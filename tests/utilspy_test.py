import unittest

from ..docsumo import Docsumo


class Testutils(unittest.TestCase):
    def test_page_soup(self):
        r = Docsumo().limit
        print(r)
        self.assertGreater(len(r.keys()), 2)


if __name__ == "__main__":
    unittest.main()
