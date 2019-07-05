rule all:
	input:
		"C:/Users/wimme/PycharmProjects/snakemake_project/variant_min_NA_gen.txt",
		"C:/Users/wimme/PycharmProjects/snakemake_project/sort_AF.txt",
		"C:/Users/wimme/PycharmProjects/snakemake_project/Experiment_report.pdf",
		"C:/Users/wimme/PycharmProjects/snakemake_project/Experiment.zip"

		
rule remove:
	input:
		"C:/Users/wimme/PycharmProjects/snakemake_project/filtered_variant_list.txt"
	output:
		"C:/Users/wimme/PycharmProjects/snakemake_project/variant_min_NA_gen.txt"
	shell:
		"python remove.py {input}"

rule sort:
	input:
		"C:/Users/wimme/PycharmProjects/snakemake_project/variant_min_NA_gen.txt"
	output:
		"C:/Users/wimme/PycharmProjects/snakemake_project/sort_AF.txt"
	shell:
		"python sort.py {input}"
		
rule makePDF:
	input:
		"C:/Users/wimme/PycharmProjects/snakemake_project/sort_AF.txt"
	output:
		"C:/Users/wimme/PycharmProjects/snakemake_project/Experiment_report.pdf"
	shell:
		"python makePDF.py {input}"
rule zip:
	input:
		"C:/Users/wimme/PycharmProjects/snakemake_project/filtered_variant_list.txt",	
		"C:/Users/wimme/PycharmProjects/snakemake_project/variant_min_NA_gen.txt",
		"C:/Users/wimme/PycharmProjects/snakemake_project/sort_AF.txt",
		"C:/Users/wimme/PycharmProjects/snakemake_project/Experiment_report.pdf"	
	output:
		"C:/Users/wimme/PycharmProjects/snakemake_project/Experiment.zip"
	shell:
		"python zipfiles.py {input} {input} {input} {input}"
	