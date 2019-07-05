
import mysql.connector


def read_data():

    data = open(r"/data/variant_list.txt", "r")
    filtered_variants = []
    print("Dit print hij wel")
    for variant in data:
        print(variant)
        variant = (str(variant.strip()), )
        checked_variant = checkdb(variant)

        filtered_variants.append(checked_variant)


    return filtered_variants

def checkdb(variant):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'gnomad'
    }


    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    sql_select_Query = "SELECT * FROM variants where variant = %s;"
    cursor.execute(sql_select_Query, variant)
    filtered_variants = cursor.fetchall()
    cursor.close()
    connection.close()
    return filtered_variants


def make_report(filtered_variants):

    filtered_data = open(r"/data/filtered_variant_list.txt", "w")

    for variant in filtered_variants:
        if variant:
            if variant[0][3] < 0.01:
                filtered_data.write(str(variant[0])+'\n')




    filtered_data.close()

def main():
    filtered_variants = read_data()
    make_report(filtered_variants)




if __name__ == '__main__':
    main()