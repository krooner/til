# PySpark Cheatsheet

## Basics
`dataframe = spark.read.option('header', True).csv('test_data.csv')`
- Header 추가해서 불러오기

```python
from pyspark.sql.types import IntegerType
dataframe = dataframe.withColumn("ordr_dt_hhmmss", dataframe[ordr_dt_hhmmss"].cast(IntegerType()))
```
- Column Type Casting: String to Integer

## 컬럼마다 Null/NaN 값이 얼마나 있는지 세기
[stackoverflow: How to find count of Null and Nan values for each column in a PySpark dataframe efficiently?](https://stackoverflow.com/a/44631639)

## 여러 개의 parquet file을 동시에 읽기
Wildcard Symbol을 포함한 Path를 입력하면 알아서 현재 작업 디렉토리 기준 해당 Pattern에 부합하는 파일을 로드함. [stackoverflow: Read few parquet files at the same time in Spark](https://stackoverflow.com/a/37294794)

```python
dataframe = spark.read.parquet('train_data_*.parquet')
```

## 사용자 기준으로 Groupby 하되 Datetime 컬럼값 순서대로 데이터를 리스트로 모으기
시퀀스 데이터 생성을 위해 필요한 작업
[stackoverflow: collect_list by preserving order based on another variable](https://stackoverflow.com/a/50668635)

## UDF (User Defined Function, 사용자 정의 함수)

