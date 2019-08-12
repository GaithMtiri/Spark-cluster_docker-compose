#!/bin/bash

set -e

docker build -t spark-base:2.3.1 ./docker/base
docker build -t spark-master:2.3.1 ./docker/spark-master
docker build -t spark-worker:2.3.1 ./docker/spark-worker
docker build -t spark-driver:2.3.1 ./docker/spark-driver/drf_app
docker build -t spark-driver-spring:2.3.1 ./docker/spark-driver-spring
