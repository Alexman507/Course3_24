from utils import body_payment_data
from utils import filter_date
from utils import format_date
from utils import get_data
from utils import hide_data_payment
from utils import slice_payment_data
from utils import sorted_date


def test_get_data():
    data = get_data()
    assert len(data) > 0
    assert len(data) == 101
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_filter_date():
    data = filter_date()
    assert len(data) > 0
    assert len(data) == 85
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_sorted_date():
    data = sorted_date()
    assert len(data) > 0
    assert len(data) == 85
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_format_date():
    data = format_date()
    assert len(data) > 0
    assert len(data) == 85
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_hide_data_payment():
    data = hide_data_payment()
    assert len(data) > 0
    assert len(data) == 85
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_slice_payment_data():
    data = slice_payment_data()
    assert len(data) > 0
    assert len(data) == 5
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str


def test_body_payment_data():
    data = body_payment_data()
    assert len(data) > 0
    assert len(data) == 5
    assert type(data) == list
    assert type(data[0]) == dict
    assert type(data[0].get('date')) == str
