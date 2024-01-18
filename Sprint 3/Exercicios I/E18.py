speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

dict_as_list = speed.values()

list_values = list(set(dict_as_list))
print(list_values)