input = 20


def find_prime_list_under_number(number):
    result = []
    for n in range(2,number+1):
      for i in result:
        if n%i==0:
          break
      else: 
        result.append(n)
    return result


result = find_prime_list_under_number(input)
print(result)