import scipy.fftpack

class FFT_Scatter:


    def __init__(self):
        ''' Constructor for this class. '''

        return

    def make_single_fft_b_scatter(self,p,df,title='FFT Needs Title',
        xlabel='Needs xlabel',ylabel='Needs ylabel',color='navy'):
        '''Make a simple bokeh fft scatter plot.  Has simple controls for scaling,
        positioning, and reset.

        Assumes a figure (p) pre-established with sizing requirements
        df is a dataframe with xvalues (sample times in seconds) in column 0
        titles/labels are simple strings'''

        from bokeh.palettes import brewer
        from bokeh.models import ColumnDataSource,Legend, LegendItem
        import scipy.fftpack
        import numpy as np

        data_names=df.columns

        colors=brewer['RdBu'][4]
        legend_items=[]

        xs=df.index[:int(len(df)/2)]
        power_length=len(xs)

        for y in range(1,len(data_names)):

            yf = scipy.fftpack.fft(df[data_names[y]])
            power=np.abs(yf[:power_length])

            color=colors[y%4]

            r=p.circle(x=xs,y=power,size=7.5,color=color)
            legend_items.append(LegendItem(label=data_names[y], renderers=[r]))


        p.xaxis.axis_label = xlabel
        p.yaxis.axis_label = ylabel

        p.title.text = title

        legend1 = Legend(items=legend_items, location='center')
        p.add_layout(legend1,'right')
        p.legend.click_policy="hide"

        return p
