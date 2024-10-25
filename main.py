import utils.file_utils
from utils.table import Table, Seat
from utils.openspace import Openspace
import pandas as pd

def main():
    
    uploaded_path = input('Upload your xlsx file path: ')
    df = pd.read_excel(uploaded_path)
    file_path = (df["Names"]).tolist()

    set_tables = int(input('Set the number of tables in the openspace: '))
    set_seats = int(input('Set the number of seats per table in the openspace: '))

    op = Openspace(set_tables, set_seats)

    if uploaded_path:
        op.organize(file_path)
        op.display()
        op.store('hello.xlsx')
    else:
        return 'Wrong input'
        

main()