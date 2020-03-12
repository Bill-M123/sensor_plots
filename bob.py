from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
import pandas as pd
import os

import scipy.fftpack

from plot_packages.Simple_Scatter import Simple_Scatter
from plot_packages.FFT_Scatter import FFT_Scatter
from plot_packages.Sig_Analysis import Sig_Analysis

data_dir=os.getcwd()+'/data/'

make_simple=Simple_Scatter()
make_fft=FFT_Scatter()
an_sigs=Sig_Analysis()

basic_square=pd.read_csv(data_dir+'basic_square.csv',index_col=0)
noisy_square=pd.read_csv(data_dir+'noisy_square.csv',index_col=0)
basic_square=basic_square.loc[basic_square.X<100,:]
noisy_square=noisy_square.loc[noisy_square.X<100,:]
print('Noisy_Square\n',noisy_square.head())
p = figure(plot_height=300, plot_width=900)
p=make_simple.make_bokeh_scatter(p,noisy_square,title='Noisy Square',color='navy')
show(p)

print('basic_square\n',basic_square.head(3))
x_fft,ypower_fft=an_sigs.get_fft_powers_single(basic_square.X.values,basic_square.Y.values)

basic_fft=pd.DataFrame()
basic_fft['X']=x_fft
basic_fft['Y']=ypower_fft
print(basic_fft.head(4))


p = figure(plot_height=300, plot_width=900)
#p=make_simple.make_bokeh_scatter(p,basic_fft,title='Basic Square FFT',color='maroon')
x_fft,ypower_fft=an_sigs.get_fft_powers_single(noisy_square.X.values,noisy_square.Y_n.values)

noisy_fft=pd.DataFrame()
noisy_fft['X']=x_fft
noisy_fft['Y']=ypower_fft
print(basic_fft.head(4))

p=make_simple.make_bokeh_scatter(p,noisy_fft,title='Noisy Square FFT',color='yellow')
show(p)

df=basic_fft.copy()
df['Y_n']=noisy_fft['Y']
df['dif']=df['Y']-df['Y_n']

p = figure(plot_height=300, plot_width=900)
p.vbar(df.X.values,width=0.75,top=df.dif.values,bottom=0,color='maroon',
    name='Difference Square v noisy square')
show(p)




'''
output_file("bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (fruit, year) for fruit in fruits for year in years ]
print('zips',list(zip(data['2015'], data['2016'], data['2017'])))
counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack
print('counts',counts)

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None


show(p)'''
