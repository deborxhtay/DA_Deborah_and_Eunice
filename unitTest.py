import unittest
from main import EuropeStatistics


class EuropeTest(unittest.TestCase):
    def test_something(self):
        visitors = EuropeStatistics()
        result = EuropeStatistics.TotalVisitorUnitedKingdom(visitors)
        self.assertEqual(result, 116984)


