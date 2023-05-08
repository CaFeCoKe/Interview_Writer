# Interview_Writer
Text Generation Task를 수행하여 자기소개서의 질문을 입력받게 되면 모델의 답변은 얼마나 좋은 성능을 낼까라는 생각에서 비롯된 미니 프로젝트이다. 
최대한 특정 분야(개발자)에 맞는 자기소개서를 생성해내기 위해 개발자와 관련된 자기소개서 데이터를 모아 쓴다.

## 1. 알고리즘 순서도


## 2. 결과


## 3. 문제점 & 주의점
- BPE(Byte Pair Encoding)와 WordPiece <br>
BPE는 가장 작은 단위의 쌍이 포함된 token의 등장빈도에 따라 가장 많이 등장하는 쌍을 vocabulary에 추가시키는 알고리즘이다. <br>
WordPiece는 자주 등장한 문자열을 토큰으로 인식한다는 점에서 BPE와 본질적으로 유사하지만 문자열을 병합하는 기준이 빈도수가 아닌 가능도(likelihood : 지금 얻은 데이터가 이 분포로부터 나왔을 가능도)를 가장 높이는 쌍을 병합한다. <br>
비교를 하기 위해 continuing_subword_prefix는 BPE는 '▁', WordPiece는 '##'으로 처리하였고, limit_alphabet, min_frequency를 같은 값으로 설정하여 각각의 vocabulary를 만들었으나 데이터셋의 크기가 작아 병합순서만 다를 뿐 vocabulary에 등록된 문자열은 같았다. <br>
![vocab](https://user-images.githubusercontent.com/86700191/236796592-1f7bed0c-e57c-460f-b7eb-b3b74eace185.PNG)

## 4. 사용 모델과 데이터 및 참고링크
