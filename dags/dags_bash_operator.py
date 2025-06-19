

from airflow import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="example_complex",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="Asis/Seoul"),
    catchup=False
) as dag:
    create_entry_group = BashOperator(task_id="create_entry_group", bash_command="echo whoami")

    create_entry_group2 = BashOperator(task_id="create_entry_group2", bash_command="echo $HOSTNAME")


    create_entry_group >> create_entry_group2