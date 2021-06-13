# -*- coding: utf-8 -*-
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    enumList = list(enumerate(string)) #index가 포함된 list를 생성한다.
    accumList = []; #초깃값 생성
    accum = 0; #초깃값 생성

    for i in enumList:
      if(not i[1].isalpha()):
        continue;
      for j in enumList:
        if(i[0]!=j[0] and i[1]==j[1]):
          accum+=1
      accumList.insert(0,(i[1],accum))
      accum = 0
    
    accumList=set(accumList)
    default = 0;
    result = ""

    for i in accumList:
        if(i[1]>default):
          default = i[1]
          result = i[0]

    return result 

result = find_max_occurred_alphabet(input)
print(result)