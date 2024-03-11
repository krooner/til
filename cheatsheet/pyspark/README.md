# PySpark Cheatsheet

## Basics
`dataframe = spark.read.option('header', True).csv('test_data.csv')`
- Header 추가해서 불러오기

```python
from pyspark.sql.types import IntegerType
dataframe = dataframe.withColumn("ordr_dt_hhmmss", dataframe.ordr_dt_hhmmss.cast(IntegerType()))
```
- Column Type Casting: String to Integer

## 컬럼마다 Null/NaN 값이 얼마나 있는지 세기
[stackoverflow: How to find count of Null and Nan values for each column in a PySpark dataframe efficiently?](https://stackoverflow.com/a/44631639)

## 여러 개의 parquet file을 동시에 읽기
Wildcard Symbol을 포함한 Path를 입력하면 알아서 현재 작업 디렉토리 기준 해당 Pattern에 부합하는 파일을 로드함. [stackoverflow: Read few parquet files at the same time in Spark](https://stackoverflow.com/a/37294794)

```python
dataframe = spark.read.parquet('train_data*.parquet')
```

## 사용자 기준으로 Groupby 하되 Datetime 컬럼값 순서대로 데이터를 리스트로 모으기
시퀀스 데이터 생성을 위해 필요한 작업
[stackoverflow: collect_list by preserving order based on another variable](https://stackoverflow.com/a/50668635)

```python
from pyspark.sql import Window
import pyspark.sql.functions as F
def apply_groupby_id_and_sortby_date(dataframe, key_column, target_column):
  w = Window.partitionBy(key).orderBy('concat_yymmdd')

  dataframe_groupby_sorted = dataframe.withColumn('sorted_list', F.collect_list(target_column).over(w)\
    .groupby(key_column)\
    .agg(F.max('sorted_list').alias('sorted_list'))
  return dataframe_groupby_sorted

train_df = apply_groupby_id_and_sortby_date(train_df, key_column='cust_id', target_column='detail')
```

## `pyspark.sql.functions.udf` (User Defined Function, 사용자 정의 함수)
데이터 시간 순 정렬을 위해 `YYMM` 문자열 컬럼과 `DD` 문자열 컬럼을 Concat and Cast한 컬럼 `concat_yymmdd` 만들기

```python
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, StringType

def apply_udf_concat_cast(dataframe):
  concat_cast_udf = F.udf(lambda a, b: a+b, StringType())
  dataframe = dataframe.withColumn('concat_yymmdd', concat_cast_udf(dataframe.YYMM, dataframe.DD))
  dataframe = dataframe.withColumn('concat_yymmdd', dataframe.concat_yymmdd.cast(IntegerType()))
  return dataframe

train_df = apply_udf_concat_cast(train_df)
```

## `pyspark.sql.dataframe.filter`
2023년 1월 31일 이전 데이터만 활용하기

```python
import pyspark.sql.functions as F
train_df = train_df.filter((F.col('concat_yymmdd')<=230131))
```
