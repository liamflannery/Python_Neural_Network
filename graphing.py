## bokeh serve --show graph_data_points.py

import numpy as np
import neural_network as nn
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Slider
from bokeh.io import curdoc
from bokeh.plotting import figure, show



def graphData(red_x_points, red_y_points,blue_x_points, blue_y_points):
    weight_1_1 = Slider(start=-1, end=1, value=-0.8, step=.1, title="Weight 1_1")
    weight_2_1 = Slider(start=-1, end=1, value=-0.9, step=.1, title="Weight 2_1")
    weight_1_2 = Slider(start=-1, end=1, value=-0.8, step=.1, title="Weight 1_2")
    weight_2_2 = Slider(start=-1, end=1, value=-0.7, step=.1, title="Weight 2_2")

    bias_1 = Slider(start=0, end=100, value=10, step=1, title="Bias_1")
    bias_2 = Slider(start=0, end=100, value=0, step=1, title="Bias_2")
    
    plot = figure(width=800, height=800)
    redSource = ColumnDataSource()
    blueSource = ColumnDataSource()
    def shadeRedBlue(attr, old, new):
        x_y = nn.ClassifyPoints(weight_1_1.value, weight_2_1.value, weight_1_2.value, weight_2_2.value, bias_1.value, bias_2.value)
        x = x_y[0]
        y = x_y[1]
        bx = x_y[2]
        by = x_y[3]
        redSource.data = dict(x=x, y=y)
        blueSource.data = dict(x=bx, y=by)
    
    shadeRedBlue(None, None, None)
    

        

    
    plot.rect(x='x', y='y', source=redSource, width=1, height=1, fill_color='red', fill_alpha = 0.2, line_color=None)
    plot.rect(x='x', y='y', source=blueSource, width=1, height=1, fill_color='blue', fill_alpha = 0.2, line_color=None)




    plot.circle(x=red_x_points, y=red_y_points, size=10, fill_color="#ff5454")
    plot.circle(x=blue_x_points, y=blue_y_points, size=10, fill_color="#545dff")
    
    plot.add_tools(HoverTool(tooltips=[('X','@x'), ('Y', '@y')]))


    weight_1_1.on_change('value', shadeRedBlue)
    weight_2_1.on_change('value', shadeRedBlue)
    weight_1_2.on_change('value', shadeRedBlue)
    weight_2_2.on_change('value', shadeRedBlue)
    bias_1.on_change('value', shadeRedBlue)
    bias_2.on_change('value', shadeRedBlue)

    layout = column(plot, weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2)
    curdoc().add_root(layout)
 