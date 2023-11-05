# 데이터 전처리
# dplyr은 전처리에 특화된 패키지다

library(dplyr)
exam = read.csv("../Data/csv_exam.csv")
exam

#filter()는 특정한 값을 가진 열만 가져온다

exam %>% filter(class == 1)
# %>% 파이프 연산자. 함수를 나열하는 식으로 사용함. ctrl + shift + M을 누르면 자동으로 쓰임

# 문제 class가 2인 데이터 뽑기
exam %>% filter(class==2)

# 특정 값이 아닌 데이터 가져오기
exam %>% filter(class != 1)

# 부등호도 가능하다.

# 여러 조건으로 사용하기
exam %>% filter(class==1 & math >= 50) # 여러 조건은 &(and), |(or) 연산자로 묶어서 쓴다.
exam %>% filter(class==1 | math >=50)

# %in% 기호 사용하기 포함된 데이터를 보여줌
exam %>% filter(class %in% c(1,2))

# 추출한 데이터를 새로운 변수에 저장하자
class1 = exam %>% filter(class==1)
class1

class2 = exam %>% filter(class==2)
class2
mean(class1$math)
mean(class2$math)


# 연습문제 
library(ggplot2)
mpg = as.data.frame(mpg)

#1 배기량이 4인 차와 5인차의 고속도로 연비 평균 확인
displ1 = mpg %>% filter(displ<=4)
displ2 = mpg %>% filter(displ>=5)

mean(displ1$hwy)
mean(displ2$hwy)

#2 자동차 제조사의 연비 확인
table(mpg$manufacturer)

audi = mpg %>% filter(manufacturer=="audi")
toyota = mpg %>% filter(manufacturer=="toyota")

mean(audi$cty)
mean(toyota$cty)

#3 3가지 브랜드의 고속도로 연비 평균을 알아보자

mean((mpg %>% filter(manufacturer %in% c("checrolet", "ford", "honda")))$hwy)

