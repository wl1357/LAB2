def main():
  calculate_bmi(height=1.73, weight=37)
  display_main_menu()
  F = get_user_input()
  calc_average(F)
  min_max_temp = find_min_max(F)
  print("Min & Max Temperature: ", min_max_temp[0], min_max_temp[1])
  print("median temp",calc_medium_temp(F))
  
def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi= (weight)/(height)**2
 print(bmi)
 if bmi<18.5:
  return -1
 elif bmi>=18.5 and bmi<=25:
  return 0
 elif bmi>25:
  return 1
  

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
 if len(F)==0:
  return[None,None]
 return[min(F),max(F)]
def sort_temperature(F):
 F.sort()
 G=F[:]
 return G
def calc_medium_temp(F):
 B=sorted(F)
 n=len(B)
 mid=n//2
 if n%2==0:
  return round(((B[mid-1]+B[mid])/2),2)
 else:
  return B[mid]

if __name__ == "__main__":
    main()

#def main()
# display_main_menu()
# temp_list=get_user_input(temp_list)
# avg_value=calc_average(temp_list)
# print("avg temp : ")
# min_max=find_min_max(temp_list)
# print("min & max: ,min_max[0],min_max[1])
# sorted_list =sort_temp(temp_list)
# print("sorted temp list ", sorted_list)
# meadian_value=cal_median_temp(temp_list)
# print("median temp value: ", median_value)
# return



#def get_user_input()
# input_data=input()
# reuturn float_list 
#def calc_avgerage(temp_list)
# avg_value