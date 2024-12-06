class AllowedDistributionTypes:
    LINEAR = "linear"
    COSINE = "cosine"


class Wing:
    """
    Object that represents a Wing in the simulations
    Based on user inputs, generates the geometry needed for simulation
    """
    def __init__(self): ...

    def generate_mesh(self):
        '''Generates a wing's mesh, used for simulation'''

        # the ideal scenario would be to bound every geometric entity into the same for loop for both performance and better undestandment
        ...

    def calculate_unit_vectors(self):
        '''Calculate unit vectors use to represent the orientation of a wing's sections'''
        ...

    def calculate_collocation_points(self): ...

    def calculate_vertice_points(self): ...

    def calculate_sweep(self): ...

    def calculate_dihedral(self): ...

    def calculate_twist(self): ...

    

    @property
    def MAC(self): ...

    @property
    def AR(self): ...

    @property
    def total_area(self): ...


class CollocationPoint:
    def __init__(self): ...


class Vertice:
    def __init__(self): ...