#!/usr/bin/env python
# -*- coding: utf-8 -*-
import coloredlogs
import json
import logging


# Create a top level logging object.
logFormatter = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.DEBUG, logger=logger)
logger.disabled = True


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
        logger.info("Setting Name to '{name}'".format(name=value))
        self.__name = value

    @name.deleter
    def name(self):
        """
        Cleanup name
        :return: void
        """
        logger.debug("Deleting name property.")
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
        logger.info("Setting Street to '{street}'".format(street=value))
        self.__street = value

    @street.deleter
    def street(self):
        """
        Cleanup the street value
        :return: void
        """
        logger.debug("Deleting street property.")
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
        logger.info("Setting street2 to '{street2}'".format(street2=value))
        self.__street2 = value

    @street2.deleter
    def street2(self):
        """
        Cleanup after street 2
        :return: void
        """
        logger.debug("Deleting street2 property.")
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
        logger.info("Setting city to '{city}'".format(city=value))
        self.__city = value

    @city.deleter
    def city(self):
        """
        Cleanup city data
        :return: void
        """
        logger.debug("Deleting city property.")
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
        logger.info("Setting state to '{state}'".format(state=value))
        self.__state = value

    @state.deleter
    def state(self):
        """
        Cleanup state dat
        :return: void
        """
        logger.debug("Deleting state property.")
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
        logger.info("Setting zip_code to '{zip_code}'".format(zip_code=value))
        self.__zip_code = value

    @zip_code.deleter
    def zip_code(self):
        """
        Cleanup zip code data
        :return: void
        """
        logger.debug("Deleting zip_code property.")
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
        logger.info('Exporting address to JSON object.')
        logger.debug(output)
        return json.dumps(output)

    def import_json_str(self, in_address=None):
        """
        Take a JSON encoded string and import it into an Address object
        :param in_address: String[JSON]
        :return:void
        """
        logger.info('Importing json string.')
        logger.debug(in_address)
        temp = json.loads(in_address)
        self.name = temp.get("name", None)
        self.street = temp.get("street", None)
        self.street2 = temp.get("street2", None)
        self.city = temp.get("city", None)
        self.state = temp.get("state", None)
        self.zip_code = temp.get("zip_code", None)
        logger.debug(str(self))

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
        logger.debug("Performing address cleanup.")
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
        logger.info('Initializing Address')
        self.name = None
        self.street = None
        self.street2 = None
        self.city = None
        self.state = None
        self.zip_code = None


if __name__ == "__main__":
    print("This is a library file not intended to be called directly.")
