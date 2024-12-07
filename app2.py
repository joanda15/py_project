# Lists
list_names = ["Joan", "Paola", "Michell"]
list_ages = [35, 34, 30]
print("Print 2do name list's: ", list_names[1])
print("Print 1 list of 2", list_names+list_ages)
list_names = list_names + ["Vero"]
print("Print new list Vero add", list_names)
list_ages.append(50)
print(list_ages)

# Tuplas
tuple_names = ("David", "Joana", "Marcela")
print(tuple_names.count("Joana"))