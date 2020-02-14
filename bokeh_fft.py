import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import bokeh

from bokeh.plotting import figure
import bokeh.plotting
from bokeh.io import output_notebook, curdoc, show

import scipy.fftpack

from plot_packages.Simple_Scatter import Simple_Scatter
from plot_packages.FFT_Scatter import FFT_Scatter
from plot_packages.Make_Wave_Data import Make_Wave_Data


scatter_plot=Simple_Scatter()
fft_plot=FFT_Scatter()
wave_data=Make_Wave_Data()

# Create sample data
df=wave_data.make_square_wave()
df2=wave_data.add_noise(df,fs_ratio=0.2)


p = figure(plot_height=300, plot_width=900)
p = scatter_plot.make_bokeh_scatter(p,df,title='First Try',xlabel='X readings')
show(p)
p = figure(plot_height=300, plot_width=900)
p = scatter_plot.make_bokeh_scatter(p,df2,title='First Try+noise',xlabel='X readings')
show(p)

p = figure(plot_height=300, plot_width=900)
p=fft_plot.make_single_fft_b_scatter(p,df)
show(p)
p = figure(plot_height=300, plot_width=900)
p=fft_plot.make_single_fft_b_scatter(p,df2)
show(p)
