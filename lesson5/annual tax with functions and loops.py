def tax(salary, stages, taxes):
    annual_salary_tax = 0
    for i, stage in enumerate(stages):
        if salary < stage:
            annual_salary_tax += taxes[i] * salary
            break
        else:
            annual_salary_tax += taxes[i] * stage
            salary -= stage
    return annual_salary_tax


annual_salary = int(input("insert your annual salary: "))

stages_list = [77400, 110880 - 77400, 178080 - 110880, 247440 - 178080, 514920 - 247440, 663240 - 514920, 0]

taxes_list = [0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5]

print(tax(annual_salary, stages_list, taxes_list))
