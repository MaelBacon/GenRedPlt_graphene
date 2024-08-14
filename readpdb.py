import numpy as np

def read_pdb(file_path):
    atom_positions = []
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                atom_positions.append([x, y, z])
                
    atom_positions = np.array(atom_positions)
    return atom_positions