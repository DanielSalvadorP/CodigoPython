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

#Carga de datos
data=pd.read_csv('insurance.csv')#,sep="\t"

#Numero de registros
print("número de registros",len(data))

#Miramos las columnas y datos que tienen
print(data.head())

#Miramos la información del tipo de datos que tienen las columnas
data.info()

#Eliminamos valores nulos
data= data.dropna()
print("El número total de datos después de eliminar las filas con valores faltantes es:", len(data))

#Revisamos cuantos valores nulos hay
print(data.isnull().sum())

#Reformateamos los datos de los valores decimales de punto decimal a coma decimal en el estandar latino.
columna_charges= data['charges'].astype(str).str.replace('.', ',')
print(columna_charges)
columna_bmi= data['bmi'].astype(str).str.replace('.', ',')
print(columna_bmi)