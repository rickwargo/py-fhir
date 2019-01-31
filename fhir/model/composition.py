# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property
from . import FHIRBase, Element, Extension, Reference

from .backboneelement import BackboneElement
from .domainresource import DomainResource

from ._code import code
from ._datetime import dateTime
from ._string import string

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .narrative import Narrative
from .period import Period

__author__ = "Melle Sieswerda"
__copyright__  = "Copyright 2017, Melle Sieswerda"
__license__ = "GPL"
__version__ = "0.8"

__all__ = ['Composition']

class Attester(BackboneElement):
    """Autogenerated class for implicit type."""
    mode = Property('mode', 'code', '1', '1')
    time = Property('time', 'dateTime', '0', '1')
    party = Property('party', Reference("http://hl7.org/fhir/StructureDefinition/Patient", "http://hl7.org/fhir/StructureDefinition/RelatedPerson", "http://hl7.org/fhir/StructureDefinition/Practitioner", "http://hl7.org/fhir/StructureDefinition/PractitionerRole", "http://hl7.org/fhir/StructureDefinition/Organization"), '0', '1')        

class RelatesTo(BackboneElement):
    """Autogenerated class for implicit type."""
    code = Property('code', 'code', '1', '1')
    target = Property('target', ['Identifier', 'Reference("http://hl7.org/fhir/StructureDefinition/Composition")'], '1', '1')

class Event(BackboneElement):
    """Autogenerated class for implicit type."""
    code = Property('code', 'CodeableConcept', '0', '*')
    period = Property('period', 'Period', '0', '1')
    detail = Property('detail', Reference("http://hl7.org/fhir/StructureDefinition/Resource"), '0', '*')        

class Section(BackboneElement):
    """Autogenerated class for implicit type."""
    title = Property('title', 'string', '0', '1')
    code = Property('code', 'CodeableConcept', '0', '1')
    author = Property('author', Reference("http://hl7.org/fhir/StructureDefinition/Practitioner", "http://hl7.org/fhir/StructureDefinition/PractitionerRole", "http://hl7.org/fhir/StructureDefinition/Device", "http://hl7.org/fhir/StructureDefinition/Patient", "http://hl7.org/fhir/StructureDefinition/RelatedPerson", "http://hl7.org/fhir/StructureDefinition/Organization"), '0', '*')        
    focus = Property('focus', Reference("http://hl7.org/fhir/StructureDefinition/Resource"), '0', '1')        
    text = Property('text', 'Narrative', '0', '1')
    mode = Property('mode', 'code', '0', '1')
    orderedBy = Property('orderedBy', 'CodeableConcept', '0', '1')
    entry = Property('entry', Reference("http://hl7.org/fhir/StructureDefinition/Resource"), '0', '*')        
    emptyReason = Property('emptyReason', 'CodeableConcept', '0', '1')
    section = Property('section', 'Section', '0', '*')


# ------------------------------------------------------------------------------
# Composition
# ------------------------------------------------------------------------------
class Composition(DomainResource):
    """
    A set of healthcare-related information that is assembled together
    into a single logical package that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. A
    Composition defines the structure and narrative content necessary for
    a document. However, a Composition alone does not constitute a
    document. Rather, the Composition must be the first entry in a Bundle
    where Bundle.type=document, and any other resources referenced from
    Composition must be included as subsequent entries in the Bundle (for
    example Patient, Practitioner, Encounter, etc.).
    
    Autogenerated class.
    """
    _url = 'http://hl7.org/fhir/StructureDefinition/Composition'
    
    identifier = Property('identifier', Identifier, '0', '1')
    status = Property('status', code, '1', '1')
    type = Property('type', CodeableConcept, '1', '1')
    category = Property('category', CodeableConcept, '0', '*')
    subject = Property('subject', Reference("http://hl7.org/fhir/StructureDefinition/Resource"), '0', '1')
    encounter = Property('encounter', Reference("http://hl7.org/fhir/StructureDefinition/Encounter"), '0', '1')
    date = Property('date', dateTime, '1', '1')
    author = Property('author', Reference("http://hl7.org/fhir/StructureDefinition/Practitioner", "http://hl7.org/fhir/StructureDefinition/PractitionerRole", "http://hl7.org/fhir/StructureDefinition/Device", "http://hl7.org/fhir/StructureDefinition/Patient", "http://hl7.org/fhir/StructureDefinition/RelatedPerson", "http://hl7.org/fhir/StructureDefinition/Organization"), '1', '*')
    title = Property('title', string, '1', '1')
    confidentiality = Property('confidentiality', code, '0', '1')
    attester = Property('attester', Attester, '0', '*')
    custodian = Property('custodian', Reference("http://hl7.org/fhir/StructureDefinition/Organization"), '0', '1')
    relatesTo = Property('relatesTo', RelatesTo, '0', '*')
    event = Property('event', Event, '0', '*')
    section = Property('section', Section, '0', '*')
