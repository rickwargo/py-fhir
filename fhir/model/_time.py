# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, PropertyDefinition, BaseType, dateTimeBase

__all__ = ['time', ]

class time(dateTimeBase):
    """Autogenerated time type."""
    _regex = '([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?'    
    # value = Property(PropertyDefinition('value', dateTimeBase, '1', '1', 'xmlAttr'))
    value = Property(PropertyDefinition('value', str, '1', '1', 'xmlAttr'))

