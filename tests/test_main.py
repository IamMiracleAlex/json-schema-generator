import unittest
import os

from main import JSONSchemaGenerator


class JSONSchemaGeneratorTest(unittest.TestCase):
	def setUp(self) -> None:
		self.test_file_path = "tests/test_data.json"
		self.schema_generator = JSONSchemaGenerator("Test Generator", self.test_file_path)

	def test_json_schema_generator(self):
		"Assert json schema generator works properly"

		self.schema_generator.run()
		test_schema_path = self.test_file_path.replace("data", "schema")
		self.assertTrue(os.path.exists(test_schema_path))


	def test_generate_schema_method_for_string(self):
		"""
		Assert the generate schema method works as expected for strings
		Assert data in "attributes" key is ignored
		   
		"""

		data = {
			"attributes": {
				"appName": "ABCDEFGHIJKLMNOPQRSTUVW",
				},
			"message": {
				"name": "John",
				}
		}
		expected = {
			"name": {
				"type": "string",
				"tag": "",
				"description": "",
				"required": False
			},
		}
		processed = self.schema_generator.generate_schema(data["message"])

		self.assertEqual(expected, processed)

	def test_generate_schema_method_for_integer(self):
		"""Assert the generate schema method works as expected for integer"""

		data = {
			"message": {
				"time": 890,
				}
		}

		expected = {
			"time": {
				"type": "integer",
				"tag": "",
				"description": "",
				"required": False
			},
		}
		processed = self.schema_generator.generate_schema(data["message"])

		self.assertEqual(expected, processed)

	def test_generate_schema_method_for_enum(self):
		"""Assert the generate schema method works as expected for enum"""

		data = {
			"message": {
				"countries": [
					"ABCDEFGHIJKLMNOPQRSTUVWXYZA",
        			"ABCDEFGHIJKLMNOPQ",
					],
				}
		}

		expected = {
			"countries": {
				"type": "enum",
				"tag": "",
				"description": "",
				"required": False
			},
		}
		processed = self.schema_generator.generate_schema(data["message"])

		self.assertEqual(expected, processed)


	def test_generate_schema_method_for_array(self):
		"""Assert the generate schema method works as expected for array"""

		data = {
			"message": {
				"cities": [
					{
						"town": "ABCDEFGHIJKLMNOPQ"
					}
					],
				}
		}

		expected = {
			"cities": {
				"type": "array",
				"tag": "",
				"description": "",
				"required": False
			},
		}
		processed = self.schema_generator.generate_schema(data["message"])

		self.assertEqual(expected, processed)