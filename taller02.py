# -*- coding: utf-8 -*-
"""Taller02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ptxO2mWDVIk1hnb8V7nizg2ZUlbNW8Mu
"""

salario_b = float(input("¿Cuál es su salario base?"))
print("Salario base es ${:,.0f}".format(salario_b))
venta_1 = float(input("Ingrese valor de la venta 1 = "))
venta_2 = float(input("Ingrese valor de la venta 2 = "))
venta_3 = float(input("Ingrese valor de la venta 3 = "))
total_v = venta_1 + venta_2 + venta_3
print("El total de las tres ventas es ${:,.0f}" .format(total_v))
comision = total_v * 0.10
print("La comisión es de ${:,.0f}" .format(comision))
total = salario_b + comision
print("El salario total es de ${:,.0f}" .format(total))

valor_c = float(input("Ingrese valor de la compra = $"))
desc = valor_c * 0.15
print("El descuento es de ${:,.1f}" .format(desc))
total = valor_c - desc
print("El valor a pagar es de ${:,.1f}" .format(total))

nota_1 = float(input("Ingrese la nota No. 1: "))
nota_2 = float(input("Ingrese la nota No. 2: "))
nota_3 = float(input("Ingrese la nota No. 3: "))
total = round((nota_1 + nota_2 + nota_3)/3, 2)
print(f"La nota final es {total}")

hombres = int(input("¿Cuántos hombres hay?"))
mujeres = int(input("¿Cuántas mujeres hay?"))
total = hombres + mujeres 
porcen_h = round((hombres * 100)/total, 2)
porcen_m = 100 - porcen_h
print(f"El porcentaje de hombres es {porcen_h}% y el porcentaje de mujeres es {porcen_m}%")