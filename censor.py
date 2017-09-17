def censor(text, word):
  text_list = text.split(' ')
  for i in range(len(text_list)):
    if text_list[i] == word:
      text_list[i] = "*" * len(text_list[i])
    new_text = ' '.join(text_list)
  return new_text
  