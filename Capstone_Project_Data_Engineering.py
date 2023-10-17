# Load Credit Card Database (SQL)
# Data Extraction and Transformation with Python and PySpark

# For “Credit Card System,” create a Python and PySpark SQL program to read/extract the following JSON files according to the specifications found in the mapping document

# 1. CDW_SAPP_BRANCH.JSON
# 2. CDW_SAPP_CREDITCARD.JSON
# 3. CDW_SAPP_CUSTOMER.JSON


import pyspark
import mysqlSecrets
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
  .option("user", mysqlSecrets.mysql_username) \
  .option("password", mysqlSecrets.mysql_password) \
  .save()

# creating a table called 'CDW_SAPP_CREDIT_CARD' into creditcard_capstone database from SparkSQL Dataframe by connecting mysql workbench
df_creditCard_new.write.format("jdbc") \
  .mode("append") \
  .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
  .option("dbtable", "creditcard_capstone.CDW_SAPP_CREDIT_CARD") \
  .option("user", mysqlSecrets.mysql_username) \
  .option("password", mysqlSecrets.mysql_password) \
  .save()

# creating a table called 'CDW_SAPP_BRANCH' into creditcard_capstone database from SparkSQL Dataframe by connecting mysql workbench
df_customer_new.write.format("jdbc") \
  .mode("append") \
  .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
  .option("dbtable", "creditcard_capstone.CDW_SAPP_CUSTOMER") \
  .option("user", mysqlSecrets.mysql_username) \
  .option("password", mysqlSecrets.mysql_password) \
  .save()

df_branch_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user = mysqlSecrets.mysql_username,\
 password = mysqlSecrets.mysql_password,\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_BRANCH").load()
df_branch_new.show(5)

df_creditCard_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user = mysqlSecrets.mysql_username,\
 password = mysqlSecrets.mysql_password,\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_CREDIT_CARD").load()
df_creditCard_new.show(5)

df_customer_new=spark.read.format("jdbc").options(driver="com.mysql.cj.jdbc.Driver",\
 user = mysqlSecrets.mysql_username,\
 password = mysqlSecrets.mysql_password,\
 url="jdbc:mysql://localhost:3306/creditcard_capstone",\
 dbtable="creditcard_capstone.CDW_SAPP_CUSTOMER").load()
df_customer_new.show(5)


'''2. Functional Requirements - Application Front-End
Once data is loaded into the database, we need a front-end (console) to see/display data. For that, 
create a console-based Python program to satisfy System Requirements 2 (2.1 and 2.2).'''

#2.1 Transaction Details Module
 
'''1)  Used to display the transactions made by customers living in a given zip code for a given month and year.
Order by day in descending order.'''

from pyspark.sql.functions import year, month, dayofweek
df_cus_tr = df_creditCard_new

df_cus_tr = df_cus_tr.withColumn('Day', col('TIMEID')[6:8])
df_cus_tr = df_cus_tr.withColumn('Month',month(col('TIMEID')))
df_cus_tr = df_cus_tr.withColumn('Year', col('TIMEID')[0:4])

df_creditCard_new.show(5)
df_cus_tr.show(5)

#create temporary view for both transaction and customer data
df_cus_tr.createOrReplaceTempView("cus_transaction")
df_customer_new.createOrReplaceTempView("customer_detail")



def transaction_inzip():
        #enter customer zip Code
    cust_zip_code = input("Enter zip code: ")

    #enter customer LAST_UPDATED month
    Cust_tra_month = input("Enter transaction month: ")

    #enter customer LAST_UPDATED year
    cust_tra_year = input("Enter year: ")
    spark.sql(f"select  cd.FIRST_NAME, cd.MIDDLE_NAME, cd.LAST_NAME, ct.CREDIT_CARD_NO, cd.CUST_ZIP, ct.BRANCH_CODE, ct.TRANSACTION_TYPE, ct.TRANSACTION_VALUE, ct.TRANSACTION_ID, ct.TIMEID  from customer_detail cd inner join cus_transaction ct on  cd.CREDIT_CARD_NO = ct.CREDIT_CARD_NO where cd.CUST_ZIP = {cust_zip_code} AND ct.Month = {Cust_tra_month} AND ct.Year = {cust_tra_year} order by ct.Day DESC").show()# correct 
transaction_inzip()


'''2)   Used to display the number and total values of transactions for a given type.'''

def transaction_type():

    transaction_type = input("enter customer transaction type: ")

    spark.sql(f"select count(TRANSACTION_ID), sum(TRANSACTION_VALUE) FROM cus_transaction WHERE TRANSACTION_TYPE='{transaction_type}'").show()
transaction_type()


'''3) Used to display the total number and total values of transactions for branches in a given state.'''

def transaction_byState():
#enter state of branches
    state = input("enter state of a branchs: ")
    df_creditCard_new.createOrReplaceTempView("cus_tran_card")
    df_branch_new.createOrReplaceTempView("cus_branch")
    spark.sql(f"select count(ct.TRANSACTION_ID), sum(ct.TRANSACTION_VALUE) from cus_tran_card ct inner join cus_branch b on ct.BRANCH_CODE = b.BRANCH_CODE where b.BRANCH_STATE = '{state}'").show()
transaction_byState()

'''
2.2 Customer Details Module

1) Used to check the existing account details of a customer.'''

#Get user first name, last name and email from the user input
#for the customer  security the user input should be first name, last name and customer email
def cust_detail():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    customer_info = spark.sql(f"select substring(SSN, 6, 8) as LAST_4_DIGIT_SSN, FIRST_NAME, MIDDLE_NAME, LAST_NAME, CREDIT_CARD_NO, FULL_STREET_ADDRESS, CUST_CITY, CUST_STATE, CUST_COUNTRY, CUST_ZIP, CUST_PHONE, CUST_EMAIL, LAST_UPDATED from customer_detail where '{first_name}' = FIRST_NAME AND '{last_name}' = LAST_NAME AND '{email}' = CUST_EMAIL")
    customer_info.show()
cust_detail()

#To test this use first name = "Elsa",  lastname-  "Truong" and email  -ETruong@example.com 

'''2) Used to modify the existing account details of a customer.'''

import mysqlSecrets
import mysql.connector as mydbconnection 
from mysql.connector import Error 

def connect():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    
    #To test this use first name = "Elsa",  lastname-  "Truong" and email  -3242
    #To test this use col_to_modify - FIRST_NAME = Delina 

    sql = f"UPDATE CDW_SAPP_CUSTOMER SET {col_to_modify} = '{updated_value}' WHERE FIRST_NAME = '{first_name}' AND LAST_NAME = '{last_name}' AND substring(SSN, 6, 8) = '{last_4_digit_SSN}'"
    try:
        mycursor.execute(sql)
    

    except:
        conn.rollback()
    sql = f"select * from CDW_SAPP_CUSTOMER where substring(SSN, 6, 8) = '{last_4_digit_SSN}'"

    mycursor.execute(sql)


    print(mycursor.fetchall())
    mycursor.close()
    conn.close()

if __name__ == '__main__':

    #Get user first name, last name and email from the user input
    #for the customer  security the user input should be first name, last name and customer email
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    last_4_digit_SSN = input("Enter last 4 digit number of your Social security number: ")
    col_to_modify = input("enter the section to be modified:")
    updated_value = input ("enter the new value that you want to update: ")
    connect()

'''3) Used to generate a monthly bill for a credit card number for a given month and year.'''

df_cus_tr.createOrReplaceTempView("cus_transaction")
#spark.sql("select * from cus_transaction").show()
df_customer_new.createOrReplaceTempView("customer_detail")
def monthly_bill():
    creditCardNumber = input("Enter your credit card number: ")
    month = input("Enter month for the bill you want: ")
    year = input("Enter year for the bill you want: ")
    #Enter creditCardNumber - 4210653348611322, month - 1, year - 2018

    spark.sql(f"select  FIRST_NAME, LAST_NAME, ct. CREDIT_CARD_NO, BRANCH_CODE, TRANSACTION_TYPE, TRANSACTION_VALUE, TRANSACTION_ID from customer_detail cd left join cus_transaction ct ON ct. CREDIT_CARD_NO = cd.CREDIT_CARD_NO  where ct.CREDIT_CARD_NO = '{creditCardNumber}'AND ct.Month = '{month}' AND ct.Year = '{year}'").show()
monthly_bill()

'''4) Used to display the transactions made by a customer between two dates. Order by year, month, and day in descending order'''

def transaction_twoDates():
    df_cus_tr.createOrReplaceTempView("cus_transaction")
    #spark.sql("select * from cus_transaction").show()
    df_customer_new.createOrReplaceTempView("customer_detail")

    #To test this use first name = "Lillie",  lastname-  "Barrett" and email -  LBarrett@example.com  first date = 201839  last date = 201899
    first_name = input("Enter your first name: ")
    last_name =  input("Enter your last_name: ")
    email = input("Enter your email: ")
    first_date = input("Enter the first date: ")
    second_date = input("Enter the second date: ")

    spark.sql(f"select  FIRST_NAME, LAST_NAME, cd.CUST_EMAIL, ct.CREDIT_CARD_NO, BRANCH_CODE, TRANSACTION_TYPE, TRANSACTION_VALUE, TRANSACTION_ID, ct.TIMEID from customer_detail cd left join cus_transaction ct ON ct. CREDIT_CARD_NO = cd.CREDIT_CARD_NO  where cd.FIRST_NAME = '{first_name}' AND cd.LAST_NAME = '{last_name}' AND cd.CUST_EMAIL = '{email}' AND TIMEID BETWEEN '{first_date}'AND '{second_date}' order by ct.TIMEID DESC").show()
transaction_twoDates()