#f=c*9/5+32
#c=5/9*(f-32)
#Kelvin (K) = (Fahrenheit - 32) / 1.8 + 273.15.
#° F = 9/5 (K - 273) + 32
#Celsius to Kelvin, K = C + 273.15
#Kelvin to Celsius,C=K-237.15
x=lambda a:(a*9/5)+32
y=lambda a:5/9*(a-32)
z=lambda a:(a-32)/1.8+237.15
zy=lambda a:9/5*(a-273)+32
zx=lambda a:a+273.15
xz=lambda a:a-237.15
b=int(input("1.Celsius to Fehrenheit\n2.Fehrenheit to Celsius\n3.Fehrenheit To Kelvin\n4.Kelvin to Fehrenheit\n5.Celsius to Kelvin\n6.Kelvin To Celsius\nWhat Do You Want to Convert:-"))
if b>6:
    raise "give input correctly"
try:
    a=int(input("Give Temperature number:-"))

    if b==1:
        print(x(a))
    elif b==2:
        print(y(a))
    elif b==3:
        print(z(a))
    elif b==4:
        print(zy(a))
    elif b==5:
        print(zx(a))
    elif b==6:
        print(xz(a))

    else:
        print("Give valid input")
except:
    print("give value in int only")
