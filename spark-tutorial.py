#Spark Basic Architecture and Terminology

# Spark Session vs Spark Context vs SQL Context vs Hive Context

#Spark 1.x Entry points - Spark Context vs SQL Context vs Hive Context

#Spark Context

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('app').setMaster('local[*]')
sc = SparkContext(conf = conf)

#SQL Context

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

conf = SparkConf().setAppName('app').setMaster('local[*]')
sc = SparkContext(conf = conf)
sql_context = SQLContext(sc)

#Hive Context

from pyspark import SparkContext, SparkConf, HiveContext

conf = SparkConf().setAppName('app').setMaster('local[*]')
sc = SparkContext(conf = conf)
hive_context = HiveContext(sc)
hive_context.sql("select * from tableName limit 0")

#Spark 2.x Entry points - Spark Session

from pyspark.sql import SparkSession
spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()

spark_context = spark_session._sc
spark_context = spark_session.sparkContext

#Parameters of Spark Context

Master
appName
sparkHome
pyFiles
Environment
batchsize
Serializer
conf
Gateway
JSC
profile_cls

#RDD

In-memory computation
Lazy evaluation
Fault tolerant
Immutable
Partitioning
Persistence
Coarse gained operation

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("Pyspark Tutorials").getOrCreate()

data = [2,4,6,8,10]
rdd = spark.sparkContext.parallelize(data)

rdd2 = spark.sparkContext.textFile("/path/textFile.txt")

rdd3 = spark.sparkContext.wholeTextFiles("/path/textFile.txt")

emptyRdd = spark.sparkContext.emptyRDD

print("Initial partition count: " + str(rdd.getNumPartitions()))

reparRdd = rdd.repartition(4)
print("Re-partition count: " + str(reparRdd.getNumPartitions()))

reparCoRdd = rdd.coalesce(4)
print("Re-partition count: " + str(reparCoRdd.getNumPartitions()))

df = spark.read.csv('iris.csv')
df.printSchema()

df = spark.read.option('header', True).csv('iris.csv')
df.printSchema()

df = spark.read.csv('path1,path2,path3')

df = spark.read.csv('folder path')

df = spark.read.option(header = 'True', inferSchema = 'True', delimiter = ',').csv('iris.csv')
print(df.show())
df.printSchema()

File formats

1. Text files - human readable
2. Sequence files - not human readable
3. JSON - key value pairs
4. AVRO - row based lightweight and fast serialization and deserialization
5. Parquet - column oriented and gives better compression ratio

from pyspark import SparkContext

sc = SparkContext("local", "Accumulator App")

num = sc.accumulator(10)

def f(x):
    global num
    num += x

rdd = sc.parallelize([20,30,40,50])

rdd.foreach(f)
final = num.value
print("Accumulated value is -> %i" % final)

from pyspark import SparkConf, SparkContext

sc = SparkContext("local", "Accumulator app")

counter = sc.accumulator(0)

print("Initial Value of Accumulator - Counter Variable: ", counter)

def error_logs(line):
    if "error" in line:
        counter.add(1)
        
log = sc.textFile("Sample.txt")
log.foreach(lambda x: error_logs(x))
print("Final value of Accumulator - Counter Variable: ", counter)

from pyspark import SparkContext

sc = SparkContext("local", "Broadcast app")
teams = {"MI":"Mumbai Indians",
"CSK": "Chennai Super Kings",
"KKR": "Kolkata Knight Riders"}
broadcastTeams = sc.broadcast(teams)

data = [("Rohit Sharma", "MI", "34"), ("Ravindra Jadeja", "CSK", "33"), ("Shreyas Iyer", "KKR", "27")]

rdd = sc.parallelize(data)

def team_convert(code):
    return broadcastTeams.value[code]
    
result = rdd.map(lambda x: (x[0], team_convert(x[1]), x[2])).collect()

print(result)

Spark Transformations and Actions

1. Lazy Evaluation

Actions
Transformations

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark Transformation - Map').getOrCreate()

rdd = spark.sparkContext.textFile(r'sample.txt')
number_of_words = rdd.map(lambda line: len(line.split()))

final_list = number_of_words.collect()

for line in final_list:
    print(line)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark Transformation - FlatMap').getOrCreate()

data = ["Apache Spark", "Data Science", "Machine Learning", "Artificial Intelligence"]

rdd = spark.sparkContext.parallelize(data)

print("Data before transformation:")

for element in rdd.collect():
    print(element)

print("\n\n Data after transformation with FlatMap")

rdd2 = rdd.flatMap(lambda x: x.split(" "))

for element in rdd2.collect():
    print(element)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark Transformation - Filter').getOrCreate()
data = [["Rohit Sharma", "MI", "34"],["Ravindra Jadeja", "CSK", "33"], ["Shreyas Iyer", "KKR", "27"], ["MS Dhoni", "CSK", "40"]]

columns = ['Player Name', 'Team', 'Age']

ipl_df = spark.createDataFrame(data, columns)

ipl_df.show()

ipl_df.filter(ipl_df["Team"] == "CSK").show()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark Actions Examples').getOrCreate()

df = spark.read.csv("airports.csv", inferSchema = True, header = True)
df.printSchema()

df.first()

df.take(10)

df.count()

df_ca = df.filter(df['state'] = 'CA')
df_ca.count()

for element in df_ca.collect():
    print(element)
    
df_ca.toPandas().to_csv('output.csv', index = False)

df.rdd.getNumPartitions()

c = df.rdd.repartition(5)

c.take(20)

c.getNumPartitions()

d = df.repartition(3, "state")
d.show()

e = df.repartition(3, 'state', 'city')
e.show()

e.getNumPartitions()

rdd = spark.sparkContext.parallelize((0,1,2,3,4,5,6,7))
rdd.collect()

rdd.getNumPartitions()

rdd1 = rdd.coalesce(4)

rdd1.getNumPartitions()

load().map().filter().coalesce(1).save() -> load().coalesce(1).map().filter().save()
load().map().filter().repartition(1).save()

