from pathlib import Path


class CommonPaths:
    @staticmethod
    def project_root() -> Path:
        return Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def env_booking_config_path() -> Path:
        return (
            CommonPaths.project_root()
            / "src"
            / "resources"
            / "env_configs_booking.yaml"
        )

    @staticmethod
    def env_json_placeholder_config_path() -> Path:
        return (
                CommonPaths.project_root()
                / "src"
                / "resources"
                / "env_configs_json_placeholder.yaml"
        )

