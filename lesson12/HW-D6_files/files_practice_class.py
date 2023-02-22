import csv
import json
import os


# ex1

# def ex1(file_path: str, start_line: int, end_line: int):
#     relevant = ''
#     if not os.path.exists(file_path):
#         print('file not found')
#         return
#     else:
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#         if len(lines) - 1 < end_line or len(lines) - 1 <= start_line:
#             print('not valid start line or end line')
#             return
#         for i in range(start_line - 1, end_line):
#             relevant = relevant + lines[i]
#         return relevant
#
#
# print(ex1('../../../evening-ninjas/lesson12/files/data/alice_in_wonderland.txt', 1, 10))


# ex2
# def ex2(file_path: str):
#     sum_rows: int = 0
#     with open(file_path, 'r') as file:
#         reader = csv.DictReader(file)
#         names = reader.fieldnames
#         # col_amount = len(names[0].split(";"))
#         for row in reader:
#             sum_rows += 1
#     return names, sum_rows, len(names)
#
#
# print(ex2("../../../evening-ninjas/lesson12/files/data/AAPL.csv"))


# ex3
# relative_path = "../../../evening-ninjas/lesson12/files/data/AAPL.csv"
# json_path = "D6_ex3.json"
# reader_list = []
#
# with open(relative_path, 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         reader_list.append(row)
#
# with open(json_path, 'w') as f:
#     json.dump(reader_list, f)


# ex4
def json2csv(filepath: str):
    with open(filepath, 'r') as file1:
        data = json.load(file1)

        keys = list(data[0].keys())
        with open('D6_ex4.csv', 'w') as file2:
            writer = csv.DictWriter(file2, fieldnames=keys)
            writer.writeheader()

            for item in data:
                writer.writerow(item)


json2csv('D6_ex3.json')

