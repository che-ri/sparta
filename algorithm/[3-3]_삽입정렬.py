array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):#array[i]를 적절한 위치에 보내게 됩니다!
  print(f'i는 {i}입니다.')
  for j in range(i, 0, -1): 
    print(j)
    if array[j]<array[j-1]: #한 칸씩 왼쪽으로 이동
      print(f'j는 {array[j]} j-1는 {array[j-1]}')
      array[j], array[j-1] = array[j-1], array[j]
    else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)