import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import bokeh

from bokeh.plotting import figure
import bokeh.plotting
from bokeh.io import output_notebook, curdoc, show

from plot_packages.Simple_Scatter import Simple_Scatter

my_plot=Simple_Scatter()

x_samples = range(12)
y_samples = [x**2 if x<=5 else x**2-(x-1)**2 for x in x_samples]
z_samples = [x**2 if x<=5 else x**2-2*(x-1)**2 for x in x_samples]
a_samples = [x**2 if x<=4 else x**2-(x-1)**2 for x in x_samples]
b_samples = [x**2 if x<=4 else x**2-1.3*(x-1)**2 for x in x_samples]

df=pd.DataFrame(columns=['X','Y','Z','A','B'])
df['X']=x_samples
df['Y']=y_samples
df['Z']=z_samples
df['A']=a_samples
df['B']=b_samples

p = figure(plot_height=300, plot_width=900)
p = my_plot.make_bokeh_scatter(p,df,title='First Try',xlabel='X readings')
show(p)
