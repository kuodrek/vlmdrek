import numpy as np

def get_spanwise_distribution(): ...

def get_local_chord(y, root, tip, span):
    return (tip - root) / span * y + root


class EulerMatrix: ...

def get_euler_matrix(dihedral, twist, sweep):
    # TODO: peguei essa funcao do lltdrek, precisa melhorar
    # Utilizando-se rotação XYZ -> Ângulos de Tait-Bryan
    # REFERÊNCIA: https://en.wikipedia.org/wiki/Euler_angles#Conversion_to_other_orientation_representations
    c1 = np.cos(dihedral)
    c2 = np.cos(twist)
    c3 = np.cos(sweep)
    s1 = np.sin(dihedral)
    s2 = np.sin(twist)
    s3 = np.sin(sweep)
    euler_matrix = np.array([
        [c2*c3, -c2*s3, s2],
        [c1*s3+c3*s1*s2, c1*c3-s1*s2*s3, -c2*s1],
        [s1*s3-c1*c3*s2, c3*s1+c1*s2*s3, c1*c2]
        ])
    return euler_matrix
