# IMPORTING THE LATEST VERSION OF pyPDF2-3.0.1
from pyPDF2 import PdfMerger # type: ignore
import sys

# fetching the file names in the command palette :
inputs = sys.argv[1:]

#defining the function to merge n-pdfFiles :
def pdf_merger(pdf_list):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('Super.pdf') #storing the merged pdfFiles in a single file...
    merger.close()




