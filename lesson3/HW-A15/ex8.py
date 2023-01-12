various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
int_var = []

for var in various:
    if type(var) == int:
        if var > 0:
            int_var.append(var)

print(int_var)
