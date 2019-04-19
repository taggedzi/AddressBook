#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from src.Address import Address

SAMPLE_NAME = "Name"
SAMPLE_STREET = "Street"
SAMPLE_STREET2 = "Street2"
SAMPLE_CITY = "City"
SAMPLE_STATE = "Stage"
STATE_ZIP_CODE = "Zip_Code"


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


def build_json(name="Test", street="Street", street2="Street2", city="City", state="State", zip_code="Zip_Code"):
    return json.dumps({
        "name": name,
        "street": street,
        "street2": street2,
        "city": city,
        "state": state,
        "zip_code": zip_code
    })


def build_object(name="Test", street="Street", street2="Street2", city="City", state="State", zip_code="Zip_Code"):
    output = Address()
    output.name = name
    output.street = street
    output.street2 = street2
    output.city = city
    output.state = state
    output.zip_code = zip_code
    return output


def test_export_json_str():
    test = build_object()
    assert test.export_json_str() == build_json()


def test_export_json_str_name_fail():
    test = build_object()
    test.name = "Different"
    assert test.export_json_str() != build_json()


def test_export_json_str_street_fail():
    test = build_object()
    test.street = "Different"
    assert test.export_json_str() != build_json()


def test_export_json_str_street2_fail():
    test = build_object()
    test.street2 = "Different"
    assert test.export_json_str() != build_json()


def test_export_json_str_city_fail():
    test = build_object()
    test.city = "Different"
    assert test.export_json_str() != build_json()


def test_export_json_str_state_fail():
    test = build_object()
    test.state = "Different"
    assert test.export_json_str() != build_json()


def test_export_json_str_zip_code_fail():
    test = build_object()
    test.zip_code = "Different"
    assert test.export_json_str() != build_json()


def test_import_json_str():
    test = Address()
    test.import_json_str(build_json())
    assert test == build_object()


def test_import_json_str_name_fail():
    test = Address()
    test.import_json_str(build_json(name="Different"))
    assert test != build_object()


def test_import_json_str_street_fail():
    test = Address()
    test.import_json_str(build_json(street="Different"))
    assert test != build_object()


def test_import_json_str_street2_fail():
    test = Address()
    test.import_json_str(build_json(street2="Different"))
    assert test != build_object()


def test_import_json_str_city_fail():
    test = Address()
    test.import_json_str(build_json(city="Different"))
    assert test != build_object()


def test_import_json_str_state_fail():
    test = Address()
    test.import_json_str(build_json(state="Different"))
    assert test != build_object()


def test_import_json_str_zip_code_fail():
    test = Address()
    test.import_json_str(build_json(zip_code="Different"))
    assert test != build_object()


def test_eq():
    test1 = build_object()
    test2 = build_object()
    assert test1 == test2


def test_eq_name():
    test1 = build_object()
    test2 = build_object()
    test1.name = "Test1"
    test2.name = "Test1"
    assert test1 == test2


def test_eq_street():
    test1 = build_object()
    test2 = build_object()
    test1.street = "Test1"
    test2.street = "Test1"
    assert test1 == test2


def test_eq_street2():
    test1 = build_object()
    test2 = build_object()
    test1.street2 = "Test1"
    test2.street2 = "Test1"
    assert test1 == test2


def test_eq_city():
    test1 = build_object()
    test2 = build_object()
    test1.city = "Test1"
    test2.city = "Test1"
    assert test1 == test2


def test_eq_state():
    test1 = build_object()
    test2 = build_object()
    test1.state = "Test1"
    test2.state = "Test1"
    assert test1 == test2


def test_eq_zip_code():
    test1 = build_object()
    test2 = build_object()
    test1.zip_code = "Test1"
    test2.zip_code = "Test1"
    assert test1 == test2


def test_ne():
    test1 = build_object()
    test2 = build_object()
    assert test1 == test2

