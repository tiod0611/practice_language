# 결측치 정제하기

df = data.frame(sex = c("M", "F", NA, "M", "F"),
                score = c(5, 4, 3, 4, NA))
df

# 결측치 확인 
# is.na()

is.na(df)
table(is.na(df))

table(is.na(df$sex))
table(is.na(df$score))

# 결측치 제거하기
# is.na()에 filter()를 적용하면 결측치 행을 제거할 수 있음

library(dplyr)
df %>% filter(is.na(score)) # score에 NA인 행을 출력함

# 결측치가 없는 데이터만 살펴보기
df %>% filter(!is.na(score)) # score에 결측치가 없는 데이터를 보여줌. 다른 열에는 NA가 있을 수 있다

# 결측치를 없엔 후 정제된 데이터를 변수에 저장하기
df_nomiss = df %>% filter(
  !is.na(score) & !is.na(sex)
)
df_nomiss  # 결과를 보면 결측치가 보함된 행들은 모두 삭제제거 됨.
# 하지만 이런 방식은 변수가 많은 데이터에 적용하려고 하면 번거롭다. 
# 당연히 한번에 처리하는 방법이 있다.
# na.omit()

df_nomiss2 = na.omit(df)
df_nomiss2

# 그런데 이 방법은 주의해야 한다. 결측치가 있는 행을 무조건 제거하는 것은 데이터 손실을 유발할 수 있으므로 적절한 EDA를 통해 꼭 필요없는 데이터를 삭제하는 쪽이 옳다



# 통계 함수에서 결측치를 무시하고 존재하는 데이터로 측정하기
# na.rm 파라미터

mean(df$score) #결과 NA
mean(df$score, na.rm=T) # 결과 4

# summariase() 같은 함수에도 na.rm 파라미터를 적용할 수 있다
 
exam = read.csv("../Data/csv_exam.csv")
exam
exam[c(3, 8, 15), 'math'] = NA # 3, 8, 15 행에 NA 값을 입력. []는 index에 접근하는 방법이다.
exam

exam %>% summarise(mean_math = mean(math)) #결과 NA
exam %>% summarise(mean_math = mean(math, na.rm=T)) # 결과 55.23..

# 결측치 대체하기
# 결측치 행을 무작정 제거하지 않고 결측 데이터를 평균이나 최빈값 등으로 치환해서 분석할 수 있다.

exam$math = ifelse(is.na(exam$math), mean(exam$math, na.rm=T), exam$math)
table(is.na(exam$math))


# 연습 문제
# mpg 데이터에 결측치를 만들고 이를 해결해보자
library(ggplot2)
mpg = as.data.frame(ggplot2::mpg)
mpg[c(67, 124, 23, 87, 48, 5), "hwy"] = NA

table(is.na(mpg))

# 1 drv와 hwy에 결측치 개수 확인하기
table(is.na(mpg$drv))
table(is.na(mpg$hwy))

mpg %>% 
  filter(!is.na(mpg$hwy)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy=mean(hwy)) %>% 
  arrange(desc(mean_hwy))
