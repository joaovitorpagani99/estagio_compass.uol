from pyspark.sql import SparkSession
from pyspark.sql.functions import length

df = spark.read.text("/workspaces/estagio_compass.uol/Sprint 7/exercicios/secao 3 - Exercicios/tarefa 2/README.md")

filtrar_linhas = df.filter(length("value") > 0)

palavras_divididas = filtrar_linhas.rdd.flatMap(lambda x: x[0].split(' '))

palavras_contar = palavras_divididas.map(lambda x:(x,1))

palavras_contar = palavras_divididas.map(lambda x:(x,1)).reduceByKey(lambda x, y: x + y).map(lambda x: (x[1], x[0])).sortByKey(False)

for palavras in palavras_contar.collect():
	print(palavras)