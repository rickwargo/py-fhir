# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension


from ._code import code
from ._string import string

from .period import Period

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Address']


# ------------------------------------------------------------------------------
# Address
# ------------------------------------------------------------------------------
class Address(Element):
    """
    There is a variety of postal address formats defined around the world.
    This format defines a superset that is the basis for all addresses
    around the world.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Address'
    
    use = Property(PropertyDefinition('use', code, '0', '1'))
    type = Property(PropertyDefinition('type', code, '0', '1'))
    text = Property(PropertyDefinition('text', string, '0', '1'))
    line = Property(PropertyDefinition('line', string, '0', '*'))
    city = Property(PropertyDefinition('city', string, '0', '1'))
    district = Property(PropertyDefinition('district', string, '0', '1'))
    state = Property(PropertyDefinition('state', string, '0', '1'))
    postalCode = Property(PropertyDefinition('postalCode', string, '0', '1'))
    country = Property(PropertyDefinition('country', string, '0', '1'))
    period = Property(PropertyDefinition('period', Period, '0', '1'))
    