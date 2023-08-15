# Tests for functions regarding variable studio scope

import unittest

from onshape_variables.variables import Variables

from .test_data import *


class TestScope(unittest.TestCase):
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

    def test_get_scope(self):
        # Arrange

        # set the eid for this test
        self.variables_with_eid.eid = get_scope_eid
        # update the endpoint
        self.variables_with_eid.update_urls()

        expected_result = {"isAutomaticallyInserted": False}

        # Act
        result = self.variables_with_eid.get_scope()

        # Assert
        self.assertEqual(result, expected_result)

    def test_get_scope_invalid_eid(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.get_scope()

    # TESTS FOR set_scope HERE
    def test_set_scope_true(self):
        # this is the default case when set_scope() is called

        # Arrange
        # set the eid for this test
        self.variables_with_eid.eid = set_scope_eid
        # update the endpoint
        self.variables_with_eid.update_urls()

        expected_scope = {"isAutomaticallyInserted": True}

        # Act
        try:
            self.variables_with_eid.set_scope()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

        # verify that the scope is successfully set to all ("True" case)
        set_scope = self.variables_with_eid.get_scope()
        self.assertEqual(set_scope, expected_scope)

    def test_set_scope_false(self):
        # case when scope is set to false

        # Arrange
        # set the eid for this test
        self.variables_with_eid.eid = set_scope_eid
        # update the endpoint
        self.variables_with_eid.update_urls()

        expected_scope = {"isAutomaticallyInserted": False}

        # Act
        try:
            self.variables_with_eid.set_scope(all=False)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

        # verify that the scope is successfully set to false
        set_scope = self.variables_with_eid.get_scope()
        self.assertEqual(set_scope, expected_scope)

    def test_set_scope_invalid_eid(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.set_scope()


if __name__ == "__main__":
    unittest.main()
