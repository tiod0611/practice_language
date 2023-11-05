'''
multi processing 테스트
'''

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time

def do_kmeans():
    '''생성된 데이터에 대한 KMeans 클러스터링'''

    X, _ = make_blobs(n_samples=100000, venters=3, n_features=10, random_state=0)
    kmeans = KMeans(n_clusters=3) # 3 군집으로 나눔
    t0 = time.time()
    kmeans.fit(X)

    print(f"KMeans cluster fit in  {time.time()-t0}") # 걸린 시간 출력

def main():
    """모두 실행"""

    count = 10
    t0 = time.time()
    for _ in range(count): # kmeans cluster를 10번 실행
        do_kmeans()
    
    print(f'Performed {count} KMeans in total time: {time.time()-t0}')

if __name__=='__main__':
    main()
    


