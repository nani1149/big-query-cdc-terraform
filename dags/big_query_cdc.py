import time
from datetime import datetime
from pathlib import Path

from airflow.models.dag import DAG
import json
from airflow.operators.python import PythonOperator
from include.bigquery_cdc.sample_cdc import BigQueryStorageWriteAppend
from include.bigquery_cdc.bq_table_alter import alter_table_max_staleness

DAG_ID = "bigquery_cdc_pipeline"

#with open('new_customers.json', 'r') as json_file:
with open('../include/bigquery_cdc/new_customers.json','r') as json_file:
    #with open('modified_customers2.json','r') as json_file:
    customer_data = json.load(json_file)

with open('../include/bigquery_cdc/modified_customers1.json','r') as json_file:
    #with open('modified_customers2.json','r') as json_file:
    new_customer_data = json.load(json_file)


with DAG(
    DAG_ID,
    schedule="@once",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example", "bigquery"],
) as dag:
    
    bq_alter_table_staleness = PythonOperator(task_id="alter_bq_table", python_callable=alter_table_max_staleness,)
    bq_insert_task= PythonOperator(task_id="insert_customer_data", python_callable=BigQueryStorageWriteAppend,op_kwargs={'project_id': 'sacred-alliance-433217-e3', 'dataset_id': 'bigquery_cdc', 'table_id': 'bigquery_customers_cdc', 'data': customer_data})
    bq_upsert_task= PythonOperator(task_id="customer_data_cdc", python_callable=BigQueryStorageWriteAppend,op_kwargs={'project_id': 'sacred-alliance-433217-e3', 'dataset_id': 'bigquery_cdc', 'table_id': 'bigquery_customers_cdc', 'data': new_customer_data})

    (bq_alter_table_staleness >> bq_insert_task >> bq_upsert_task)

    

    

    