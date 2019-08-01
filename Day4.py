# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:26:00 2019

@author: STEM
"""
import pandas as pd
dir(pandas)
import plotly
from plotly.offline import plot
import plotly.graph_objs as go


wodf = pd.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
wodf
