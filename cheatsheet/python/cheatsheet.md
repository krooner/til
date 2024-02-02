# Python Cheatsheet

## regex

[알파벳, 숫자, 한글, Whitespace를 제외한 나머지 문자들을 제거하기](https://stackoverflow.com/a/23853882)

```python
import re

input_text = "LG 스타일러 30% 할인 중!!!!! (사은품 증정)"
re.sub(r'[^a-zA-Z0-9가-힣 ]+', r'', input_text)

input_text # 'LG 스타일러 30 할인 중 사은품 증정'
```

[텍스트 내 연속된 알파벳 Substring Index 찾기]()

```python
import re
input_text = "틔운 미니의 제품코드는 L023E1"

[obj.span() for obj in re.finditer(r'[a-zA-Z]', input_text)] # [(13, 14), (17, 18)]
```

## matplotlib.pyplot and seaborn

[Plot에 텍스트 표시할 때 서로 겹치지 않도록 하는 라이브러리: adjustText](https://github.com/Phlya/adjustText)

![example](https://github.com/Phlya/adjustText/raw/master/figures/mtcars.gif)

## numpy

[Top-k maximum/minimum 값에 대한 Indices 계산하기]()

```python
import np

k = 2
input_array = np.array([1, 3, 2, 4])

np.argsort(input_array)[-k:] # array([1, 3])
# Top-k maximum value는 3, 4
# 3의 index인 1
# 4의 index인 3을 반환
```
