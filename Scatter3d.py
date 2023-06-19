import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fileName = "FixCenter.csv"
df = pd.read_csv(fileName)

def drawScatter(df, x, y, z, Is3d = False):
    cm = plt.cm.get_cmap('jet')
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(1,2,1,projection = '3d')
    ax2 = fig.add_subplot(1,2,2)
    mappable = ax.scatter(df.iloc[:,x], df.iloc[:,y], df.iloc[:,z], c = df.iloc[:,z], cmap = cm)
    mappable2 = ax2.scatter(df.iloc[:,x], df.iloc[:,y], df.iloc[:,z], c = df.iloc[:,z], cmap = cm)
    fig.colorbar(mappable2, ax=ax2)
    ax.set_title(df.columns[z])
    ax.set_xlabel(df.columns[x])
    ax.set_ylabel(df.columns[y])
    ax2.set_title(df.columns[z])
    ax2.set_xlabel(df.columns[x])
    ax2.set_ylabel(df.columns[y])
    

drawScatter(df, 0, 1, 2)
drawScatter(df, 0, 1, 3)
drawScatter(df, 0, 1, 4, True)
drawScatter(df, 2, 3, 4)

plt.show()