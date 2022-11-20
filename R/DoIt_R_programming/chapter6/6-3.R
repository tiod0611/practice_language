# select()
# 필요한 변수만 사용하기

exam %>% select(math)
exam %>% select(math, english)
exam %>% select(c("math", "english"))

# 변수 제외하기
exam %>% select(-math)

# dplyr과 조합하여 사용하기
exam %>% filter(class==1) %>% 
  select(math) %>% 
  table %>% 
  mean
