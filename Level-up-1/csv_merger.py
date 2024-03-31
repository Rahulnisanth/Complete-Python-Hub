# MERGING ALL THE CSV_FILES AS DICTIONARIES :
import csv

def merge_csv(csv_list, output_path):
    # build a list with all field names :
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    # write the contents to the output file as per the fieldnames:
    with open (output_path,'w+',encoding="UTF-8",newline='')as outFile:
        writer=csv.DictWriter(outFile,fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file , "r", encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)