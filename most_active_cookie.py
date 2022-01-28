import argparse
import csv


class CookieTracker:
    def __init__(self):
        """
        Initializes the CookieTracker object.
        """
        self.cookies_by_date_dict = {}


    def process_data(self, log_file):
        """
        The function reads and processes the data from the cookie log file.

        Pramams:
            log_file: the path to the log file

        """
        with open(log_file, 'r') as cookie_log:
            log = csv.DictReader(cookie_log)
            for row in log:
                cookie, timestamp = row['cookie'], row['timestamp']
                date = timestamp.split("T")[0]
                
                # update the cookies dictionary
                if date not in self.cookies_by_date_dict:
                    self.cookies_by_date_dict[date] = {cookie: 1}
                else:
                    self.cookies_by_date_dict[date][cookie] = self.cookies_by_date_dict[date].get(cookie, 0) + 1

    
    def find_most_active_cookie_by_date(self, date):
        """
        Finds the most active cookies for a specified date from the preprocessed data.

        Params:
            date: the date to find the most active cookies for

        Returns:
            most_active_cookies: set of most active cookies
        """
        most_active_cookies = set()
        if date in self.cookies_by_date_dict:
            max_occurrence = max(self.cookies_by_date_dict[date].values())
            for cookie, occurrence in self.cookies_by_date_dict[date].items():
                if occurrence == max_occurrence:
                    print(cookie)
                    most_active_cookies.add(cookie)
        return most_active_cookies


if __name__ == '__main__':
    # Process the Command Line Input
    parser = argparse.ArgumentParser(prog='most_active_cookie.py', description='Program to find the most active cookies on a particular date')
    parser.add_argument("file_name", help="Name of the cookie log file")
    parser.add_argument("--date", "-d", required=True, help="Date to find the most active cookie for")
    args = parser.parse_args()
    
    # Process the data and find the most active cookie
    cookie_processsor = CookieTracker()
    cookie_processsor.process_data(args.file_name)
    cookie_processsor.find_most_active_cookie_by_date(args.date)
