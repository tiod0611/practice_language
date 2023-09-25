# 1. midwest를 df 형태로 불러온 뒤 데이터 특징 파악하기
midwest=as.data.frame(ggplot2::midwest)
head(midwest)
dim(midwest)
str(midwest)
summary(midwest)

# 2. poptotal 변수를 total로 popasian 변수를 asian으로 수정
## library(dplyr)
midwest_new = midwest
midwest_new = rename(midwest_new, total=poptotal, asian=popasian)
names((midwest_new))

# 3. total과 asian 변수를 이용해 '전체 인규 대비 아시아 인구 백분율' 변수를 만들고 히스토 그램으로 도시 분포를 살펴보자

# 3-1 새로운 변수만들기
midwest_new$per_asian = (midwest_new$asian/midwest_new$total) *100
midwest_new$per_asian
# 3-2 도시 분포 보기
table(midwest_new$state)
qplot(midwest_new$state)

##
hist(midwest_new$per_asian)

# 4. 아시아 인구 전체 평균을 구하고 이를 기준으로 파생변수 만들기
# 4-1 아시아 비율 전체 평균 구하기
mean_per_asian = mean(midwest_new$per_asian)
mean_per_asian
midwest_new$grade_per_asian = ifelse(midwest_new$per_asian > mean_per_asian, "large", 'small')
midwest_new$grade_per_asian

# 5. 4의 결과물을 히스토그램으로 보기
## library(ggplot2)
qplot(midwest_new$grade_per_asian)

