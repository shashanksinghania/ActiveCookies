import unittest
from most_active_cookie import CookieTracker


class Tester(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_date_DNE(self):
        """
        Test with a date that does not exist in the logs
        """
        cookie_processor = CookieTracker()
        cookie_processor.process_data("cookie_log.csv")
        computed_cookies = cookie_processor.find_most_active_cookie_by_date("2022-01-28")
        self.assertEqual(set(), computed_cookies)

    def test_valid_date_single_cookie(self):
        """
        A simple test where the maximum occurrence cookies occur on the query date
        :return: void
        """
        cookie_processor = CookieTracker()
        cookie_processor.process_data("cookie_log.csv")
        computed_cookies = cookie_processor.find_most_active_cookie_by_date("2018-12-09")
        self.assertEqual(set(['AtY0laUfhglK3lC7']), computed_cookies)

    def test_multiple_cookies(self):
        """
        A test where the maximum occurrence cookies occur likely on different dates
        :return: void
        """
        cookie_processor = CookieTracker()
        cookie_processor.process_data("cookie_log.csv")
        computed_cookies = cookie_processor.find_most_active_cookie_by_date("2018-12-08")
        self.assertEqual(set(['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']), computed_cookies)


if __name__ == '__main__':
    unittest.main()