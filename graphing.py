''' An interactive plot of the ``sin`` function. This example demonstrates
adding widgets and ``CustomJS`` callbacks that can update a plot.

.. bokeh-example-metadata::
    :apis: bokeh.plotting.figure.line, bokeh.layouts.column, bokeh.layouts.row, bokeh.models.CustomJS, bokeh.models.Slider
    :refs: :ref:`ug_interaction_js_callbacks_customjs`
    :keywords: javascript callback

'''
import numpy as np

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider, Band
from bokeh.plotting import figure, show

def graphData(red_x_points, red_y_points,blue_x_points, blue_y_points):
    x = np.linspace(0, 100, 500)
    y = np.sin(x)

    source = ColumnDataSource(data=dict(x=x, y=y))

    plot = figure(width=800, height=800)

    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    upper = 20
    band = Band(base='x', lower=0, upper=20, source=source,
            fill_alpha=0.3, fill_color="gray", line_color="black")
    plot.add_layout(band)



    plot.circle(x=red_x_points, y=red_y_points, size=10, fill_color="#ff5454")
    plot.circle(x=blue_x_points, y=blue_y_points, size=10, fill_color="#545dff")


    amp = Slider(start=0.1, end=10, value=1, step=.1, title="Amplitude")
    freq = Slider(start=0.1, end=10, value=1, step=.1, title="Frequency")
    phase = Slider(start=-6.4, end=6.4, value=0, step=.1, title="Phase")
    offset = Slider(start=-9, end=9, value=0, step=.1, title="Offset")
    

    callback = CustomJS(args=dict(source=source, amp=amp, freq=freq, phase=phase, offset=offset),
                        code="""
        const A = amp.value
        const k = freq.value
        const phi = phase.value
        const B = offset.value

        const x = source.data.x
        const y = Array.from(x, (x) => B + A*Math.sin(k*x+phi))
        source.data = { x, y }
    """)

    amp.js_on_change('value', callback)
    freq.js_on_change('value', callback)
    phase.js_on_change('value', callback)
    offset.js_on_change('value', callback)

    show(row(plot, column(amp, freq, phase, offset)))