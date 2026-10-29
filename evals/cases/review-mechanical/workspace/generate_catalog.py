"""Generate static catalog entries; not used by the endpoint."""
import json


def generate(version):
    return [{"id": i, "generator": version} for i in range(1200)]


if __name__ == "__main__":
    print(json.dumps(generate(2), indent=2))
