from gcdb_sentinel.utils import extract_from_row


def test_extract_from_row():
    row = (999531, 2016.0, 6.0, 15.0, 17.80506667, -77.0046)
    expected_date = datetime(2016, 6, 15)
    expected_coordinates = [17.80506667, -77.0046]

    date, coordinate = extract_from_row(row)
    assert date == expected_date
    assert coordinate == expected_coordinates
