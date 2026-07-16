hours_work = int(input("Enter the number of hours worked: "))
hours_rate = float(input("Enter the hourly pay rate: "))
if hours_work <= 40:
    gross_pay = hours_work * hours_rate
else:
    regular_pay = 40 * hours_rate
    overtime_pay = (hours_work - 40) * hours_rate * 1.5
    gross_pay = regular_pay + overtime_pay
    
print(f"The gross pay is: ${gross_pay:.2f}")
