import numpy as np 

a =  [[1, 2, 3, 4], [5, 6, 7, 8]]

narr = np.array(a)
# print(narr.dtype)

# print(np.zeros(10))
# print(np.ones(10))
# print(np.zeros((3,6)))
# print(np.empty((2, 3)))
# print(np.arange(15))
# print(np.eye(3,2))

# print(np.random.randn(4,7))
# arr = np.empty((8, 4))
# for i in range(8):
#     arr[i] = i
# print(arr)
# print(arr[[4, 3, 0, 6]])

#Transpose
# arr = np.arange(15).reshape((3,5))
# print(arr)
# print(arr.T)

# arr = np.arange(16).reshape((2, 2, 4))
# print(arr)
# arr.transpose((1, 0, 2))
# print(arr.swapaxes(1,2))

# arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr_3d)
# print(arr_3d.transpose(1, 0, 2))  # Rearranges the axes

#FUnctionalities

# points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
# xs, ys = np.meshgrid(points, points)
# import matplotlib.pyplot as plt
# z = np.sqrt(xs ** 2 + ys ** 2)
# plt.title("Image plot of sqrt(x^2 + y^2) for a grid of values")
# plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
# plt.colorbar()
# plt.show()

#Sorting
# arr = np.random.randn(5, 3)
# print(arr)
# arr.sort(0)
# print(arr)

# File saving
# arr = np.arange(10)
# np.save('some_array', arr)
# a = np.load('some_array.npy')
# print(a)


"""
Example: Random Walks
An illustrative application of utilizing array operations is in the simulation of random
walks. Let’s first consider a simple random walk starting at 0 with steps of 1 and -1
occurring with equal probability. A pure Python way to implement a single random
walk with 1,000 steps using the built-in random module:
"""
import random
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

# Plotting the walk
plt.plot(walk)
plt.title('1D Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Position')
plt.show()