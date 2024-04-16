from .measure import calculate_distance

"""
Functions for molecule analysis
"""

def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
    
    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    
    """

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Build a list of bonds in a set of coordinates based on a distance criteria.

    Parameters
    ----------
    coordinates: np.ndarray
        The coordinates of the atoms to analyze in an (natoms, ndim) array.

    max_bond: float, optional
        The maximum distance for two atoms to be considered bonded.

    min_bond: float, optional
        The minimum distance for two atoms to be considered bonded.

    Returns
    -------
    bonds: dict
        A dictionary containing bonded atoms with atom pairs as keys and the distance between the atoms as the value.
    """

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds