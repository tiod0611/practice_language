# arrange()
# 데이터 정렬하기

# 오름차순
exam %>% arrange(math)

# 내림차순
exam %>% arrange(desc(math))
desc(exam$math) # desc은 음수로 바꿔주네

# 그룹으로 하기
exam %>% arrange(class, english)

# 연습문제
# audi 자동차 중 hwy 연비가 높은 5개의 데이터를 출력
mpg %>% filter(manufacturer=="audi") %>% 
  arrange(desc(hwy)) %>% 
  head(5)
