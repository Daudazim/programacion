mi_bool = 4<5<6
print(mi_bool)
mi_bool = 4<5>6
print(mi_bool)

print("\n")
mi_bool = 4<5 and 5>6
print(mi_bool)
mi_bool = 4<5 and 5==3+2
print(mi_bool)

print("\n")
mi_bool = 4<5 or 5>6
print(mi_bool)
mi_bool = 4<5 or 5==3+2
print(mi_bool)

print("\n")
mi_bool = not ("a" == "a")
print(mi_bool)
mi_bool = not ("a" != "a")
print(mi_bool)