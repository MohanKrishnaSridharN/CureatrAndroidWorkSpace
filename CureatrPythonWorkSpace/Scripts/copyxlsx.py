import os,sys
import shutil
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.cell import Cell
from openpyxl.utils import  coordinate_from_string,column_index_from_string,get_column_letter

def copyWorkBook():
    shutil.copy("/Users/macmini/Cureatr/CureatrPythonWorkSpace/InputFiles/Web/Results.xlsx", "/Users/macmini/Cureatr/CureatrPythonWorkSpace/OutPutFiles/2016-04-26")
    
copyWorkBook()