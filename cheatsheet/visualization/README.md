# Visualization Cheatsheet

`matplotlib.pyplot`, `seaborn`

## Plot에서 Text가 서로 겹치지 않게 하려면

[adjustText](https://github.com/Phlya/adjustText)

![example](https://github.com/Phlya/adjustText/raw/master/figures/mtcars.gif)

## Plot에서 한글 글꼴이 깨질 때
일반적으로 Docker Image에는 한글 글꼴을 추가하지 않아서, Docker Container에서 Visualization 작업을 수행할 경우 글꼴이 깨질 수 있다. 그렇기 때문에 `맑은 고딕` 글꼴을 다운로드 받아서 폰트 경로에 추가시켜준다.

```bash
cd /home/kisookim
wget https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun-gothic.zip && unzip malgun-gothic.zip
```

```python

from matplotlib import font_manager
font_manager.fontManager.addfont("/home/kisookim/malgun.ttf")
plt.rcParams['font.family'] = 'Malgun Gothic'

# minus symbol
plt.rcParams['axes.unicode_minus'] = False
```