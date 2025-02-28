# Modeling Large Scale and High Temperature Heat Pumps

A python package to calculate coefficients of performance (COP) and power
outputs of large scale and high temperature (up to 160 °C) heat pumps.

## Install

Requires Python >= 3.8.

`pip install .`

## Usage

Check the examples folder.

## Testing

Requires pytest:

`pip install .[testing]`

Then, run the tests in `./test`

`pytest test/installation.py test/cops.py`

## Documentation

Docs can be compiled with sphinx:

`pip install .[docs]`

Generate the api doc of the modules in `./pyheatpump`

`sphinx-apidoc -o docs/source/modules pyheatpump`

Then build them:

`cd docs`
`sphinx-build -b html source build`
