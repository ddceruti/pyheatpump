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

Then, run the test in `./test`

`pytest test`

## Documentation

Docs can be compiled with sphinx:

`pip install .[docs]`

Then build them:

`sphinx-build -b html ./docs/source build`
