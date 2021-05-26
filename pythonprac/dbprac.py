from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# update_one 배우기
db.users.delete_many({'name':'bobby'})
#name이 bobby인 데이터 모두를 삭제합니다.
