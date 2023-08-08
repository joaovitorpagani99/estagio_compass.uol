1 - spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes  = spark.read.csv('nomes_aleatorios.txt')

df_nomes.show()


2- 
df_nomes = df_nomes.withColumnRenamed("_c0","Nomes")
df_nomes.show(20)


3-
from pyspark.sql.functions import col, when, rand
df_nomes = df_nomes.withColumn("Escolaridade", when(rand() < 0.33, "Fundamental")
.when(rand() < 0.66, "Medio").otherwise("Superior"))

df_nomes.show(100, truncate=False)

4-

paises_america_sul = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']
get_pais = udf(lambda: random.choice(paises_america_sul), StringType())
df_nomes = df_nomes.withColumn('Pais', get_pais())

5-

get_random_ano_nascimento = udf(lambda: random.randint(1945, 2010), IntegerType())
df_nomes = df_nomes.withColumn('AnoNascimento', get_random_ano_nascimento())


6-

df_select = df_nomes.filter(col('AnoNascimento') >= 2000)
df_select.select('Nomes').show(10)

7-
df_nomes.createOrReplaceTempView("pessoas")
df_select = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_select.select('Nomes').show(10)

8 -
df_millennials = df_nomes.filter((df_nomes['AnoNascimento'] >= 1980) & (df_nomes['AnoNascimento'] <= 1994))

num_millennials = df_millennials.count()

print("Número de pessoas da geração Millennials:", num_millennials)

9 - 

df_millennials = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994")

num_millennials = df_millennials.count()

print("Número de pessoas da geração Millennials:", num_millennials)

10 -

df_quantidade_por_pais_geracao = spark.sql("""
    SELECT Pais, 
           CASE WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                WHEN AnoNascimento BETWEEN 1995 AND 2023 THEN 'Geração Z'
                ELSE 'Outra' END AS Geracao, 
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, 
             CASE WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                  WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                  WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                  WHEN AnoNascimento BETWEEN 1995 AND 2023 THEN 'Geração Z'
                  ELSE 'Outra' END
    ORDER BY Pais, Geracao
""")
df_quantidade_por_pais_geracao.show()