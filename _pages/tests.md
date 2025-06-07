


---
title: "테스트 파일 확인용"
tags:
    - user manual
    - markdown
    - writing format
date: "2023-09-05"
thumbnail: 
bookmark: true
---





# 안녕하세요! GitHub 블로그 테스트 포스트입니다.

이 포스트는 GitHub 블로그에 마크다운 파일을 업로드했을 때 어떻게 표시되는지 확인하기 위한 **테스트 목적**으로 작성되었습니다.

---

## 텍스트 스타일

다양한 텍스트 스타일을 시도해볼까요?

* **볼드체 텍스트**를 사용하려면 `**` 또는 `__`를 사용합니다.
* *이탤릭체 텍스트*를 사용하려면 `*` 또는 `_`를 사용합니다.
* ***볼드 + 이탤릭체 텍스트***도 가능하죠.
* ~~취소선 텍스트~~는 `~~`로 감싸줍니다.

---

## 목록

### 순서 없는 목록 (Unordered List)

* 항목 1
    * 하위 항목 1.1
    * 하위 항목 1.2
* 항목 2
* 항목 3

### 순서 있는 목록 (Ordered List)

1.  첫 번째 항목
2.  두 번째 항목
    1.  하위 항목 2.1
    2.  하위 항목 2.2
3.  세 번째 항목

---

## 코드 블록

인라인 코드 `print("Hello, World!")`는 백틱(`)으로 감쌉니다.

여러 줄의 코드 블록은 다음과 같이 사용할 수 있습니다.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 함수 호출 예시
result = factorial(5)
print(f"5! = {result}")
