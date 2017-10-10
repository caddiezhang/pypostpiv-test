"""Module for visualizing PIV data objects."""

import numpy as np
import bokeh
import pandas as pd
import holoviews as hv

hv.extension('bokeh')
from holoviews.plotting.bokeh.element import (line_properties, fill_properties,
                                              text_properties)

def plot(piv_data):
    """Generates a plot of your PIV data.
    """

    

