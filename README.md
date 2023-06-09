
# JSON Schema Generator

Generate a JSON Schema from a JSON file


To run:
```python

python3 main.py <file_name>
```
Note: `<file_name>` should be the name of a json file in `./data` directory.


Example:
```python

python3 main.py data2.json
```


The Generated schema is store in `./schema` directory.


### Tests

To run:

```python

python3 -m unittest tests.test_main
```