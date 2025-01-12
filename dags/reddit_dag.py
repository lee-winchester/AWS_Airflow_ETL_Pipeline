from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline
default_args={
    'owner':'Leepaakshi Gokulkrishnan',
    'start_date':datetime(2025,1,10)

}
file_postfix=datetime.now().strftime("%y%m%d")
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)
extract=PythonOperator(
    task_id='extraction_from_reddit',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit':'awww',
        'time_filter':'day',
        'limit':300
        },
    dag=dag
)

