# 데이터 합치기

# 가로로 합치기
# left_join()
test1 = data.frame(id = c(1,2,3,4,5), # 중간고사 데이터
                   midterm = c(70,72, 80,60,86))

test2 = data.frame(id = c(1,2,3,4,5), # 기말고사 데이터
                   final = c(90, 90, 70,80,88))

total = left_join(test1, test2, by="id") # id를 기준으로 데이터 합치기. index가 같아줘야겠지? by를 안하면 알아서 같은 index로 되나보다
total

# 다른 데이터를 활용해 변수 추가

name = data.frame(class=c(1,2,3,4,5),
                  teacher=c('kim', 'lee','kim', 'park','choi'))

exam_new = left_join(exam, name, by='class')
exam_new

# 세로로합치기
# bind_rows

group_a = data.frame(id=c(1,2,3,4,5),
                     test=c(60, 40, 60,70,60))
group_b = data.frame(id=c(6,7,8,9,10),
                     test=c(89,56,75,85,67))

group_all = bind_rows(group_a, group_b) # columns를 기준으로 데이터를 합침. 칼럼이 다르다면?
group_all

bind_rows(group_all, name) # 새로운 칼럼이 추가되고 없는 행에는 NA가 들어간다. 오류는 없다

# 연습문제

fuel = data.frame(fl = c("c", "d","e","p","r"),
                         price_fl=c(2.35, 2.38, 2.11, 2.76, 2.22),
                         stringsAsFactors=F)
fuel

# 1 mpg의 연료 종류를 나타내는 f1 변수에는 가격이 없음 가격 변수를 추가해보자.
head(mpg)
mpg_new = left_join(mpg, fuel, by="fl")
head(mpg_new)

# 2 변수가 잘 추가되었나 확인을 위해 "model", "fl", "price_fl"을 select를 활용해 앞의 5행을 출력해보자
mpg_new %>% 
select(model, fl, price_fl) %>% 
  head(5)
