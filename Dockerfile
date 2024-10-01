FROM apache/airflow:2.6.0-python3.9

# Chuyển sang người dùng root để cài đặt Java
USER root

# Cài đặt Java OpenJDK 11
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Trở về người dùng airflow
USER airflow
