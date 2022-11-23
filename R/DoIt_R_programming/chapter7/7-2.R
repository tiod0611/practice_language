# 이상치 정제하기
outlier = data.frame(sex = c(1,2,1,3,2,1),
                     score = c(5,3,4,1,2,6))

table(outlier$sex)
table(outlier$score)

# 이상치를 NA로 치환하기
outlier$sex = ifelse(outlier$sex == 3, NA, outlier$sex)
outlier

outlier$score = ifelse(outlier$score > 5, NA, outlier$score)
outlier

# 결측치 처리하기
library(dplyr)
outlier %>% 
  filter(!is.na(sex) & !is.na(score)) %>% 
  group_by(sex) %>% 
  summarise(mean_score = mean(score))

# boxplot을 이용해 극단값 확인하기

mpg = as.data.frame(ggplot2::mpg)

boxplot(mpg$hwy)

boxplot(mpg$hwy)$stats # 박스의 경계값들을 보여줌


# 결측 처리하기
mpg$hwy = ifelse(mpg$hwy < 12 | mpg$hwy >37, NA, mpg$hwy)
table(is.na(mpg$hwy))

mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm=T))

# 연습문제
