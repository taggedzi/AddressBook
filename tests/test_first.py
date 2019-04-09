#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.first import test as test_func


def test_first_pass():
    assert test_func(0) == 2


def test_first_fail():
    assert test_func(1) != 2


