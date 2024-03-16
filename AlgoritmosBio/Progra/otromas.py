import pandas as pd

# Ejemplo de DataFrame con columnas binarias y una columna de label
data = {
    'feature1': [1, 0, 1, 1, 0],
    'feature2': [0, 1, 1, 0, 0],
    'feature3': [1, 1, 1, 0, 1],
    'label': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Calcular la frecuencia de cada valor en cada columna
value_counts = df.apply(pd.Series.value_counts)

# Ordenar las columnas según la frecuencia de cada valor
sorted_columns = value_counts.sort_values(by=1, axis=1, ascending=False)

# Obtener las columnas ordenadas
ordered_columns = sorted_columns.columns

# Crear un nuevo DataFrame con las columnas ordenadas
df_ordered = df[ordered_columns]

print("DataFrame original:")
print(df)
print("\nDataFrame con columnas ordenadas según la frecuencia de cada valor:")
print(df_ordered)
