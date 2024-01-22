# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM cschranz/gpu-jupyter:v1.5_cuda-11.6_ubuntu-20.04

LABEL maintainer="Crossent"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Spark dependencies
# Default values can be overridden at build time
# (ARGS are in lower case to distinguish them from ENV)
ARG openjdk_version="11"

RUN apt-get update --yes && \
apt-get install --yes --no-install-recommends \
"openjdk-${openjdk_version}-jre-headless" \
ca-certificates-java && \
apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools wheel &&\
pip3 install pandas &&\
pip3 install scikit-learn &&\
pip3 install tensorflow &&\
pip3 install torch

# Spark installation
ARG spark_version="3.5.0"
ARG hadoop_version="3"

ENV APACHE_SPARK_VERSION="${spark_version}" \
HADOOP_VERSION="${hadoop_version}"

WORKDIR /tmp

COPY spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz .
RUN tar xzf "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
rm "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

WORKDIR /usr/local

# Configure Spark
ENV SPARK_HOME=/usr/local/spark
ENV SPARK_OPTS="--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info" \
PATH="${PATH}:${SPARK_HOME}/bin"

RUN ln -s "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" spark && \
# Add a link in the before_notebook hook in order to source automatically PYTHONPATH
mkdir -p /usr/local/bin/before-notebook.d && \
ln -s "${SPARK_HOME}/sbin/spark-config.sh" /usr/local/bin/before-notebook.d/spark-config.sh

# Fix Spark installation for Java 11 and Apache Arrow library
# see: https://github.com/apache/spark/pull/27356, https://spark.apache.org/docs/latest/#downloading
RUN cp -p "${SPARK_HOME}/conf/spark-defaults.conf.template" "${SPARK_HOME}/conf/spark-defaults.conf" && \
echo 'spark.driver.extraJavaOptions -Dio.netty.tryReflectionSetAccessible=true' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
echo 'spark.executor.extraJavaOptions -Dio.netty.tryReflectionSetAccessible=true' >> "${SPARK_HOME}/conf/spark-defaults.conf"

#COPY hadoop-aws-3.3.4.jar /usr/local/spark/jars/
#COPY aws-java-sdk-bundle-1.12.316.jar /usr/local/spark/jars/

USER ${NB_UID}

# Install pyarrow
RUN mamba install --quiet --yes \
'pyarrow' && \
mamba clean --all -f -y && \
fix-permissions "${CONDA_DIR}" && \
fix-permissions "/home/${NB_USER}"

WORKDIR "${HOME}"

RUN pip install findspark
