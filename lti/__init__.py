"""
LMV Trading--Indicators  (lti) python library

lti is a python library for calculating more than 60 trading technical
indicators from stocks data. The library provides an API for:

* trading technical indicators value calculation
* trading technical indicators graph preparation
* trading signal calculation
* trading simulation based on trading signals
* prices direction prediction based on machine learning algorithms 


"""

from lti import indicators
from lti import utils

__version__ = '0.2.2'

__all__ = ['indicators', 'utils','Marché']
