# Archivo: modelo_predictivo.py
# Modelo predictivo de ventas usando PySpark para Store Chile

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# ===============================
# 1. Inicializar SparkSession
# ===============================
spark = SparkSession.builder \
    .appName("ModeloPredictivoVentas") \
    .getOrCreate()

# ===============================
# 2. Cargar dataset desde HDFS
# ===============================
ventas_df = spark.read.csv(
    "hdfs:///storechile/ventas/ventas.csv",
    header=True,
    inferSchema=True
)

# ===============================
# 3. Preprocesamiento de datos
# ===============================
# Seleccionamos solo la columna 'precio' como variable predictora ejemplo
assembler = VectorAssembler(
    inputCols=['precio'],
    outputCol='features'
)
data = assembler.transform(ventas_df)

# Dividir en entrenamiento y prueba (70%-30%)
train_data, test_data = data.randomSplit([0.7, 0.3])

# ===============================
# 4. Definición y entrenamiento del modelo
# ===============================
rf = RandomForestRegressor(
    featuresCol='features',
    labelCol='precio',
    numTrees=100,
    maxDepth=5
)
model = rf.fit(train_data)

# ===============================
# 5. Realizar predicciones
# ===============================
predictions = model.transform(test_data)

# ===============================
# 6. Evaluación del modelo
# ===============================
evaluator = RegressionEvaluator(
    labelCol='precio',
    predictionCol='prediction',
    metricName='rmse'
)
rmse = evaluator.evaluate(predictions)
print(f"RMSE del modelo: {rmse}")

# ===============================
# 7. Guardar modelo (opcional)
# ===============================
# model.save("hdfs:///storechile/modelos/random_forest_ventas")

# ===============================
# 8. Cerrar SparkSession
# ===============================
spark.stop()
