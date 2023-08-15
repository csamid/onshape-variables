# Tests for functions regarding  variable studio references

import unittest

from onshape_variables.variables import Variables

from .test_data import *


class TestReferences(unittest.TestCase):
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

    def test_get_references_empty(self):
        # test case for when no references exist in the eid

        expected_response = {"references": []}

        # Act
        result = self.variables_with_eid.get_references()

        # Assert
        self.assertEqual(result, expected_response)

    def test_get_references_exists(self):
        # test case for when a eid does have one or more references

        # Arrange

        # change to the eid for this test
        self.variables_with_eid.eid = "ec3fece406061218ba0465f7"
        # update the endpoint
        self.variables_with_eid.update_urls()

        expected_response = references_exists

        # Act
        result = self.variables_with_eid.get_references()

        # Assert
        self.assertEqual(result, expected_response)

    def test_get_references_invalid_eid(self):
        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.assign_variables(self.variables_without_value)

    def test_append_references_basic(self):
        # basic test case where a reference exists

        # Arrange

        # change to the eid for this test
        self.variables_with_eid.eid = "ec3fece406061218ba0465f7"
        # update the endpoint
        self.variables_with_eid.update_urls()

        existing_references = references_exists
        references_to_append = {
            "references": [
                {
                    "variableNames": [],
                    "entireVariableStudio": True,
                    "referenceDocumentId": "",
                    "referenceVersionId": "",
                    "referenceElementId": test_eid_empty,
                }
            ]
        }

        expected_response = (
            references_exists["references"] + references_to_append["references"]
        )

        # Act
        result = self.variables_with_eid.append_references(references_to_append)

        # Assert
        self.assertEqual(result, expected_response)

    def test_append_references_with_empty_list(self):
        # Arrange

        # change to the eid for this test
        self.variables_with_eid.eid = "ec3fece406061218ba0465f7"
        # update the endpoint
        self.variables_with_eid.update_urls()

        existing_references = references_exists
        references_to_append = {"references": []}

        expected_response = (
            references_exists["references"] + references_to_append["references"]
        )

        # Act
        result = self.variables_with_eid.append_references(references_to_append)

        # Assert
        self.assertEqual(result, expected_response)

    def test_append_references_to_empty_list(self):
        # Arrange

        # change to the eid for this test
        self.variables_with_eid.eid = test_eid_empty
        # update the endpoint
        self.variables_with_eid.update_urls()

        existing_references = {"references": []}
        references_to_append = {
            "references": [
                {
                    "variableNames": [],
                    "entireVariableStudio": True,
                    "referenceDocumentId": "",
                    "referenceVersionId": "",
                    "referenceElementId": test_eid_with_data,
                }
            ]
        }

        expected_response = (
            existing_references["references"] + references_to_append["references"]
        )

        # Act
        result = self.variables_with_eid.append_references(references_to_append)

        # Assert
        self.assertEqual(result, expected_response)

    def test_set_references_append(self):
        # Arrange
        # change the eid for this test
        self.variables_with_eid.eid = append_references_eid
        # update the endpoint
        self.variables_with_eid.update_urls()

        references_to_append = references_exists
        existing_references = {"references": []}

        # Act
        try:
            self.variables_with_eid.set_references(references_to_append, append=True)
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

        # verify that references are successfully append
        set_references = self.variables_with_eid.get_references()["references"]
        expected_references = (
            references_to_append["references"] + existing_references["references"]
        )
        self.assertEqual(set_references, expected_references)

    def test_set_references_replace(self):
        # Arrange
        # change the eid for this test
        self.variables_with_eid.eid = replace_references_eid
        # update the endpoint
        self.variables_with_eid.update_urls()

        references_that_replace = references_exists

        # Act
        try:
            self.variables_with_eid.set_references(
                references_that_replace, append=False
            )
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

        # verify that references are successfully append
        set_references = self.variables_with_eid.get_references()["references"]
        expected_references = references_that_replace["references"]
        self.assertEqual(set_references, expected_references)

    def test_set_references_invalid_eid(self):
        # verify that a 'ValueError' is raised
        # Act and Assert
        with self.assertRaises(ValueError):
            self.variables_without_eid.assign_variables(self.variables_without_value)


if __name__ == "__main__":
    unittest.main()
