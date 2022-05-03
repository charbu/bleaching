import sqlite3
from datetime import datetime


class GCBD_iterator(object):
    def __init__(self, sqlite_file):
        self.conn = sqlite3.connect(sqlite_file)

    def __call__(self):
        cursor = self.conn.execute(self.request)
        for row in cursor:
            yield self.extract_from_row(row)

    def extract_from_row(self, row):
        date_str = "{}/{:02d}/{:02d}".format(int(row[1]), int(row[2]), int(row[3]))
        date = datetime.strptime(date_str, "%Y/%m/%d")
        coordinate = [row[4], row[5]]
        return date, coordinate

    @property
    def request(self):
        return """
            SELECT
                site.Site_ID, Date_year, Date_month, Date_day, Latitude_Degrees, Longitude_Degrees
            FROM Sample_Event_tbl as sample
            INNER JOIN Site_Info_tbl site
            ON sample.Site_ID = site.Site_ID
            WHERE Date_year >= 2016
        """
