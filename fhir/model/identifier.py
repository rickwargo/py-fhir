# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition
from . import FHIRBase, Element, Extension, Reference


from ._string import string
from ._uri import uri
from ._code import code

from .period import Period
from .codeableconcept import CodeableConcept

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Identifier']


# ------------------------------------------------------------------------------
# Identifier
# ------------------------------------------------------------------------------
class Identifier(Element):
    """
    A technical identifier - identifies some entity uniquely and
    unambiguously.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Identifier'
    
    use = Property(PropertyDefinition('use', code, '0', '1'))
    type = Property(PropertyDefinition('type', CodeableConcept, '0', '1'))
    system = Property(PropertyDefinition('system', uri, '0', '1'))
    value = Property(PropertyDefinition('value', string, '0', '1'))
    period = Property(PropertyDefinition('period', Period, '0', '1'))
    assigner = Property(PropertyDefinition('assigner', Reference(reference="None"), '0', '1'))
