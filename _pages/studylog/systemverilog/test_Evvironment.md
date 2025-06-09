---
title: "language basics: arr"
tags:
    - testbench
    - systemverilog
    - 
date: "2025-06-09"
thumbnail: ""
bookmark: true
---

# ARRAY
---

SystemVerilog에는 데이터를 효율적으로 저장하고 관리할 수 있는 네 가지 주요 배열(Array) 유형이 있어요. 각각의 특징과 장단점을 간단히 알아볼게요.

1. Fixed-size Arrays (고정 크기 배열)
2. Dynamic Arrays (동적 배열)
3. Queues (큐)
4. Associative Arrays (연관 배열)
5. 
**Fixed-size Arrays, Dynamic Arrays, Queues (1, 2, 3번)**는 데이터가 메모리에 연속적으로 할당되는 경향이 있어요. 그래서 메모리 관리가 비교적 쉽고 접근 속도가 빠르죠. 하지만 Fixed-size Arrays처럼 크기가 미리 정해져 있으면, 실제 데이터 사용량보다 많은 메모리를 차지할 수도 있습니다.

반면, **Associative Arrays (4번)**는 데이터가 메모리에 산발적으로 할당돼요. 이 때문에 관리가 조금 더 복잡할 수 있지만, 필요한 부분에만 메모리를 할당해서 메모리 사용량을 훨씬 절약할 수 있다는 큰 장점이 있습니다.

4개 형태의 array가 존재한다.


1. Fixed size Arrays
2. daynamic Arrays
3. que
4. absiocity


1번 2번 3번은 메모리 관리가 쉽다.
속도가 빠르지만, 메모리를 너무 잡아 먹는다.

4번은 산탄적으로 이루어지고 관리가 어렵지만, 관리만 잘한다면, 메모리 용량을 훨씬 절약할 수 있는 장점이 있다.




### FIXED-SIZE Arrays
---


![alt text](data_arrays-fix.jpg)

**선언 형태:**
`data_type [vector_width] array_name [dimension1_range][dimension2_range]...;`

* **`data_type`**: 배열 요소의 데이터 타입 (예: `bit`, `logic`, `int` 등).
* **`vector_width`**: 배열 요소가 비트 벡터(vector)일 경우, 해당 **개별 요소의 비트 너비**를 정의해요. 예를 들어 `bit [3:0]`는 4비트 너비를 가진 요소를 의미합니다.
* **`array_name`**: 배열의 이름.
* **`[dimension_range]`**: 배열의 차원과 각 차원의 크기를 정의해요. `[msb:lsb]` 형태로 지정하며, 이들은 **배열의 인덱스 범위**를 나타냅니다.

**예시 설명:**
`bit [3:0] c [0:1][0:2];`

* `bit [3:0]`은 `c` 배열의 **각 요소**가 4비트 너비의 벡터임을 나타냅니다. 즉, 각 요소는 0부터 15까지의 값을 저장할 수 있어요.
* `c`는 배열의 이름입니다.
* `[0:1]`은 첫 번째 차원이 2개의 요소(인덱스 0과 1)를 가진다는 의미입니다.
* `[0:2]`는 두 번째 차원이 3개의 요소(인덱스 0, 1, 2)를 가진다는 의미입니다.

따라서 `c`는 `2 x 3` 형태의 2차원 배열이며, 각 칸에는 4비트 벡터 값이 들어갑니다. 이미지의 ``{{3,7,1},{5,1,9}}`` 는 이 2차원 배열의 값들을 초기화하는 것으로, `c[0]`에 `{3,7,1}`이, `c[1]`에 `{5,1,9}`가 할당되는 것을 의미합니다.


### Dynamic Arrays
---

![alt text](<data-arrays-Dynami Arrays.jpg>)

**Dynamic Arrays (동적 배열)**는 이름처럼 런타임에 배열의 크기를 자유롭게 조절할 수 있는 유연한 배열이에요. Fixed-size Arrays와 달리 선언 시에는 크기를 지정하지 않습니다.

**선언 형태:**
`data_type array_name [];`

**주요 특징:**

* 선언 시 크기를 지정하지 않지만, **사용하기 전에 반드시 `new` 연산자를 사용하여 크기를 할당**해야 합니다.
    ```systemverilog
    logic my_dynamic_array[];       // 선언
    my_dynamic_array = new[10];     // 런타임에 10개의 요소로 크기 할당
    ```
* `new` 연산자를 사용할 때 `new[size](copy_from_array)` 형태로 기존 배열의 내용을 복사하면서 새로운 크기를 할당할 수도 있어요.
    ```systemverilog
    logic my_old_array[] = {1, 2, 3};
    logic my_new_array[];
    my_new_array = new[5](my_old_array); // my_old_array의 내용을 복사하여 5개 요소 할당. 나머지 2개는 기본값
    // my_new_array는 {1, 2, 3, x, x} (logic 타입의 기본값은 x)
    ```
* **크기 변경 시 초기화 동작:** Dynamic Arrays의 크기를 변경하기 위해 `new`를 다시 호출하면, **기존의 모든 요소가 타입의 기본값으로 초기화**돼요.
    * `logic` 타입의 기본값은 `x`입니다.
    * `int`나 `byte` 같은 정수형의 기본값은 `0`입니다.
    예시에서 `ID[200] <= ID[100]`처럼 크기가 늘어날 때, 새로 할당된 부분은 타입의 기본값(`x` 또는 `0`)으로 채워지는 것이죠. 이는 단순히 배열의 크기를 200으로 재할당하고, 이전 100개 요소의 값을 복사하는 것이며, 나머지 100개는 초기화되는 것입니다.

기존의 fixed와는 다르게 []안에 어떤 것도 들어가 있지 않는다. (new뒤에는 []에 넣어야 한다.)


danamic이라는 말과 같게 유동적으로 내가 배열의 value를 바꿀 수 있다.
type logic의 default value가 x라서 data_array를
ID[200] <= ID[100]이 들어갈 경우에 나머지 값들이 전부 x로 정해져버린다. 


### Queues
---

![alt text](Queues.jpg)
**Queues (큐)**는 SystemVerilog에서 제공하는 가변 길이의 순서 있는 리스트예요. 데이터를 한쪽 끝(`push_back()`)에서 추가하고 다른 쪽 끝(`pop_front()`)에서 제거하는 방식(FIFO: First-In, First-Out)으로 동작하는 자료구조입니다. 스택(Stack)처럼 한쪽 끝에서만 추가/제거(`push_front()`, `pop_back()`)도 가능해서 매우 유연하게 사용할 수 있습니다.

**선언 형태:**
`data_type array_name [$[:bound]];`

* `$`: 큐임을 나타내는 필수 기호입니다.
* `bound`: 큐의 **최대 크기**를 나타냅니다. `bound`를 생략하면 **unbound (무제한)** 큐가 돼요. 즉, 갯수의 제한 없이 요소를 추가할 수 있습니다.

**주요 특징 및 메서드:**

* **`insert(index, value)`**: 특정 `index`에 `value`를 삽입합니다. 삽입된 위치 뒤의 모든 요소들은 자동으로 한 칸씩 밀려나요.
* **`delete(index)`**: 특정 `index`의 요소를 삭제합니다. 삭제된 위치 뒤의 요소들은 자동으로 당겨지죠.
* **`push_back(value)`**: 큐의 마지막에 `value`를 추가합니다.
* **`push_front(value)`**: 큐의 맨 앞에 `value`를 추가합니다.
* **`pop_back()`**: 큐의 마지막 요소를 제거하고 해당 값을 반환합니다.
* **`pop_front()`**: 큐의 맨 앞 요소를 제거하고 해당 값을 반환합니다.
* **`size()`**: 큐에 현재 저장된 요소의 개수를 반환합니다.

큐는 FIFO(First-In, First-Out) 또는 LIFO(Last-In, First-Out) 동작을 구현할 때 매우 유용하며, 가변적인 데이터 스트림을 모델링하는 데 적합합니다.

type array_name [$[:bound]] 와 같이 괄호 안의 형태가 다음과 같ㅇ다면 queues arr라고 생각하면 된다.
stack과 비슷한 구조이고 bound를 쓰지 않는다면 unbound,
즉 갯수의 제한을 두지 않겠다는 뜻이다.
선언한 뒤에 [arr].insert같은 함수의 형태로 배열을 쌓을 수 있다.


### associative ARR
---

![alt text](associative_arr.jpg)

**Associative** **Arrays** (연관 배열)는 "결합 배열"이라고도 불리며, 일반적인 배열과 달리 순차적인 정수 인덱스가 아닌, **사용자가 정의한 키(key)를 사용하여 데이터에 접근**하는 방식이에요. 해시 맵(Hash Map)이나 딕셔너리(Dictionary)와 유사한 개념이라고 볼 수 있습니다.

**선언 형태:**
`data_type array_name [index_type];`

* **`index_type`**: 인덱스로 사용될 데이터의 타입 (예: `int`, `string`, `bit`, `enum` 등). 이 타입이 데이터에 접근하기 위한 "키"가 됩니다.

**주요 특징:**

* **희소 배열(Sparse Array):** Associative Arrays는 미리 메모리를 할당하지 않고, **요소가 실제로 저장될 때만 메모리를 할당**해요. 이로 인해 메모리 사용 효율이 매우 좋습니다. 제공된 설명처럼 "내가 필요한 부분에만 arr가 배치되어 있어서" 메모리 할당 수가 적다는 장점이 있죠.
* **관리의 까다로움:** 인덱스가 순차적이지 않고 임의의 키가 될 수 있으므로, 어떤 키가 존재하는지 등을 관리하는 것이 Fixed-size Arrays나 Dynamic Arrays보다 까다로울 수 있습니다.
* **키 기반 접근:** `arr[key_value]` 형태로 데이터에 접근합니다.

**예시:**

```systemverilog
int my_associative_array[string]; // string을 키로, int를 값으로 가지는 연관 배열
my_associative_array["apple"] = 10;
my_associative_array["banana"] = 20;
$display("Value for apple: %0d", my_associative_array["apple"]); // 출력: 10결합 배열.
```







