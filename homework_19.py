import os
import json
import yaml


# cars = []
# while True:
#     input_ = input("model year color?\n")
#     model = input_.split()[0]
#     year = input_.split()[1]
#     color = input_.split()[2]
#     dict_ = dict(
#         model=model,
#         year=year,
#         color=color
#     )
#     cars.append(dict_)
#     check = input("Enough? yes for exit: ")
#     if check == "yes":
#         break

# with open("car.json", "w") as json_file:
#     json.dump(cars, json_file, indent=3)

with open("car.json", "r") as json_file:
    data = json.load(json_file)
    print(data, type(data))

json_str = json.dumps(data)
with open("cars.txt", "w") as text_file:
    text_file.write(json_str)

with open("test.yaml", "w") as yml:
    yaml.dump(data, yml, allow_unicode=True)

with open("test.yaml", "r") as yml1:
    yaml_data = (yaml.dump(yaml.load(yml1, Loader=yaml.FullLoader)))
    print(yaml_data)

with open("new_car.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent=4)

with open("new_car_text.txt", "w") as text_file:
    text_file.write(yaml_data)






