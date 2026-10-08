import os
import unittest
from unittest.mock import patch

import config


class ConfigTests(unittest.TestCase):
    def test_api_key_is_read_from_environment(self):
        with patch.dict(os.environ, {"MEDILINK_API_KEY": "test-key"}):
            self.assertEqual(config.get_api_key(), "test-key")

    def test_api_key_has_a_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertTrue(config.get_api_key())

    def test_timeout_is_read_from_environment(self):
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "10"}):
            self.assertEqual(config.get_request_timeout(), 10)

    def test_timeout_must_be_greater_than_zero(self):
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "0"}):
            with self.assertRaises(ValueError):
                config.get_request_timeout()

    def test_timeout_rejects_negative_values(self):
        with patch.dict(os.environ, {"REQUEST_TIMEOUT": "-3"}):
            with self.assertRaises(ValueError):
                config.get_request_timeout()


if __name__ == "__main__":
    unittest.main()