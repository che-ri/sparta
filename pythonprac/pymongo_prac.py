from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스 영화평점과 같은 영화 찾기
metrics = db.movies.find_one({'title':'매트릭스'})
print(metrics['star'])
same_star = list(db.movies.find({'star': metrics['star']}))
for movie in same_star:
    if(movie): print(movie['title'])

# 매트릭스 평점 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})