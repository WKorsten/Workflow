import sys

def remove(file):

    data = open(file)
    variant_min_NA_gen = open("C:/Users/wimme/PycharmProjects/snakemake_project/variant_min_NA_gen.txt", "w")

    for variant in data:
        variant = variant.replace('(', '').replace(')', '').replace("'", '')
        if variant.split(",")[2] != " N/A":
            print(variant.split(",")[2])
            variant_min_NA_gen.write(variant)

if __name__ == '__main__':
    file = str(sys.argv[1])
    remove(file)