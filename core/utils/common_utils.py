import json
from pathlib import Path

SCHEMA_DIR = (Path(__file__).resolve()
              .parent
              .parent
              .parent
              .joinpath('rest_api')
              .joinpath('schemas'))


def load_schema(schema_file_name):
    schema_path = SCHEMA_DIR.joinpath(schema_file_name)
    with open(schema_path) as schema_file:
        return json.load(schema_file)
