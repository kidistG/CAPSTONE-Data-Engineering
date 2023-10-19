# Load Credit Card Database (SQL)
# Data Extraction and Transformation with Python and PySpark

# For “Credit Card System,” create a Python and PySpark SQL program to read/extract the following JSON files according to the specifications found in the mapping document

# 1. CDW_SAPP_BRANCH.JSON
# 2. CDW_SAPP_CREDITCARD.JSON
# 3. CDW_SAPP_CUSTOMER.JSON

# import all required libraries and packages


from pyspark.sql.types import IntegerType, StringType, TimestampType, DoubleType, StructType, StructField
from pyspark.sql.functions import concat, lit, col, initcap, lower, month, length, lpad
import mysql.connector as mydbconnection 
import requests
import random
import pandas as pd
from matplotlib import pyplot as plt
from pyspark.sql import SparkSession, Row
import mysqlSecrets


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


# If the source value is null load default (99999) value else Direct move

df_branch_new.na.fill(value=99999,subset=["BRANCH_ZIP"]).show(5)

# Change the format of phone number to (XXX)XXX-XXXX
df_branch_new.select("BRANCH_ZIP").where(length(col("BRANCH_ZIP")) < 5).show(5)

df_branch_new =df_branch_new.withColumn("BRANCH_PHONE", concat(lit("("),col("BRANCH_PHONE").substr(1, 3), lit(")"),\
                                                        col("BRANCH_PHONE").substr(4, 3), lit("-"), \
                                                        col("BRANCH_PHONE").substr(7, 4)))

df_branch_new = df_branch_new.withColumn('BRANCH_ZIP', lpad(df_branch_new.BRANCH_ZIP,5, '0'))



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


df_creditCard_new = df_creditCard_new\
.withColumn('CREDIT_CARD_NO', df_creditCard_new.CREDIT_CARD_NO.cast(StringType()))\
.withColumn('DAY', df_creditCard_new.DAY.cast(StringType()))\
.withColumn('MONTH', df_creditCard_new.MONTH.cast(StringType()))\
.withColumn('YEAR', df_creditCard_new.YEAR.cast(StringType()))\
.withColumn('CUST_SSN', df_creditCard_new.CUST_SSN.cast(IntegerType()))\
.withColumn('BRANCH_CODE', df_creditCard_new.BRANCH_CODE.cast(IntegerType()))\
.withColumn('TRANSACTION_TYPE', df_creditCard_new.TRANSACTION_TYPE.cast(StringType()))\
.withColumn('TRANSACTION_VALUE', df_creditCard_new.TRANSACTION_VALUE.cast(DoubleType()))\
.withColumn('TRANSACTION_ID', df_creditCard_new.TRANSACTION_ID.cast(IntegerType()))\

df_creditCard_new.dtypes 

# Convert DAY, MONTH, and YEAR into a TIMEID (YYYYMMDD)


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
# The CUST_PHONE has 7 digit the so add the posible area code for the united state phone


df_customer_new.show(5)
area_code_list = []
invalid_numbers = [211, 311, 411, 511, 611, 711, 811, 911]

for i in range(201, 990):
    area_code_list.append(i)

for j in (invalid_numbers):
    area_code_list.remove(j)
df_customer_new = df_customer_new\
    .withColumn("FIRST_NAME", initcap(df_customer_new["FIRST_NAME"]))\
    .withColumn("MIDDLE_NAME", lower(df_customer_new["MIDDLE_NAME"]))\
    .withColumn("LAST_NAME", initcap(df_customer_new["LAST_NAME"]))\
    .withColumn("FULL_STREET_ADDRESS", concat(df_customer_new["STREET_NAME"],lit(", "), df_customer_new["APT_NO"]))\
    .withColumn("CUST_PHONE", concat(lit("("), lit(random.choice(area_code_list)), lit(")"), col("CUST_PHONE").substr(1, 3), lit("-"),\
                                                        col("CUST_PHONE").substr(4, 4)))
    

df_customer_new.show(5)

df_customer_new = df_customer_new.withColumn("FULL_STREET_ADDRESS", df_customer_new.FULL_STREET_ADDRESS.cast(StringType()))

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

def modify_customerInfo():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    
    #To test this use first name = "Elsa",  lastname-  "Truong" and last 4 digit ssn  -3242
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
    modify_customerInfo() # call the function here

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

'''Data Analysis and Visualization'''

''' Functional Requirements 3.1

Find and plot which transaction type has the highest transaction count.
Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED! '''

def highest_TRANSACTION_TYPE():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    sql = f"select TRANSACTION_TYPE, count(*) as NUM_TRANSACTION\
    from cdw_sapp_credit_card \
    group by TRANSACTION_TYPE ORDER BY NUM_TRANSACTION DESC"

    
    try:
        mycursor.execute(sql)
         

    except:
        conn.rollback()
        
    highest = mycursor.fetchall()
     # create DataFrame using data
    df = pd.DataFrame(highest, columns =['TRANSACTION_TYPE', 'NUM_TRANSACTION'])
    
    fig = plt.figure(figsize =(8, 4))
    print( "The Highest Transaction count Type is the ", df["TRANSACTION_TYPE"][0], "with total count of ", df["NUM_TRANSACTION"][0], "\n")
    
    plt.bar(df["TRANSACTION_TYPE"], df["NUM_TRANSACTION"])
    plt.xlabel("Transaction type")
    plt.ylabel("Number of Transaction")
    plt.title("Number of Transaction Based on Transaction Type")
    print(df)
    mycursor.close()
    conn.close()
highest_TRANSACTION_TYPE()


'''Functional Requirements 3.2	

Find and plot which state has a high number of customers.

Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!'''

def customer_by_state():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    sql = f"select CUST_STATE, COUNT(SSN) AS NUM_CUSTOMER \
    FROM cdw_sapp_customer \
    group by CUST_STATE\
    ORDER BY NUM_CUSTOMER DESC"
    
    try:
        mycursor.execute(sql)  

    except:
        conn.rollback()
    
    highest = mycursor.fetchall()
      # create DataFrame using data
    df = pd.DataFrame(highest, columns =['CUST_STATE', 'NUM_CUSTOMER'])
    
    fig = plt.figure(figsize =(10, 6))
    print( "The Highest number of customer state is ", df["CUST_STATE"][0], "with total customer of ", df["NUM_CUSTOMER"][0])
    
    plt.bar(df["CUST_STATE"], df["NUM_CUSTOMER"])
    plt.xlabel("state")
    plt.ylabel("Number of Customer")
    plt.title("Number of Customer by State")
    mycursor.close()
    conn.close()
customer_by_state()


'''Functional Requirements 3.3

Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.
Hint (use CUST_SSN). 

Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!'''
def top_ten_customers():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    sql = f"select CUST_SSN, SUM(TRANSACTION_VALUE) AS TOTAL_TRANSACTION \
    from cdw_sapp_credit_card \
    group by CUST_SSN \
    order by TOTAL_TRANSACTION DESC"
    try:
        mycursor.execute(sql)
    except:
        conn.rollback()

    highest = mycursor.fetchall()
      # create DataFrame using data
    df = pd.DataFrame(highest, columns =['CUST_SSN', 'TOTAL_TRANSACTION']).head(10)
    print("sum of all transactions for the top 10 customers")
    print(df)
        #fig = plt.figure(figsize =(10, 6))

    df.plot.bar(x = 'CUST_SSN', y = 'TOTAL_TRANSACTION', title ="Top 10 customers total transaction amount ", figsize =(8, 5))
    
    mycursor.close()
    conn.close()
top_ten_customers()


'''4. Functional Requirements - LOAN Application Dataset
Req-4	 Access to Loan API Endpoint'''

'''4.1 Create a Python program to GET (consume) data from the above API endpoint for the loan application dataset.'''

url = "https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json"

response = requests.get(url)
#convert json object to python dictionary object
loan_app_data = response.json()
print(loan_app_data)
print(type(loan_app_data))


'''4.2  Find the status code of the above API endpoint.

Hint: status code could be 200, 400, 404, 401.'''

print("The status code of the of this API is:", response.status_code)

'''4.3 Once Python reads data from the API, utilize PySpark to load data into RDBMS (SQL). The table name should be CDW-SAPP_loan_application in the database.

Note: Use the “creditcard_capstone” database.'''

spark = SparkSession.builder.appName('load_app').getOrCreate()
# Convert the list to a list of Row objects
rows = [Row(**row) for row in loan_app_data]

rows[0:5]

# Define the schema for the loan dataset

schema = StructType([
    StructField("Application_ID", StringType(), True),
    StructField("Gender", StringType(), True),
    StructField("Married", StringType(), True),
    StructField("Dependents", StringType(), True),
    StructField("Education", StringType(), True),
    StructField("Self_Employed", StringType(), True),
    StructField("Credit_History", IntegerType(), True),
    StructField("Property_Area", StringType(), True),
    StructField("Income", StringType(), True),
    StructField("Application_Status", StringType(), True),

])

# Create a DataFrame
df_loan = spark.createDataFrame(rows, schema)
df_loan.show(5)

df_loan.write.format("jdbc")\
    .mode("overwrite") \
    .option("url", "jdbc:mysql://localhost:3306/creditcard_capstone") \
    .option("dbtable", "`CDW-SAPP_loan_application`") \
    .option("user", mysqlSecrets.mysql_username) \
    .option("password", mysqlSecrets.mysql_password) \
    .save()
df_loan.show(5)

'''5. Functional Requirements - Data Analysis and Visualization for LOAN Application

After the data is loaded into the database, the business analyst team wants to analyze and visualize the data.
Use Python libraries for the below requirements:

Req-5	Data Analysis and Visualization'''

# Functional Requirements 5.1	

# Find and plot the percentage of applications approved for self-employed applicants.
# Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!'''

def  approved_self_emp ():

    df_loan.createOrReplaceTempView("loan_application")

    self_emp_all = spark.sql(f"select * from loan_application where Self_Employed = 'Yes'").count()


    self_emp_approved = spark.sql(f"select * from loan_application where Self_Employed = 'Yes' AND Application_Status ='Y'").count()
    lables = ["Approved", "Not approved"]
    if self_emp_all == 0:
        approved_app_percentage = 0
    else:
        approved_app_percentage = (self_emp_approved / self_emp_all) * 100

    fig = plt.figure(figsize =(6, 6))

    plt.pie([approved_app_percentage, 100 - approved_app_percentage], colors=['blue', 'red'], labels=lables, autopct='%1.2f%%' )
    plt.title("Percentage of Approved Self Employed")
    plt.show()
approved_self_emp()

# Functional Requirements 5.2	

# Find the percentage of rejection for married male applicants.
# Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!

def rejected_married_M():
    married_male = spark.sql("select * from loan_application where Gender = 'Male' AND Married = 'Yes'").count()
    married_male_reje = spark.sql("select * from loan_application where Gender = 'Male' AND Married = 'Yes' AND Application_Status = 'N'").count()
    lables = ["Rejected", "Approved"]

    if married_male == 0:
        rejected_app_percentage = 0
    else:
        rejected_app_percentage = (married_male_reje / married_male) * 100
    print("The percentage of rejected married male applicants is " + str(round(rejected_app_percentage, 2)) + '%')
    fig = plt.figure(figsize =(6, 6))

    plt.pie([rejected_app_percentage, 100 - rejected_app_percentage], colors=['red', 'blue'], labels=lables, autopct='%1.2f%%' )
    plt.title("Percentage of Rejected Married Male Applicant")
    plt.show()
rejected_married_M()


# Functional Requirements 5.3	

# Find and plot the top three months with the largest volume of transaction data.
# Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!

def top3_largest_transaction():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    sql = f"select substring(TIMEID, 1, 6) as month, sum(TRANSACTION_VALUE) as total_TRANSACTION_VALUE from cdw_sapp_credit_card group by month order by total_TRANSACTION_VALUE DESC LIMIT 3 "
    try:
        mycursor.execute(sql)
         

    except:
        conn.rollback()
        
    top_3 = mycursor.fetchall()
    # create DataFrame using data
    df = pd.DataFrame(top_3, columns =['month', 'total_TRANSACTION_VALUE'])
    fig = plt.figure(figsize =(8, 6))

    plt.bar(df["month"], df["total_TRANSACTION_VALUE"])
    plt.xlabel("Month")
    plt.ylabel("Total transaction value")
    plt.title("Top three months with the largest volume of transaction")
    print(df)
    mycursor.close()
    conn.close()
top3_largest_transaction()

# Functional Requirements 5.4	
# Find and plot which branch processed the highest total dollar value of healthcare transactions.
# Note: Save a copy of the visualization to a folder in your github, making sure it is PROPERLY NAMED!. 

def highest_transaction():
    
    conn = mydbconnection.connect(
                    host = 'localhost',
                    database='creditcard_capstone',
                    user = mysqlSecrets.mysql_username,
                    password = mysqlSecrets.mysql_password
        )
                     
    mycursor = conn.cursor()   
    
    sql = f"SELECT BRANCH_CODE, SUM(TRANSACTION_VALUE) AS TOTAL_HEALTHCARE_TRANSACTION \
    FROM cdw_sapp_credit_card \
    WHERE TRANSACTION_TYPE = 'Healthcare'group by BRANCH_CODE \
    order by TOTAL_HEALTHCARE_TRANSACTION desc limit 1"
    try:
        mycursor.execute(sql)
         

    except:
        conn.rollback()
        
    highest = mycursor.fetchall()
    # create DataFrame using data
    df = pd.DataFrame(highest, columns =['BRANCH_CODE', 'TOTAL_HEALTHCARE_TRANSACTION'])
    fig = plt.figure(figsize =(4, 6))

    plt.bar(df["BRANCH_CODE"], df["TOTAL_HEALTHCARE_TRANSACTION"])
    plt.xlabel("Branch Code")
    plt.ylabel("Total Healthcare Transaction")
    plt.title("The highest total dollar value of healthcare transactions")
    print(df)
    print(highest)
    mycursor.close()
    conn.close()
highest_transaction()