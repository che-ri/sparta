input = "abacabade"


def find_not_repeating_character(string):
    for i, val1 in enumerate(string):
      accum = 0        
      for j, val2 in enumerate(string):
        if i!=j and val1==val2:
          accum+=1
      if accum<1: 
        return val1
result = find_not_repeating_character(input)
print(result)