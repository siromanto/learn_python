with open("text.txt", "w") as my_file:
  my_file.write("Success!")

if not my_file.closed:
  my_file.close()

print my_file.closed