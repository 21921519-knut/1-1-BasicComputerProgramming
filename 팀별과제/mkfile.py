import pickle
import random

fd = open('data.dat','wb')

for i in range(0,1000,1):
    pickle.dump(random.randint(0,101), fd )

fd.close()

print('데이터 파일 생성 완료')

