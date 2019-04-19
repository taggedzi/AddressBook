#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.Address import Address


def test_init_address_pass():
    Address()


def assert_name_value(set_=None, expected=None):
    test = Address()
    test.name = set_
    assert test.name == expected


def test_name_empty():
    assert_name_value('', '')


def test_name_none():
    assert_name_value(None, '')


def test_name_value():
    assert_name_value('random_string', 'random_string')


def assert_street_value(set_=None, expected=None):
    test = Address()
    test.street = set_
    assert test.street == expected


def test_street_empty():
    assert_street_value(None, '')


def test_street_none():
    assert_street_value('', '')


def test_street_value():
    assert_street_value('random_string', 'random_string')


def assert_street2_value(set_=None, expected=None):
    test = Address()
    test.street2 = set_
    assert test.street2 == expected


def test_street2_empty():
    assert_street2_value(None, '')


def test_street2_none():
    assert_street2_value('', '')


def test_street2_value():
    assert_street2_value('random_string', 'random_string')


def assert_city_value(set_=None, expected=None):
    test = Address()
    test.city = set_
    assert test.city == expected


def test_city_empty():
    assert_city_value(None, '')


def test_city_none():
    assert_city_value('', '')


def test_city_value():
    assert_city_value('random_string', 'random_string')


def assert_state_value(set_=None, expected=None):
    test = Address()
    test.state = set_
    assert test.state == expected


def test_state_empty():
    assert_state_value(None, '')


def test_state_none():
    assert_state_value('', '')


def test_state_value():
    assert_state_value('random_string', 'random_string')


def assert_zip_code_value(set_=None, expected=None):
    test = Address()
    test.zip_code = set_
    assert test.zip_code == expected


def test_zip_code_empty():
    assert_zip_code_value(None, '')


def test_zip_code_none():
    assert_zip_code_value('', '')


def test_zip_code_value():
    assert_zip_code_value('random_string', 'random_string')


def test_export_json_str():
    test = Address()
    test.name = "Test"
    test.street = "Street"
    test.street2 = "Street2"
    test.city = "City"
    test.state = "State"
    test.zip_code = "Zip_Code"
    result = test.export_json_str()
    expected = '{"name": "Test", "street": "Street", "street2": "Street2", "city": "City", "state": "State", ' \
               '"zip_code": "Zip_Code"}'
    assert result == expected


def test_export_json_str_fail():
    test = Address()
    test.name = "Test1"
    test.street = "Street"
    test.street2 = "Street2"
    test.city = "City"
    test.state = "State"
    test.zip_code = "Zip_Code"
    result = test.export_json_str()
    expected = '{"name": "Test", "street": "Street", "street2": "Street2", "city": "City", "state": "State", ' \
               '"zip_code": "Zip_Code"}'
    assert result != expected


def test_import_json_str():
    sample = '{"name": "Test", "street": "Street", "street2": "Street2", "city": "City", "state": "State", ' \
             '"zip_code": "Zip_Code"}'
    test = Address()
    test.import_json_str(sample)
    expected = Address()
    expected.name = "Test"
    expected.street = "Street"
    expected.street2 = "Street2"
    expected.city = "City"
    expected.state = "State"
    expected.zip_code = "Zip_Code"
    assert test == expected


def test_eq():
    sample = '{"name": "Test", "street": "Street", "street2": "Street2", "city": "City", "state": "State", ' \
             '"zip_code": "Zip_Code"}'
    test = Address()
    test.import_json_str(sample)
    expected = Address()
    expected.name = "Test"
    expected.street = "Street"
    expected.street2 = "Street2"
    expected.city = "City"
    expected.state = "State"
    expected.zip_code = "Zip_Code"
    assert test == expected


def test_ne():
    sample = '{"name": "Test1", "street": "Street", "street2": "Street2", "city": "City", "state": "State", ' \
             '"zip_code": "Zip_Code"}'
    test = Address()
    test.import_json_str(sample)
    expected = Address()
    expected.name = "Test"
    expected.street = "Street"
    expected.street2 = "Street2"
    expected.city = "City"
    expected.state = "State"
    expected.zip_code = "Zip_Code"
    assert test != expected
