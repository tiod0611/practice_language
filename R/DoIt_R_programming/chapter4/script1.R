english = c(90, 80, 60, 70)
english
math <- c(50, 60, 100, 20)

# DF 만들기
df_midterm <- data.frame(english, math)
df_midterm


# columns 추가
class = c(1, 1, 2, 2)
class
df_midterm = data.frame(english, math, class)
df_midterm

# 간단한 열 분석
mean(df_midterm$english)
mean(df_midterm$math)


# 연습문제 DF 만들어보기

product_info = data.frame(
  p_name = c('사과', '딸기', '수박'),
  price = c(1800, 1500, 3000),
  volume = c(24, 38, 13)
)
product_info
