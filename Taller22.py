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

days = []
d1 = max(dates)
for i in dates:
    delta = d1 - i
    days.append(delta)
data["Customer_For"] = days
data["Customer_For"] = pd.to_numeric(data["Customer_For"], errors="coerce")

estadomarital = data["Marital_Status"].value_counts()
print("Total de categorías en la caracteristica Marital_Status:\n",estadomarital,"\n")
print("Categorías totales en la función educación:\n", data["Education"].value_counts())

data["age"]=2021-data["Year_Birth"]
data["spent"]=data["MntWines"]+data["MntFruits"]+data["MntMeatProducts"]+data["MntFishProducts"]
data["Living_With"]=data["Marital_Status"].replace({"Married":"Partner","Together":"Partner",
                                                    "Absurd":"Alone","Widow":"Alone",
                                                    "YOLO":"Alone","Divorced":"Alone",
                                                    "Single":"Alone",})
data["Children"]=data["Kidhome"]+data["Teenhome"]

data["Family_Size"]=data["Living_With"].replace({"Alone":1,"Partner":2})+data["Children"]

data["Is_Parent"]=np.where(data.Children>0,1,0)

data["Education"]=data["Education"].replace({"Basic":"Undergraduate","2n Cycle":"Undergraduate",
                                             "Graduation":"Graduate","Master":"Postgraduate",
                                             "PhD":"Postgraduate",})
to_drop=["Marital_Status","Dt_Customer","Z_CostContact","Z_Revenue","Year_Birth","ID"]
data=data.drop(to_drop,axis=1)

data=data[(data["age"]<90)]
data=data[(data["Income"]<600000)]
print("El número total de puntos de datos depues de eliminar los valores atipicos es:", len(data))

#Matriz de correlación
corrmat=data.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corrmat,annot=True,center=0)

