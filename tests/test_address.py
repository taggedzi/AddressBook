#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.Address import Address


def test_init_address_pass():
    test = Address()


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