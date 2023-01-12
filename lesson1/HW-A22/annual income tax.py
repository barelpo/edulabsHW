annual_salary = int(input("insert you income: "))
tax = 0
if annual_salary < 77400:
    tax = 0.1 * annual_salary
else:
    tax = 0.1 * 77400
    annual_salary = annual_salary - 77400

    if annual_salary < (110880 - 77401):
        tax = tax + 0.14 * annual_salary
    else:
        tax = tax + 0.14 * (110880 - 77401)
        annual_salary = annual_salary - (110882 - 77401)

        if annual_salary < (178080 - 110881):
            tax = tax + 0.2 * annual_salary
        else:
            tax = tax + 0.2 * (178080 - 110881)
            annual_salary = annual_salary - (178080 - 110881)

            if annual_salary < (247440 - 178081):
                tax = tax + 0.31 * annual_salary
            else:
                tax = tax + 0.31 * (247440 - 178081)
                annual_salary = annual_salary - (247440 - 178081)

                if annual_salary < (514920 - 247441):
                    tax = tax + 0.35 * annual_salary
                else:
                    tax = tax + 0.35 * (514920 - 247441)
                    annual_salary = annual_salary - (514920 - 247441)

                    if annual_salary < (663240 - 514921):
                        tax = tax + 0.47 * annual_salary
                    else:
                        tax = tax + 0.47 * (663240 - 514921)
                        annual_salary = annual_salary - (663240 - 514921)

                        if annual_salary > 0:
                            tax = tax + 0.5 * annual_salary

print(f"the annual tax you have to pay is: {tax}")
