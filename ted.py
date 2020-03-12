import matplotlib.pyplot as plt
import pandas as pd

from plot_packages.Matplotlib_Basics import Matplotlib_Basics

import os

data_dir=os.getcwd()+'/data/'

df=pd.read_csv(data_dir+'corvid19_summary_dat.csv')

df_test=df[['Unnamed: 0','Cases','Deaths','Recoveries']]
try:
    df_test=df_test.rename(columns={'Unnamed: 0':'Xs'})
except:
    pass
print(df_test.head(2))

mb=Matplotlib_Basics()

#mb.basic_plot(df_test,title='df_test')

#df_test=df[['Cases','Deaths']]
#mb.scatter_plot(df_test,title='Corvid19',x_label='Cases by Country',y_label='Deaths')

df_test=df[['Cases','Deaths','Recoveries']]
mb.matshow(df_test.corr(),title='Correlation Matrix')
