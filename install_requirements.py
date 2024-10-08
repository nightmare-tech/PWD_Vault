# adding packages in requirements.txt to pyproject.toml

import subprocess
from typing import TextIO


def install_requirements(filename: TextIO) -> None:
    with open(filename, "r") as file:
        packages = file.readlines()
    for package in packages:
        package = package.strip()
        if package and not package.startswith("#"):
            subprocess.run(["poetry", "add", package], check=True)


install_requirements("requirements.txt")
