"""Wrapper around the eveapi library

Single way to retrieve underlying library. This allows the library to be easily
replaced in future. We also implement a custom Cache handler using Django's
caching backend.
"""
from eveapi import EVEAPIConnection

def get_api():
    """Return an instance of the eveapi
    """
    return EVEAPIConnection()