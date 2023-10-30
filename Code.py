import csv

# Replace 'input.csv' with the path to your CSV file
csv_file = 'protein seq.csv'
# Replace 'output.fasta' with the desired output FASTA file path
fasta_file = 'output.fasta'

# Open the CSV file for reading and the FASTA file for writing
with open(csv_file, 'r') as csvfile, open(fasta_file, 'w') as fastafile:
    csv_reader = csv.reader(csvfile)

    
    for row in csv_reader:
        if len(row) == 2:
            name, sequence = row
            # Write the FASTA entry to the FASTA file
            fastafile.write(f'>{name}\n{sequence}\n')
