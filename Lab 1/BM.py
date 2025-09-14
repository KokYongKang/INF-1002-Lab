import sys

if len(sys.argv) != 4:
    print("Your input is invalid!")
else:
    units = sys.argv[1].lower()
    height = float(sys.argv[2])
    weight = float(sys.argv[3])

    if units in ["metric", "imperial"] and height > 0 and weight > 0:
        if units == "metric":
            bmi = weight / (height ** 2)
        elif units == "imperial":
            bmi = (weight * 703) / (height ** 2)

        if bmi < 16:
            print("%.2f %18s" % (bmi, "severe Thinness"))
        elif 16 <= bmi < 17:
            print("%.2f %18s" % (bmi, "Moderate Thinness"))
        elif 17 <= bmi < 18.5:
            print("%.2f %18s" % (bmi, "Mild Thiness"))
        elif 18.5 <= bmi < 25:
            print("%.2f %18s" % (bmi, "Normal"))
        elif 25 <= bmi < 30:
            print("%.2f %18s" % (bmi, "Overweight"))
        elif 30 <= bmi < 35:
            print("%.2f %18s" % (bmi, "Obese Class I"))
        elif 35 <= bmi < 40:
            print("%.2f %18s" % (bmi, "Obese Class II"))
        else:
            print("%.2f %18s" % (bmi, "Obese Class III"))

    else:
        print("your input is invalid!")
