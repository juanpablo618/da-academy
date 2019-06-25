from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

# Create the DataFrame
df = sqlContext.read.csv("2015-12-12.csv")

# Show the content of the DataFrame
df.show()
## age  name
## null Michael
## 30   Andy
## 19   Justin

# Print the schema in a tree format
df.printSchema()

# Select only the country column
df.select("_c8").show()


# show if the value of the row on country is equals to DE

df.select(df['_c8']=='DE').show()
+----------+
|(_c8 = DE)|
+----------+
|     false|
|     false|
|      true|
|     false|
|     false|
|      true|
|      true|
|      true|
|      true|
|      true|
|      true|
|      true|
|     false|
|     false|
|     false|
|     false|
|     false|
|     false|
|     false|
|     false|
+----------+
only showing top 20 rows

# Count people by country
df.groupBy("_c8").count().show()

+---+-----+                                                                     
|_c8|count|
+---+-----+
| LT|  321|
| DZ|   55|
| FI| 1344|
| AZ|   24|
| SC|   15|
| UA|  848|
| RO| 1081|
| ZM|   14|
| NL| 3857|
| BW|   21|
| PL| 3418|
| RE|    9|
| PS|   79|
| AM|   11|
| MK|   19|
| MX| 1472|
| PF|    1|
| GL|    1|
| EE|  102|
| CN|68372|
+---+-----+
only showing top 20 rows

" filters the lines that don’t have google, ask or yahoo as referers and writes the resulting Dataframe to disk in Parquet format." 


df.select("_c8").write.save("c8Juan.parquet", format="parquet")



definition:
Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.


val newDataDF = sqlContext.read.parquet("c8Juan.parquet")
  // show contents
  newDataDF.show()

dfJuanCuello = spark.read.parquet("c8Juan.parquet")



>>> dfJuanCuello.show()
+-------+
|    _c8|
+-------+
|country|
|     CZ|
|     DE|
|     CZ|
|     CZ|
|     DE|
|     DE|
|     DE|
|     DE|
|     DE|
|     DE|
|     DE|
|     ES|
|     US|
|     HK|
|     US|
|     US|
|     US|
|     CA|
|     GB|
+-------+
only showing top 20 rows



D. Create a PySpark script that reads the resulting Parquet files from exercise 2, loads them to a Dataframe and generates a Matplotlib pie chart that shows the percentage of occurrence of each status code.

import matplotlib.pyplot as plt


parquetJuan = spark.read.parquet("c8Juan.parquet")



sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=dfJuanCuello.show(), colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)



plt.axis('equal')
plt.show()









