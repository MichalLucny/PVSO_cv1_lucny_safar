import numpy as np
from sklearn.mixture import GaussianMixture
import open3d as o3d
import matplotlib.pyplot as plt
import pdb

def load_point_cloud(file_path):
    pc = None
    pcd = o3d.io.read_point_cloud(file_path)
    pcd_points = np.asarray(pcd.points)
    pcd_colors = np.asarray(pcd.colors)
    pc = np.concatenate([pcd_points, pcd_colors], axis=1)

    return pcd_points, pcd_colors, pc

def coords_to_pcl(coordarray):
    xyz = coordarray[0:None, 0:3]
    rgb = coordarray[0:None, 3:None]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(rgb)

    return pcd

coord = o3d.geometry.TriangleMesh().create_coordinate_frame(size=0.25)
pc_xyz,_,_ = load_point_cloud("conv.ply")  #returns numpy array

gmm = GaussianMixture(n_components=8, random_state=0).fit(pc_xyz)  #Estimate model parameters with the EM algorithm
labels = gmm.predict(pc_xyz)

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters from GMM")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels<0] = 0

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pc_xyz)
pcd.colors = o3d.utility.Vector3dVector(colors[:,:3])

o3d.visualization.draw_geometries([pcd, coord])