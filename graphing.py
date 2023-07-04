## bokeh serve --show graph_data_points.py

import numpy as np
import Classifier as nn
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Slider
from bokeh.io import curdoc
from bokeh.plotting import figure, show



def graphData(red_x_points, red_y_points,blue_x_points, blue_y_points):
    

    
    
    hw11 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    hw12 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    hw13 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    hw21 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    hw22 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    hw23 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow11 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow12 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow21 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow22 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow31 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight")
    ow32  = Slider(start=-1, end=1, value=0, step=.1, title="Weight")

    # bias_1 = Slider(start=0, end=100, value=10, step=1, title="Bias_1")
    # bias_2 = Slider(start=0, end=100, value=0, step=1, title="Bias_2")
    def shadeRedBlue(attr, old, new):
        x_y = nn.ClassifyPoints(hw11.value, hw12.value, hw13.value,
                                hw21.value, hw22.value, hw23.value,
                                ow11.value, ow12.value,
                                ow21.value, ow22.value,
                                ow31.value, ow32.value)
        x = x_y[0]
        y = x_y[1]
        bx = x_y[2]
        by = x_y[3]
        redSource.data = dict(x=x, y=y)
        blueSource.data = dict(x=bx, y=by)
        
    plot = figure(width=800, height=800)
    redSource = ColumnDataSource()
    blueSource = ColumnDataSource()
    
    
   
    
    hw12.on_change('value', shadeRedBlue)
    hw11.on_change('value', shadeRedBlue)
    hw13.on_change('value', shadeRedBlue)
    hw21.on_change('value', shadeRedBlue)
    hw22.on_change('value', shadeRedBlue)
    hw23.on_change('value', shadeRedBlue)
    ow11.on_change('value', shadeRedBlue)
    ow12.on_change('value', shadeRedBlue)
    ow21.on_change('value', shadeRedBlue)
    ow22.on_change('value', shadeRedBlue)
    ow31.on_change('value', shadeRedBlue)
    ow32.on_change('value', shadeRedBlue)

        

    
    plot.rect(x='x', y='y', source=redSource, width=1, height=1, fill_color='red', fill_alpha = 0.2, line_color=None)
    plot.rect(x='x', y='y', source=blueSource, width=1, height=1, fill_color='blue', fill_alpha = 0.2, line_color=None)




    plot.circle(x=red_x_points, y=red_y_points, size=10, fill_color="#ff5454")
    plot.circle(x=blue_x_points, y=blue_y_points, size=10, fill_color="#545dff")
    
    plot.add_tools(HoverTool(tooltips=[('X','@x'), ('Y', '@y')]))


    layout = column(plot, hw11, hw12, hw13,
    hw21, hw22, hw23,
    ow11, ow12,
    ow21, ow22,
    ow31, ow32)
    curdoc().add_root(layout)
 