from pathlib import Path


class CommonPaths:
    @staticmethod
    def project_root() -> Path:
        return Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def env_config_path() -> Path:
        return (
            CommonPaths.project_root()
            / "src"
            / "resources"
            / "env_configs_booking.yaml"
        )

    #TODO - maybe an additional method is needed for json placeholder

