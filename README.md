# CAPSTONE-Data-Engineering
## ETL process for a Loan Application dataset and a Credit Card dataset

## Description 
This is a Capeston project for demonstrating what we learn through out Data Engineering training at Perscholas cohort with TEKSystems. This Project is to manage An ETL process for a Loan Application dataset and a Credit Card dataset using Python (Pandas, advanced modules, e.g., Matplotlib), SQL, Apache Spark (Spark Core, Spark SQL), and Python Visualization and Analytics libraries. For this project there are two datasets credit card and loan application datasets. The Credit Card System database is an independent system developed for managing activities such as registering new customers and approving or canceling requests, etc., using the architecture. 

### Credit Card System database contains the following datasets

a)	CDW_SAPP_CUSTOMER.JSON: This file has the existing customer details.
b)	CDW_SAPP_CREDITCARD.JSON: This file contains all credit card transaction information.
c)	CDW_SAPP_BRANCH.JSON: Each branch’s information and details are recorded in this file. 

Click here to download the Credit Card system files.
mapping document = https://docs.google.com/spreadsheets/d/1t8UxBrUV6dxx0pM1VIIGZpSf4IKbzjdJ/edit?usp=sharing&ouid=109108037194607248998&rtpof=true&sd=true

### loan application database API data
API Endpoint: https://raw.githubusercontent.com/platformps/LoanDataset/main/loan_data.json



## Technologies

### Python (Pandas, advanced modules, e.g., Matplotlib)
python programming language is used to preprocess, clean and transform the data. pandas library is used to 
manipulate and analysis the datasets. pandas is a software library written for the Python programming language for data manipulation and analysis. Matplotlib is used to data analysis and visualization.

### SQL
Relational database language that allows to extract from data tables a series of records with selection, sorting and computation criteria, or to update, delete or add records. SQL is used in this project with pySpark to extract and data analysis 

### Apache Spark (Spark Core, Spark SQL, pyspark) 
Apache Spark is used to process the datasets
pyspark is a Python API for Spark used in this project to help the collaboration of Apache Spark and Python
 
### MYSql Database 
 MYSql Database is an open-source relational database management system (RDBMS). it use to store Etracted, cleaned and transformed data

### Visual Studio code 
Visual Studio Code is a source-code editor used for building and debugging the project 
### Jupyter Notebook

The Jupyter Notebook is an open source web application that you can use to create and share documents that contain live code, equations, visualizations, and text. see the notebook file also and walk through each stage of the project development.

## visual of how the projects works
Find and plot which transaction type has the highest transaction count.

![Alt text](<Highest count Transaction Type.png>)

Find and plot which state has a high number of customers.

![Alt text](<State_with High Number of Customers.png>)

Find and plot the sum of all transactions for the top 10 customers, and which customer has the highest transaction amount.
![Alt text](<Sum of All Transactions for the Top 10 Customers.png>)

Find and plot the percentage of applications approved for self-employed applicants.

Percentage of Approved Self Employed

![Alt text](<Percentage of Approved Self Employed-1.png>)

The percentage of rejected married male applicants is 28.43%

![Alt text](<Percentage of Rejected Married Male Applicant.png>)

Find and plot the top three months with the largest volume of transaction data.

top three months with the largest volume of transaction data

![Alt text](<Top Three Months with the Largest Volume of Transaction.png>)

Find and plot which branch processed the highest total dollar value of healthcare transactions.

 highest total dollar value of healthcare transactions

![Alt text](<The Highest Total Dollar Value of Healthcare Transactions.png>)




## user instruction 
To use this project download all the repo and use requirements.txt to install the required module and packages on your local machine. use the following command to install requirements.txt

        pip install -r requirements.

To create your own requirements,txt use the following command

        pip freeze
        pip freeze > requirements.txt
        
## Credits 
Thank you all this training instructors Valerie, Benjamine, Aikrem for your greate support.


# contact
 contact me at kidiyeamanueal21@gmail.com if you have any questions