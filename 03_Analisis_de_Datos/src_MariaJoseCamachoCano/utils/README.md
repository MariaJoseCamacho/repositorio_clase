# Análisis del Valor de los Cómics como Objetos de Coleccionista

## Objetivo

Este proyecto tiene como objetivo principal responder a la siguiente pregunta:

> **¿Qué características tienen mayor peso a la hora de elevar el valor de un cómic en el mercado de coleccionismo?**

Se ha realizado un Análisis Exploratorio de Datos (EDA) para detectar patrones, relaciones y factores determinantes en el precio de los cómics.

---

## 🧩 Dataset

Se trabaja con tres tablas que contienen información sobre diferentes aspectos de los cómics:

- **comics_data.csv**: Datos principales de los cómics (título, editorial, año de publicación, autor, etc.).
- **Complete_DC_Comic_Books.csv**: Datos principales de los cómics centrados en un tipo de personajes del universo DC.
- **Marvel_Comics.csv**: Datos principales de los cómics centrados en un tipo de personajes del universo Marvel.

Las tablas han sido unificadas y limpiadas para facilitar el análisis conjunto.

---

## Librerías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Proceso de trabajo

1. **Carga y exploración de datos**  
   Se exploran las tres tablas de forma independiente y posteriormente se fusionan.

2. **Limpieza de datos**  
   - Tratamiento de valores nulos  
   - Conversión de tipos de datos  
   - Normalización de campos (nombres de editoriales, fechas, etc.)

3. **Análisis exploratorio (EDA)**  
   - Distribución de precios por editorial, año o autor  
   - Relación entre número de ejemplares disponibles y precio  
   - Comparación entre editoriales y su influencia en el valor del cómic  
   - Impacto del estado de conservación (si está disponible en los datos)

4. **Visualizaciones**  
   - Gráficos de dispersión, histogramas, boxplots y heatmaps para identificar correlaciones y tendencias.

5. **Conclusiones**  
   Se resumen las variables con mayor correlación con el precio y se extraen insights clave.

---

## 📌 Conclusiones preliminares

> (Este bloque debe completarse una vez terminado el análisis. Aquí se incluirán los principales hallazgos, por ejemplo:)

- Los cómics publicados antes del año 1980 tienen, de media, un precio significativamente más alto.
- El número de ejemplares disponibles guarda una relación inversa con el precio.
- Algunas editoriales (como Marvel o DC) presentan un precio medio más alto, especialmente en ciertas décadas.
- El autor también es un factor determinante en algunos casos.

---