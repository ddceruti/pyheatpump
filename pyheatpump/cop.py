"""Calculates the cop of large scale heat pumps based on the
Jesper et al. regression models.

The model is based on the following paper:
 @article{jesper2021large,
    title={Large-scale heat pumps: Uptake and performance modelling of market-available devices},
    author={Jesper, Mateo and Schlosser, Florian and Pag, Felix and Walmsley, Timothy Gordon and Schmitt, Bastian and Vajen, Klaus},
    journal={Renewable and Sustainable Energy Reviews},
    volume={137},
    pages={110646},
    year={2021},
    publisher={Elsevier}
    }
"""

import warnings
from typing import Union

__author__ = "Amedeo Ceruti"


# Hardcoded dictionary with heat pump parameters from paper
HP_PARAMETERS = {
    "conventional": {
        "T_sink_out_low": 0,
        "T_sink_out_high": 100,
        "a": 1.4480E12,
        "b": 88.730,
        "c": -4.9460,
        "d": 0.0000
    },
    "very high temperature": {
        "T_sink_out_low": 100,
        "T_sink_out_high": 160,
        "a": 1.9118,
        "b": -0.89094,
        "c": 0.67895,
        "d": 0.044189
    }
}


def classify_hp(T_sink_out: float,
                parameters: Union[dict, None] = None) -> str:
    """
    Classify the heat pump based on the sink temperature (delivered temperature).

    Args:
        T_sink_out (float): Outlet temperature of the sink.
        parameters (dict): Parameters of the heat pump model. Default is None, in which case
            the default, hardcoded parameters are used.

    Returns:
        str: Type of heat pump based on the sink (either "conventional",
            "very high temperature" or None if the conditions are not met).
    """
    _type = None
    for key, values in parameters.items():
        # if between the source and sink temperatures return the type
        cond_sink = values['T_sink_out_low'] <= T_sink_out <= values['T_sink_out_high']
        if cond_sink:
            _type = key
    return _type


def jesper_conventional(delta_T: float,
                        T_sink_out: float,
                        parameters: dict = None) -> float:
    """Conventional heat pump model according to Jesper et al.

    Args:
        Delta_T (float): Temperature difference between heat source and sink.
        T_sink_out (float): Outlet temperature of the sink.
        parameters (dict): Parameters of the heat pump model.

    Returns:
        float: Coefficient of performance of the conventional heat pump.

    The model is defined as:

    .. math::
        COP = a \cdot (\Delta T + 2b)^c \cdot (T_{sink} + b)^d
    """
    term1 = parameters["a"]*(delta_T + 2*parameters["b"])**parameters["c"]
    term2 = (T_sink_out + parameters["b"])**parameters["d"]
    return term1 * term2


def jesper_very_high(delta_T: float,
                     T_sink_out: float,
                     parameters: dict) -> float:
    """Calculate the very high temperature heat pump efficiency.

    Args:
        delta_T (float): Temperature difference between heat source and heat sink [K].
        T_sink_out (float): Temperature of the heat sink outlet [°C].
        parameters (dict): Dictionary containing the parameters of the heat pump.

    Returns:
        float: Coefficient of performance of the high temperature heat pump.

    The model is defined as:

    .. math::
        COP = a \cdot (\Delta T + 2d)^b \cdot (T_{sink} + d)^c
    """
    term1 = parameters["a"]*(delta_T + 2*parameters["d"])**parameters["b"]
    term2 = (T_sink_out + parameters["d"])**parameters["c"]
    return term1*term2


def carnot(delta_T: float,
           T_sink_out: float,
           quality_factor: float = 0.4) -> float:
    """Calculate the Carnot efficiency of the heat pump.

    Args:
        delta_T (float): Temperature difference between heat source and heat sink [K].
        T_sink_out (float): Temperature of the heat sink outlet [K].
        quality_factor (float): Quality factor of the heat pump. Default is 0.4.

    Returns:
        float: Coefficient of performance of the heat pump.
    
    The model is defined as:

    .. math::

        COP = quality_factor \cdot T_{sink} / \Delta T
    
    """
    cop = quality_factor*(T_sink_out/delta_T)
    return cop


def calculate(source_temperature: float,
              sink_temperature: float,
              parameters: dict = None) -> float:
    """Main calculation function for the COP of large scale heat pumps.

    Classifies the HP into a type and then calculates the COP with a regression
    or a Carnot model depending on the boundary conditions.

    Args:
        source_temperature (float): Temperature of the heat source in °C.
        sink_temperature (float): Temperature of the heat sink output in °C.
        parameters (dict): Dictionary of parameters for the model (see the default parameters, HP_PARAMETERS).

    Returns:
        float: Coefficient of performance of the heat pump.
    """
    if parameters is None:
        parameters = HP_PARAMETERS
    else:
        # check if conforms to the dict structure
        for key, value in HP_PARAMETERS.items():
            if key not in parameters:
                raise ValueError(f"The key {key} is missing in the parameters dict.")
            for k, v in value.items():
                if k not in parameters[key]:
                    raise ValueError(f"The key {k} is missing in the parameters dict.")

    hp = classify_hp(sink_temperature, parameters)
    if hp is None:
        warnings.warn(f"The heat pump with sink temperature {sink_temperature} °C could not be classified. The COP will be calculated with a Carnot model.")

    T = sink_temperature + 273.15  # °C to K
    delta = sink_temperature - source_temperature

    p = parameters[hp]
    if hp == "conventional":
        cop = jesper_conventional(delta, T, p)
        if 10 > delta > 78:
            warnings.warn(f"The temperature difference {delta} is outside the range of the model [10, 78] K.")
        if -10 > source_temperature > 60:
            warnings.warn(f"The temperature of the source {source_temperature} is outside the range of the model [25, 110] K.")    
    elif hp == "very high temperature":
        cop = jesper_very_high(delta, T, p)
        if 25 > delta > 95:
            warnings.warn(f"The temperature difference {delta} is outside the range of the model [10, 78] K.")
        if 25.1 > source_temperature > 110.1:
            warnings.warn(f"The temperature of the source {source_temperature} is outside the range of the model [25, 110] K.")
    else:
        cop = carnot(delta, T)

    return cop
