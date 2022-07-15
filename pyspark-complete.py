from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import sqrt
from pyspark.sql.types import IntegerType
#sparkdriver = SparkSession.builder.master('local').appName('demoApp').getOrCreate()
sparkdriver = SparkSession.builder.master('local').appName('demoApp').config('spark.jars.packages', 'mysql:mysql-connector-java:5.1.44').getOrCreate()
sparkdriver

sch = StructType([StructField('id', StringType()), StructField('starttime', StringType()), StructField('endtime', StringType()), StructField('status', StringType()), StructField('fromno', LongType()), StructField('tono', LongType())])

df_hdfs = sparkdriver.read.format('csv').option('delimeter', '\t').schema(sch).load('hdfs://172.16.38.131:8020/dfdata1/part-0000-333f.csv')
df_hdfs.show(5)

print(df_hdfs.rdd.getNumPartitions())

print(sparkdriver.sparkContext.defaultParallelism)

df_hdfs.printSchema()

df_hdfs.where('status = "SUCCESS"').show(5)

#df_hdfs.withColumn('fromno', col('fromno').cast('long')).select('fromno', col('fromno')/10).show(5)

df_hdfs.select('fromno', col('fromno')/10).show(5)

df_hdfs.withColumn('fromno', col('fromno').cast('long')).withColumn('fromnonew', col('fromno')/10).show(5)

df_hdfs.select('status').distinct().show()

df_hdfs.withColumn('severity', when(col('status') == "DROPPED", 'critical').when(col('status')=="FAILED", 'medium').otherwise('ok')).show(5)

df_hdfs.registerTempTable('temptable1')
df_hdfs.write.saveAsTable('db1.permtable')

sparkdriver.sql('select status, count(*) from temptable1 group by status').show()
sparkdriver.sql('create database db1')
sparkdriver.sql('show databases').show()
sparkdriver.sql('show tables in default').show()

df_mysql = sparkdriver.read.format('jdbc').option('url', 'jdbc:mysql://localhost:3306').option('driver', 'com.mysql.jdbc.Driver').option('user', 'root').option('password', 'pass').option('query', 'select status, count(*) from dbsample.samplecalldata group by status').load()

df_mysql.show(5)

#jsonlint.com
df_json = sparkdriver.read.format('json').option('multiline': True).load('D:\\Users\\j1.txt')
df_json.printSchema()

import requests
import json

jsonapidata = requests.request('GET','https://api.github.com/users/hadley/orgs')
print(type(jsonapidata.json()))
print(len(jsonapidata.json()))
file = open('D:\\Users\\restapi', 'a')
jsondata = jsonapidata.json()
for record in jsondata:
    file.write("%s \n" %record)
    
df_json = sparkdriver.read.format('json').load('D:\\Users\\restapi')
df_json.show(10)
df_json.printSchema()

Lecture - 9

f1 = sparkdriver.sql('show functions')
print(type(f1))
print(f1.count())
f1.collect()
f1.show(296)
sparkdriver.sql('describe function aggregate').collect()

df_mysql.show(5)
df1 = df_mysql.withColumn("day", current_date())
df1 = df_mysql.withColumn("day", date_add(current_date(),1))
df1.write.partitionBy('day').mode('append').saveAsTable('calldatatable')
df.show()
print('success')

spark.sql('show databases').count()
spark.sql('select * from default.accountdevice limit 10').show()

df_hive1 = spark.read.table('default.accountdevice')
df_hive1
df_hive1.printSchema()

df_hive1.show(5)

df_hive2 = spark.sql('select * from default.accountdevice')
df_hive2

df_hive2 = spark.sql('select * from default.accountdevice where device_id = 29')
df_hive2.count()
df_hive1.count()

#domain specific language
df_hive1 = spark.read.table('default.accountdevice').filter('device_id = 29')

df_hive1.show(5)

df3 = df_hive.withColumn('newc', current_timestamp())

df3.show(5)

df3.write.format('csv').saveAsTable('default.testsparkdf2')

df4 = spark.read.format('csv').load('hdfs://172.16.38.131:8020//user/part-0000-333f.csv')

df4.show

from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('sparkapp').getOrCreate()
spark

r1 = spark.sparkContext.textFile('C:\\Users\\sample.txt')
print(r1.collect())
print(r1.count())

r2 = r1.map(lambda x:(str)(x)).map(lambda x:x.split(' '))
print(r2.collect())

r3 = r2.map(lambda x:len(x))
columnsize = r3.collect()
print(columnsize)

def fillmissing(x):
    result = []
    for i in range(columnsize):
        try:
            result.append(x[i])
        except:
            result.append('nodata')
    return result
    
print(fillmissing(['spark','spark']))

resultdata = r2.map(lambda x: fillmissing(x))
print(resultdata.collect(x))
df1 = resultdata.toDF()
df1.show()

df2 = spark.read.format('csv').option('inferSchema', True).option('header', True).load('C:\\Users\\sample.txt')

df2.show(5)

df2.select('Age', sqrt('Age')).show(5)

df3 = df2.na.drop()
df3.show()
def f2(x):
    return (x*x - x)/2
    
f2(20)

spark.udf.register('myfunc', f2, IntegerType())
myfunc = udf(f2,IntegerType())  
df3.select('Age', myfunc('Age')).show(5)

f2.printSchema()


spark-submit

Driver Memory
Executor Memory
Driver Core
Executor Core

from pyspark.sql import SparkSession
sparkdriver = SparkSession.builder.master('yarn').appName('demoApp').getOrCreate()

spark-submit --help

from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').appName('demoApp').getOrCreate()
spark

rd1 = spark.sparkContext.textFile(C:\\Users\\sample.txt)
print(rd1.collect())
rd1.count()

rd2 = rd1.map(lambda x:x.encode('utf-8'))
print(rd2.collect())

rd3 = rd2.flatMap(lambda x: x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
rd3.collect()

CACHS >>> RAM >> DISK

spark.conf.set('spark.sql.repl.eagerEval.enabled', True) 

- Connecting with Spark (Our own Spark Session)

#test.py
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("myApp").getOrCreate()
print("Hello World!")

spark-submit test.py

- Reading in Data

titanic = spark.read.format("csv").\
                     option("separator", ",").\
                     option("header", True).\
                     option("inferSchema", True).\
                     load("file:///home/spark/titanic.csv")
                     
titanic.show()
titanic.printSchema()

people = spark.read.format("json").\
                     option("multiline", True).\
                     load("file:///home/spark/example.json")
                     
people.show()
people.printSchema()

data = spark.read.parquet("file:///home/spark/userdata/userdata1.parquet")

data.show()

data_folder = spark.read.parquet("file:///home/spark/userdata/")

data_folder.show()

data.count()
data_folder.count()

sql_df = spark.read.format("jdbc").\
                    option("url", "jdbc:postgresql://localhost:5432/tutorial").\
                    option("dbtable", "dummy").\
                    option("user", "postgres").\
                    opion("password", "Test").\
                    option("driver", "org.postgresql.Driver").\
                    load()
                    
sql_df.show()
sql_df.printSchema()

- Select, Filter, and Sort

titanic.select("Name", "Survived").show()
titanic.select(["Name", "Survived"]).show()

titanic = titanic.drop("Siblings/Spouses Aboard", "Parents/Children Aboard")

import pyspark.sql.functions as f
titanic.filter(f.col("Sex") == "female").show()
titanic.filter((f.col("Sex") == "female") & (f.col("Pclass") == 1)).show()
titanic.filter(((f.col("Sex") == "female") & (f.col("Pclass") == 1)) | ((f.col("Sex") == "male") & (f.col("Pclass") == 3))).show()
titanic.sort("Age").show()
titanic.sort("Age", ascending = False).show()
titanic_sorted = titanic.sort("Pclass", f.desc("Age"))
titanic_sorted.show()

- Aggregation 

titanic.groupBy("Pclass").agg({"Fare":"mean"}).show()
titanic.groupBy("Pclass").agg(f.mean("Fare"), f.max("Fare")).show()
fare_aggr = titanic.groupBy("Pclass", "Sex").agg(f.mean("Fare"), f.max("Fare"), f.mean("Age"), f.max("Age"), f.min("Age"))
fare_aggr.show()
fare_aggr.sort("Pclass", "Sex")
fare_aggr.sort("Pclass", "Sex").show()
fare_aggr = fare_aggr.withColumnRenamed("max(Fare)", "Fare_max")
fare_aggr.show()
titanic.count()
titanic.groupBy("Pclass", "Sex").count().show()
titanic.groupBy("Pclass", "Sex").count().sort("Pclass", "Sex").show()
titanic.select("Pclass").distinct().show()


- Functions

import pyspark.sql.functions as f
titanic.filter(f.col("Sex") == "female").show()
titanic = titanic.withColumn("FirstClass", f.col("Pclass") == 1)
titanic.show()
titanic.withColumn("Ship", f.lit("Titanic")).select("Name", "Ship").show()
titanic.withColumn("One", f.lit("1")).select("Name", "One").show()
titanic = titanic.withColumn("Fare_log", f.log(f.col("Fare")))
titanic.select("Fare", "Fare_log").show()
titanic = titanic.withColumn("Age_Class", f.when(f.col("Age") < 18, f.lit("Minor")).otherwise(f.lit("Adult")))
titanic.select("Age", "Age_Class").show()
titanic = titanic.withColumn("Title", f.regexp_extract(f.col("Name"), r"^\S+", 0))
titanic.select("Name", "Title").show()
titanic = titanic.withColumn("CommonTitle", f.col("Title").isin(["Mr.", "Mrs.", "Miss."]))
titanic.select("Title", "CommonTitle").show()
titanic.withColumn("Name_Lower", f.lower(f.col("Name"))).select("Name", "Name_Lower").show()


- Join, Union, and Pivot 

employees = spark.read.format("csv").\
                       options(separator = ",", header = True, inferSchema = True).\
                       load("file:///home/spark/office/employees.csv")
employees.show()

salaries = spark.read.format("csv").\
                      options(separator = ",", header = True, inferSchema = True).\
                      load("file:///home/spark/office/salaries.csv")
salaries.show()

jobs = spark.read.format("csv").\
                  options(separator = ",", header = True, inferSchema = True).\
                  .load("file:///home/spark/office/jobs.csv")
jobs.show()
                  
employees = employees.join(jobs, "job", "left")
employees.show()

salaries = salaries.join(employees.select("employees", "department"), "employee", "left")
salaries.show()

salaries_department = salaries.groupBy("date", "department").\
agg({"salary":"sum"})
salaries_department.show()
salaries_department.sort("department", "date").show()

salary_recent = salaries.groupBy("employee").agg({"date":"max"})
salary_recent.show()

salary_recent = salaries.join(salary_recent, "employee", "left").\
filter(f.col("date") == f.col("max(date)"))
salary_recent.show()

employees = employees.join(salary_recent.select("employee", "salary"), "employee", "left")
employees.show()

7 - User Defined Functions, Pandas, and Collect 

a = [("A", 100), ("B", 200)]
b = [("C", 300), ("D", 400)]
a = spark.createDataFrame(a, schema = ["string", "number"])
b = spark.createDataFrame(b, schema = ["string", "number"])
a.show()
b.show()
c = a.union(b)
c.show()

salaries.show()

salaries_pivot = salaries.groupBy("employee").\
                          pivot("date").\
                          sum("salary").\
                          fillna(0)
salaries_pivot.show()

import pyspark.sql.types as t
def to_upper(s: str):
    return s.upper()
    
import pyspark.sql.functions as f
udf_to_upper = f.udf(to_upper, t.StringType())
titanic.withColumn("name_upper", udf_to_upper(f.col("name"))).select("name", "name_upper").show()

titanic_pd = titanic.toPandas()
titanic_spark = spark.createDataFrame(titanic_pd)
titanic_spark.show()

titanic_collect = titanic.select("name", "fare").collect()
for x in titanic_collect:
    print("Name: " + x[0])
    print("Fare: " + str(x[1]))
titanic = spark.read.format("csv").\
                     options(separator = ",", header = True, inferSchema = True).\
                     load("file:///home/spark/titanic.csv")
import pyspark.sql.functions as f
titanic = titanic.withColumn("name_upper", f.upper(f.col("name"))).\
withColumn("fare_log", f.log(f.col("fare")))
titanic.select("name_upper", "fare_log").show()


- Writing Data 

titanic.write.format("csv").\
options(separator = ",").\
save("file:///home/spark/titanic_new.csv")

titanic.repartition.\
write.\
format("csv").\
options(separator = ",").\
save("file:///home/spark/titanic_new.csv")

titanic.select("name", "fare").\
write.\
parquet("file:///home/spark/titanic_new.parquet")

titanic.write.format("jdbc").\
              option("url", "jdbc:postgresql://localhost:5432/tutorial").\
              option("dbtable", "titanic").\
              option("user", "postgres").\
              option("password", "test").\
              option("driver", "org.postgresql.Driver").\
              save()

create table table1(pid INT, pname STRING, drug STRING, tot_amt INT) row format delimited fields terminated by ',' stored as textfile;

load data local inpath '/home ubuntu/data_301.txt' into table table1;
load data local inpath '/home ubuntu/data_301.txt' into table table1;

show create table table1;

create table table2(pid INT, pname STRING, drug STRING, tot_amt INT) row format delimited fields terminated by ',' stored as orc;

insert overwrite table table2 select * from table1;

show create table table2;

select count(*) from table1 where tot_amt = 110;
select count(*) from table2 where tot_amt = 110;
