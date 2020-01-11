import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import bokeh

from bokeh.plotting import figure
import bokeh.plotting
from bokeh.io import output_notebook, curdoc, show

from plot_packages.Categorical_Scatter import Categorical_Scatter

my_plot=Categorical_Scatter()

tools=['T3','T5','T9','T37']
x_samples = range(12)
y_samples = ['T5','T3','T9','T37','T5','T5','T5','T5','T5','T3','T9','T37']
z_samples = ['T5','T3','T9','T37','T3','T3','T3','T5','T3','T3','T9','T37']
a_samples = ['T5','T9','T9','T37','T9','T9','T5','T5','T9','T9','T9','T37']


df=pd.DataFrame(columns=['X','Y','Z','A'])
df['X']=x_samples
df['Y']=y_samples
df['Z']=z_samples
df['A']=a_samples


p = figure(plot_height=300, plot_width=900,y_range=tools)
p = my_plot.make_bokeh_cat_scat(p,df,title='First Try',xlabel='X readings')
show(p)
