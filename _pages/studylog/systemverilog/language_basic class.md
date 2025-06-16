---
title: "language basics: class"
tags:
    - testbench
    - systemverilog
    -  class
date: "2025-06-11"
thumbnail: ""
bookmark: true
---


# CLASS

![alt text](/FPGA_multi_asset/0610 sysverilog_img/comparertl.jpg)

`structure`는 `RTL`과 유사한 점이 많습니다.

 `module`은 `class`로 바꿔 부릅니다.
 `instance`는 주로 `object`로 부르고, 이름은 `handle`이라고 부릅니다.
 `reg`와 `wire`는 `variables`로 부르며, `task`, `function`과 같이 동작하는 블록들은 `subroutine`으로 통칭합니다.

<br>

![alt text](/FPGA_multi_asset/0610 sysverilog_img/class_ex.jpg)



다음은 객체 지향(`OOP`) `class`의 예시 사진입니다.

 `variables`(변수)는 `properties`(속성)이라고 부릅니다.
 `subroutine`은 `method`라고 부릅니다.
 이 두 가지 요소를 통칭해서 `members`라고 부릅니다.

<br>
<br>

# Why use class 

![alt text](/FPGA_multi_asset/0610 sysverilog_img/why_class.jpg)

`class`를 사용하는 이유는 다음과 같습니다.

 `object`(객체)는 `dynamic`(동적)이지만, `module`은 `static`(정적)입니다. 따라서 `object`는 우리의 필요에 따라 지우고 다시 생성할 수 있습니다.
 `object`(객체)에 맞는 `handle point`를 작성할 수 있습니다.
 `object handler`는 `argument`(인수)를 전달할 수 있습니다.
 `object memory`는 복사하거나 비교할 수 있습니다.
 이것들은 모두 `module`의 `instance`가 처리 불가능한 일입니다.
 `class`는 상속 가능하지만, `module`은 그렇지 못합니다.
 `class`는 정보를 수정해도 `기존의 user`에게 피해가 가지 않지만 `module`은 그렇지 않습니다.

<br>

# new(); 로 초기화 하는 이유

![alt text](/FPGA_multi_asset/0610 sysverilog_img/constructing.jpg)



`OOP object`는 `class` 정의에 의해 만들어집니다.

 이러한 정의는 `new();`를 사용하여 이루어집니다.
 사용 방법은 위 사진처럼 만들어진 `class`를 `handle`로 호출하여 사용할 때, `new();`를 통해 초기화하는 것을 확인할 수 있습니다.
 이러한 초기화를 하지 않는다면 `memory allocation`이 일어나지 않아 결국 `runtime error`로 이어질 가능성이 높습니다.

<br>


![alt text](/FPGA_multi_asset/0610 sysverilog_img/new_class.jpg)



그리고 `new();`의 경우에는 `return`이 없는 `type`의 선언입니다. 실행 즉시 `객체에 동적 메모리를 할당하기 때문에` 기존의 `.`을 활용해서 불러올 경우 `access`하지 못한다는 뜻입니다.

`function으로 사용할 때 꼭 유유의하도록 합시다.`

<br >

#  keword
---
![alt text](/FPGA_multi_asset/0610 sysverilog_img/this_class.jpg)

 `this` keyword는 객체 스스로를 가리키는 `handle`입니다.
 `class members` 중에서 가장 가깝게 `instance`된 `object`를 가리킵니다.
 위 사진에서처럼 `this`를 사용한다면 가장 최근에 선언된 `sa`를 가리키고, 우측 항에 존재하는 `sa`는 `function`의 `arguments`가 들어가게 됩니다.

# Static access

```systemverilog
program automatic test;

class Packet;
    static int count =0;
    int id;
    static function int get_count();
    return count;
    endfunction
    function new();
        this.id =count++;
    endfunction
endclass: Packet


initial begin
    Packet pkt0 = new();
    Packet pkt1 = new();
    $display("pkt0 id is: %0d", pkt0.id);
    $display("pkt1 id is: %0d", pkt1.id);
    $display("count: %0d", Packet::count);
    $display("count: %0d", Packet::count);
end

endprogram: test
<br>
```
우리는 `class`에 `static` keyword를 사용할 수도 있습니다. 변수를 정적으로 선언한다는 것인데, 위와 같은 예시를 들자면,

 `function`에서 정의된 `count++;`는 후위 연산자입니다.

 우리가 값을 가져올 때 `count` 값은 항상 초기화되기 때문에 `count`가 1씩 더해지는 의도한 동작을 체크하기가 어렵습니다.

 그래서 정적인 동작을 의도하는 `static`을 활용해서 다음에 값을 받도록 설정할 수 있습니다.

 그렇지만 여기에서도 문제가 존재합니다. `pkt0`이라는 `class`를 `handle`할 때마다 `new();` 함수를 사용하기 때문에 `count`의 값이 올라가서 정적인 접근을 하기가 어렵습니다.

 그래서 기존에 `.`을 이용한 호출과 달리 `::`(double colon)을 통한 정적인 접근으로 원하는 `count`값을 가져올 수 있습니다.

 예시 코드대로라면 `pkt0.id`는 후위 연산이 되기 전인 `0`이 나옵니다.

 다음 `pkt1.id`는 연산이 되고 난 뒤에 적용된 `1`이 나옵니다.

 그리고 `Packet::count` 두 문장 중 첫 문장은 이전의 연산이 적용된 `2`가 나옵니다.

 하지만 다음 접근은 `static members`에 `only access`하기 때문에 어떠한 값 변화도 없이 `2`가 나옵니다.

<br>


![alt text](/FPGA_multi_asset/0610 sysverilog_img/const_class.jpg)

`const`를 통해 우리의 모든 `properties`를 상수화할 수 있습니다. 그중에서도 두 개의 `case`로 나눠서 다르게 적용되는 점이 있습니다.

`instance constant`로 선언할 경우에는 `static`하게 바뀌지 않습니다.
`Global constant`로 선언할 경우에는 일반적으로 `static`하게 바뀝니다.
공통적으로 이 두 종류의 `constant`는 당연하게 모든 값이 `modified`될 수 없게 변환됩니다.

![alt text](/FPGA_multi_asset/0610 sysverilog_img/work_class.jpg)
`class`는 정적이기 때문에 `initial`문이나 `always` 같은 블록을 할당하기가 어렵습니다.
비슷하게 구현할 수 있는 `fork`문을 이용하여 `class` 내부의 동작을 제어할 수 있습니다.

![alt text](/FPGA_multi_asset/0610 sysverilog_img/protect_class.jpg)
`localparameter`를 통해 변수의 변경을 막을 수 있다면, 반대로 `protected` 선언을 통해 변수의 변경을 가능하게 만들 수도 있습니다. (`parameterized`)
<br>
![alt text](/FPGA_multi_asset/0610 sysverilog_img/protected2_class.jpg)
<br>

위 사진의 경우 `int_stack` `class`의 `queues array`의 `push`, `pop` 동작을 위해 `protected`를 사용하고 다시 사용할 수 있게끔 `parameter` 값들을 선언해 둔 것을 볼 수 있습니다.
<br>

![alt text](/FPGA_multi_asset/0610 sysverilog_img/forward_class.jpg)
<br>

<br>
다음은 `typedef`를 사용할 때 일어나는 흔한 실수로 매개변수를 `class` 이후에 선언하는 잘못입니다. 순서가 어긋나서 이 부분은 `typedef`가 `Packet` 변수를 읽지 못하기 때문에 `compile`되지 않게 됩니다.
<br>
<br>

![alt text](/FPGA_multi_asset/0610 sysverilog_img/best1_class.jpg)

<br>
가장 좋은 연습은 `class` 안에 직접 `task`를 작성하지 않고 외부에서 작성한 뒤 `extern`을 통해 불러오는 것입니다.

주의해야 할 점은 `task` 이후에 `class`에 첨부할 `method`이기 때문에 `double(::)`을 통해 연관 지어 주는 것이 좋습니다.
![alt text](/FPGA_multi_asset/0610 sysverilog_img/quiz2_class.jpg)

마지막으로 간단하게 문제를 하나 풀어보자면, `$display`를 통해 출력될 `o1.a`, `o2.a`를 구하는 문제입니다.

 `class`는 단순하게 `int a`만을 선언한다.

 `class abc`의 `handle`을 `o1`, `o2`에 `new();` 함수를 통해 초기화해준다.

 `o1`은 5, `o2`는 50을 바라보고 있다.

 그러므로 첫 번째 `$display`에는 `o1.a = 5`가 출력되고, `o2.a = 50`이 출력된다.

 두 번째 초기화에서는 `o2`는 `o1`을 바라보고 있다.

 그러한 상황에서 `o1.a`가 500을 바라보게 된다.

 계속 바라본다라는 표현을 하고 있는데, 현재 `class handle`들이 직접적으로 `call by value`하고 있는 것이 아닌, `call by reference`하고 있다는 것을 의미한다.
그래서 후에 `o2.a`에 들어갈 값이 5라고 착각할 수 있지만, `pointer`의 개념처럼 `o1`을 바라보기 때문에, 500의 값을 출력한다.
