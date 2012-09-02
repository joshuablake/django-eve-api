"""Test basic functionality.

Copyright 2012 Joshua Blake

"""

from api import get_api
from django.core.cache import cache
from django.test import TestCase
from eveapi import _RootContext
from time import sleep

class WrapperTest(TestCase):
    class Cachable(object):
            def __init__(self):
                self.currentTime = 100
                self.cachedUntil = 300
                
    def setUp(self):
        self.api = get_api()
        self.cache = self.api._root._handler
        
    def tearDown(self):
        cache.clear()
    
    def test_api_returned(self):
        """Test that method call returns an instance of the base eveapi class."""
        self.assertIsInstance(self.api, _RootContext)
        
    def test_cache_implemented(self):
        """Test that cache is implemented."""
        self.assertIsNotNone(self.cache)
        
    def test_set_cache(self):
        """Test that we can add something to the cache."""
        self.cache.store('api.localhost', '/EVE/Alliances.xml.aspx', {},
                         '<xml></xml>', self.Cachable())
        
    def test_retrieve(self):
        """Test the data can be retrieved."""
        self.cache.store('api.localhost', '/EVE/Alliances.xml.aspx', {},
                         '<xml></xml>', self.Cachable())
        self.assertEqual(self.cache.retrieve('api.localhost',
                                '/EVE/Alliances.xml.aspx', {}),
                         '<xml></xml>')
        
    def test_empty_return(self):
        """Test that `None` is returned when no data is stored"""
        self.assertIsNone(self.cache.retrieve('api.localhost',
                                '/EVE/Alliances.xml.aspx', {}))
        
    def test_cache_expires(self):
        """Test that the cache automatically expires"""
        obj = self.Cachable()
        obj.cachedUntil = 100.01
        self.cache.store('api.localhost', '/EVE/Alliances.xml.aspx', {},
                         '<xml></xml>', obj)
        sleep(0.02)
        self.assertIsNone(self.cache.retrieve('api.localhost',
                                '/EVE/Alliances.xml.aspx', {}))