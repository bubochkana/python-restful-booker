import json

from src.common.common_paths import root_dir


def load_schema(schema_file_name):
    schema_path = root_dir.joinpath('rest_api').joinpath('schemas').joinpath(schema_file_name)
    with open(schema_path) as schema_file:
        return json.load(schema_file)
