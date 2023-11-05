# 5-3 파생변수 만들기 (새로운 변수 만들기)

df = data.frame(var1 = c(4, 3, 8),
                var2 = c(2, 6, 1))
df

# 변수를 추가하자~
df$var_sum = df$var1 + df$var2
df

df$var_mean = (df$var_sum)/2
df

# 연습문제 mpg 통합 연비 변수 만들기

mpg$total = (mpg$cty+mpg$hwy)/2
head(mpg)

# 조건문 함수를 이용하기
# 고연비 자동차 여부 조사

# 1. 기준값 정하기
summary(mpg)
hist(mpg$total)

# 조건에 따른 값을 새로운 변수로 만들기
mpg$test = ifelse(mpg$total >= 20, "pass", "fail")
head(mpg$test) 
head(mpg)

# 빈도수 확인
table(mpg$test)
library(ggplot2)
qplot(mpg$test)


#연습문제 중첩 조건문을 활용하기
mpg$grade = ifelse(mpg$total >29, "A", 
                   ifelse(mpg$total >19, "B", "C"))
head(mpg)
table(mpg$grade)

qplot(mpg$grade)
