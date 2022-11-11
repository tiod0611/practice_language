# 배열 만들기
var1 = c(1,2,3,4,5)
var2 = c(1:5) # 파이썬은 마지막 원소의 -1까지 였다면 R은 모두 포함이다.
var3 = seq(1, 5)
var4 = seq(1, 10, by = 2) # 1부터 10까지 만들고 2 간격씩 생성성

var1 + 1
var1 
var1 + var4

# 문자형 변수도 가능
str1 = 'A'
str2 = c('hello', 'world', '!')
#내장 함수 다뤄보기
mean(var1)
paste(str2, collapse=" ") # 파이썬의 join과 비슷 

# R package 이해하기~
# 설치는 한번만, 사용할 때는 반드시 로드! import 하는 작업과 같군
install.packages("ggplot2")
library(ggplot2)

x = c('a', 'b', 'c', 'd', 'a','a','e','d')
qplot(x)

# 내장 데이터로 연습해보기
mpg
qplot(data = mpg, x = hwy) 
# 변수 2개 사용하여 그래프
qplot(data = mpg, x = drv, y = hwy)
# 변수 2개를 사용한 선 그래프
qplot(data=mpg, x=drv, y=hwy, geom="line")
# 변수 2개를 사용해 박스 플롯
qplot(data=mpg, x=drv, y=hwy, geom='boxplot')
# 변수 2개와 박스플롯 그리고 색갈
qplot(data=mpg, x=drv, y=hwy, geom="boxplot", color=drv)


# 함수가 궁금할 땐!? 앞에 ?를 넣어보자
?ggplot

# 연습문제
# q1 시험 점수 변수 만들고 출력하기 
scores = c(80, 60, 70, 50, 90)
# q2 전체 평균 구하기
mean(scores)
# q3 평균을 변수에 담고 출력
meanResult = mean(scores)
meanResult
