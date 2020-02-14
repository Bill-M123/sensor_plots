

class Make_Wave_Data:

    def __init__(self):
        ''' Constructor for this class. '''

        return

    def make_square_wave(self,duty_cyclce=0.5,period_seconds=100,
        total_seconds=3600,samples_per_sec=1,first_state=1,
        alt_state=0):
        '''Generate a squarewave based in input conditions.  Return as
        dataframe in form of df['X','Y'] where X is in seconds from origin.
        Valid first_state 1 or 0'''

        import pandas as pd
        total_samples=int(total_seconds/samples_per_sec)
        if (first_state not in [0,1]):
            first_state=1
            alt_state=0
        if (alt_state not in [0,1]):
            alt_state=0
            first_state=1


        period=period_seconds/samples_per_sec
        n_periods=int(total_samples/period)

        x=[x/samples_per_sec for x in range(total_samples)]
        y=[]
        for i in range(n_periods):
            for j in range(int(period/2)):
                if i%2 ==0:
                    y.append(first_state)
                    last_state=first_state
                else:
                    y.append(alt_state)
                    last_state=alt_state

            for j in range(int(period/2)):
                if i%2 ==0:
                    y.append(alt_state)
                    last_state=alt_state
                else:
                    y.append(first_state)
                    last_state=first_state

        df=pd.DataFrame(columns=['X','Y'])
        df['X']=x[:len(y)]
        df['Y']=y
        return df

    def add_noise(self,df,fs_ratio=0.1,random_seed=42):
        '''df is df['X','Y1','Y2',...]
        return df with _n appended to column names, and
        noise = +/- fs_ratio*random added to all y points (note:
        fs_ratio defaults to 0.1 or +/- 10% of full scale noise level).'''

        import numpy as np
        import random

        df_n=df.copy()
        df_col=list(df_n.columns)
        for n in range(1,len(df.columns)):
            range_max=np.abs(fs_ratio)
            range_min=0-range_max
            df_n[df_col[n]]=df[df_col[n]].apply(lambda x:\
                x+random.uniform(range_min,range_max))
            df_col[n]=df_col[n]+'_n'
        df_n.columns=df_col
        return df_n
