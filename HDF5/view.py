import pandas as pd
import os as os

def view_hdf5(path: str):
    # Load the HDF5 file
    df = pd.read_hdf(path, key='data')

    # Display the DataFrame
    print(df)

def lsPipeCd(input_dir: str):
    print("Viewable HDF5's: ")
    for filename in os.listdir(input_dir):
        print(os.path.splitext(filename)[0])
    print()
    name = input("What would you like to view? Please enter file-basename only ")
    view_hdf5(input_dir+"/"+name+".h5")

def repeat(choice: str):
    if (choice.lower() == 'yes' or choice == 'y' or choice == 'ye'):
        return True
    else:
        return False

while(True):
    viewing = input("Would you like to view 'COVID' or 'Stock'? (Type 'e' to exit) ")
    if (viewing.lower() == 'covid'):
        lsPipeCd('HDF5/COVID Data/')
        choice = input("View more? (Y/N) ")
        if (repeat): continue
        else: break
    elif (viewing.lower() == 'stock'):
        lsPipeCd('HDF5/Stock Data/')
        choice = input("View more? ")
        if (repeat): continue
        else: break
    elif (viewing.lower() == 'e'):
        break
    else:
        print("Valid inputs are: 'COVID' or 'Stock' only! (Type 'e' to exit) ")