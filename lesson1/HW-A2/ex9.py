current_salary = int(input("insert your current salary: "))
future_salary = int(input("insert your future salary: "))
future_salary_year = future_salary * 12
current_salary_year = current_salary * 12

if current_salary < future_salary:
    print(f"you will earn {future_salary_year - current_salary_year} more per year")
elif current_salary == future_salary:
    print("you will earn the same amount of money per year")
else:
    print(f"you will earn {current_salary_year10 - future_salary_year} less per year")
