import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (15,10)

def karstuma_karte(datne):
    data_file = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(data_file.corr(), annot=True, cmap='magma')
    plt.show()
    return

def datu_biezums(datne, collom):
    data_file = pd.read_csv(datne)
    sb.distplot(data_file[collom], color='r')
    plt.title(collom.capitalize() + " biežums", fontsize=16)
    plt.xlabel(collom.capitalize(), fontsize=14)
    plt.ylabel("Biežums", fontsize=12)
    plt.xticks(fontsize=14)
    plt.show()
    return


datne1 = "data/auto_simple.csv"
datne2 = "data/auto_imports.csv"
# karstuma_karte(datne2)
datu_biezums(datne2, "price")
