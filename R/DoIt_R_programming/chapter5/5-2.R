# column name 변경하기
df_raw = data.frame(var1 = c(1, 2, 3),
                    var2 = c(2, 3, 2))
df_raw

#dplyr 설치하고 가져오기
install.packages('dplyr')
library(dplyr)

# 복사본 만들기. 파이썬과 차이가 나는 부분이다. 파이썬은 리스트를 변수에 넣으면 주소값이 입력되어 새로운 변수에 변형을 줄 경우 원본에도 영향을 끼친다

df_new = df_raw
df_new

# column 명 변경
df_new = rename(df_new, v2= var2) # var2라는 column을 v2로 변경경
df_new

# 연습문제 mpg 속 column명을 바꿔보자
mpg_new = mpg
mpg_new = rename(mpg_new, city=cty, highway=hwy)
head(mpg_new)

