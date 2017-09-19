def purify(odd_list):
  new_list = []
  for i in range(len(odd_list)):
    char = odd_list[i]
    if not(char%2):
      new_list.append(char)
  return new_list


print purify([1,2,3])