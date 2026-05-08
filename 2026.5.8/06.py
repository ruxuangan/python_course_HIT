import matplotlib.pyplot as plt

# x = ["A", "B", "C"]
# y = [5, 15, 12]
# fig,ax = plt.subplots(figsize=(2,2))
# ax.plot(x,y, linewidth = 2, color = "black", linestyle = ":");   #plot is a line plot  
# ax.scatter(x, y);

# fig,ax = plt.subplots(nrows = 1 , ncols = 2 , figsize = (5,2))
# ax[0].plot(x, y);
# ax[1].bar(x,y);

# fig, ax = plt.subplots(nrows = 3 , ncols = 2 , figsize = (3,5))
# ax[0][1].scatter(x,y)

# plt.show()

students = {"Bob" : 18 ,"Alice" : 12 , "John" : 15}
x = students.keys()
y = students.values()
avg = sum(y)/ len(y)

fig, ax = plt.subplots( figsize = (2,2 ))
ax.bar(x,y);
ax.set_xlabel("names");
ax.set_ylabel("grades");
ax.set_title("Python Class");
ax.axhline( avg , color = "green");
ax.text(3, avg, f"average:{avg}", color = "green");
plt.show()















