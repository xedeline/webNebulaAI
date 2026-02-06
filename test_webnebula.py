# test_webnebula.py
"""
Tests for webNebula module.
"""

import unittest
from webnebula import webNebula

class TestwebNebula(unittest.TestCase):
    """Test cases for webNebula class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = webNebula()
        self.assertIsInstance(instance, webNebula)
        
    def test_run_method(self):
        """Test the run method."""
        instance = webNebula()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
