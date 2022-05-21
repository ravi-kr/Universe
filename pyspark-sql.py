!pip install pyspark

import pyspark

import pandas as pd
type(pd.read_csv('test1.csv

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Practise').getOrCreate()
spark

df_pyspark = spark.read.csv('test1.csv')
df_pyspark = spark.read.option('header', 'true').csv('test1.csv')

type(df_pyspark)
df_pyspark.printSchema()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Dataframe').getOrCreate()
spark
df_pyspark = spark.read.option('header', 'true').csv('test1.csv', inferSchema=True)
df_pyspark.printSchema()

df_pyspark=spark.read.csv('test1.csv',header=True,inferSchema=True)
df_pyspark.show()
df_pyspark.printSchema()

type(df_pyspark)

df_pyspark.head(3)

df_pyspark.show()

df_pyspark.select(['Name', 'Experience']).show()

df_pyspark['name']

df_pyspark.dtypes

df_pyspark.describe().show()

df_pyspark=df_pyspark.withColumn('Experience after 2 year', df_pyspark['Experience']+2)

df_pyspark.show()

df_pyspark.drop('Experience after 2 year')

df_pyspark.show()

df_pyspark.withColumnRenamed('Name', 'New Name').show()

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Practise').getOrCreate()

df_pyspark = spark.read.csv('test2.csv', header=True, inferSchema=True)
df_pyspark.printSchema()

df_pyspark.show()

df_pyspark.drop('Name').show()

df_pyspark.show()

df_pyspark.na.drop().show()

df_pyspark.na.drop(how = 'any').show()

df_pyspark.na.drop(how = 'any', thresh=3).show()

df_pyspark.na.drop(how = 'any', subset = ['Age']).show()

df_pyspark.na.fill('Missing Values', ['Experience', 'Age']).show()

df_pyspark.show()

df_pyspark.printSchema()

from pyspark.ml.feature import Imputer

imputer = Imputer(inputcols= ['age', 'Experience', 'Salary'],
outputcols = ["{}_imputed".format(c) for c in ['age', 'Experience', 'Salary']]).setStrategy("median")

imputer.fit(df_pyspark).transform(df_pyspark).show()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('dataframe').getOrCreate()

df_pyspark = spark.read.csv('test1.csv', header = True, inferSchema = True)
df_pyspark.show()

df_pyspark.filter("Salary<=20000").show()

df_pyspark.filter("Salary<=20000").select(['Name', 'Age']).show()

df_pyspark.filter(df_pyspark['Salary']<=20000).show()

df_pyspark.filter((df_pyspark['Salary']<=20000) | (df_pyspark['Salary']>=15000)).show()

df_pyspark.filter(~(df_pyspark['Salary']<=20000)).show()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Agg').getOrCreate()

spark

df_pyspark=spark.read.csv('test3.csv', header=True, inferSchema=True)

df_pyspark.show()

df_pyspark.printSchema()

df_pyspark.groupBy('Name').avg().show()

df_pyspark.groupBy('Departments').mean().show()

df_pyspark.groupBy('Departments').count().show()

df_pyspark.agg({'Salary':'sum'}).show()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Missing').getOrCreate()

training = spark.read.csv('test1.csv', header = True, inferSchema = True)
training.show()

training.printSchema()

training.columns

from pyspark.ml.feature import VectorAssembler
featureassembler = VectorAssembler(inputcols = ["age", "Experience"], outputcol = "Independent Features")

output = featureassembler.transform(training)

output.show()

output.columns

finalized_data = output.select("Independent Features", "Salary")

finalized_data.show()

from pyspark.ml.regression import LinearRegression

train_data, test_data = finalized_data.randomSplit([0.75, 0.25])
regressor = LinearRegression(featuresCol = 'Independent Features', labelCols = 'Salary')
regressor =tregressor.fit(train_data)
regressor.coefficients

regressor.intercept

pred_results = regressor.evaluate(test_data)

pred_results.predictions.show()

pred_results.meanAbsoluteError, pred_results.meanSquaredError

