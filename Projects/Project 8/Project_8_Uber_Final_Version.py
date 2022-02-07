#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # For dataframes
from pandas import DataFrame # For dataframes
from numpy import ravel # For matrices
import matplotlib.pyplot as plt # For plotting data
import seaborn as sns # For plotting data
from sklearn.model_selection import train_test_split # For train/test splits
from sklearn.neighbors import KNeighborsClassifier # The k-nearest neighbor classifier
from sklearn.feature_selection import VarianceThreshold # Feature selector
from sklearn.pipeline import Pipeline # For setting up pipeline
from sklearn.metrics import accuracy_score
# Various pre-processing steps
from sklearn.preprocessing import Normalizer, StandardScaler, MinMaxScaler, PowerTransformer, MaxAbsScaler, LabelEncoder
from sklearn.model_selection import GridSearchCV # For optimization
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


# In[63]:


data1=pd.read_csv('/Users/nadimsaad/Desktop/IRONHACK/Module 3/Week 8/Day 40/Project 8/uber-raw-data-jul14.csv')


# In[64]:


data = data1.sample(frac =.05)
data.drop_duplicates(inplace=True)


# In[65]:


data.head()


# In[66]:


data.dtypes


# In[67]:


data.shape


# In[68]:


data.isna().sum()


# In[69]:


data['datetime'] = pd.to_datetime(data['Date/Time'])


# In[70]:


data['hour']=data.datetime.dt.hour
data['weekday']=data.datetime.dt.day_name()


# In[71]:


data.drop(columns='Date/Time', inplace=True )


# In[72]:


data.hist()


# In[73]:


data.weekday.value_counts()


# In[74]:


data.hour.value_counts()


# In[75]:


#data = pd.get_dummies(data = data, columns=['weekday'], drop_first=True).copy()


# In[76]:


from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['weekday']=encoder.fit_transform(data['weekday'])


# In[77]:


from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
data['Base']=encoder.fit_transform(data['Base'])


# In[78]:


data.Base.value_counts()


# In[79]:


data.weekday.value_counts()


# In[80]:


data.reset_index(inplace=True)


# In[81]:


data.head()


# In[82]:


df1=data[['Lat', 'Lon', 'Base',	'hour',	'weekday' ]]
df=data[['Lat', 'Lon' ]]


# ## KMeans

# In[83]:


from sklearn.cluster import KMeans


# In[84]:


from yellowbrick.cluster import KElbowVisualizer


# In[85]:


model = KMeans()
visualizer = KElbowVisualizer(estimator = model, k = (2,10))
visualizer.fit(df)
visualizer.poof()


# In[86]:


model = KMeans(5)
model.fit(df)
y_pred = model.predict(df)
y_pred


# #### Kmeans: silhouette score

# In[87]:


print('silhouette score: ',silhouette_score(df,y_pred))

KMeans is especially vulnerable to outliers. As the algorithm iterates through centroids, outliers have a significant impact on the way the centroids moves before reaching stability and convergence. Furthermore, KMeans has problems accurately clustering data where the clusters are of different sizes and densities. K-Means can only apply spherical clusters and its accuracy will suffer if the data is not spherical.
# In[88]:


df1["cluster_kmeans"]=y_pred
df1["cluster_kmeans"].value_counts()
centroids=model.cluster_centers_
centroids


# In[28]:


sns.scatterplot(x='Lon', y='Lat', hue='cluster_kmeans', data=df1)


# ## DBSCAN
DBSCAN does not have centroids, the clusters are formed by a process of linking neighbor points together.
# In[ ]:


'''
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

output_dict={}

for eps in range (18,23):
    for min_samples in [100]:
        db = DBSCAN(eps=eps/10, min_samples=min_samples, n_jobs=-1).fit(df)
        cl=len(np.unique(db.labels_))
        
        key="n clusters: "+str(cl)+"eps: "+str(eps)+"ms: "+str(min_samples)
        output_dict[key] = db.labels_
'''


# In[ ]:


'''
from sklearn.metrics import silhouette_score, calinski_harabasz_score, adjusted_mutual_info_score, completeness_score, homogeneity_score, adjusted_rand_score, fowlkes_mallows_score
def Silhouette_Coefficient(X, y_pred):
print("Silhouette Coefficient is equal to:")
print(silhouette_score(X,y_pred))
'''


# In[ ]:


'''
for key in output_dict:
print(key)
Silhouette_Coefficient(X=df, y_pred=output_dict[key])
'''


# In[33]:


db = DBSCAN(eps=0.2, min_samples=100, n_jobs=-1)
db.fit(df)
y_pred_db = db.labels_


# #### dbscan: silhouette score

# In[34]:


print('silhouette score: ',silhouette_score(df,y_pred_db))


# #### plot

# In[35]:


df1['cluster_dbscan'] = db.labels_
df1['cluster_dbscan'].value_counts()


# In[36]:


sns.scatterplot(x='Lon', y='Lat', hue='cluster_dbscan', data=df1)


# ## Spectral model

# In[48]:


#from sklearn.cluster import SpectralClustering


# In[ ]:


#clustering = SpectralClustering(n_clusters=4,
#                                assign_labels='discretize',
#                                random_state=0, n_jobs=-1).fit(df)
#clustering.labels_


# In[ ]:


#spectral_model_nn = SpectralClustering(n_clusters = 5, affinity ='nearest_neighbors', n_jobs=-1) 
  
# Training the model and Storing the predicted cluster labels 
#labels_nn = spectral_model_nn.fit_predict(df)


# In[ ]:


#df1['cluster_spectral'] = labels_nn


# ## Agglomerative Clustering

# In[37]:


from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram


# In[38]:


dendrogram = sch.dendrogram(sch.linkage(df, method='ward'))


# In[41]:


model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
model.fit(df)
labels_agglo = model.labels_


# In[42]:


print('silhouette score: ',silhouette_score(df,y_pred))


# In[43]:


df1['cluster_agglo'] = labels_agglo
df1['cluster_agglo'].value_counts()


# In[45]:


sns.scatterplot(x='Lon', y='Lat', hue='cluster_agglo', data=df1)


# # Models Comparisons

# In[47]:


fig = plt.figure(figsize=(12, 10))
fig.subplots_adjust(hspace=0.2, wspace=0.4)
fig.suptitle('Comparison of KMeans with diffrent number of clusters\nGrocery vs. Milk ', fontsize=14, fontweight='bold')

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)

sns.scatterplot(x='Lon', y='Lat', hue='cluster_kmeans', data=df1, ax=ax_1 )
sns.scatterplot("Lon","Lat", data=df1,  hue='cluster_dbscan',ax=ax_2)
sns.scatterplot("Lon","Lat", data=df1, hue='cluster_agglo',ax=ax_3)


# # Map

# In[50]:


import folium


# In[59]:


def create_map(df, cluster_column):
    m = folium.Map(location=[df.Lat.mean(), df.Lon.mean()], zoom_start=9, tiles='OpenStreet Map')
    for _, row in df.iterrows():
        if row[cluster_column] == -1:
            cluster_colour = '#68228B'
        elif row[cluster_column] == 0:
            cluster_colour = '#006400'
            folium.CircleMarker(
                location= [row['Lat'], row['Lon']],
                radius=5,
                popup= row[cluster_column],
                color=cluster_colour,
                fill=True,
                fill_color=cluster_colour
            ).add_to(m)
    return m


# In[60]:


create_map(df1, 'cluster_dbscan')


# In[89]:


def generateBasemap(default_location=[40.796580 , -73.873417], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map
map_centroids = generateBasemap()
for i in centroids:
    folium.CircleMarker(location=([i[0], i[1] ]), radius=20, color='darkblue').add_to(map_centroids)


# In[104]:


map_centroids


# In[93]:


df1


# In[94]:


df1.groupby(['cluster_kmeans', 'weekday']).weekday.agg(['count'])
#df.groupby(['cluster', 'weekday']).weekday.agg(['count'])


# In[97]:


freq_hour=df1.groupby(['cluster_kmeans','hour']).hour.agg(['count'])
freq_hour


# In[ ]:




