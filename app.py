# Python

# Variables string, int, float, bool, list, tupla, dic
var_firstname = "Joan David"
var_lastname = "Gomezjurado Sanchez"
var_age = 35
var_height = 1.70
var_weigth = 75.00
var_sex = "Man"
var_gender = "Transgender woman"
var_sexorientation = "Pansexual"
var_true = True
var_false = False

list_name = [var_firstname, var_lastname]
tuple_sex = (var_gender, var_gender, var_sexorientation)
dic_measurements = {"Bust":108, "Waist":101, "Hips":107}

print(dic_measurements)

# Entradas
print("Good morning, what it's your name?")
var_namein = input()
print("Hello: ", var_namein)

# Caracteres especiales
var_especial = "Texto"
print("Jameson\nJoan")
print("Jameson\tJoan")
print("Jameson\\Joan")
print("Jameson\"Joan")
print("Jameson\'Joan")

print("Insert list food")
var_food = input()
list_food = var_food.split(",")
list_food = [item.split() for item in list_food]
print("Lists food's: ", list_food)

# Operadores aritmeticos
var_arit = int(input("Plis insert first number: "))
var_brit = int(input("Plis insert last number: "))
var_add = var_arit + var_brit
var_sus = var_arit - var_brit
var_mul = var_arit * var_brit
var_div = var_arit / var_brit
print("Add: ", var_add, "Sus: ", var_sus, "Mul: ", var_mul, "Div: ", var_div)

# Seleciona una opcion
var_F = False
var_V = True
print("Falso: ", var_F, "Verdadero: ", var_V)

# Operador logico AND
var_AND1 = True and True
var_AND2 = True and False
var_AND3 = False and True
var_AND4 = False and False
print(var_AND1, var_AND2, var_AND3, var_AND4)

# Operador OR
var_OR1 = True or True
var_OR2 = True or False
var_OR3 = False or True
var_OR4 = False or False
print(var_OR1, var_OR2, var_OR3, var_OR4)

# Operador NOT
var_NOT1 = not True
var_NOT2 = not False
print(var_NOT1, var_NOT2)

# Operadores logicos
var_numA = int(input("ingrese el numero A: "))
var_numB = int(input("ingrese el numero B: "))
var_igual = var_numA == var_numB
var_diferente = var_numA != var_numB
var_mayor = var_numA > var_numB
var_menor = var_numA < var_numB
var_mayorigual = var_numA >= var_numB
var_menorigual = var_numA <= var_numB
print(var_igual, var_mayor, var_mayorigual, var_menor, var_menorigual)

# Cadena de string
var_cadena1 = str(input("first string: "))
var_cadena2 = str(input("last string: "))
var_cadenas = (var_cadena1 + var_cadena2)
print(var_cadenas)