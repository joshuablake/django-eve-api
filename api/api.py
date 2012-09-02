"""Wrapper around the eveapi library

Single way to retrieve underlying library. This allows the library to be easily
replaced in future. We also implement a custom Cache handler using Django's
caching backend.

Functions:
    `get_api()`: Return connection to the EvE API.

Copyright 2012 Joshua Blake

"""

from eveapi import EVEAPIConnection
from django.core.cache import cache

def get_api():
    """Return connection to the EvE API.
    
    Uses the `eveapi` library. The library is created. By consolidating all
    initialisations here we make it easier to install mocks and if ever needed
    implement a full wrapper.
    
    Returns:
        An instance of `eveapi._RootContext`
    
    """
    return EVEAPIConnection(cacheHandler=_CacheHandler())

class _CacheHandler(object):
    def retrieve(self, host, path, params):
        return cache.get(hash((host, path, frozenset(params))))
    
    def store(self, host, path, params, doc, obj):
        key = hash((host, path, frozenset(params)))
        cache.set(key, doc, obj.cachedUntil-obj.currentTime)
