import matplotlib.pyplot as plt

x = ["A", "B", "C"]
y = [5, 15, 12]
fig,ax = plt.subplots(figsize=(2,2))
ax.plot(x,y, linewidth = 2, color = "black", linestyle = ":");   #plot is a line plot  
ax.scatter(x, y);

fig,ax = plt.subplots(nrows = 1 , ncols = 2 , figsize = (5,2))
ax[0].plot(x, y);
ax[1].bar(x,y);

fig, ax = plt.subplots(nrows = 3 , ncols = 2 , figsize = (3,5))
ax[0][1].scatter(x,y)

plt.show()

# students = {"Bob" : 18 ,"Alice" : 12 , "John" : 15}
# x = students.keys()
# y = students.values()
# avg = sum(y)/ len(y)

# fig, ax = plt.subplots( figsize = (2,2 ))
# ax.bar(x,y);
# ax.set_xlabel("names");
# ax.set_ylabel("grades");
# ax.set_title("Python Class");
# ax.axhline( avg , color = "green");
# ax.text(3, avg, f"average:{avg}", color = "green");
# plt.show()

import numpy as np
import pandas as pd
my_data = {
  "Name": ["Bob","Alice", "John", "Eric"],
  "City": ["Paris", "Harbin", "Harbin", "Lyon"], 
  "Age": [17, 19 , 21, 18]
  }

df = pd.DataFrame( data = my_data, index = ["a", "b", "c", "d"])
# print(df)

# print( df.shape)
# print( df.columns)
# print( df.index)
# print(df.info())
# df.describe()  # get stats info on numerical cols
# df.describe(include = "o")  # get stats info on object cols

# #access col /cols
# print(df["City"])
# print(df[["City", "Age"]])

# # access row/ rows
# print(df.loc["b"])
# print(df.loc[["b", "c"]])

# #select data from multiple rows or cols
# print(df.loc["b", "Age"])
# print(df.loc[["b", "c"],["City", "Age"]])

# # the same
# print(df.iloc[1, 2])
# print(df.iloc[[1, 2], [1, 2]])
# print(df.iloc[1: 3, 1: 3])

# numbers = ["A", "B", "C", "D"]
# numbers_array = np.array(numbers)
# mask = [True, False,False, True]
# print(numbers_array[mask])

# print(df.loc[ mask ])

# # select rows where city is Harbin
# mask = df["City"] == "Harbin"
# print(df[mask])

# # add a col
df.insert(2, "Sex", ["Male", "Female", "Male", "Female"])
# print(df)
# #remove a col ( two way )
# df.drop(columns= ["Sex"], inplace = True)
# print(df)
# df = df.drop(columns= ["Sex"])
# print(df)

# level 1 aggregation -- what is the average of age
print(df["Age"].mean()) # size, max, count, size
# level 2 aggregation -- what is the average of age in each city
print(df.groupby("City")["Age"].mean())
# level 3 aggregation -- the average of age per city and per sex
print(df.pivot_table(index = "City", columns = "Sex", values = "Age", aggfunc = "mean"))
# index : first group
# columns :second group




