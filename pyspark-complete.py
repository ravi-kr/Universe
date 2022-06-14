from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
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
