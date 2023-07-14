## bokeh serve --show graph_data_points.py

import numpy as np
import Classifier as nn
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, HoverTool, Slider, Text
from bokeh.io import curdoc
from bokeh.plotting import figure, show



def graphData(red_x_points, red_y_points,blue_x_points, blue_y_points, training_red, training_blue):
    

    
    
    hw11 =  Slider(start=-1, end=1, value=-0.6, step=.1, title="Weight 11")
    hw12 =  Slider(start=-1, end=1, value=-0.3, step=.1, title="Weight 12")
    hw13 =  Slider(start=-1, end=1, value=0.2, step=.1, title="Weight 13")
    hw21 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight 21")
    hw22 =  Slider(start=-1, end=1, value=0.2, step=.1, title="Weight 22")
    hw23 =  Slider(start=-1, end=1, value=-.7, step=.1, title="Weight 23")
    ow11 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight O11")
    ow12 =  Slider(start=-1, end=1, value=0.6, step=.1, title="Weight O12")
    ow21 =  Slider(start=-1, end=1, value=0, step=.1, title="Weight O21")
    ow22 =  Slider(start=-1, end=1, value=-.4, step=.1, title="Weight O22")
    ow31 =  Slider(start=-1, end=1, value=-.6, step=.1, title="Weight O31")
    ow32  = Slider(start=-1, end=1, value=0.5, step=.1, title="Weight O32")
    b1 = Slider(start=-100, end=100, value=0, step=1, title="Bias 1")
    b2 = Slider(start=-100, end=100, value=0, step=1, title="Bias 2")
    b3 = Slider(start=-100, end=100, value=23, step=1, title="Bias 3")
    b4 = Slider(start=-100, end=100, value=0, step=1, title="Bias 4")
    b5 = Slider(start=-100, end=100, value=0, step=1, title="Bias 5")
    
    graphResolution = 1
    # bias_1 = Slider(start=0, end=100, value=10, step=1, title="Bias_1")
    # bias_2 = Slider(start=0, end=100, value=0, step=1, title="Bias_2")
    def shadeRedBlue(attr, old, new):
        weights = [ hw11.value, hw12.value, hw13.value,
                    hw21.value, hw22.value, hw23.value,
                    ow11.value, ow12.value,
                    ow21.value, ow22.value,
                    ow31.value, ow32.value]
        biases = [
            b1.value, b2.value, b3.value, b4.value, b5.value
        ]
        x_y = nn.ClassifyPoints(weights,biases,
                                training_red, training_blue, graphResolution)
        x = x_y[0]
        y = x_y[1]
        bx = x_y[2]
        by = x_y[3]
        print("Cost: ", x_y[4])
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
    b1.on_change('value', shadeRedBlue)
    b2.on_change('value', shadeRedBlue)
    b3.on_change('value', shadeRedBlue)
    b4.on_change('value', shadeRedBlue)
    b5.on_change('value', shadeRedBlue)
    
        

    
    plot.rect(x='x', y='y', source=redSource, width=1/graphResolution, height=1/graphResolution, fill_color='red', fill_alpha = 0.2, line_color=None)
    plot.rect(x='x', y='y', source=blueSource, width=1/graphResolution, height=1/graphResolution, fill_color='blue', fill_alpha = 0.2, line_color=None)




    plot.circle(x=red_x_points, y=red_y_points, size=10, fill_color="#ff5454")
    plot.circle(x=blue_x_points, y=blue_y_points, size=10, fill_color="#545dff")
    
    plot.add_tools(HoverTool(tooltips=[('X','@x'), ('Y', '@y')]))

    inputs = column(hw11, hw12, hw13,
    hw21, hw22, hw23,
    ow11, ow12,
    ow21, ow22,
    ow31, ow32, b1, b2, b3, b4, b5)
    layout = row([plot,inputs])

    curdoc().add_root(layout)
 