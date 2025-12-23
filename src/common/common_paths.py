from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent

def get_dev_env_dir():
    return root_dir.joinpath('src').joinpath('resources').joinpath('dev')

def get_qa_env_dir():
    return root_dir.joinpath('src').joinpath('resources').joinpath('qa')
