# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .resource import Resource


from .narrative import Narrative

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['DomainResource']


# ------------------------------------------------------------------------------
# DomainResource
# ------------------------------------------------------------------------------
class DomainResource(Resource):
    """
    A resource that includes narrative, extensions, and contained
    resources.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/DomainResource'
    
    text = Property('text', Narrative, '0', '1')
    contained = Property('contained', Resource, '0', '*')
    extension = Property('extension', Extension, '0', '*')
    modifierExtension = Property('modifierExtension', Extension, '0', '*')
