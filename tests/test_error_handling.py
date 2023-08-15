# Tests for error handling function(s) from the Variables class

import unittest

from onshape_variables.variables import Variables

from .test_data import *


class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        # create Variables instance with a valid eid
        self.variables_with_eid = Variables(
            test_api_keys, test_did, test_wid, test_eid_empty
        )
        # create a Variables instance with an empty eid
        self.variables_without_eid = Variables(test_api_keys, test_did, test_wid)

        # assign variables with data for testing
        self.variables_with_value = variables_with_value
        self.variables_without_value = variables_without_value

    def test_eid_error_handling_valid(self):
        # Test with a valid eid, no exception should be raised
        try:
            self.variables_with_eid.eid_error_handling()
        except ValueError:
            self.fail("Unexpected ValueError raised")

    def test_eid_error_handling_empty_eid(self):
        # Test with an empty eid, expect a ValueError
        with self.assertRaises(ValueError) as context:
            self.variables_without_eid.eid_error_handling()
        expected_error_message = "'eid' is missing. Call create_variable_studio() first OR include an existing eid when creating a Variable object."
        self.assertIn(expected_error_message, str(context.exception))

    def test_eid_error_handling_invalid_eid(self):
        # Test with an invalid eid, expect a ValueError
        self.variables_with_eid.eid = "e9989d4fab94ba77afdeed5"  # 23 len instead of 24
        with self.assertRaises(ValueError) as context:
            self.variables_with_eid.eid_error_handling()
        self.assertIn(
            "Invalid eid. The eid must be a string of 24 characters",
            str(context.exception),
        )


if __name__ == "__main__":
    unittest.main()
