input_line = []

while True:
    try:
        line = input()
        input_line.append(line)
    except EOFError:
        break
# print(input_line)
# print(type(input_line))

# new_input_line = input_line.split(',')
# print(new_input_line)

par = [int(num) for num in input_line[0].split(',')]
score_num = [int(num) for num in input_line[1].split(',')]
# print(f"list1 : {par}")
# print(f"list2 : {score_num}")

s = {5: 'ホールインワン', 4: 'コンドル', 3: 'アルバトロス', 2: 'イーグル', 1: 'バーディ', 0: 'パー', -1: 'ボギー', -2: '2ボギー', -3: '3ボギー', -4: '4ボギー', -5:'5ボギー'}

score_str = []
for a, b in zip(par, score_num):
  # condor(par:5 and score:1)
  if a == 5 and b == 1:
    score_str.append(s[4])
  # hole in one (score:1)
  elif b == 1:
    score_str.append(s[5])
  # albatross(par:5 and score:2)
  elif a == 5 and b == 2:
    score_str.append(s[3])
  else:
    score_str.append(s[a - b])
# print(f"Golf score: {score_str}")
# print(type(score_str))
new_score_string = ", ".join(score_str)
print(new_score_string)
# for i in range(input_line):
#     s = input().rstrip().split(',')
#     print("hello = "+s[0]+" , world = "+s[1])
    # s.append(i)
# print(f"create list : {s[1]}"
