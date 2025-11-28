import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o')
plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

sizes = [20,30,40,50]
label = ["apples","banana","cherry","dates"]
colors = [ "gold","yellowgreen","lightcoral","lightskyblue"]
explode = [0.1,0,0,0,]

plt.pie(sizes,
        explode=explode,
        labels=label,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
plt.title("fruit distribution")
plt.axis('equal')
plt.show()
