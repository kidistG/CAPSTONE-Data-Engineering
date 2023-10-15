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