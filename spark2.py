val spark = SparkSession.builder.appName("Spark Program").master("local[*]").getOrCreate()

mySchema = "campaign_id bigint, campaign_name string, campaign_date string, campaign_team string, campaign_country string"


val df1 = spark.read().format("csv").path("s3 path").option("header", true).schema(mySchema)

val df2 = df1.withColumn("UnixTimeStamp", unix_timestamp("campaign_date"))

val df3 = df2.dropDuplicate(col("campaign_id"))

df3.createOrReplaceTempTable("campaign")

val df4 = spark.sql("select count(campaign_name) from campaign where month(campaign_date) = 4")

val df5 = spark.sql("select * from campaign")

df5.write().format("parquet").partitionBy("campaign_country").append().path("s3 path")
