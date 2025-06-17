---
title: "CMOS design rule"
tags:
    - systemverilog
    - simulation
    - place and route
    - CMOS design
date: "2025-06-17"
thumbnail: "![alt text](wallpaper.jpg)"
bookmark: true
---



![alt text](well_substrate-1.png)


다음은 공정을 마친 `MOS`를 간략하게 표현한 것이다.
설계 영역의 이야기를 주로 하기 위해 8대 공정에 대한 이야기는 간략화 한다.


* oxidation 과정과 photoresist, uv, eching을하는 것을 반복해서
  원하는 패턴의 gate,source, drain 을 증착 시킨다.

* dopamant 과정을 통해서 p 또는 n well을 기판 위에 생성한다.

* `n well` 혹은 `p well`에 반대되는 `diffusion region`을 생성하고, `body`를 끌어내는 `p region`과 `n region`의 옆에 붙혀둔다. 

* `electron`의 `mobility`가 `hole`의 `mobility`가 훨씬 빠르기 때문에, 
  `NMOS`의 `CHANNEL lenth`를 `hole`보다 조금 줄이거나, 조치를 해야될 필요가 있다.
  <br>(Ids= 1/2 un Cox W/L (Vgs - Vth)^2) (un= 전자이동도, Cox = 산화층 커패시턴스, W= channel 높이, L = channel 폭)

* L의 값을 임의로 조정하기엔 어렵기 때문에 W= 높이를 조정하는 것으로 해당 mobility 값을 조정한다.
               

# Dopament (gas or Ion)

![alt text](ionimplement-1.png)

* 이온 증착을 통해서 실제 `n-diffusion`을 형성하면 여러각도로 들어오는 전자에 의해서 설계했던거 보다 큰 `n-diffusion`을 형성하게 된다. 이에 채널 lenth가 작아짐에 따라 설계했던거 보다 더 높은 전류를 요구할 수도 있다.
<br>

# Design rules

![alt text](<simplified design rules-1.png>)

해당 그림은 pmos와 nmos 사이의 관계를 나타낸다.
주요 지켜야할 rule은
1. metal 사이의 거리기 적당한가.
2. diffusion 사이의 간격은 올바르게 유지되어 n-well이 겹치지 않았는가.
3. 등등


# Stick diagram 

![alt text](stickdiagram-1.png)

* 1. 출력에 기생 커패시턴스가 3개 물려있다.

* 2. 출력에 기생 커패시턴스 2개가 물려있다.
