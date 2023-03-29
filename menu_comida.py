from collections import Counter 
import os
total = 0
lista_pedido = []
tacos = {1:"Pollo", 2:"Carne", 3:"Costilla", 4:"Vegetariano"}
precios = {1: 50, 2: 60, 3: 70, 4: 80}

nombre = input("Digita tu nombre: ")
os.system("cls")
while True:
     
    print("""   +--    MENU DE TACOS           --+
             +-- 1 . Pollo         $50        --+
             +-- 2 . Carne         $60        --+
             +-- 3 . Costilla      $70        --+
             +-- 4 . Vegetariano   $80        --+
             +-- 5 . Salir                   --+""" )
    try:
        opcion = int(input("Selecciona una opcion: "))
        if opcion == 5: break
    

        if opcion >= 1 and opcion <=5:
            seleccionar_tacos = tacos.get(opcion)
            precio = precios.get(opcion)
            lista_pedido.append(seleccionar_tacos)

            total = total + precio
            os.system("cls")
            print(f"Has seleccionado {seleccionar_tacos}")
            print("Subtotal: ", total)


        else:
            os.system("cls")
            print("Selecciona una opcion valida")
            print("Subtotal: ", total)
            
            
    except ValueError:
        os.system("cls")
        print("Selecciona una opcion valida")
        print("Subtotal: ", total)




numero_tacos = len(lista_pedido)
os.system("cls")
print(f"Pedido de {nombre} se ha formado: ")
for tacos in lista_pedido:
    print(tacos)


taquitos = Counter(lista_pedido)
print("Total de tacos: ", numero_tacos)
print(taquitos)
print("Total: ", total)