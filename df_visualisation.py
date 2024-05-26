import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns


class Plotter:

    def __init__(self, df):
        self.df = df

    def df_hist(self):
        fig=plt.figure(figsize=(20,20))
        ax=fig.gca()
        return self.df.hist(ax=ax)
    
    def plt_boxplot(self):
        plt.figure(figsize=(20,20))

        for ele in enumerate(self.df.columns):
            plt.subplot(4,4,ele[0]+1)
            sns.boxplot(self.df[ele[1]])
            
    def plot_heatmap(self):
        fig, ax = plt.subplots(figsize=(20,20))
        return sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm', ax=ax)
