
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}





# reo_id = []
# for user, num in ids.items():
#   number = num
#   for nn in number:
#      if nn not in reo_id:
#       reo_id.append(nn)
# print(reo_id)




result = []
for i in ids.values():

    result.extend(i)

result = list(set(result))
print(' ===> ', result)