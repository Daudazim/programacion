dictionary = {"c1": "value1", "c2": "value2"}
print(type(dictionary))
print(dictionary)

result = dictionary["c1"]
print(result)

customer = {"name": "Jose", "last_name": "Ortega", "age": 40, "size_shoe": 45}
consultation = (customer["last_name"])
print(consultation)

dic = {"c1": "gato", "c2": [12, 15, 16], "c3": {"a1": 100, "a2": 200}}
print(dic["c2"][0])
print(dic["c3"]["a1"])

dict_2 = {"C1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dict_2["c2"][1].upper())

dic_2 = {1: "a", 2: "b", 3: "c"}
print(dic_2)
dic_2[4] = "d"
print(dic_2)