array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #0~array의 길이만큼
  min_index = i #i는 바꿀 자리의 인덱스 값이 된다.
  for j in range(i+1, len(array)): #1부터 array의 길이만큼
    #i는 비교값A, j는 비교값B
    if array[min_index] > array[j]:
      min_index = j #결과적으로 j를 가장 작은 수로 만드는 것이다.
  array[i], array[min_index] = array[min_index], array[i] #파이썬은 이렇게 스와핑 문법이 가능하다!
  #그래서 제일 작은 값은 array[i]로 가고, array[i]의 값은 array[min_index]값으로 간다!

print(array)
