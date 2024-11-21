# CSV to HDF5 Converter Documentation

## Overview

This script converts all CSV files in a specified input directory into HDF5 format and stores them in an output directory. It uses the `pandas` library to handle data manipulation and conversion.

## Requirements

- Python 3.x
- pandas library
- os library

You can install the required library using pip:

```bash
pip install pandas
```
## Directory Structure
The script expects a directory named COVID Data/ containing CSV files. It creates a corresponding output directory named HDF5/COVID Data/ for storing the converted files
```
.
├── COVID Data/
│   ├── file1.csv
│   ├── file2.csv
│   └── ...
├── Stock Data/
│   ├── stock1.csv
│   └── ...
└── HDF5/
    └── COVID Data/
```

## Script Details
### Input Directory
- Path: COVID Data/ or Stock Data/
- File Type: CSV (.csv)
### Output Directory
- Path: HDF5/COVID Data/ or HDF5/Stock Data/
- File Type: HDF5 (.h5)

### Key Functions
1. os.makedirs(): Creates the output directory if it does not already exist.
2. os.listdir(): Lists all files in the input directory.
3. pandas.read_csv(): Reads a CSV file into a DataFrame.
4. DataFrame.to_hdf(): Converts the DataFrame to HDF5 format.
5. pandas.read_hdf(): Loads the HDF5 file into a DataFrame for display.

### Conversion Process
1. Loop through each file in the input directory.
2. Check if the file has a .csv extension.
3. Read the CSV file into a DataFrame.
4. Convert the DataFrame to HDF5 format and save it in the output directory.
5. Load the newly created HDF5 file and print its contents.

## Example
To use the script, ensure your directory structure is set up as described, then run the script. It will convert all .csv files in the COVID Data/ directory to .h5 files and display the contents of each converted DataFrame.

```bash
python your_script.py
```
### Output

The console will print messages indicating the conversion status of each file:

```bash
Converted COVID Data/file1.csv to HDF5/COVID Data/file1.h5
   Column1  Column2
0        1        2
1        3        4
```

## Notes
Ensure the input directory contains only CSV files, as the script currently filters for .csv extensions only.
The script overwrites existing HDF5 files without warning. Adjust the mode in to_hdf() if you wish to append or modify existing files.