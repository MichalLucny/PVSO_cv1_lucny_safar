import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from sklearn.cluster import Birch



#print("Loading downloaded pointcloud")
#pcd = o3d.io.read_point_cloud("Cloud.ply")


print("Loading captured pointcloud")
pcd = o3d.io.read_point_cloud("conv.ply")

print(pcd)
print(np.asarray(pcd.points))
#o3d.visualization.draw_geometries([pcd])


#ransac

cl, ind = pcd.remove_statistical_outlier(nb_neighbors=12,std_ratio=2.2)


inlier_cloud = pcd.select_by_index(ind)
outlier_cloud = pcd.select_by_index(ind, invert=True)

inlier_cloud.paint_uniform_color([1, 0, 0])
outlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])
#o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

#o3d.visualization.draw_geometries([cl])


#birch
#https://towardsdatascience.com/machine-learning-birch-clustering-algorithm-clearly-explained-fb9838cbeed9
#http://www.open3d.org/docs/latest/tutorial/Basic/pointcloud.html#DBSCAN-clustering

#downloaded one
#brc = Birch(branching_factor=40, n_clusters=56, threshold=2)

#kinect one
brc = Birch(branching_factor=40, n_clusters=8, threshold=0.71)

brc.fit(np.asarray(cl.points))


labels = brc.predict(np.asarray(cl.points))
max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
cl.colors = o3d.utility.Vector3dVector(colors[:, :3])


o3d.visualization.draw_geometries([cl])
