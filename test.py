import matplotlib.pyplot as plt
data = [
    ('a', 4),
    ('b', 5),
    ('c', 5),
    ('d', 4),
    ('e', 2),
    ('f', 5),
]
labels, y = zip(*data)

x = range(len(y))
plt.stem(x, y)
plt.xticks(x, labels)
plt.axis([-1, 6, 0, 6])
plt.show()
