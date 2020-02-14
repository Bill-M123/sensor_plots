import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import bokeh

from bokeh.plotting import figure
import bokeh.plotting
from bokeh.io import output_notebook, curdoc, show

from plot_packages.Cat_w_Float_Scatter import Categorical_w_Float_Scatter

my_plot=Categorical_w_Float_Scatter()



cat_order=['A','B','C','D','E','F']
x_samples = range(12)
y_samples = [3,3,3,3,3,3,3,3,3,3,3,3]
z_samples = [1,2,3,4,5,6,5,4,3,2,1,2]
a_samples = ['A','B','C','D','E','F','C','C','B','B','A','A']


df=pd.DataFrame(columns=['X','Y','Z','A'])
df['X']=x_samples
df['Y']=y_samples
df['Z']=z_samples
df['A']=a_samples


p = figure(plot_height=300, plot_width=900)
p = my_plot.make_bokeh_cat_float_scat(p,df,cat_order,
    title='First Try',xlabel='X readings')
show(p)
