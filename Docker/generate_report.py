import sys
from fpdf import *

def write_pdf(file):

    #filtered_data = open("variant_list/filtered_variant_list.txt")
    filtered_data = open(file)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=50)
    pdf.cell(200, 10, txt="Variant Report", ln=1, align="C")
    for line in filtered_data:
        line = line.replace('(', '').replace(')', '').replace("'", '')
        datalijst = line.split(',')
        variant = datalijst[0]
        gene = datalijst[1]
        uniprot = datalijst[2].strip()
        AF = datalijst[3]


        pdf.set_font("Arial", size=12)
        pdf.cell(200, 20, txt="", ln=1, align="L")
        pdf.cell(200, 10, txt="Variant:  "+variant, ln=1, align="L")
        pdf.cell(200, 10, txt="Gen:  " + gene, ln=1, align="L")
        pdf.cell(200, 10, txt="Uniprot accesiecode:  " + uniprot, ln=1, align="L", link= "https://www.uniprot.org/uniprot/"+uniprot)
        pdf.cell(200, 10, txt="Allele Frequency:  " + AF, ln=1, align="L")
    pdf.output("Experiment.pdf")


    linkdieikwil = "https://www.uniprot.org/uniprot/Q6XZB0"

if __name__ == '__main__':
    file = str(sys.argv[1])
    write_pdf(file)