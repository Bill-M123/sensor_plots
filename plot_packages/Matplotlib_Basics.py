class Matplotlib_Basics():

    def __init__(self):
        return

    def basic_plot(self,df,title='Title',x_label='x_axis',y_label='y_axis',
        ylim=None,xlim=None,figsize=(10,3.5),dpi=100):
        ''' df is a dataframe where the first column is the X data,
        all other columns are y data.'''
        #import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        colors=plt.cm.brg(np.linspace(0,1,len(df.columns)-1))
        cols=df.columns
        print(cols)

        plt.figure(figsize=figsize,dpi=dpi)
        for line in range(1,len(df.columns)):
            plt.plot(df[cols[0]],df[cols[line]],label=cols[line],color=colors[line-1])

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='best')
        if ylim!=None:
            plt.ylim(xlim[0],xlim[1])
        if xlim!=None:
            plt.xlim(xlim[0],xlim[1])
        plt.show()
        return

    def scatter_plot(self,df,title='Title',x_label='x_axis',y_label='y_axis',
        ylim=None,xlim=None,figsize=(10,3.5),dpi=100):
        ''' df is a dataframe where the first column is the X data,
        all other columns are y data. Returns Scatter plot'''
        #import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        colors=plt.cm.brg(np.linspace(0,1,len(df.columns)-1))
        cols=df.columns
        print(cols)

        plt.figure(figsize=figsize,dpi=dpi)
        for line in range(1,len(df.columns)):
            plt.scatter(df[cols[0]],df[cols[line]],label=cols[line],
            color=colors[line-1],marker='o',s=25)

        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='best')
        if ylim!=None:
            plt.ylim(xlim[0],xlim[1])
        if xlim!=None:
            plt.xlim(xlim[0],xlim[1])
        plt.show()
        return

    def matshow(self,df,title='Title',x_label='x_axis',y_label='y_axis',
        ylim=None,xlim=None,figsize=(10,3.5),dpi=100):
        ''' df is a dataframe where all columns are features, aligned to index.
        Returns Correlation Plot'''
        #import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        colors=plt.cm.brg(np.linspace(0,1,len(df.columns)-1))
        cols=df.columns
        print(cols)

        fig = plt.figure(figsize=(6,16),dpi=100)
        ax = fig.add_subplot(111)
        plt.matshow(df,cmap=plt.cm.brg)  # display the matrix
        plt.colorbar(cmap=plt.cm.brg)

        plt.title(title)
        plt.xticks(list(range(len(df.columns))), df.columns)
        plt.yticks(list(range(len(df.columns))), df.columns)
        plt.show()
        return
