


# #    link_new = r"C:\Users\saisa\Desktop\updated_csv.csv"
#     # data = [{"NAME":"Bob The Builder", "HOBBIE":"Building", "AGE":'INFINITY'},
#     #         {"NAME":"Pokemon", "HOBBIE":"Gaming", "AGE":'0'},
#     #         {"NAME":"Doraemon", "HOBBIE":"Having Fun", "AGE":'Robot'}]
#     # headers_list = ['NAME', 'HOBBIE', 'AGE']

#     # with open(link_new, "w") as new_file:
#     #     csv_writer = csv.DictWriter(new_file, fieldnames=headers_list, delimiter=',')
#     #     csv_writer.writeheader()

#     #     for i in data:
#     #         csv_writer.writerow(i)



# .CSV FILES

# Comma Seperated Values

# NAME    HOBBIE   AGE
# Ayan  , Pokemon , 8
# Maheen, Shorts  , 12
# Sai   , Flute   , 15

# > EASY TO USE - FLEXIBLE
# > Light weight
# > Easily accesible/modifiable


# import csv
# import matplotlib.pyplot as plt
# import collections

# link = r"C:\Users\saisa\Desktop\2023 Car Dataset.csv"
# with open(link, "r") as file:
#     csv_file_reader = csv.reader(file, delimiter=',')
#     data = []
#     for row in csv_file_reader:
#         #print(row)
#         data.append(row[-1].strip().lower())


# """


import csv 
import collections
from matplotlib import pyplot as plt

file_path = r"C:\Users\saisa\Desktop\2023 Car Dataset.csv"
with open(file_path, 'r') as file:
    complete_data = csv.reader(file)
    
    car_makers = []
    
    for i in complete_data:
        car_makers.append(i[-1].strip())
    
car_makers = car_makers[1:]


frequency = collections.Counter(car_makers)
dict_frequency = dict(frequency)

keys = list(dict_frequency.keys())
values = list(dict_frequency.values())
print(values)

# print(car_makers)
# Ford = 0
# for i in car_makers:
#     if i == 'Ford':
#         Ford += 1
# print(Ford)
plt.bar(keys,values, color = 'r', label = 'CAR MANUFACTURERS')
plt.legend()
plt.show()