from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Sales") \
    .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow") \
    .getOrCreate()

df = spark.read.csv("cleaned_sales.csv", header=True, inferSchema=True)

print("Full Data:")
df.show()

print("South Region:")
df.filter(df["region"] == "South").show()

print("Revenue by Category:")
df.groupBy("category").sum("revenue").show()

spark.stop()