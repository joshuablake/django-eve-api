"""Test basic functionality"""

from django.test import TestCase
from api import get_api
from eveapi import _RootContext

class WrapperTest(TestCase):
    def setUp(self):
        self.api = get_api()
    
    def test_api_returned(self):
        """Test that method call returns an instance of the base eveapi class"""
        self.assertIsInstance(self.api, _RootContext)