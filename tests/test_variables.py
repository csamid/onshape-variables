# Tests for creating a variable studio and other variable related functions


import unittest
from copy import deepcopy

from onshape_variables.variables import Variables

from .test_data import *


class TestVariables(unittest.TestCase):
    def setUp(self):
        # create Variables instance with a valid eid
        self.variables_with_eid = Variables(
            test_api_keys, test_did, test_wid, test_eid_empty
        )
        # create a Variables instance with an empty eid
        self.variables_without_eid = Variables(test_api_keys, test_did, test_wid)

        # assign variables with data for testing
        self.variables_with_value = deepcopy(variables_with_value)
        self.variables_without_value = deepcopy(variables_without_value)

    def test_create_variable_studio(self):
        # Act
        self.variables_without_eid.create_varaible_studio()
        # Assert
        self.assertIsNotNone(self.variables_without_eid.eid)

    def test_has_duplicates_with_duplicates(self):
        # update variables to have duplicates
        variables = self.variables_with_value
        print(self.variables_with_value)
        variables[1]["name"] = variables[0]["name"]
        print(self.variables_with_value)
        # self.variables_without_value[1]["name"] = self.variables_without_value[0][
        #     "name"
        # ]

        # Act
        result = self.variables_with_eid.has_duplicates(variables)

        # Assert
        self.assertTrue(result)

    def test_has_duplicates_without_duplicates(self):
        # Act
        # variables = self.variables_with_value
        print(self.variables_with_value)
        result = self.variables_with_eid.has_duplicates(self.variables_with_value)

        # Assert
        self.assertFalse(result)

    def test_get_variables_empty(self):
        # Act
        result = self.variables_with_eid.get_variables()

        expected_data = [{"variableStudioReference": None, "variables": []}]

        actual_data = result

        # Assert
        self.assertEqual(actual_data, expected_data)

    def test_get_variables_with_data(self):
        # Arrange
        self.variables_with_eid.eid = test_eid_with_data
        # update the endpoint
        self.variables_with_eid.update_urls()

        # Act
        result = self.variables_with_eid.get_variables()

        expected_data = [
            {"variableStudioReference": None, "variables": self.variables_with_value}
        ]

        actual_data = result

        # # Assert
        self.assertEqual(actual_data, expected_data)

    def test_get_variables_without_eid(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.get_variables()

    def test_get_variables_invalid_len_eid(self):
        # invalid length eid
        invalid_eid = "e9989d4fab94ba77afdeed5"  # 23 character string instead of 24
        # update variables eid
        self.variables_with_eid.eid = invalid_eid
        # update endpoints
        self.variables_with_eid.update_urls()

        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_with_eid.get_variables()

    def test_get_variables_invalid_type_eid(self):
        # invalid type eid
        invalid_eid = int("111111111111111111111111")
        # update variables eid
        self.variables_with_eid.eid = invalid_eid
        # update endpoints
        self.variables_with_eid.update_urls()

        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_with_eid.get_variables()

    def test_append_variables_basic(self):
        # Arrange

        # change the eid for this test
        self.variables_with_eid.eid = append_variables_eid
        # update endpoints
        self.variables_with_eid.update_urls()

        # variables for this test
        existing_variables = self.variables_with_value[0]
        variables_to_append = self.variables_with_value[1:]

        # Act
        result = self.variables_with_eid.append_variables(variables_to_append)

        # Assert
        expected_result = [existing_variables] + variables_to_append
        self.assertEqual(result, expected_result)

    def test_append_variables_with_duplicate(self):
        # Arrange

        # change the eid for this test
        self.variables_with_eid.eid = append_variables_eid
        # update endpoints
        self.variables_with_eid.update_urls()

        # update variables to have a duplicate
        variables_to_append = self.variables_with_value
        variables_to_append[1]["name"] = variables_to_append[0]["name"]
        variables_to_append = variables_to_append[1:]
        # self.variables_with_value[1]["name"] = self.variables_with_value[0]["name"]
        # variables_to_append = self.variables_with_value[1:]

        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_with_eid.append_variables(variables_to_append)

    def test_append_variables_with_empty_list(self):
        # Arrange

        # change the eid for this test
        self.variables_with_eid.eid = append_variables_eid
        # update endpoints
        self.variables_with_eid.update_urls()

        # variables for this test
        existing_variables = self.variables_with_value[0]
        variables_to_append = []  # empty list

        # Act
        result = self.variables_with_eid.append_variables(variables_to_append)

        # Assert
        expected_result = [existing_variables] + variables_to_append
        self.assertEqual(result, expected_result)

    def test_append_variables_to_empty_list(self):
        # Arrange

        # default eid targets an empty variable studio :)

        # variables for this test
        existing_variables = []
        variables_to_append = self.variables_with_value

        # Act
        result = self.variables_with_eid.append_variables(variables_to_append)

        # Assert
        expected_result = existing_variables + variables_to_append
        self.assertEqual(result, expected_result)

    def test_assign_variables_with_append(self):
        try:
            # Arrange

            # change the eid for this test
            self.variables_with_eid.eid = append_variables_eid
            # update endpoints
            self.variables_with_eid.update_urls()

            # set the variables for this test
            variables_to_append = self.variables_with_value[1:]

            # Act
            try:
                self.variables_with_eid.assign_variables(
                    variables_to_append, append=True
                )
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

            # verify that variables are successfully assigned with the append option
            assigned_variables = self.variables_with_eid.get_variables()[0]["variables"]
            expected_variables = self.variables_with_value
            self.assertEqual(assigned_variables, expected_variables)
        finally:
            # clean up specific
            self.variables_with_eid.assign_variables(
                [self.variables_with_value[0]], append=False
            )

    def test_assign_variables_without_append(self):
        try:
            # Arrange

            # change the eid for this test
            self.variables_with_eid.eid = replace_variables_eid
            # update endpoints
            self.variables_with_eid.update_urls()

            # set the variables for this test
            variables_that_override = self.variables_with_value

            # Act
            try:
                self.variables_with_eid.assign_variables(
                    variables_that_override, append=False
                )
            except Exception as e:
                self.fail(f"Unexpected exception: {e}")

            # verify that variables are successfully assigned
            assigned_variables = self.variables_with_eid.get_variables()[0]["variables"]
            expected_variables = self.variables_with_value
            self.assertEqual(assigned_variables, expected_variables)
        finally:
            # clean up specific
            self.variables_with_eid.assign_variables(
                [self.variables_with_value[0]], append=False
            )

    def test_assign_variables_with_duplicate(self):
        # verify that a 'ValueError' is raised

        # update variables to have a duplicate
        variables = self.variables_without_value
        variables[1]["name"] = self.variables_without_value[0]["name"]

        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_with_eid.assign_variables(variables)

    def test_assign_variables_invalid_eid(self):
        # verify that a 'ValueError' is raised

        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.assign_variables(self.variables_with_value)


if __name__ == "__main__":
    unittest.main()
