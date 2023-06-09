
# JSON Schema Generator

Generate a JSON Schema from a JSON file


## Requirements
- No external dependencies required.
- **Python version 3.8 or above**



To run:
```python

python3 main.py <file_name>
```
Note: `<file_name>` should be the name of a json file in `./data` directory.


Example:
```python

python3 main.py data2.json
```


The Generated schema is stored in `./schema` directory.


## Tests

To run tests:

```python

python3 -m unittest tests.test_main
```