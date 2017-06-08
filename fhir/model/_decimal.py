# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime as dt
import logging

from . import Property, DateTimeProperty, PropertyDefinition, BaseType, dateTimeBase

__all__ = ['decimal', ]

class decimal(BaseType):
    """Autogenerated decimal type."""
    
    value = Property(PropertyDefinition('value', float, '1', '1', 'xmlAttr'))
    
    def __init__(self, value=None):
        """Initialize a new decimal instance."""
        if value is not None:
            value = float(value)

        super(decimal, self).__init__(value)
    
    def __float__(self):
        return float(self.value)

    def __eq__(self, other):
        if self.value is None or other is None:
            return self.value is None and other is None
        if isinstance(other, decimal):
            return self.value.__eq__(other.value)
        elif isinstance(other, float):
            return self.value.__eq__(other)
        
        return self.value.__eq__(other)
        
    def __ne__(self, other):
        if self.value is None or other is None:
            return not (self.value is None and other is None)
        if isinstance(other, decimal):
            return self.value.__ne__(other.value)
        elif isinstance(other, float):
            return self.value.__ne__(other)
        
        return self.value.__ne__(other)
        
    def __lt__(self, other):
        if isinstance(other, decimal):
            return self.value.__lt__(other.value)
        elif isinstance(other, float):
            return self.value.__lt__(other)
        
        return self.value.__lt__(other)
        
    def __le__(self, other):
        if isinstance(other, decimal):
            return self.value.__le__(other.value)
        elif isinstance(other, float):
            return self.value.__le__(other)
        
        return self.value.__le__(other)
        
    def __gt__(self, other):
        if isinstance(other, decimal):
            return self.value.__gt__(other.value)
        elif isinstance(other, float):
            return self.value.__gt__(other)
        
        return self.value.__gt__(other)
        
    def __ge__(self, other):
        if isinstance(other, decimal):
            return self.value.__ge__(other.value)
        elif isinstance(other, float):
            return self.value.__ge__(other)
        
        return self.value.__ge__(other)
        
    def __add__(self, other):
        if isinstance(other, decimal):
            return decimal(self.value.__add__(other.value))
        elif isinstance(other, float):
            return self.value.__add__(other)
        
        return self.value.__add__(other)
        
    __radd__ = __add__
    
    
    def __div__(self, other):
        """x / y <==> x.__div__(y)"""
        if isinstance(other, float) or isinstance(other, decimal):
            return decimal(float(self).__div__(float(other)))
            
        return other.__rdiv__(float(self))

    def __rdiv__(self, other):
        """y / x <==> x.__rdiv__(y)"""
        if isinstance(other, float) or isinstance(other, decimal):
            return decimal(float(self).__rdiv__(float(other)))
            
        return other.__div__(float(self))
    
    def __mul__(self, other):
        """x * y <==> x.__mul__(y)"""
        return decimal(float(self).__mul__(other))

    def __rmul__(self, other):
        """y * x <==> x.__rmul__(y)"""
        return decimal(float(self).__mul__(other))



