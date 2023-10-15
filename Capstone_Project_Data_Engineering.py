# Load Credit Card Database (SQL)
# Data Extraction and Transformation with Python and PySpark

# For “Credit Card System,” create a Python and PySpark SQL program to read/extract the following JSON files according to the specifications found in the mapping document

# 1. CDW_SAPP_BRANCH.JSON
# 2. CDW_SAPP_CREDITCARD.JSON
# 3. CDW_SAPP_CUSTOMER.JSON
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Capstone_demo').getOrCreate()

#Read json file which holds branch information into dataframe
df_branch = spark.read.json("cdw_sapp_branch.json")
df_branch.show(5)

#Read json file which holds credit card information into dataframe
df_creditCard = spark.read.load("cdw_sapp_credit.json", format="json", header = True,inferSchema = True)
df_creditCard.show(5)

#Read json file which holds customer information into dataframe
df_customer = spark.read.load("cdw_sapp_custmer.json", format="json", header = True,inferSchema = True)
df_customer.show(5)

#Extract the JSON files based on the mapping 

df_branch_new = df_branch.select("BRANCH_CODE", "BRANCH_NAME", "BRANCH_STREET", "BRANCH_CITY", "BRANCH_STATE", "BRANCH_ZIP", "BRANCH_PHONE", "LAST_UPDATED")
# display the schema in tree format
df_branch_new.printSchema()
#show the five rows
df_branch_new.show(5)


df_creditCard_new = df_creditCard.select("CREDIT_CARD_NO","DAY", "MONTH", "YEAR", "CUST_SSN", "BRANCH_CODE", "TRANSACTION_TYPE", "TRANSACTION_VALUE", "TRANSACTION_ID")
# display the schema in tree format
df_creditCard_new.printSchema()
#show the first five rows
df_creditCard_new.show(5)

df_customer_new=df_customer.select("SSN", "FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "CREDIT_CARD_NO", "STREET_NAME", "APT_NO", "CUST_CITY",
"CUST_STATE", "CUST_COUNTRY", "CUST_ZIP", "CUST_PHONE", "CUST_EMAIL", "LAST_UPDATED")
# display the schema in tree format
df_customer_new.printSchema()
#show the first five rows
df_customer_new.show(5)

# change the data type to the following based on the mapping
# [('BRANCH_CODE', 'int'),
#  ('BRANCH_NAME', 'varchar'),
#  ('BRANCH_STREET', 'varchar'),
#  ('BRANCH_CITY', 'varchar'),
#  ('BRANCH_STATE', 'varchar'),
#  ('BRANCH_ZIP', 'int'),
#  ('BRANCH_PHONE', 'varchar'),
#  ('LAST_UPDATED', 'TIMESTAMP')]

from pyspark.sql.types import IntegerType, StringType, TimestampType
df_branch_new = df_branch_new\
.withColumn('BRANCH_CODE', df_branch_new.BRANCH_CODE.cast(IntegerType()))\
.withColumn('BRANCH_NAME', df_branch_new.BRANCH_NAME.cast(StringType()))\
.withColumn('BRANCH_STREET', df_branch_new.BRANCH_STREET.cast(StringType()))\
.withColumn('BRANCH_CITY', df_branch_new.BRANCH_CITY.cast(StringType()))\
.withColumn('BRANCH_STATE', df_branch_new.BRANCH_STATE.cast(StringType()))\
.withColumn('BRANCH_ZIP', df_branch_new.BRANCH_ZIP.cast(IntegerType()))\
.withColumn('BRANCH_PHONE', df_branch_new.BRANCH_PHONE.cast(StringType()))\
.withColumn('LAST_UPDATED', df_branch_new.LAST_UPDATED.cast(TimestampType()))
print(type(df_branch_new))


#If the source value is null load default (99999) value else Direct move

df_branch_new.na.fill(value=99999,subset=["BRANCH_ZIP"]).show(5)

# Change the format of phone number to (XXX)XXX-XXXX

from pyspark.sql.functions import concat, lit, col

df_branch_new =df_branch_new.withColumn("BRANCH_PHONE", concat(lit("("),col("BRANCH_PHONE").substr(1, 3), lit(")"),\
                                                        col("BRANCH_PHONE").substr(4, 3), lit("-"), \
                                                        col("BRANCH_PHONE").substr(7, 4)))

df_branch_new.show(5)


''' change the data type of the credit data to the following 
[('CREDIT_CARD_NO', 'varchar'),
 ('DAY', 'varchar'),
 ('MONTH', 'varchar'),
 ('YEAR', 'varchar'),
 ('CUST_SSN', 'int'),
 ('BRANCH_CODE', 'int'),
 ('TRANSACTION_TYPE', 'varchar'),
 ('TRANSACTION_VALUE', 'double'),
 ('TRANSACTION_ID', 'int')] '''

from pyspark.sql.types import IntegerType, VarcharType, DoubleType
df_creditCard_new = df_creditCard_new\
.withColumn('CREDIT_CARD_NO', df_creditCard_new.CREDIT_CARD_NO.cast(VarcharType(30)))\
.withColumn('DAY', df_creditCard_new.DAY.cast(StringType()))\
.withColumn('MONTH', df_creditCard_new.MONTH.cast(StringType()))\
.withColumn('YEAR', df_creditCard_new.YEAR.cast(StringType()))\
.withColumn('CUST_SSN', df_creditCard_new.CUST_SSN.cast(IntegerType()))\
.withColumn('BRANCH_CODE', df_creditCard_new.BRANCH_CODE.cast(IntegerType()))\
.withColumn('TRANSACTION_TYPE', df_creditCard_new.TRANSACTION_TYPE.cast(StringType()))\
.withColumn('TRANSACTION_VALUE', df_creditCard_new.TRANSACTION_VALUE.cast(DoubleType()))\
.withColumn('TRANSACTION_ID', df_creditCard_new.TRANSACTION_ID.cast(IntegerType()))\

df_creditCard_new.dtypes 

''' Convert DAY, MONTH, and YEAR into a TIMEID (YYYYMMDD)'''

from pyspark.sql.functions import concat, lit, col

df_creditCard_new =df_creditCard_new.withColumn("TIMEID",concat(col("YEAR"),
                                                        col("MONTH"), 
                                                        col("DAY")))

df_creditCard_new.show(5)


df_creditCard_new = df_creditCard_new.select("CREDIT_CARD_NO","TIMEID", "CUST_SSN", "BRANCH_CODE", "TRANSACTION_TYPE", "TRANSACTION_VALUE", "TRANSACTION_ID")
df_creditCard_new.show(5)


'''Convert the first Name to Title Case
Convert the middle name in lower case
Convert the Last Name in Title Case
Concatenate Apartment no and Street name of customer's Residence with comma as a seperator (Street, Apartment)

Change the format of phone number to (XXX)XXX-XXXX '''

from pyspark.sql.functions import initcap, lower, concat_ws
df_customer_new = df_customer_new\
    .withColumn("FIRST_NAME", initcap(df_customer_new["FIRST_NAME"]))\
    .withColumn("MIDDLE_NAME", lower(df_customer_new["MIDDLE_NAME"]))\
    .withColumn("LAST_NAME", initcap(df_customer_new["LAST_NAME"]))\
    .withColumn("FULL_STREET_ADDRESS", concat(df_customer_new["STREET_NAME"],lit(", "), df_customer_new["APT_NO"]))\
    

df_customer_new =df_customer_new.withColumn("CUST_PHONE", concat(lit("("),col("CUST_PHONE").substr(1, 3), lit(")"),\
                                                        col("CUST_PHONE").substr(4, 3), lit("-"), \
                                                        col("CUST_PHONE").substr(7, 4)))

df_customer_new.show(5)

df_customer_new = df_customer_new.withColumn("FULL_STREET_ADDRESS", df_customer_new.FULL_STREET_ADDRESS.cast(VarcharType(50)))
df_customer_new = df_customer_new.select("SSN", "FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "CREDIT_CARD_NO", "FULL_STREET_ADDRESS", "CUST_CITY",
"CUST_STATE", "CUST_COUNTRY", "CUST_ZIP", "CUST_PHONE", "CUST_EMAIL", "LAST_UPDATED")
df_customer_new.show(5)

df_customer_new.dtypes

'''Req-1.2  Data loading into Database
 Once PySpark reads data from JSON files, and then utilizes Python, PySpark, and Python modules to load data into RDBMS(SQL), perform the following:

Create a Database in SQL(MySQL), named “creditcard_capstone.”
Create a Python and Pyspark Program to load/write the “Credit Card System Data” into RDBMS(creditcard_capstone).
Tables should be created by the following names in RDBMS:
CDW_SAPP_BRANCH
CDW_SAPP_CREDIT_CARD
CDW_SAPP_CUSTOMER +- 
Create a Database in SQL(MySQL), named “creditcard_capstone.”'''

'''A Database is created on MySQL workbench 
syntax for creating database “creditcard_capstone." 

CREATE DATABASE `creditcard_capstone` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;'''

# creating a table called 'CDW_SAPP_BRANCH' into creditcard_capstone database from SparkSQL Dataframe
# by connecting mysql workbench

df_branch_new.write.format("jdbc") \
  .mode("append") \
  .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
  .option("dbtable", "creditcard_capstone.CDW_SAPP_BRANCH") \
  .option("user", "root") \
  .option("password", "password") \
  .save()

# creating a table called 'CDW_SAPP_CREDIT_CARD' into creditcard_capstone database from SparkSQL Dataframe by connecting mysql workbench
df_creditCard_new.write.format("jdbc") \
  .mode("append") \
  .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
  .option("dbtable", "creditcard_capstone.CDW_SAPP_CREDIT_CARD") \
  .option("user", "root") \
  .option("password", "password") \
  .save()

# creating a table called 'CDW_SAPP_BRANCH' into creditcard_capstone database from SparkSQL Dataframe by connecting mysql workbench
df_customer_new.write.format("jdbc") \
  .mode("append") \
  .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
  .option("dbtable", "creditcard_capstone.CDW_SAPP_CUSTOMER") \
  .option("user", "root") \
  .option("password", "password") \
  .save()

df_branch_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user="root",\
 password="password",\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_BRANCH").load()
df_branch_new.show(5)

df_creditCard_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user="root",\
 password="password",\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_CREDIT_CARD").load()
df_creditCard_new.show(5)

df_customer_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user="root",\
 password="password",\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_CUSTOMER").load()
df_customer_new.show(5)
