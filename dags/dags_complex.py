<<<<<<< HEAD
=======


>>>>>>> 5c7a06bc1735bc0f0a47d719fb248d0b0672d0b0
from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_complex",
<<<<<<< HEAD
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 6, 28, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id = 'bash_t1',
        bash_command = 'echo whoami',
    )

    bash_t2 = BashOperator(
        task_id = 'bash_t2',
        bash_command = 'echo $HOSTNAME',
    )

    bash_t1 >> bash_t2
=======
    schedule=None,
    start_date=pendulum.datetime(2025, 6, 22, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    create_tag = BashOperator(task_id="create_tag", 
                              bash_command="echo whoami")
    
    create_tag2 = BashOperator(task_id="create_tag2", 
                              bash_command="echo $HOSTNAME")
    
    create_tag >> create_tag2
>>>>>>> 5c7a06bc1735bc0f0a47d719fb248d0b0672d0b0
