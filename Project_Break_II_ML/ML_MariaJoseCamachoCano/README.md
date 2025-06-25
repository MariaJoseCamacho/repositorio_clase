# Predicción de Rotación de Empleados (Churn Laboral)
## Descripción del proyecto  

En este proyecto desarrollo un modelo de Machine Learning para predecir qué empleados tienen mayor probabilidad de abandonar una empresa. Esta herramienta es útil para departamentos de recursos humanos que desean anticiparse a la rotación laboral y aplicar estrategias de retención basadas en datos objetivos.

La rotación de empleados puede suponer un alto coste económico y de productividad, por lo que contar con un modelo predictivo permite tomar decisiones más informadas en cuanto a contratación, clima laboral y promociones.

# Employee Attrition Prediction  
## Project Description  

In this project, I develop a Machine Learning model to predict which employees are more likely to leave a company. This tool is useful for HR departments looking to proactively manage talent and reduce attrition costs by identifying at-risk employees based on objective data.

Employee churn can result in high costs and loss of knowledge, so having a predictive model allows better planning in hiring, training, and retention strategies.

---

## Dataset empleado  
He utilizado el dataset público **IBM HR Analytics Employee Attrition Dataset**, disponible en Kaggle, que contiene información de 1.470 empleados, con variables demográficas, laborales, de rendimiento y satisfacción. La variable objetivo es `Attrition`, que indica si el empleado ha dejado la empresa.

Puedes acceder al dataset en el siguiente enlace:  
[IBM HR Analytics - Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

### Variables destacadas:  
- Edad, sexo, estado civil  
- Departamento, puesto, salario, tiempo en la empresa  
- Nivel de satisfacción, número de proyectos, evaluaciones  
- Balance vida-trabajo, horas extra  
- Variable objetivo: `Attrition` (Sí/No)

## Dataset Used  
I used the public **IBM HR Analytics Employee Attrition Dataset**, available on Kaggle, which includes data on 1,470 employees and their demographic, job, performance, and satisfaction details. The target variable is `Attrition`, indicating whether an employee has left the company.

You can access the dataset here:  
[IBM HR Analytics - Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## Solución adoptada  
Para resolver el problema, utilizo una combinación de técnicas de aprendizaje supervisado y no supervisado:

- Clasificación supervisada: entreno modelos como Regresión Logística, Random Forest y XGBoost para predecir si un empleado se marchará o no.
- Segmentación no supervisada: aplico clustering (KMeans y/o HDBSCAN) para identificar perfiles de empleados según características como la satisfacción, el rendimiento o la antigüedad.
- Reducción de dimensionalidad (PCA o t-SNE) para visualizar los clusters de empleados de forma más clara.
- Evaluación con métricas como Accuracy, Recall, F1-score y AUC-ROC.
- Interpretación del modelo para entender qué variables influyen más en la rotación.

Este enfoque permite combinar predicción y análisis estratégico del capital humano.

## Solution Adopted  
To solve the problem, I use a combination of supervised and unsupervised learning techniques:

- **Supervised classification**: I train models like Logistic Regression, Random Forest, and XGBoost to predict whether an employee will leave.
- **Unsupervised segmentation**: I apply clustering (KMeans and/or HDBSCAN) to group employees based on satisfaction, performance, or tenure.
- **Dimensionality reduction** (PCA or t-SNE) is used to visualize employee clusters.
- **Evaluation metrics**: Accuracy, Recall, F1-score, and AUC-ROC are used to measure model performance.
- **Interpretability**: I analyze feature importance to understand which factors most influence attrition.

This approach combines predictive power with strategic workforce analysis.

---

## Estructura del repositorio  

ML_ChurnLaboral_MariaJoseCamacho/  
├── README.md                  # Documentación general del proyecto  
├── main.ipynb                 # Notebook principal con el proceso completo  
├── src/  
│   ├── data_sample/           # Muestra reducida del dataset para subir al repositorio  
│   ├── models/                # Modelos entrenados guardados (pkl, joblib...)  
│   ├── notebooks/             # Notebooks de exploración, pruebas y desarrollo  
│   └── utils/                 # Módulos o funciones auxiliares del proyecto  
├── requirements.txt           # Lista de librerías necesarias  
└── report.pdf                 # Informe final para presentación del proyecto  

---

## Métricas y evaluación  
Para evaluar la calidad del modelo, utilizo:

- **Accuracy**: porcentaje de empleados correctamente clasificados.  
- **Recall**: de los empleados que realmente se fueron, cuántos detectó el modelo.  
- **Precision**: de los que el modelo predijo que se irían, cuántos realmente se fueron.  
- **F1-score**: equilibrio entre precisión y recall.  
- **AUC-ROC**: curva para analizar el rendimiento general del modelo.  

También analizo la **importancia de las variables** y visualizo los resultados para entender el comportamiento del modelo y generar conclusiones prácticas para recursos humanos.

---

## Recomendaciones futuras  
Este modelo puede ampliarse con más datos reales, incorporar datos de encuestas internas o de clima laboral, y conectarse a sistemas de RRHH en tiempo real para automatizar alertas de riesgo de abandono.

---

✅ Proyecto sencillo de exponer, con fuerte conexión con el negocio y fácil de entender para perfiles no técnicos.

