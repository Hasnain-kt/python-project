# import numpy as np
# import matplotlib.pyplot as plt

# A = np.array([
#     [0, -1],
#     [1,  0]
# ])

# v = np.array([3, 4])

# result = A @ v
# print(result)

# plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)
# plt.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1)

# plt.xlim(0, 10)
# plt.ylim(0, 10)
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# A = np.array([
#     [2, 0],
#     [0, 2]
# ])

# points = np.array([
#     [1, 0],
#     [0, 1],
#     [1, 1],
#     [2, 1],
#     [2, 2]
# ])

# transformed = points @ A.T

# plt.scatter(points[:, 0], points[:, 1])
# plt.scatter(transformed[:, 0], transformed[:, 1])

# plt.grid()
# plt.axis("equal")
# plt.show()

import matplotlib.pyplot as plt

data = [23, 10, 35, 15, 12]

plt.pie(data)
plt.show()


# plt.plot(x,y)
# plt.title("hello")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# import matplotlib.pyplot as plt

# x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
#      21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

# plt.hist(x, bins=5, color='blue')
# plt.title("Histogram")
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")
# plt.show()