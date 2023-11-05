# group_by()와 summarise()
# 집단별로 요약하기

library(dplyr)
exam = read.csv("../Data/csv_exam.csv")

exam %>% summarise(mean_math = mean(math))

# group_by 활용하기
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math), 
            mean_english = mean(english))  # class별로 그룹을 묶은 다음에 학 평균을 내라라


# 각종 통계량을 적용할 수도 있다.
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math),
            sum_math = sum(math),
            median_math = median(math),
            num_student = n()) # 데이터 행의 개수를 구함

exam %>% 
  group_by(class) %>% 
  summarise(n = n())

# 집단의 집단 나누기
mpg %>% 
  group_by(manufacturer, drv) %>% # 회사별, 구동방식 별
  summarise(mean_cty = mean(cty)) %>% 
  head(10)

# 연습문제: 회사별로 "suv" 자동차의 도시 및 고속도로 통합 연비 평균을 구해 내림차순 정렬하고 상위 5개 데이터만 보기
head(mpg)

mpg %>% 
  group_by(manufacturer) %>% 
  filter(class == "suv") %>% 
  mutate(total=(cty+hwy)/2) %>% # 새로운 변수 만들기
  summarise(mean_total = mean(total)) %>% # total의 전체 평균
  arrange(desc(mean_total)) %>% 
  head()

# 연습문제
# 1 어떤 차종의 연비가 좋은지 살펴보자. #2 정렬까지 해보자
# class별 cty 평균을 구하자

mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty=mean(cty)) %>% 
  arrange(desc(mean_cty))

#3 어떤 "회사"가 고속도로 연비가 높은지 보려고 한다. 가장 높은 3 회사를 알아보자
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mean_hwy=mean(hwy)) %>% 
  arrange(desc(mean_hwy)) %>% 
  head(3)

#4 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보자. 각 회사별 compact 차종 개수를 내림차순 정렬하자

mpg %>% 
  group_by(manufacturer) %>% 
  filter(class=="compact") %>% 
  summarise(num_compact = n()) %>% 
  arrange(desc(num_compact))
  
