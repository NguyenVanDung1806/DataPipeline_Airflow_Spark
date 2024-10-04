from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

###############################################
# Parameters
###############################################
spark_master = "spark://spark-master:7077/spark"
postgres_driver_jar = "/usr/local/spark/resources/jars/postgresql-42.2.19.jar"
video_views = "/usr/local/spark/resources/data/video_views_mini.csv"
videos = "/usr/local/spark/resources/data/videos.json"
postgres_db = "jdbc:postgresql://postgres/test"
postgres_user = "test"
postgres_pwd = "postgres"

###############################################
# DAG Definition
###############################################
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 10, 4),  # Ngày khởi động
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    "spark-postgres-percentage", 
    default_args=default_args, 
    schedule=timedelta(days=1)  # Lịch chạy hàng ngày
)

start = EmptyOperator(task_id="start", dag=dag)

spark_job_load_data = SparkSubmitOperator(
    task_id="job-load-data",
    application="/usr/local/spark/app/load-data.py",
    name="load-postgres",
    conn_id="spark_default",
    verbose=1,
    conf={
        "spark.master": spark_master,
        "spark.driver.extraClassPath": postgres_driver_jar,
        "spark.executor.extraClassPath": postgres_driver_jar
    },
    application_args=[video_views, videos, postgres_db, postgres_user, postgres_pwd],
    jars=postgres_driver_jar,
    dag=dag
)

start >> spark_job_load_data
