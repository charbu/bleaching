from gcbd_sentinel.gcbd_reader import GCBD_iterator
from unittest.mock import MagicMock
from datetime import datetime


def test_extract_from_row():
    row = (999531, 2016.0, 6.0, 15.0, 17.80506667, -77.0046)
    expected_date = datetime(2016, 6, 15)
    expected_coordinates = [17.80506667, -77.0046]
    gcbd_iter = GCBD_iterator("")
    gcbd_iter.conn = MagicMock()
    gcbd_iter.conn.execute = MagicMock(return_value=[row] * 5)

    for date, coordinate in gcbd_iter():
        assert date == expected_date
        assert coordinate == expected_coordinates
