# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .resource import Resource

from ._code import code
from ._decimal import decimal
from ._instant import instant
from ._string import string
from ._unsignedint import unsignedInt
from ._uri import uri

from .backboneelement import BackboneElement
from .identifier import Identifier
from .signature import Signature

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Bundle']

class Link(BackboneElement):
    """Autogenerated class for implicit type."""
    relation = Property('relation', 'string', '1', '1')
    url = Property('url', 'uri', '1', '1')

class Entry(BackboneElement):
    """Autogenerated class for implicit type."""
    link = Property('link', 'Link', '0', '*')
    fullUrl = Property('fullUrl', 'uri', '0', '1')
    resource = Property('resource', 'Resource', '0', '1')
    search = Property('search', 'Search', '0', '1')
    request = Property('request', 'Request', '0', '1')
    response = Property('response', 'Response', '0', '1')

class Search(BackboneElement):
    """Autogenerated class for implicit type."""
    mode = Property('mode', 'code', '0', '1')
    score = Property('score', 'decimal', '0', '1')

class Request(BackboneElement):
    """Autogenerated class for implicit type."""
    method = Property('method', 'code', '1', '1')
    url = Property('url', 'uri', '1', '1')
    ifNoneMatch = Property('ifNoneMatch', 'string', '0', '1')
    ifModifiedSince = Property('ifModifiedSince', 'instant', '0', '1')
    ifMatch = Property('ifMatch', 'string', '0', '1')
    ifNoneExist = Property('ifNoneExist', 'string', '0', '1')

class Response(BackboneElement):
    """Autogenerated class for implicit type."""
    status = Property('status', 'string', '1', '1')
    location = Property('location', 'uri', '0', '1')
    etag = Property('etag', 'string', '0', '1')
    lastModified = Property('lastModified', 'instant', '0', '1')
    outcome = Property('outcome', 'Resource', '0', '1')


# ------------------------------------------------------------------------------
# Bundle
# ------------------------------------------------------------------------------
class Bundle(Resource):
    """
    A container for a collection of resources.

    Implements iteration over Bundle.entry.resource.
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Bundle'
    
    identifier = Property('identifier', Identifier, '0', '1')
    type = Property('type', code, '1', '1')
    timestamp = Property('timestamp', instant, '0', '1')
    total = Property('total', unsignedInt, '0', '1')
    link = Property('link', Link, '0', '*')
    entry = Property('entry', Entry, '0', '*')
    signature = Property('signature', Signature, '0', '1')


    # FIXME: implement logic for following <link> tags
    def __iter__(self):
        return iter([entry.resource for entry in self.entry])
    
    
    def __len__(self):
        return len(self.entry)
