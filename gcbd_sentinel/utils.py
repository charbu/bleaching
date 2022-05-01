from datetime import datetime


def extract_from_row(row):
    date_str = "{}/{:02d}/{:02d}".format(int(row[1]), int(row[2]), int(row[3]))
    date = datetime.strptime(date_str, "%Y/%m/%d")
    coordinate = (row[4], row[5])
    return date, coordinate
