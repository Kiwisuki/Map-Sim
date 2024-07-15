# Covid Grid Simulation

[![Python 3.9](https://img.shields.io/badge/Python-3.9-3776AB)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## About the Project

Simple simulation of a grid with people and a virus spreading. The simulation is similar to the [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) but with a virus spreading.

## Generated Visual

![Demo](output/output.gif)

## Tools Used in This Project

* [poetry](https://github.com/python-poetry/poetry): Python packaging and dependency management.
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting.
* [black](https://pypi.org/project/black/): Python code formatter.
* [isort](https://pypi.org/project/isort/): Library to sort imports alphabetically.
* [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter (flake8 replacement).
* [mypy](https://mypy.readthedocs.io/en/stable/): Static type checker.

## Getting Started

1. Set up and install the environment: `$ make env`
2. (Optional) Install the git hook scripts: `$ make dependencies`
3. (Optional) Run all pre-commit hooks: `$ pre-commit run --all-files`


## Contact

[Marius Arlauskas](marius.arlauskas01.dev@gmail.com)
