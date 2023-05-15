# Interview_Writer
Text Generation Task를 수행하여 자기소개서의 질문을 입력받게 되면 모델의 답변은 얼마나 좋은 성능을 낼까라는 생각에서 비롯된 미니 프로젝트이다. 
최대한 특정 분야(개발자)에 맞는 자기소개서를 생성해내기 위해 개발자와 관련된 자기소개서 데이터를 모아 쓴다.

## 1. 알고리즘 순서도


## 2. 결과


## 3. 문제점 & 주의점
- 크롤링을 사용 안한 이유 <br>
크롤링은 HTML 페이지를 가져와서, HTML/CSS등을 파싱하고, 필요한 데이터만 추출하는 기법이다. 파이썬의 경우 BeautifulSoup, Selenium 등과 같은 패키지로 크롤링이 가능한데, 본인은 Selenium은 써본적이 없는 관계로 배제하였다. <br>
BeautifulSoup은 HTML의 태그를 파싱하여 데이터를 추출해내는데 여기서 필요한 URL 주소가 일정한 패턴이 있다면 사용하려 하였지만 개발자와 관련된 자기소개서 데이터만 찾다보니 URL의 경로가 일정한 패턴을 가지고 있지않아 하나하나 해당 페이지의 URL을 가지고 데이터를 뽑는것은 의미가 없다라고 생각하여 쓰지 않았다.

- BPE(Byte Pair Encoding)와 WordPiece <br>
BPE는 가장 작은 단위의 쌍이 포함된 token의 등장빈도에 따라 가장 많이 등장하는 쌍을 vocabulary에 추가시키는 알고리즘이다. <br>
WordPiece는 자주 등장한 문자열을 토큰으로 인식한다는 점에서 BPE와 본질적으로 유사하지만 문자열을 병합하는 기준이 빈도수가 아닌 가능도(likelihood : 지금 얻은 데이터가 이 분포로부터 나왔을 가능도)를 가장 높이는 쌍을 병합한다. <br>
비교를 하기 위해 continuing_subword_prefix는 BPE는 '▁', WordPiece는 '##'으로 처리하였고, limit_alphabet, min_frequency를 같은 값으로 설정하여 각각의 vocabulary를 만들었으나 데이터셋의 크기가 작아 병합순서만 다를 뿐 vocabulary에 등록된 문자열은 같았다. <br>
![vocab](https://user-images.githubusercontent.com/86700191/236796592-1f7bed0c-e57c-460f-b7eb-b3b74eace185.PNG)

## 4. 사용 모델과 데이터 및 참고링크
- [합격 자기소개서 자료(잡코리아)](https://www.jobkorea.co.kr/)