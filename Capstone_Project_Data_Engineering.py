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