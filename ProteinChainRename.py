def change_chain_names(input_file, output_file):
    chain_names = ['A', 'B']  # New chain names for the dimeric protein
    current_chain = chain_names[0]

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        previous_residue_number = None
        for line in lines:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                residue_number = int(line[22:26].strip())
                if previous_residue_number is not None and residue_number < previous_residue_number:
                    current_chain = chain_names[1]

                line = line[:21] + current_chain + line[22:]
                f.write(line)

                previous_residue_number = residue_number

            else:
                f.write(line)

    print("Chain names changed successfully!")


#input_pdb_file = '3SNA_dimer.pdb'
#output_pdb_file = '3SNA_Dimer.pdb'

#change_chain_names(input_pdb_file, output_pdb_file)
