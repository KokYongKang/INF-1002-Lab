# Develop weekly Payment Calculator

import sys

if len(sys.argv) != 4:
    print("Your input is invalid!")

else:
    try:
        hours_worked = float(sys.argv[1])
        normal_rate = float(sys.argv[2])
        overtime_rate = float(sys.argv[3])

        if hours_worked >= 10000:
            print("Your input is invalid!")
        else:
            if hours_worked <= 40:
                normal_hours = hours_worked
                overtime_hours = 0

            else:
                normal_hours = 40
                overtime_hours = hours_worked - 40

            normal_payment = normal_hours * normal_rate
            overtime_payment = overtime_hours * overtime_rate
            total_payment = normal_payment + overtime_payment

            print(
                f"Normal Salary:{normal_payment:.2f}, Extra Salary:{overtime_payment:.2f}, Total Salary:{total_payment:.2f}", end="")

    except ValueError:
        print("Your input is invalid!")
