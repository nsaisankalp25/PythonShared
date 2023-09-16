import csv

link = r"C:\Users\saisa\Desktop\sample_csv.csv"
with open(link, "r") as file:
    csv_file_reader = csv.reader(file, delimiter=',')
    for row in csv_file_reader:
        print(row)

    link_new = r"C:\Users\saisa\Desktop\updated_csv.csv"
    # data = [{"NAME":"Bob The Builder", "HOBBIE":"Building", "AGE":'INFINITY'},
    #         {"NAME":"Pokemon", "HOBBIE":"Gaming", "AGE":'0'},
    #         {"NAME":"Doraemon", "HOBBIE":"Having Fun", "AGE":'Robot'}]
    # headers_list = ['NAME', 'HOBBIE', 'AGE']

    # with open(link_new, "w") as new_file:
    #     csv_writer = csv.DictWriter(new_file, fieldnames=headers_list, delimiter=',')
    #     csv_writer.writeheader()

    #     for i in data:
    #         csv_writer.writerow(i)











a= """











.CSV FILES

Comma Seperated Values

NAME    HOBBIE   AGE
Ayan  , Pokemon , 8
Maheen, Shorts  , 12
Sai   , Flute   , 15

> EASY TO USE - FLEXIBLE
> Light weight
> Easily accesible/modifiable












"""