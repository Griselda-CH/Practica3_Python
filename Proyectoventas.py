"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
datos= pd.read_csv('C:\\Users\\Intel i5\\.spyder-py3\\Proyecto Final\\tiendaonline.csv')
print(datos.head())
print(datos.info())
# Verificar la cantidad de valores nulos por columna
print(datos.isnull().sum())

# Opcional: eliminar filas con valores nulos
datos_limpios = datos.dropna(subset=['Gender', 'Age', 'Amount_spent'])

# Convertir la columna 'Transaction_date' a tipo datetime
datos_limpios['Transaction_date'] = pd.to_datetime(datos_limpios['Transaction_date'], format='%m/%d/%Y')

# Mostrar los datos limpios
print(datos_limpios.info())
# ANALISIS DE VENTAS POR ESTADO
# Agrupar por estado y calcular el monto total gastado
ventas_por_estado = datos_limpios.groupby('State_names')['Amount_spent'].sum()

# Mostrar los resultados
print(ventas_por_estado)

# Visualizar los resultados
import matplotlib.pyplot as plt

ventas_por_estado.plot(kind='bar', figsize=(10,6))
plt.title('Ventas Totales por Estado')
plt.xlabel('Estado')
plt.ylabel('Monto Total Gastado')
plt.show()
# ANALISIS POR SEGMENTO
# Agrupar por segmento y calcular el monto total gastado
ventas_por_segmento = datos_limpios.groupby('Segment')['Amount_spent'].sum()

# Mostrar los resultados
print(ventas_por_segmento)

# Visualizar los resultados
ventas_por_segmento.plot(kind='bar', figsize=(8,5))
plt.title('Ventas Totales por Segmento')
plt.xlabel('Segmento')
plt.ylabel('Monto Total Gastado')
plt.show()
#ANALISIS POR METODO DE PAGO
# Agrupar por método de pago y calcular el monto total gastado
ventas_por_metodo_pago = datos_limpios.groupby('Payment_method')['Amount_spent'].sum()

# Mostrar los resultados
print(ventas_por_metodo_pago)

# Visualizar los resultados
ventas_por_metodo_pago.plot(kind='pie', autopct='%1.1f%%', figsize=(7,7))
plt.title('Distribución de Ventas por Método de Pago')
plt.ylabel('')
plt.show()
#ANALISIS TEMPORAL DE VENTAS
# Extraer el mes de la columna de fechas
datos_limpios['Month'] = datos_limpios['Transaction_date'].dt.month

# Agrupar por mes y calcular el monto total gastado
ventas_por_mes = datos_limpios.groupby('Month')['Amount_spent'].sum()

# Mostrar los resultados
print(ventas_por_mes)

# Visualizar los resultados
ventas_por_mes.plot(kind='line', marker='o', figsize=(8,5))
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Monto Total Gastado')
plt.grid(True)
plt.show()
# ANALISIS DE CLIENTES POR LA EDAD
# Definir por rangos de edad
bins = [0, 18, 25, 35, 45, 55, 65, 100]
labels = ['<18', '18-25', '26-35', '36-45', '46-55', '56-65', '65+']
datos_limpios['Age_group'] = pd.cut(datos_limpios['Age'], bins=bins, labels=labels)

# Agrupar por grupo de edad y calcular el monto total gastado
ventas_por_grupo_edad = datos_limpios.groupby('Age_group')['Amount_spent'].sum()

# Mostrar los resultados
print(ventas_por_grupo_edad)

# Visualizar los resultados
ventas_por_grupo_edad.plot(kind='bar', figsize=(8,5))
plt.title('Ventas Totales por Grupo de Edad')
plt.xlabel('Grupo de Edad')
plt.ylabel('Monto Total Gastado')
plt.show()
# Exportar datos 
datos_limpios.to_csv('resultados_limpios.csv', index=False)
