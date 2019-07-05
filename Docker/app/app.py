from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import vcf

#app = Flask(__name__)

def get_data():
    dataset = vcf.Reader(
        #open(r"gnomad.exomes.r2.1.1.sites.21.vcf", 'r'))
        open(r"/data/gnomad.exomes.r2.1.1.sites.21.vcf", 'r'))
    count = 0
    for record in dataset:
        print("nste record: ", count)
        if len(record.REF) > 1:
            continue
        variant = str(record.CHROM) + '-' + str(record.POS) + '-' + str(record.REF) + '-' + str(record.ALT[0])
        gene = record.INFO['vep'][0].split('|')[3]
        if not gene:
            gene = 'N/A'
        uniprot = record.INFO['vep'][0].split('|')[-37]
        if not uniprot:
            uniprot = 'N/A'
        try:
            AF = float(record.INFO['AF'][0])
        except:
            continue
        aa_pos = record.INFO['vep'][0].split('|')[14]
        if not aa_pos:
            aa_pos = 'N/A'
        aa_change = record.INFO['vep'][0].split('|')[15]
        if not aa_change:
            aa_pos = 'N/A'

        data = (variant, gene, uniprot, AF)
        db_fill(data)
        count += 1



def db_fill(data):

    #print("haha")
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'gnomad'
    }

    insert_stmt = (
        "INSERT INTO variants (variant, gene, uniprot, AF) VALUES (%s, %s, %s, %s)"
    )

    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()





    try:
        cursor.execute(insert_stmt, data)
        print("Data toegevoegd: ", data)
    except:
        return
    connection.commit()
    cursor.close()
    connection.close()

def db_check():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'gnomad'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    sql_select_Query = "select * FROM variants where AF >= 0.01;"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for row in records:
        print("Variant = ", row[0],)
        print("Gene = ", row[1])
        print("Uniprot  = ", row[2])
        print("AF  = ", row[3], "\n")
    cursor.close()
    connection.close()
    return



#@app.route('/')
def main():
    dataset = get_data()
    db_fill(dataset)




if __name__ == '__main__':
    main()
    #app.run(host='0.0.0.0')
