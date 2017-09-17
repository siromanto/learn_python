def count(sequence, item):
  print 'sequence', sequence
  print 'item', item
  sum = 0
  for i in range(len(sequence)):
    print sequence[i]
    if sequence[i] == item:
    	sum += 1
  return sum
  
  