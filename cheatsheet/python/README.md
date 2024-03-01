# Python Cheatsheet

## String interpolation
표현식 안에 문자열을 넣는 것.

[Python 문자열 출력 형식](https://realpython.com/python-f-strings/)

## argparse

- [`argparse` Basics](https://greeksharifa.github.io/references/2019/02/12/argparse-usage/)
- [argparse를 활용해서 True/False 저장](https://noanomal.tistory.com/221)

```python
# main.py
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", help="batch size of training data", type=int, default=128)
    parser.add_argument("--learning-rate", help="learning rate of optimizer", type=float, default=1e-3)
    parser.add_argument("--gpu", help="using gpu acceleration for train", action="store_true")

    args = parser.parse_args()
    print(args.batch_size, args.learning_rate)

    if args.gpu:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    else:
        device = "cpu"
    print(device)

```

```bash
$ python main.py --batch-size 256 --learning-rate 1e-4 --gpu
256, 1e-4
cuda
```

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

## ETC
- `r'\d+'`: One or more digits
- `r'\w+'`: One or more alphanumeric chars
