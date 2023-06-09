import json
import argparse
from typing import Any


class JSONSchemaGenerator:
	"""
	A class to generate json schema.

	...

	Attributes
	----------
	file_path : str
		file path of json data
	schema_path : str
		file path of schema data
	parser : ArgumentParser
		cli arguments parser
	args: Namespace
		args retrieved from the cli

	Methods
	-------
	run():
		Runs the entire program.
	fail(message: str):
		Prints an error message to the cli.
	success(message: str):
		Prints a success message to the cli..
	get_type(val: Any):
		Returns the json type of a given value.
	get_json_data(file_path: str):
		Return json file data as dict
	generate_schema(message: dict):
		Generate schema for a given data
	write_data_to_file(data: dict, file_path: str):
		Writes processed data to a json file
	"""

	def __init__(self, prog: str = "Json Schema Generator", file_path: str = "") -> None:
		"""
		Constructs all the necessary attributes for the JSONSchemaGenerator object.

		Parameters
		----------
			name : str
				The name of the program
			file_path : str
				The file path; used to run the program outside of the cli
		"""

		self._create_parser(prog)
		self.file_path: str = file_path or f"data/{self.args.filename}" 
		self.schema_path: str = self.file_path.replace("data", "schema")

	def run(self):
		"""
		Runs the program: extract data from json file, add types and create a json schema
		"""		

		data: dict = self.get_json_data(self.file_path)

		# capture only attributes within "message"
		message: dict = data.get("message", {})

		processed: dict = self.generate_schema(message)
		self.write_data_to_file(processed, self.schema_path)
		self.success(f"Schema generated successfully and saved in {self.schema_path}")

	
	def fail(self, message):
		"""
		Prints a well formatted error message to the cli.

			Parameters:
				message (str): The message to be printed
		"""	

		self.parser.error(message)

	def success(self, message):
		"""
		Prints a success message to the cli.

			Parameters:
				message (str): The message to be printed
		"""			
		
		print(message)

	def _create_parser(self, prog: str) -> None:
		"""
		Creates a parser and args.

			Parameters:
				prog (str): The prog name
		"""		

		self.parser = argparse.ArgumentParser(
					prog=prog,
					description="Generate a JSON schema from a json file",
				)
		self.parser.add_argument("filename", 
				help="File name containing json data: file should be in `./data` directory",
				)
		self.args = self.parser.parse_args()

	def get_type(self, val: Any) -> str:
		"""
		Returns the json type of a given value.

			Parameters:
				val (Any): The value to get type for

			Returns:
				_type (str): The json type of the value
		"""	

		_type = "invalid"
		if isinstance(val, str):
			_type = "string"
		elif isinstance(val, int):
			_type = "integer"
		# elif isinstance(val, dict):
		# 	_type = "object"
		elif isinstance(val, list):
			if not val:
				_type = "enum"
			elif isinstance(val[0], str):
				_type = "enum"
			elif isinstance(val[0], dict):
				_type = "array"
		return _type

	def get_json_data(self, file_path: str) -> dict:
		"""
		Retrieves the json data from a file and return as dict.

			Parameters:
				file_path (str): The file path
		"""	

		try:
			with open(file_path, "r") as f:
				data = json.loads(f.read())
				return data
		except Exception as e:
			self.fail(e)

	def generate_schema(self, message: dict) -> dict:
		"""
		Generate schema for a given dict and returns a dict.

			Parameters:
				message (dict): The message dict

			Returns:
				processed (dict): The processed dict with types
		"""		

		processed: dict = {}
		for key, val in message.items():
			# handle nested data
			if isinstance(val, dict):
				processed[key] = self.generate_schema(val)
			
			else:
				processed[key] = {
					"type": self.get_type(val),
					"tag": "",
					"description": "",
					"required": False
				}
		
		return processed			

	def write_data_to_file(self, data: dict, file_path: str) -> None:
		"""
		Writes schema data to a json file.

			Parameters:
				data (dict): The data dict
		"""		

		# convert data to json
		try:
			json_data = json.dumps(data)
			with open(file_path, "w") as f:
				f.write(json_data)
		except Exception as e:
			self.fail(e)





if __name__ == "__main__":
	JSONSchemaGenerator().run()
	

