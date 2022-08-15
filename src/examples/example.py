import os
import sys
from enum import Enum

import numpy as np

# add SimpleFEM root directory to path in order to make relative imports works
FEM_PATH = os.path.abspath("SimpleFEM")
sys.path.append(FEM_PATH)

from SimpleFEM.source.mesh import Mesh
from src.optimization import Optimization, MaterialProperty

if __name__ == '__main__':
    mesh_path = os.path.join(os.path.dirname(__file__), 'meshes/rectangle180x60.msh')
    mesh = Mesh(mesh_path)
    mesh.set_boundary_condition(Mesh.BoundaryConditionType.DIRICHLET, ['down'])
    mesh.set_boundary_condition(Mesh.BoundaryConditionType.NEUMANN, ['left'])

    mesh.draw(True)

    rhs_func = lambda x: np.array([0, 0])
    dirichlet_func = lambda x: np.array([0, 0])
    neumann_func = lambda x: np.array([1., 0])

    optim = Optimization(
        mesh=mesh,
        penalty=3,
        volume_fraction=0.4,
        material=MaterialProperty.CastIron,
        rhs_func=rhs_func,
        dirichlet_func=dirichlet_func,
        neumann_func=neumann_func
    )
    optim.optimize(iteration_limit=5)
