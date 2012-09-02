"""Test basic functionality.

Copyright 2012 Joshua Blake

"""

from api import get_api
from django.test import TestCase
from eveapi import _RootContext

class WrapperTest(TestCase):
    def setUp(self):
        self.api = get_api()
        self.cache = self.api._root._handler
    
    def test_api_returned(self):
        """Test that method call returns an instance of the base eveapi class."""
        self.assertIsInstance(self.api, _RootContext)
        
    def test_cache_implemented(self):
        """Test that cache is implemented."""
        self.assertIsNotNone(self.cache)
