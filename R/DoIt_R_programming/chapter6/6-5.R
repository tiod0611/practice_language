# mutate()
# 파생변수 추가하기

exam %>% mutate(total = math+english+science)

# 여러개 만들기
exam %>% mutate(total = math+english+science,
                mean = (math+english+science)/3)

# ifelse 사용하여 특정 값 넣기
exam %>% mutate(test = ifelse(math>70, "pass", "fail"))

# 파생변수를 추가한 후 dplyr 함수 사용
exam %>% mutate(total = math+english+science) %>% 
  arrange(desc(total))
