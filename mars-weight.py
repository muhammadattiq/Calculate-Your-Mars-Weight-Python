## This Prgram will caculte the weight of user according to Mars ( the weight on Mars is 37.8% ) ##

user_weight = float(input("please enter your weight in KG : "))

mars_weight = 37.8/100*user_weight

weight = round(mars_weight,4)

print(f"Your weight on Mars will be : {weight}")