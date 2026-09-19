vlan = int(input("Ingrese número de VLAN: "))

if vlan >= 1 and vlan <= 1005:
    print("Corresponde a una VLAN de rango normal")
elif vlan >= 1006 and vlan <= 4094:
    print("Corresponde a una VLAN de rango extendido")
else:
    print("No corresponde a una VLAN válida")
