import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering
from matplotlib.colors import ListedColormap
from sklearn import metrics
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")
    np.random.seed(42)

data= pd.read_csv('Campaña_marketing.csv',sep='\t')
print("Número de registros:",len(data))
data.head()
data.info()
data= data.dropna()
print("El número total de datos después de eliminar las filas con valores faltantes es:", len(data))
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"])
dates = []
for i in data["Dt_Customer"]:
    i=i.date()
    dates.append(i)

print("La fecha de inscripcion del cliente mas reciente en los registros:",max(dates))
print("La fecha de inscripcion del cliente mas antiguo en los registros:",min(dates))