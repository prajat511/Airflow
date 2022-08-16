# Airflow 
 Sam.py and table.py is python script file.
 
 airflow_pyspark.py and airflow_pyspark2.py is pyspark script file.
 
 pyspark.py is pyspark dag file.
 
 simple.py is python dag file.

                                  
For installation of Airflow Refer to below link

https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html

Mysql database:
CREATE DATABASES airflow_db

To initialize a database in an airflow environment.
airflow db init 

Integrity Error: airflow db upgrade

Run the airflow webserver in an airflow environment.
airflow webserver

Run the airflow scheduler in an airflow environment.
airflow scheduler

Create a dags folder in the airflow directory and put all your dag scripts and python or pyspark scripts there.

After Opening dag on browser go to Admin >> Connection and put connection_id any name and same update in conn_id in dag script also. 
Connection type for the spark file should be spark. 
Host=local[*]
Port 3306

For Parallels Task:

Change SequentialExecutor to LocalExecutor.

Change the sql_alchemy_conn in airflow.cfg file to the given below line.
sql_alchemy_conn =mysql+mysqldb://root:password@localhost:3306/airflow_db




For adding spark in connection: Run following command in ubuntu terminal on airflow environment.

export SPARK_HOME=/path_to_the_spark_home_dir
export PATH=$PATH:$SPARK_HOME/bin 

Install java on airflow environment Using below command to avoid JAVA_HOME is not set error.

sudo apt-get update
sudo apt-get install openjdk-8-jdk






