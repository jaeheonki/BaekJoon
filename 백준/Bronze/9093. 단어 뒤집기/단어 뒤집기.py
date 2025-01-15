n = int(input())
for _ in range(n):
  words = list(input().split())
  for word in words:
    reversed_word = ''
    for char in word:
      reversed_word = char + reversed_word
    print(reversed_word, end = ' ')
