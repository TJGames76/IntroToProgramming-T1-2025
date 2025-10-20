def Hurricane_Classifier():
    wind_speed = input("input wind speed\n> ")
    if int(wind_speed) <= 74:
        print("Tropical storm")
    elif int(wind_speed) >= 96 and int(wind_speed)< 111:
        print("Category 1")
    elif int(wind_speed) >= 111 and int(wind_speed)< 130:
        print("Category 2")
    elif int(wind_speed) >= 120 and int(wind_speed)< 157:
        print("Category 3")
    elif int(wind_speed) >= 157 and int(wind_speed)< 158:
        print("Category 4")
    elif int(wind_speed) >= 158:
        print("Category 5")
    else:
        print("normal weather")
Hurricane_Classifier()