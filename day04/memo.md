# 오늘 배울 내용
- 센서퓨전 = 여러 센서를 합쳐 정확도를 높이는 것
- 위치 추정 알고리즘
- 베이즈 필터 = 예측 + 보정으로 위치를 업데이트
- 파티클
- 칼만

관련 논문

http://reports-archive.adm.cs.cmu.edu/anon/2000/CMU-CS-00-125.pdf
https://docs.ros.org/en/kinetic/api/robot_localization/html/_downloads/robot_localization_ias13_revised.pdf

| 항목 | Kalman | EKF | Particle |
|------|--------|-----|----------|
| 시스템 | 선형 | 비선형 | 제한 없음 |
| 표현 방식 | 하나의 평균 | 하나의 평균 | 여러 입자 |
| 정확도 | 낮음 (단순 환경) | 중간 | 높음 |
| 계산량 | 낮음 | 중간 | 높음 |
| 사용 예 | 단순 센서 | 일반 로봇 | AMCL |

##  베이즈 필터 (Bayes Filter)

###  정의
이전 상태와 현재 센서 정보를 이용해서  
현재 상태(위치)를 확률적으로 추정하는 방법
<br>현재 상태 = 이전 상태 × 센서 정보
---

