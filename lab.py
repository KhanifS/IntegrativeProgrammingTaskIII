class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

# Input weight and height from the user
weight1 = float(input("Enter weight for person 1 in kilograms: "))
height1 = float(input("Enter height for person 1 in meters: "))

weight2 = float(input("Enter weight for person 2 in kilograms: "))
height2 = float(input("Enter height for person 2 in meters: "))

# Create BMI objects
person1 = BMI(weight1, height1)
person2 = BMI(weight2, height2)

# Print BMI values
print("BMI Person 1:", person1.BMI_Value())
print("BMI Person 2:", person2.BMI_Value())

# Comparing two BMI objects
if person1 == person2:
    print("Both persons have the same weight and height.")
else:
    print("Persons have different weight or height.")
