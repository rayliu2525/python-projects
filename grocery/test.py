test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))

# using list comprehension
# to remove duplicated
# from list
res = []

x = [res.append(x) for x in test_list if x not in res]
print(x)