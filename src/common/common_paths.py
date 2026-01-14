from pathlib import Path
from typing import Literal

EnvName = Literal["dev", "qa"]


class CommonPaths:
    @staticmethod
    def project_root() -> Path:
        return Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def env_config_file_path(env: EnvName) -> Path:
        filename = f"{env}_configs.yaml"
        return (CommonPaths.project_root()
                .joinpath('src')
                .joinpath('resources')
                .joinpath(f'{env}')
                .joinpath(filename)
        )


