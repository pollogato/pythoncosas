######## GENERADOR DE NUMEROS #####
import numpy as np

arreglo_aleatorio = np.random.uniform(1.0, 7.01, 19)

arreglo_redondeado = [round(float(num), 1) for num in arreglo_aleatorio]

arreglo_redondeado = ','.join(list(map(str,arreglo_redondeado)))
print(arreglo_redondeado)
######## GENERADOR DE NUMEROS #####


#### IMPORTACIONES ####
import statistics as st

#### ENTRADA ####
promedios = input('Ingrese promedios: ')

#### DESARROLLO - GENERACION LISTAS ####
lista_promedios = promedios.split(',') 
lista_prom_num = []

for promedio in lista_promedios:
    lista_prom_num.append((float(promedio)))


#### DESARROLLO - CALCULO ESTADISTICOS ####    
promedio_curso = round(st.mean(lista_prom_num),1)
dev_est = round(st.stdev(lista_prom_num), 1)
mediana = round(st.median(lista_prom_num), 1)

#### DESAROLLO - CALCULO PORCENTAJE APROBADOS ####
aprobados = 0
for promedio in lista_prom_num:
    if promedio >= 4.0:
        aprobados += 1
        
procentaje_aprobados = round(aprobados * 100 / len(lista_prom_num), 1)

#### SALIDA ####
print('Promedio del curso:', promedio_curso)
print('Desviacion estandar:', dev_est) 
print('Mediana:', mediana)
print('Porcentaje de aprobacion:',str(procentaje_aprobados) + '%')