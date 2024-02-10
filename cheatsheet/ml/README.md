# ML library 

## scikit-learn

[sklearn.metrics.roc_auc_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
- Prediction score로부터 ROC Curve의 AUC 를 계산하는 함수
    - ROC = Receiver Operating Characteristic
    - AUC = Area Under Curve
- Parameters
    - `y_true`: True label indicator
        - N-class 분류 (N>1) 의 경우에는 `(n_samples,)` 형태
    - `y_score`: Target scores
        - Binary의 경우 `(n_samples, )` 형태의 배열이며, __큰 Label에 대한 확률 (probability of the class with the greater label)__ 이어야 한다.
        - 

```python
from sklearn.metrics import roc_auc_score

# If binary classification,
y_true = np.array([1, 1, 0, 1])
y_output = np.array([
    [.2, .8], 
    [.3, .7], 
    [.1, .9], 
    [.6, .4]
])

y_pred = np.argmax(y_output, axis=1) 
# [1, 1, 1, 0] (decision boundary = .5)

y_score = y_output[:, -1] 
# [.8, .7, .9, .4] (the probability of greater label (1))

ra_score = roc_auc_score(y_true, y_score)
# 0.0
```