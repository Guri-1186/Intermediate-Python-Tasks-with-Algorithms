my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}
result = []

for key in my_dict:
    if key in my_dict.values():
        result.append(key)

print(result)

 