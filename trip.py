def hotel_cost(nights):
    return 140 * nights
    
    
    
def plane_ride_cost(city):
    if(city == "Charlotte"):
        return 183
    elif(city == "Tampa"):
        return 220
    elif(city == "Pittsburgh"):
        return 222
    elif(city == "Los Angeles"):
        return 475
        
def rental_car_cost(days):
    totalcost = days * 40
    if(days >= 7):
        totalcost = totalcost - 50
    elif(days >= 3):
        totalcost = totalcost - 20
    return totalcost
    
def trip_cost(city,days,spending_money):
    return (hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)) + spending_money

#print (trip_cost("Los Angeles", 5, 600))

usrcity = input (str(("city ?")))
usrdays = input ("days ?")
usrmon = input ("extra money ?")

print (trip_cost(usrcity,usrdays,usrmon))
