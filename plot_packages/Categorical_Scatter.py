class Categorical_Scatter:

    def __init__(self):
        ''' Constructor for this class. '''

        return

    def make_bokeh_cat_scat(self,p,df,title='Needs Title',xlabel='Needs xlabel',ylabel='Needs ylabel',color='navy'):
        '''Make a simple bokeh scatter plot with categorical on y axis.  Has
        simple controls for scaling, positioning, and reset.

        Assumes a figure p pre-established
        df is a dataframe with xvalues in column 0
        titles/labels are simple strings'''

        from bokeh.palettes import brewer
        from bokeh.models import ColumnDataSource,Legend, LegendItem

        data_names=df.columns

        colors=brewer['RdBu'][4]
        legend_items=[]

        for y in range(1,len(data_names)):
            color=colors[y%4]
            r=p.circle(x=df.iloc[:,0],y=df.iloc[:,y],size=7.5,color=color)
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

        return p
