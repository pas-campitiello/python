D = float(input("Insert diameter or the characteristic linear dimension in m: "))
v = float(input("Insert the velocity of the fluid with respect to the object in m/s: ")) 
rho = float(input("Insert the density of the fluid in SI units kg/m^3: "))
mu = float(input("Insert the dynamic viscosity of the fluid in Pa·s or N·s/m^2 or kg/m·s: "))

Re = (D*v*rho) / mu  

print(Re)

if (Re <= 2100):
    print("Laminar flow")
elif (Re > 2100 and Re <= 4000):
    print("Transient flow") 
else:
    print("Turbulent Flow")
