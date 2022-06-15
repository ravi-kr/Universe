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
