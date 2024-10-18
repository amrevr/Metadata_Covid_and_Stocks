import pandas as pd
import os as os

# Set the directory containing the CSV files
input_directory = 'Stock Data/'
output_directory = 'HDF5/COVID Data/'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        csv_file_path = os.path.join(input_directory, filename)
        hdf5_file_path = os.path.join(output_directory, filename.replace('.csv', '.h5'))

        # Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Convert to HDF5
        df.to_hdf(hdf5_file_path, key='data', mode='w')
        print(f'Converted {csv_file_path} to {hdf5_file_path}')

        # Load the HDF5 file
        df = pd.read_hdf(hdf5_file_path, key='data')

        # Display the DataFrame
        print(df)
