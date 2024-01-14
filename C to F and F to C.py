def convert_temperature():

    scale = (input("ENTER c OR f FOR CONVERION FROM TO: "))
    temp = float(input("ENTER THE TEMPERTAURE: "))


    if scale.lower() == "c":
        return temp * 9/5 + 32  
    elif scale.lower() == "f":
        return (temp - 32) * 5/9
    else:
        return "Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit."

print(convert_temperature())
