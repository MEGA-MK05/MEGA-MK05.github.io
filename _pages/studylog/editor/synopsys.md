---
title: "Synopsys 툴 사용법과 기본 개념"
permalink: /studylog/VLSI/0618synopsys/synopsys
toc: true
layout: page
---

# Synopsys 툴 소개

Synopsys는 반도체 설계 및 검증을 위한 EDA(Electronic Design Automation) 툴을 제공하는 선두 기업입니다. 주요 툴들과 그 용도를 살펴보겠습니다.

## 주요 툴 소개

### 1. Design Compiler (DC)
- RTL 합성 툴
- HDL(Verilog/VHDL)을 게이트 레벨 네트리스트로 변환
- 타이밍, 면적, 전력 최적화 수행

### 2. IC Compiler (ICC)
- 물리적 설계 자동화 툴
- 배치 및 배선(Place and Route)
- 클록 트리 합성(CTS)
- 전력 네트워크 설계

### 3. PrimeTime
- 정적 타이밍 분석 툴
- 셋업/홀드 타임 체크
- 크리티컬 패스 분석

### 4. VCS
- HDL 시뮬레이션 툴
- 기능 검증
- 테스트벤치 실행 및 디버깅

## 기본 설계 플로우

1. RTL 설계
   - HDL 코딩
   - 기능 검증 (VCS 사용)

2. 논리 합성
   - Design Compiler 사용
   - 타이밍 제약 설정
   - 최적화 수행

3. 물리적 설계
   - IC Compiler 사용
   - 플로어플래닝
   - 배치 및 배선
   - 타이밍 최적화

4. 검증
   - PrimeTime으로 타이밍 분석
   - DRC/LVS 체크
   - 포스트 레이아웃 시뮬레이션

## 주요 명령어

```tcl
# Design Compiler 명령어
read_verilog design.v
analyze -library WORK -format verilog design.v
elaborate design
check_design
compile_ultra

# IC Compiler 명령어
create_floorplan
place_opt
clock_opt
route_opt