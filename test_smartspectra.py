# test_smartspectra.py
"""
Tests for SmartSpectra module.
"""

import unittest
from smartspectra import SmartSpectra

class TestSmartSpectra(unittest.TestCase):
    """Test cases for SmartSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartSpectra()
        self.assertIsInstance(instance, SmartSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
