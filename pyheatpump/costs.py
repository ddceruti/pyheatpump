"""This file contains the costs for the heat pumps."""

import bisect

# dict containing the costs for the heat pumps for size [MW] : cost [EUR/MW_th]
# source: Danish Energy Agency (Feb. 2025), excess heat heat pump (from1  to 10 MW)
# source: Danish Energy Agency (Feb. 2025), seawater heat pump (20 MW)
COST_REGRESSION = {
    1.: 1.32e6,
    3.: 0.91e6,
    10.: 0.71e6,
    20.: 0.51e6
}


def interpolate(
    size: float,
    costs: dict = None) -> float:
    """Calculate the costs of a heat pump based on a linear interpolation
    between two sizes.

    Args:
        size (float): Size of the heat pump [MW].
        costs (dict): Dictionary containing the costs for the heat pumps for size [MW] : cost [EUR/MW_th].

    Returns:
        float: Cost of the heat pump [EUR].
    """
    if costs is None:
        costs = COST_REGRESSION

    if size < 0:
        raise ValueError(f"The size of the heat pump {size} must be positive.")

    if size in costs:
        return costs[size]

    keys = sorted(costs.keys())
    pos = bisect.bisect_right(keys, size)

    if pos == 0:
        raise ValueError(f"The size of the heat pump {size} is too small.")
    if pos == len(keys):
        return costs[keys[-1]]  # If size exceeds the max key, return the max cost.

    x1, x2 = keys[pos - 1], keys[pos]
    y1, y2 = costs[x1], costs[x2]

    return y1 + (y2 - y1) * (size - x1) / (x2 - x1)
