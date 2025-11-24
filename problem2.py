# get temperature in farengeith and convert into centigrate and calvin
user_input = int(input("Please enter temperature in fahrenheit :"))
def temperature(F):
    C = 5/9 * (F - 32)
    K = (F + 459.67) * 5/9
    
    return C, K
C,K = temperature(user_input)

    
print(f"Temperature {user_input} F is {round(C,2)}°C in Celsius and {round(K,2)} K in Kelvin")