class Categorical_w_Float_Scatter:

    def __init__(self):
        ''' Constructor for this class. '''

        return

    def make_bokeh_cat_float_scat(self,p,df,cat_order,
    title='Needs Title',xlabel='Needs xlabel',
    ylabel='Needs ylabel',cat_color='navy'):
        '''Make a simple bokeh scatter plot with categorical on y axis.  Has
        simple controls for scaling, positioning, and reset.

        Assumes a figure p pre-established
        df is a dataframe with:
              xvalues in column 0
              float values in columns 1 to col_max-1
              cat values in col_max

        cat_order is an ordered list that aligns cat axis
        and contains axis_labelunique categories

        titles/labels are simple strings'''

        from bokeh.palettes import brewer
        from bokeh.models import ColumnDataSource,\
            Legend, LegendItem, LinearAxis,FactorRange,\
            CategoricalAxis

        data_names=df.columns

        colors=brewer['RdBu'][4]
        legend_items=[]

        for y in range(1,len(data_names)):
            color=colors[y%4]
            r=p.circle(x=df.iloc[:,0],y=df.iloc[:,y],size=7.5,color=color)
            #items.append((data_names[y],[r]))
            legend_items.append(LegendItem(label=data_names[y], renderers=[r]))

        #Set second y_axis
        print(type(cat_order),cat_order)
        p.extra_y_ranges = {"cat_ax": FactorRange(factors=cat_order)}

        #Add second y axis
        p.add_layout(CategoricalAxis(y_range_name="cat_ax"),"right")
        last_col=len(df.columns)-1
        r=p.circle(x=df.iloc[:,0],y=df.iloc[:,last_col],
            y_range_name="cat_ax",size=7.5,color=cat_color)
        legend_items.append(LegendItem(label=data_names[last_col], renderers=[r]))

        p.xaxis.axis_label = xlabel
        p.yaxis.axis_label = ylabel

        p.title.text = title

        legend1 = Legend(items=legend_items, location='center')
        p.add_layout(legend1,'right')
        p.legend.click_policy="hide"

        return p
