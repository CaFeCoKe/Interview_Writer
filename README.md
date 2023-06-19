# Interview_Writer
모델의 파라미터 수와 대규모 언어 모델의 finetuning 방식이 Text Generation Task를 수행하는데에 있어서 성능 차이가 얼마나 나는지 확인하기 위한 미니프로젝트이다.<br>
사용한 데이터셋은 잡코리아에서 크롤링한 자기소개서 데이터이고, 모델은 KoGPT2와 파라미터 수를 변동할 수 있는 Transfomers의 GPT모델을 사용한다.

## 1. 알고리즘 순서도


## 2. 결과


## 3. 문제점 & 주의점
- BPE(Byte Pair Encoding)와 WordPiece <br>
BPE는 가장 작은 단위의 쌍이 포함된 token의 등장빈도에 따라 가장 많이 등장하는 쌍을 vocabulary에 추가시키는 알고리즘이다. <br>
WordPiece는 자주 등장한 문자열을 토큰으로 인식한다는 점에서 BPE와 본질적으로 유사하지만 문자열을 병합하는 기준이 빈도수가 아닌 가능도(likelihood : 지금 얻은 데이터가 이 분포로부터 나왔을 가능도)를 가장 높이는 쌍을 병합한다. <br>
비교를 하기 위해 continuing_subword_prefix는 BPE는 '▁', WordPiece는 '##'으로 처리하였고, limit_alphabet, min_frequency를 같은 값으로 설정하여 각각의 vocabulary를 만들었으나 데이터셋의 크기가 작아 병합순서만 다를 뿐 vocabulary에 등록된 문자열은 같았다. <br>
![vocab](https://user-images.githubusercontent.com/86700191/236796592-1f7bed0c-e57c-460f-b7eb-b3b74eace185.PNG)

## 4. 사용 모델과 데이터 및 참고링크
- [합격 자기소개서 자료(잡코리아)](https://www.jobkorea.co.kr/)
- [KoGPT2](https://github.com/SKT-AI/KoGPT2)
- [Transfomers GPT2 code](https://github.com/huggingface/transformers/blob/v4.30.0/src/transformers/models/gpt2/modeling_gpt2.py)