def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi= (weight)/(height)**2
 print(bmi)
 if bmi<18.5:
  print("underweight")
 elif bmi>=18.5 or bmi<=25:
  print("normalweight")
 elif bmi>25:
  print("overweight")
  
calculate_bmi(weight=37, height=1.73)
