from pyspark.sql import SparkSession
from pyspark.sql import *
spark = SparkSessio.builder.appName("PySpark SQL").getOrCreate()
sc = spark.sparkContext
A = sc.textFile("Filename.txt")
B = lines.map(lambda x: x.split(","))
C = parts.map(lambda a: Row(col1=a[0],col2=int(a[1])))
C_df = spark.createDataFrame(C)
C = parts.map(lambda a: Row(col1=a[0], col2=int(a[1].strip())))
schemaString = "MyTable"
D = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
E = StructType(D)
spark.createDataFrame(C, E).show()
df = spark.read.json("table.json)
df.show()
df2 = spark.read.load("tablee2.json", format="json")
df3 = spark.read.load("newFile.parquet")
df.dtypes
df.show()
df.head()
df.first(n)
df.schema
df.describe().show()
df.columns
df.count()
df.distinct().count()
df.printSchema()
df.explain()
df = df.withColumn('col1',df.table.col1).withColumn('col2',df.table.col2).withColumn('col3',df.table.col3).withColumn('col4',df.table.col4).withColumn(col5', explode(df.table.col5))
df = df.withColumnRenamed('col1', 'column1')
df = df.drop("col3", "col4")
df = df.drop(df.col3).drop(df.col4)
df.groupBy("col1").count().show()
f.filter(df["col2"]>4).show()
peopledf.sort(peopledf.age.desc()).collect()
df.sort("col1", ascending=False).collect()
df.orderBy(["col1","col3"],ascending=[0,1]).collect()
df.na.fill(20).show()
df.na.drop().show()
df.na.replace(10, 20).show()
df.repartition(10).rdd.getNumPartitions()
df.coalesce(1).rdd.getNumPartitions()
from pyspark.sql import functions as f
df.select("col1").show()
df.select("col2","col3").show()
df.select("col1", f.when(df.col2> 30, 1).otherwise(0)).show()
df[df.col1.isin("A","B")].collect()
peopledf.createGlobalTempView("column1")
df.createTempView("column1")
df.createOrReplaceTempView("column2")
df_one = spark.sql("SELECT * FROM customer").show()
df_new = spark.sql("SELECT * FROM global_temp.people").show()
rdd_1 = df.rdd
df.toJSON().first()
df.toPandas()
df.select("Col1", "Col2").write.save("newFile.parquet")
df.select("col3", "col5").writesave("table_new.json",format="json")
spark.stop()
