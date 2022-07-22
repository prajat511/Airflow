from datetime import datetime, timedelta
from textwrap import dedent
import time

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from includes.table import tablee
from includes.sam import samp

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022, 7, 15),
        'email': ['rajat@torcai.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=1),
      }

dag = DAG('simple', default_args=default_args)
task_start = BashOperator(
    task_id='start',
    bash_command='date',dag=dag
)

t1 = PythonOperator(
    task_id='t1',
    python_callable=tablee,
    dag=dag)
t2 = PythonOperator(
    task_id='t2',
    python_callable=samp,
    dag=dag)
task_start>>[t1,t2]
