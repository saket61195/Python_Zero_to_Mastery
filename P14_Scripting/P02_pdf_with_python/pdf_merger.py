import PyPDF2
import sys

inputs = sys.argv[1:]# [1:] means we can take many input 

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('./modified_pdf/merged_super.pdf')

pdf_combiner(inputs)


# how to run
# python3 pdf_merger.py ./pdf_file/dummy.pdf ./pdf_file/twopage.pdf 