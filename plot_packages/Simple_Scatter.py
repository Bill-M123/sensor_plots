class Simple_Scatter:

    def __init__(self):
        ''' Constructor for this class. '''

        return

    def make_bokeh_scatter(self,p,df,title='Needs Title',xlabel='Needs xlabel',ylabel='Needs ylabel',color='default'):
        '''Make a simple bokeh scatter plot.  Has simple controls for scaling,
        positioning, and reset.

        Assumes a figure p pre-established
        df is a dataframe with xvalues in column 0
        titles/labels are simple strings'''

        from bokeh.palettes import brewer
        from bokeh.models import ColumnDataSource,Legend, LegendItem
        from bokeh.io import show, output_file

        data_names=df.columns
        print(data_names)
        print(df.head(3))

        colors=brewer['RdBu'][4]
        legend_items=[]

        for y in range(1,len(data_names)):
            if color=='default':
                pcolor=colors[y%4]
                print('y',y,'pcolor',pcolor)
            else:
                pcolor=color
                print('y',y,'pcolor',pcolor)
            r=p.circle(x=df.iloc[:,0],y=df.iloc[:,y],size=7.5,color=pcolor)
            #items.append((data_names[y],[r]))
            legend_items.append(LegendItem(label=data_names[y], renderers=[r]))

        #p.plot_height = 300
        #p.plot_width = 800

        p.xaxis.axis_label = xlabel
        p.yaxis.axis_label = ylabel

        p.title.text = title

        legend1 = Legend(items=legend_items, location='center')
        p.add_layout(legend1,'right')
        p.legend.click_policy="hide"
        show(p)
        return p
