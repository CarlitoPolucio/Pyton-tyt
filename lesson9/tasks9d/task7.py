access_menu = "утиное филе;фланк-стейк;банановый пирог;плов"
output = "".join([x if x != ";" else ", " for x in access_menu])
print(output.title())