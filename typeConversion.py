birth_year = input('Birth year: ')
print(type(birth_year))  # type() returns the type of variable
age = 2021 - int(birth_year)  # also float() and bool()
print(type(age))
print(age)

weight_lbs = input('Weight (lbs): ')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)
