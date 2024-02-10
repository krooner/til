# NumPy Cheatsheet

Scientific Computing

## Top-k maximum/minimum 값에 대한 Indices 계산 
[`numpy.argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html)

```python
import np

k = 2
input_array = np.array([1, 3, 2, 4])

np.argsort(input_array)[-k:] # array([1, 3])
# Top-k maximum value는 3, 4
# 3의 index인 1
# 4의 index인 3을 반환
```
