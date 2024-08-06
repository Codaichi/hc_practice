input_line = []

while True:
    try:
        line = input()
        input_line.append(line)
    except EOFError:
        break


par = [int(num) for num in input_line[0].split(',')]
score_num = [int(num) for num in input_line[1].split(',')]

s = {4: 'コンドル', 3: 'アルバトロス', 2: 'イーグル', 1: 'バーディ', 0: 'パー', -1: 'ボギー'}

score_str = []
for a, b in zip(par, score_num):
  # hole in one (score:1)
  if a != 5 and b == 1:
    score_str.append('ホールインワン')
  # over double bogey
  elif a - b <= -2:
     score_str.append(f"{-(a-b)}ボギー")
  else:
    score_str.append(s[a - b])

new_score_string = ", ".join(score_str)
print(new_score_string)

