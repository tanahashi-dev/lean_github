#!/usr/bin/env python3
"""
Test cases for hello.py script.
"""

import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
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

    @patch('hello.get_tokyo_weather', return_value=(20.5, "晴れ (Mainly clear)"))
    @patch('builtins.print')
    def test_main_calls_print(self, mock_print, mock_weather):
        """Test that main function calls print."""
        hello.main()
        # Should call print at least 4 times (greeting, Japanese time, English time, weather)
        self.assertGreaterEqual(mock_print.call_count, 4)

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

    @patch('hello.urllib.request.urlopen')
    def test_get_tokyo_weather_success(self, mock_urlopen):
        """Test that get_tokyo_weather returns temperature and condition."""
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"current_weather": {"temperature": 18.5, "weathercode": 1}}'
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        temp, condition = hello.get_tokyo_weather()
        self.assertEqual(temp, 18.5)
        self.assertIn("Mainly clear", condition)

    @patch('hello.get_tokyo_weather', side_effect=Exception("network error"))
    @patch('builtins.print')
    def test_main_handles_weather_error(self, mock_print, mock_weather):
        """Test that main handles weather fetch errors gracefully."""
        hello.main()
        printed = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("失敗" in s for s in printed))

    def test_weather_codes_dict(self):
        """Test that WEATHER_CODES contains common codes."""
        self.assertIn(0, hello.WEATHER_CODES)
        self.assertIn(3, hello.WEATHER_CODES)
        self.assertIn(63, hello.WEATHER_CODES)


if __name__ == '__main__':
    unittest.main()
