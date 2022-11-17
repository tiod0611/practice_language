exam <- read.csv('../Data/csv_exam.csv')
exam
head(exam)
head(exam, 10)
tail(exam)
tail(exam, 10)

View(exam)

dim(exam)

# 속성 파악하기
str(exam)

# 데이터 요약. 기본적인 통계값을 제공한다
summary(exam)

# mpg 실습해보기

mpg = as.data.frame(ggplot2::mpg)
mpg

head(mpg)
View(mpg)
dim(mpg)
str(mpg)

summary(mpg)

?mpg