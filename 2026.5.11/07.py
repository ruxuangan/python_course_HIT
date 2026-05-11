import numpy as np
import pandas as pd
import os
# 下载文件
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'house.csv')
df = pd.read_csv(file_path)

# print(df.shape)
# print(df.head(1))

# select cols to work with
cols_to_work = ['bathrooms','bedrooms', 'floorAreaSqM', 'livingRooms', 'tenure',
'currentEnergyRating','history_price']
df = df[ cols_to_work]
# print(df.head(3))

# rename col names
cols_to_rename = {'floorAreaSqM' : 'sqm' ,
                  'currentEnergyRating' : 'energy',
                  'history_price' : 'price'}
df = df.rename(columns = cols_to_rename)
print(df.head(3))

# check for missing values
print(df.isnull().sum()) 

# missing values in numerical cols
sqm_avg = df['sqm'].mean()
df['sqm'].fillna( sqm_avg )

# missing values in categorical cols
energy_v = df['energy'].mode() #most frequent value
df['energy'].fillna( energy_v )

# # there are some advanced missing values imputation technology
# # if you fill missing values , you create fake data

# # simple approach : remove all the rows with missing values
# df = df.dropna()
# print(df.shape)
# df.head(3)
# df.isnull().sum()

# # type conversion in pandas
# df['bathrooms'] = df['bathrooms'].astype(int)
# df.dtypes
# df.head(1)

# # convert numerical col to categorical
# df['price_cat_1'] = pd.cut( df['price'], bins = 3 , labels = ['Low', 'Mid', 'High'])
# df['price_cat_1'].value_counts()
# df['price'].min(), df['price'].max()

# def my_price_map( x ):
#     if x < 100000 :
#         return "Low"
#     elif x < 500000 :
#         return 'Mid'
#     else :
#         return 'High'
# # apply a function on every value in a col
# df['price_cat_2'] = df['price'].apply( my_price_map )
# df['price_cat_2'].value_counts()
# def my_energy_map(x):
#     if x in ['A', 'B', 'C'] :
#         return 'efficient'
#     else :
#         return 'not efficient'
# df['energy'].apply( my_energy_map)
# df['energy'].apply( lambda x : 'efficient' if x in ['A', 'B', "C"] else 'not efficient')
# print(df.head(3))    


# # Data exploration
# # univariate analysis : one feature (column) at a time
# # bivariate analysis
# import matplotlib.pyplot as plt
# import seaborn as sns
# mask = df['price_cat_2'] == "Low"
# df_low = df[mask]
# df_low.shape

# # numerical cols
# # panda style
# df_low["price"].plot( kind = 'box');
# df_low['price'].plot( kind = 'hist');

# # seaborn style
# # sns.boxplot(data = df_low , x = 'price);
# # sns.histplot( data = df_low , x = 'price');
# sns.displot(data = df_low, x = 'price',kde = True);

# # categorical cols
# # pandas style
# df['energy'].value_counts().plot( kind = 'bar');

# # seaborn style
# # sns.countplot( df['energy']) ;
# sns.barplot( df['energy'].value_counts());

# # bivariate plots
# # pandas style
# # df_low.plot( kind = 'scatter', x = 'sqm' ,y = 'price');

# # seaborn style
# # sns.scatterplot( data = df_low , x = 'sqm' , y = 'price');

# #price dist.per energy level
# sns.boxplot(data = df_low , x = 'energy' , y = 'price');

# # price dist. per energy level and per tenure
# plt.figure(figsize = (10,3));
# sns.boxplot( data = df_low , x = 'energy' , y = 'price', hue = 'tenure');

# # Note : select numerical cols
# df_num = df_low.select_dtypes( include = 'number')
# df_num.head(3)

# # Correlation plot
# plt.figure( figsize = (4,3));
# sns.heatmap(df_num.corr(), annot = True ,fmt = '.1f' ,cmap = 'Blues')
# # annot : see the values
# # fmt : format of the values : 1 floating point
# # cmap : color map ( you can select from a range of color map)