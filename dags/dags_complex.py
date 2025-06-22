

from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_complex",
    schedule=None,
    start_date=pendulum.datetime(2025, 6, 22, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    create_tag = BashOperator(task_id="create_tag", 
                              bash_command="echo whoami")
    
    create_tag2 = BashOperator(task_id="create_tag2", 
                              bash_command="echo $HOSTNAME")
    
    create_tag >> create_tag2