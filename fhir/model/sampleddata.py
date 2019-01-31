# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._decimal import decimal
from ._positiveint import positiveInt
from ._string import string

from .quantity import Quantity

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['SampledData']


# ------------------------------------------------------------------------------
# SampledData
# ------------------------------------------------------------------------------
class SampledData(Element):
    """
    A series of measurements taken by a device, with upper and lower
    limits. There may be more than one dimension in the data.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/SampledData'
    
    origin = Property('origin', Quantity, '1', '1')
    period = Property('period', decimal, '1', '1')
    factor = Property('factor', decimal, '0', '1')
    lowerLimit = Property('lowerLimit', decimal, '0', '1')
    upperLimit = Property('upperLimit', decimal, '0', '1')
    dimensions = Property('dimensions', positiveInt, '1', '1')
    data = Property('data', string, '0', '1')
