import sys


def sort(file):
    data = open(file)
    sort_AF = open("C:/Users/wimme/PycharmProjects/snakemake_project/sort_AF.txt", "w")
    variant_dict = {}
    for variant in data:
        variant = variant.replace('(', '').replace(')', '').replace("'", '').replace(" ", '')
        variant_lijst = variant.split(",")
        variant_dict[float(variant_lijst[-1])] = variant_lijst[:-1]

    sorted_list = []
    for i in range(len(variant_dict.keys())):

        laagste_AF = min(variant_dict.keys())
        sorted_list.append(variant_dict[laagste_AF]+[laagste_AF])

        del variant_dict[laagste_AF]

    for line in sorted_list:
        sort_AF.write(str(line).replace("[", '').replace("]", '').replace("'", ''))
        sort_AF.write("\n")







if __name__ == '__main__':
    file = str(sys.argv[1])
    sort(file)