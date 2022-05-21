Spark

schema = StructType(List(StructField(customer_id, IntegerType),StructField(plan_id, IntegerType),StructField(start_date), DateType))

schema2 = StructType(List(StructField(plan_id, IntegerType),StructField(plan_name, StringType),StructField(price, FloatType)))

DF1 = spark.read.format("csv").option("header", true).schema(schema).option("path", "path to subscription file").load

DF1.createOrReplaceTempTable("subscriptions")
DF2 = spark.sql("select plan_id, date_format(start_date, "MMMM") as month, count(*) as count from subscriptions group by plan_id, month having plan_id = 0").select("month","count")

DF3 = spark.sql("select plan_id, date_format(start_date, "YYYY") as year, count(*) as count from subscriptions group by plan_id, year having year > 2020")

DF3.createOrReplaceTempTable("subs1")

DF4 = spark.read.format("csv").option("header", true).schema(schema2).option("path", "path to plans file").load

DF4.createOrReplaceTempTable("plans")

DF5 = spark.sql("select plan_name, count from subs1 a join plans p on s.plan_id = p.plan_id")

DF2.write.mode(SaveMode.Append).option("path", "path to save").save

DF5.write.mode(SaveMode.Append).option("path", "path to save").save

DF1 = spark.sql("select distinct(count(customer_id)) from subscriptions").toInt
DF2 = spark.sql("select count(*) from subscriptions where plan_id = 4").toInt

DF1.createOrReplaceTempTable("T1")
DF2.createOrReplaceTempTable(("T2")

spark.sql("select totalCount, round(churnCount/totalCount * 100) from subscriptions, subscriptions1")
