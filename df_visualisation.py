import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
# import plotly.express as px
# from statsmodels.graphics.gofplots import qqplot



class Plotter:

    def __init__(self, df):
        self.df = df

    def df_hist(self):
        fig=plt.figure(figsize=(20,20))
        ax=fig.gca()
        return self.df.hist(ax=ax)

    # def K2test(self, column_name):
    #     data=self.df[column_name]
    #     stat, p = normaltest(data, nan_policy='omit')
    #     return print('Statistics=%.3f, p=%.3f'%(stat, p))
    
    # def plt_hist(self, column_name, bin_num=40):
    #     return self.df[column_name].hist(bins=bin_num)
    
    # def qq_plt(self, column_name):
    #     qq_plot=qqplot(self.df[column_name], scale=1, line='q')
    #     return plt.show()
    
    def plt_boxplot(self):
        plt.figure(figsize=(20,20))

        for ele in enumerate(self.df.columns):
            plt.subplot(4,4,ele[0]+1)
            sns.boxplot(self.df[ele[1]])
            

    def plot_heatmap(self):
        fig, ax = plt.subplots(figsize=(20,20))
        return sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm', ax=ax)
