import airflow
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator


default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022, 7, 15),
        'email': ['rajat@torcai.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
      }
dag_spark = DAG(
        dag_id = "sparkoperator_demo",
#         catchup=False,
        default_args=default_args

)
task_start = BashOperator(
    task_id='start',
    bash_command='date',dag=dag_spark
)
spark_submit_local = SparkSubmitOperator(
		application ='/home/rajat/airflow/dags/includes/airflow_pyspark.py' ,
		conn_id= 'spark_local', 
		task_id='spark_submit_task', 
		dag=dag_spark
		)
spark_submit_local2 = SparkSubmitOperator(
		application ='/home/rajat/airflow/dags/includes/airflow_pyspark2.py' ,
		conn_id= 'spark_local', 
		task_id='spark_submit_task2', 
		dag=dag_spark
		)

task_start>>[spark_submit_local,spark_submit_local2]
if __name__ == "__main__":
    dag_spark.cli()