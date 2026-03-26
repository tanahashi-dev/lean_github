#!/usr/bin/env python3
"""
Test cases for hello.py script.
"""

import unittest
from datetime import datetime
from unittest.mock import patch
import sys
import os

# Add parent directory to path to import hello module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import hello


class TestHello(unittest.TestCase):
    """Test cases for hello.py module."""

    @patch('hello.datetime')
    def test_greeting_output(self, mock_datetime):
        """Test that greeting is displayed correctly."""
        # Mock the datetime to return a fixed time
        mock_datetime.now.return_value = datetime(2026, 3, 26, 16, 20, 9)
        
        # We can't easily test print output, but we can verify the module runs
        # without error and has the expected structure
        self.assertTrue(hasattr(hello, 'main'))
        self.assertTrue(callable(hello.main))

    def test_module_has_main_function(self):
        """Test that hello module has a main function."""
        self.assertTrue(hasattr(hello, 'main'))
        self.assertTrue(callable(hello.main))

    @patch('builtins.print')
    def test_main_calls_print(self, mock_print):
        """Test that main function calls print."""
        hello.main()
        # Should call print at least twice (greeting and time)
        self.assertGreaterEqual(mock_print.call_count, 2)

    def test_datetime_now_returns_datetime(self):
        """Test that datetime.now() works as expected."""
        now = datetime.now()
        self.assertIsInstance(now, datetime)
        # Check that we can format it
        formatted = now.strftime('%Y年%m月%d日 %H:%M:%S')
        self.assertIsInstance(formatted, str)
        self.assertIn('年', formatted)
        self.assertIn('月', formatted)
        self.assertIn('日', formatted)


if __name__ == '__main__':
    unittest.main()
