# 0725 관통프로젝트 리뷰_이선휘

## 학습한 내용
- API 를 request 하기
- 파이썬 버전과 패키지 호환성 문제
- dictionary를 활용하여 추출, 수정 및 통합

## 어려웠던 내용
- 재귀함수를 활용하여 키값 번역을 해보려고 시도
  - 큰그림을 제대로 그리지 않은 채 시도 하여 논리적 오류 발생
  - 90%는 완성 되었지만 10%의 오류가 지속적으로 발생
- 딕셔너리의 구조를 파악하고 필요한 데이터를 오류 없이 추출하기

## 새로 배운 것
- 무언가 알고리즘을 짤 때 먼저 큰그림을 그리고 이를 세분화 하여 작성하기
- 무언가가 오래 걸린다면 먼저 다른 것을 하여 시간 배분을 지혜롭게 하기
- isinstance
    ```python
    isinstance(object, class_or_tuples) #해당 객체가 특정 타입인지 확인해주는 메소드
    type(lst) == list # type은 텍스트를 리턴하지 않기에 오류가 난다
    ```
- .update
  ```python
  dic = {}
  dic.update({"일" : 1}) #dic = {"일" : 1}
  ```
- .values
  ```python
    dic = {"일" : 1}
    for i in len(dic.values()):
        print(i) # TypeError: 'int' object is not iterable

    for i in dic.values():
        print(i) # 1
  ```
  .values는 for문으로 바로 언패킹 할 수 있다. 단 len는 안된다. len(range(a.values))로 해야 for문에 int 로 활용이 가능하다


## 느낀 점
- 내가 정말 부족함을 알게 되었다.
- 쉬운 알고리즘은 그냥 시도 하면 되었는데, 뭔가 조금 복잡해지고 재귀함수를 사용하다 보니 내가 뭘 하고 있는지도 기억을 못하는 수준이었다. 더 차분하게 큰 그림을 그리고 필요한 기능을 분리하여 개발하는 연습을 해야겠다