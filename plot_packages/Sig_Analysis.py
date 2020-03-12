

class Sig_Analysis:


    def __init__(self):
        ''' Constructor for this class. '''

        return

    def get_fft_powers_single(self,X,Y):
        '''Accept arrays, return fft power array
        for plotting'''

        import scipy.fftpack
        import numpy as np

        xs=X[:(int(len(X)/2))]
        power_length=len(xs)

        yf = scipy.fftpack.fft(Y)
        power=np.abs(yf[:power_length])
        return xs,power

    def get_df_fft_powers_df(self,df):
        '''Accept df, return fft power df
        for plotting.  Assumes X is in col 0 and all other columns
        are signal values'''

        import scipy.fftpack
        import numpy as np

        xs=X[:(int(len(df[0])/2))]
        power_length=len(xs)

        df_fft_pow=pd.DataFrame()
        df_fft_pow['X']=xs

        for c in df.columns[1:]:
            tmp= scipy.fftpack.fft(df[c])
            df_fft_pow[c]=np.abs(tmp)
        return df_fft_pow
