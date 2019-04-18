#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Address(object):
    """
    A simple object used in learning python AND to manage addresses in a USA address format.
    """

    @property
    def name(self):
        """
        :return: String Name
        """
        return self.__name

    @name.setter
    def name(self, value=None):
        """
        Collect a value and set the address name to that value
        :param value: String
        :return: void
        """
        if value is None:
            value = ''
        self.__name = value

    @name.deleter
    def name(self):
        """
        Cleanup name
        :return: void
        """
        del self.__name

    @property
    def street(self):
        """
        :return: String Street
        """
        return self.__street

    @street.setter
    def street(self, value=None):
        """
        Collect a value for street and store it
        :param value: String Street
        :return: void
        """
        if value is None:
            value = ''
        self.__street = value

    @street.deleter
    def street(self):
        """
        Cleanup the street value
        :return: void
        """
        del self.__street

    @property
    def street2(self):
        """
        :return: String Street 2
        """
        return self.__street2

    @street2.setter
    def street2(self, value=None):
        """
        Collect a value for street 2 and store it
        :param value: String Street 2
        :return: void
        """
        if value is None:
            value = ''
        self.__street2 = value

    @street2.deleter
    def street2(self):
        """
        Cleanup after street 2
        :return: void
        """
        del self.__street2

    @property
    def city(self):
        """
        :return: String City
        """
        return self.__city

    @city.setter
    def city(self, value=None):
        """
        Collect a value for city and store it
        :param value: String City
        :return: void
        """
        if value is None:
            value = ''
        self.__city = value

    @city.deleter
    def city(self):
        """
        Cleanup city data
        :return: void
        """
        del self.__city

    @property
    def state(self):
        """
        :return: String State
        """
        return self.__state

    @state.setter
    def state(self, value=None):
        """
        Collect a state and store it
        :param value: String state
        :return: void
        """
        if value is None:
            value = ''
        self.__state = value

    @state.deleter
    def state(self):
        """
        Cleanup state dat
        :return: void
        """
        del self.__state

    @property
    def zip_code(self):
        """
        :return: String Zip code
        """
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value=None):
        """
        Collect a zip code and store it
        :param value: String zip code
        :return: void
        """
        if value is None:
            value = ''
        self.__zip_code = value

    @zip_code.deleter
    def zip_code(self):
        """
        Cleanup zip code data
        :return: void
        """
        del self.__zip_code

    def export_json_str(self):
        """
        Export an address object as a JSON String
        :return: String JSON string representing an address
        """
        output = {
            "name": self.name,
            "street": self.street,
            "street2": self.street2,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code
        }
        return json.dumps(output)

    def import_json_str(self, in_address=None):
        """
        Take a JSON encoded string and import it into an Address object
        :param in_address: String[JSON]
        :return:void
        """
        temp = json.loads(in_address)
        self.name = temp.get("name", None)
        self.street = temp.get("street", None)
        self.street2 = temp.get("street2", None)
        self.city = temp.get("city", None)
        self.state = temp.get("state", None)
        self.zip_code = temp.get("zip_code", None)

    def __repr__(self):
        """
        :return: String representation of an address object
        """
        return '<Address name="{0.name}" street="{0.street}">'.format(self)

    def __str__(self):
        """
        :return: String A user friendly string represntation of an address object.
        """
        output = '-' * 80 + "\n"
        output += "{0.name}\n"
        output += "{0.street}\n"
        if self.street2:
            output += "{0.street2}\n"
        output += "{0.city}, {0.state} {0.zip_code}\n"
        return output.format(self)

    def __eq__(self, other):
        """
        Compare all features of an address to determine if they are the same
        :param other: Address an address type object to compare with.
        :return: Bool
        """
        current = (self.name, self.street, self.street2, self.city, self.state, self.zip_code)
        other_val = (other.name, other.street, other.street2, other.city, other.state, other.zip_code)
        return current == other_val

    def __ne__(self, other):
        """
        Determine if two address type objects are NOT equal
        :param other: Object to compare
        :return: Bool
        """
        return not (self == other)

    def __lt__(self, other):
        """
        Less than comparison of an address (primarily used for sorting by address name)
        :param other: Address an Address object to compare with
        :return: Bool
        """
        return self.name.lower() < other.name.lower()

    def __gt__(self, other):
        """
        Greater than comparison of an address (primarily used for sorting by address name)
        :param other: Address an Address object to compare with
        :return: Bool
        """
        return self.name.lower() > other.name.lower()

    def __del__(self):
        """
        Self cleanup and garbage collection
        :return:
        """
        del self.name
        del self.street
        del self.street2
        del self.city
        del self.state
        del self.zip_code

    def __init__(self):
        """
        Initialization
        """
        self.name = None
        self.street = None
        self.street2 = None
        self.city = None
        self.state = None
        self.zip_code = None


if __name__ == "__main__":
    a = Address()
    a.name = 'Test'
    a.street = 'Street Rd'
    a.city = 'City'
    a.state = 'ST'
    a.zip_code = '55555'

    b = Address()
    b.name = 'Aest'
    b.street = 'Street Rd'
    b.city = 'City'
    b.state = 'ST'
    b.zip_code = '55555'

    print(a)
    print(b)
    print(a == b)
    print(a != b)
    print(sorted([a, b]))
    print(a.export_json_str())
    temp_json = '{"name": "Test", "street": "Street Rd", "street2": "", "city": "City", "state": "ST", ' \
                '"zip_code": "55555"}'
    c = Address()
    c.import_json_str(temp_json)
    print(c == a)

    # print("This is a library file not intended to be called directly.")
