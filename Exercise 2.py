def calc_weight_on_planet(weight, gravity=23.1):
    mass = weight/9.8
    weight_on_planet = mass*gravity
    return weight_on_planet

print(calc_weight_on_planet(120))
