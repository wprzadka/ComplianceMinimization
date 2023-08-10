import os
import sys

import numpy as np

# add SimpleFEM root directory to path in order to make relative imports works
FEM_PATH = os.path.abspath("SimpleFEM")
sys.path.append(FEM_PATH)

from SimpleFEM.source.mesh import Mesh
from SimpleFEM.source.examples.materials import MaterialProperty
from sources.optimization import Optimization


if __name__ == '__main__':
    mesh_path = os.path.join(os.path.dirname(__file__), './meshes/hole120x60v4.msh')
    mesh = Mesh(mesh_path)

    mesh.draw(True)

    # mesh.set_boundary_condition(Mesh.BoundaryConditionType.DIRICHLET, ['left-up', 'left-down'])
    # mesh.set_boundary_condition(Mesh.BoundaryConditionType.NEUMANN, ['circle'])

    mesh.set_boundary_condition(Mesh.BoundaryConditionType.DIRICHLET, ['left'])
    mesh.set_boundary_condition(Mesh.BoundaryConditionType.NEUMANN, ['right-down'])

    rhs_func = lambda x: np.array([0, 0])
    dirichlet_func = lambda x: np.array([0, 0])
    # neumann_func = lambda x: np.array([1, -1]) if x[0] > x[1] else np.zeros(2)
    neumann_func = lambda x: np.array([0, -1])

    optim = Optimization(
        mesh=mesh,
        material=MaterialProperty.TestMaterial,
        rhs_func=rhs_func,
        dirichlet_func=dirichlet_func,
        neumann_func=neumann_func,
        penalty=3,
        volume_fraction=0.5,
        filter_radius=3.5
    )

    optim.optimize(iteration_limit=100)
