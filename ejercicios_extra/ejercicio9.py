cantindadInvertir = int(input("Cantidad a invertir: "))
interesAnual = float(input("Interés anual: "))
años = int(input("Años: "))

print("El dinero ganado en ", años, " años será: ", (cantindadInvertir*interesAnual)/100 * años)