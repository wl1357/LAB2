def main():
 calculate_bmi(height=1.73, weight=37)
 display_main_menu()
 F = get_user_input()
 calc_average(F)
 find_min_max(F)
 pass
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
  

def display_main_menu():
 print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")
def get_user_input()-> list[float]:
 x = input()
 P = x.split(",")
 mylist=P
 F = [float(x) for x in mylist ]
 print(F)
 return(F)
def calc_average(F):
 a=(len(F))
 b=(sum(F))
 avg= b/a 
 print("the avg temp is: " + str(avg))
def find_min_max(F):
 print("Min and Max: " + min(F)+max(F))
 return [min(F), max(F)]
def sort_temperature(F):
 F.sort()
 G=F[:]
 return G

if __name__ == "__main__":
    main()