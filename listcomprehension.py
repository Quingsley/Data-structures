c = {"a": 10, "b": 1, "c": 22}
print(sorted([(v, k) for k, v in c.items()]))
#{ is same as
# list()
# for key, value in counts.items():
 #   lst.append(new_tup)
 #read on list comprehension
