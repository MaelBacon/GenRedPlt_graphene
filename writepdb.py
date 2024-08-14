import calculsheet as CS

def generate(size_desired):
    
    side_parr = (int((7.47*size_desired) - 17.5)) + 1
    CS.generate_graphene_sheet(2.46, side_parr, size_desired)

def write_pdb(positions, filename):
    
    with open(filename, 'w') as pdb_file:
        pdb_file.write("Modele    1\n")
        
        for i, pos in enumerate(positions):
            pdb_file.write("ATOM  {:5d}  C   GP00 {:4d}    {:8.3f}{:8.3f}{:8.3f}  1.00  0.00\n".format(
                i+1, 1, pos[0], pos[1], 0.0))
        
        pdb_file.write("TER\n")
        pdb_file.write("ENDMDL\n")