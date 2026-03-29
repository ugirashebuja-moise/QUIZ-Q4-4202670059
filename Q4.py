salary = float(input("Enter your salary: "))
years_0f_service = int(input("Enter your years of service: "))
if years_0f_service >= 10:
# Incremented_salary = salary + bonus
    Incremented_salary = salary + (0.2 * salary)
elif 5 <= years_0f_service <= 9:
   Incremented_salary = salary + (0.1 * salary)
elif 0 < years_0f_service < 5:
    Incremented_salary = salary + (0.05 * salary)
else:
    Incremented_salary = salary 
    print("No bonus for those on probation")

print("Your salary with bonus is:", Incremented_salary)