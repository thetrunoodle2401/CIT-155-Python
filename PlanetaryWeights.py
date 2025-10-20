merc_grav = .38
ven_grav = .91
moon_grav = .165
mars_grav = .38
jup_grav = 2.34
sat_grav = .93
uran_grav = .92
nep_grav = 1.12
pluto_grav = .066

name = input("What is your name:")
earth_weight = float( input("What is your weight:") )

weight_on_merc = (earth_weight)*(merc_grav)
weight_on_ven = (earth_weight)*(ven_grav)
weight_on_moon = (earth_weight)*(moon_grav)
weight_on_mars = (earth_weight)*(mars_grav)
weight_on_jup = (earth_weight)*(jup_grav)
weight_on_sat = (earth_weight)*(sat_grav)
weight_on_uran = (earth_weight)*(uran_grav)
weight_on_nep = (earth_weight)*(nep_grav)
weight_on_pluto = (earth_weight)*(pluto_grav)

print(name, 'here are your weights on our Solar System\'s planets:')
print(f'Weight on Mercury:{weight_on_merc:.2f}')
print(f'Weight on Venus:{weight_on_ven:.2f}')
print(f'Weight on our Moon:{weight_on_moon:.2f}')
print(f'Weight on Mars:{weight_on_mars:.2f}')
print(f'Weight on Jupiter:{weight_on_jup:.2f}')
print(f'Weight on Saturn:{weight_on_sat:.2f}')
print(f'Weight on Uranus:{weight_on_uran:.2f}')
print(f'Weight on Neptune:{weight_on_nep:.2f}')
print(f'Weight on Pluto:{weight_on_pluto:.2f}')
