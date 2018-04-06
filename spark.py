import pyspark as spark
from pyspark.sql import SparkSession
#build the session 
spark = SparkSession \ 
      .builder \ 
      .appName('Python Spark sQL basic example') \
      .config('spark.some.config.option', 'some-value') \
      .getOrCreate()
      
df = spark.read.csv('creditcard.csv')
df.printSchema()
df.head()
df.count()
df.describe().show()
# dealing with missing value
df.dropna().count()
df.fillna(-1).show(5)


sc = spark.saprkContext

rdd = sc.textFile('housing.data')
from pyspark.sql import Row 
df = rdd.map(lambda line: Row( longitude= line[0],
                              lattitude = line[1],
                              housingMedianAge = line[3],
                              totalBedRooms = line[4],
                          
                              )


