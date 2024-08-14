import numpy as np
import writepdb as WR

def generate_graphene_sheet(a, side_parr, sizeSheet):

    a1 = np.array([a, 0])
    a2 = np.array([a/2, a*np.sqrt(3)/2])
    
    num_cells = int(np.ceil(side_parr / (a * np.sqrt(3)/2))) + 1
    
    i_indices, j_indices = np.meshgrid(np.arange(num_cells), np.arange(num_cells), indexing='ij')
    
    base_positions = i_indices[..., np.newaxis] * a2 + j_indices[..., np.newaxis] * a1
    
    base_positions = base_positions.reshape(-1, 2)
    
    additional_positions = base_positions + np.array([0, a*np.sqrt(3)/3])
    
    positions = np.vstack((base_positions, additional_positions))
    
    positions = positions[(positions[:, 0] >= ((side_parr/2)-sizeSheet)) & (positions[:, 1] >= ((side_parr/2)-sizeSheet))]
    positions = positions[(positions[:, 0] <= ((side_parr/2)+sizeSheet)) & (positions[:, 1] <= ((side_parr/2)+sizeSheet))]
    positions = positions
    
    WR.write_pdb(positions, "megamultitest.pdb")
    
    return positions