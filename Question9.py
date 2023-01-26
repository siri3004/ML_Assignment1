import math

n = int(input("Enter the number of students: "))
weights_lbs = []
weights_kgs = []

for i in range(n):
    weight = float(input(f"Enter the weight of student {i+1} in pounds: "))
    weights_lbs.append(weight)
    weight_kgs = weight * 0.453592
    weights_kgs.append(weight_kgs)

print("Weights in pounds: ", weights_lbs)
print("Weights in kilograms: ", weights_kgs)
