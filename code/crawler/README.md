# Selemium 기반 크롤러

## 목적
제품 코드를 알고 있을 때, 네이버쇼핑 검색창에 제품 코드를 검색하여 가장 상단에 나타나는 제품명을 가져온다.
- 해당 예시는 사실 굳이 크롤러가 필요하진 않음.
    - iPhone 15 Pro를 검색하고 싶으면 `https://search.shopping.naver.com/search/all?query=iPhone%2015%20Pro` 처럼 URL의 query string을 바꾸면 됨
- 이전에도 크롤러 코드를 작성했다가 그냥 잊어먹었던 것이 아까워서 기록해두고자 작성함.

## 사용

```bash
# 1. 가상 환경 
$ python3 -m venv myvenv
$ source myvenv/bin/activate
# 2. 필요 라이브러리 설치
(myvenv) $ pip install -r requirements.txt
# 3. 크롤러 실행
(myvenv) $ python3 main.py --query MQ083KH/A
iPhone 14 Pro 128GB 골드 * MQ083KH/A
```

## 설명
1. selenium의 chromedriver를 호출함
    - 만약 chromedriver 이슈가 발생할 경우, [최신 Chromedriver 페이지](https://googlechromelabs.github.io/chrome-for-testing/#stable)에서 다운로드 후 압축 해제
    - `/usr/local/bin/`에 `chromedriver`를 위치시키기.
2. 네이버 쇼핑 홈페이지에 접속
3. 네이버 쇼핑의 검색창 Element를 찾음 (HTML Input Tag의 class_name으로 찾음)
4. 해당 Element에 검색어를 입력하고 Enter를 누름
5. 이동된 페이지에서 제품 리스트 Element를 찾음
6. 제품 리스트 Element에서 제품명만 추출 후 가장 첫 번째 제품명을 출력