# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference


from ._code import code
from ._id import id
from ._uri import uri

from .meta import Meta

import xml.etree.ElementTree as ET

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Resource']


# ------------------------------------------------------------------------------
# Resource
# ------------------------------------------------------------------------------
class Resource(FHIRBase):
    """
    This is the base resource type for everything.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Resource'
    
    id = Property('id', id, '0', '1')
    meta = Property('meta', Meta, '0', '1')
    implicitRules = Property('implicitRules', uri, '0', '1')
    language = Property('language', code, '0', '1')

    
    def toXML(self, parent=None, path=None):
        """Return an XML representation of this object."""
        tag = self.__class__.__name__
        
        if parent is None:
            parent = ET.Element(tag)
            parent.set('xmlns', 'http://hl7.org/fhir')
            path = [tag, ]
        else:
            # Resources *always* render their type tag (e.g. '<Patient>')
            parent = ET.SubElement(parent, tag)
        
        return super().toXML(parent, path)
