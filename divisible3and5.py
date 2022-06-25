# i = 0
# while i in range(21):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)
#     i += 1

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
    i += 1