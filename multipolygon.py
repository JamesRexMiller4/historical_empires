from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import numpy as np

polygon = Polygon([[-2, 3], [-2, 6], [3, 6], [3, 3]])

# print("Area", polygon.area)
# print("Length", polygon.length)
# print("Bounds", polygon.bounds)
# print("Boundary", polygon.boundary)
# print("Center", polygon.centroid)

plt.fill(*polygon.exterior.xy, color="red", edgecolor="black")
plt.scatter(polygon.exterior.xy[0], polygon.exterior.xy[1], edgecolor="black")
plt.plot(polygon.boundary.xy[0], polygon.boundary.xy[1], color="orange")
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-3, 5, 1))
plt.yticks(np.arange(2, 8, 1))

plt.show()
