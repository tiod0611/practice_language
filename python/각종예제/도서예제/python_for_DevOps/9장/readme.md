9장 345쪽 코드 실습 중에 sklearn.datasets의 make_blobs 메서드가 작동하지 않는 문제 발생.

원인을 살펴보니 intel의 mkl-service 패키지를 요구하고 있음.
다시 mkl-service 패키지를 설치하려고 하니 openssl 설치를 요구 하고 있음.

그런데 openssl 설치가 상당히 복잡한 과정을 요구하고 이 과정 중에 있는 nasm이란 프로그램의 환경변수 등록 문제로 더 이상 진행이 안되고 있음. 여기서부터 해결하기로 함.

참고: https://iteastory.com/176