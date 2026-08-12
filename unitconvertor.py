# unit convertor 
def fehr_to_cels():
    fahrenheit = float(input("Enter value"))
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)

def cels_to_fehr():
    celsius = float(input("Enter value"))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

def km_to_cm():
    kilometer = int(input("Enter value"))
    centi = kilometer*100000
    print(centi)

def cm_to_km():
    centimeter = int(input("Enter value"))
    kilo = centimeter/100000
    print(kilo)

while True:
    print("1:fehr_to_cels")
    print("2:cels_to_fehr")
    print("3:km_to_cm")
    print("4:m_to_km")
    print("5:exit")
    
    choice = int(input("choice : Enter choice")) 

    if choice == 1:
        fehr_to_cels()
    elif choice == 2:
        cels_to_fehr()
    elif choice == 3: 
        km_to_cm() 
    elif choice == 4:
        cm_to_km()
    elif choice == 5:
        break