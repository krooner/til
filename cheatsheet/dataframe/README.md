# Pandas cheatsheet
Pandas Dataframe

## Pandas Dataframe에서 row를 랜덤 추출하려면
Imbalanced labeled data가 있을 때 갯수를 맞춰주기 위해서 필요했다. [`pandas.DataFrame.sample`](https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/)

## Pandas Dataframe으로 불러올 때 `index_col=0` 설정을 안 하려면
저장할 때 Index를 같이 저장하기 때문에 Index는 저장하지 않도록 설정해야 한다. [stackoverflow: How to avoid pandas creating an index in a saved csv](https://stackoverflow.com/a/25230582)

## [SOLVED] ERROR

`ValueError: parquet must have string column names`
- DataFrame을 Parquet 형식으로 저장 시 오류가 발생. BERT로부터 임베딩을 추출하는 과정에서, 숫자만 텍스트 파일로 저장하는 과정에서 Column을 별도로 추가하지 않았고, Pandas로 해당 파일을 DataFrame으로 로드하는 과정에서 Int 형식의 Column이 생성됨. 추가로 Column을 추가하는 과정에서 Column name의 Type이 섞이게 됨. [github-issue: to_parquet() method fails even though column names are all strings #25043](https://github.com/pandas-dev/pandas/issues/25043#issuecomment-559683875)
