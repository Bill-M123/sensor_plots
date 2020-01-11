import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import bokeh


from bokeh.plotting import figure
import bokeh.plotting
from bokeh.io import output_notebook, curdoc, show

from working_plots.Simple_Scatter import Simple_Scatter

my_plot=Simple_Scatter()

x_samples = range(10)
y_samples = [x**2 if x<=5 else x**2-(x-1)**2 for x in x_samples]
z_samples = [x**2 if x<=5 else x**2-2*(x-1)**2 for x in x_samples]

df=pd.DataFrame(columns=['X','Y','Z'])
df['X']=x_samples
df['Y']=y_samples
df['Z']=z_samples

p = figure(plot_height=300, plot_width=900)
p = my_plot.make_bokeh_scatter(p,df,title='First Try')
show(p)
