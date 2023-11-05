install.packages("readxl")
library(readxl)

df_exam = read_excel("../Data/excel_exam.xlsx")
df_exam

#간단한 분석
mean(df_exam$math)
mean(df_exam$english)
mean(df_exam$science)

# 만약 첫번째 행이 columns 명이 아닌 경우
df_exam_novar = read_excel("../Data/excel_exam_novar.xlsx")
df_exam_novar

df_exam_novar_temp_col = read_excel("../Data/excel_exam_novar.xlsx", col_names=F)
df_exam_novar_temp_col

# 엑셀의 특정 sheet가져오기 

df_exam_sheet = read_excel("../Data/excel_exam_sheet.xlsx", sheet=3)
df_exam_sheet

# csv 다루기
df_csv_exam = read.csv("../Data/csv_exam.csv")
df_csv_exam

# csv 저장하기
df_midterm
write.csv(df_midterm, file="df_midterm.csv")

# R 전용 파일로 저장하기
save(df_midterm, file="df_midterm.rda")

# df 데이터 삭제하기

rm(df_midterm)
rm

# df 불러오기
load("df_midterm.rda")
df_midterm # 변수명까지 그대로 저장이 되어 있네

