"""
python visualize_mesh.py -f examples/planes/Reconstructions/100/Meshes/ShapeNetV2/plane/24_simplified.ply
python visualize_mesh.py -f data/processed/SdfSamples/ShapeNetV2/plane/24_simplified.npz


Initial implementation:
    https://github.com/marian42/mesh_to_sdf
"""

import trimesh
import pyrender
import numpy as np

def get_mesh_from_processed_mesh(filename: str) -> pyrender.Mesh:
    instance = np.load(filename)

    values = np.vstack((instance['pos'], instance['neg']))
    points = values[:, :3]
    sdf = values[:, -1]

    colors = np.zeros(points.shape)
    colors[sdf < 0, 0] = 1
    colors[sdf > 0, 2] = 1

    return pyrender.Mesh.from_points(points, colors=colors)

def get_mesh_from_ply(filename: str) -> pyrender.Mesh:
    return pyrender.Mesh.from_trimesh(trimesh.load(filename))

if __name__ == "__main__":

    import argparse

    arg_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Visualizes mesh (.ply, processed_mesh:*.npz)",
    )

    arg_parser.add_argument(
        "--filename",
        "-f",
        dest="filename",
        required=True,
        help="Path to file (*.ply, *.npz)",
    )

    args = arg_parser.parse_args()

    mesh = None
    if ".ply" in args.filename:
        mesh = get_mesh_from_ply(args.filename)
    elif ".npz" in args.filename:
        mesh = get_mesh_from_processed_mesh(args.filename)
    else:
        raise ValueError(f"Invalid file format {args.filename}")

    scene = pyrender.Scene()
    scene.add(mesh)
    viewer = pyrender.Viewer(scene, use_raymond_lighting=True, point_size=1)