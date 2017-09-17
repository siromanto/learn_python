remove_duplicates([1, 1, 2, 2]) should return [1, 2].


def remove_duplicates(elements):
  new_list = []
  for i in range(len(elements)):
    char = elements[i]
    if char not in new_list:
      new_list.append(char)
  return new_list