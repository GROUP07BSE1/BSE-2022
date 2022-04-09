letters = ['a', 'b', 'c', 'd', 'e']
def chop(list_name):
    del list_name[0]
    del list_name[-1]
    return None
chop(letters)

letters = ['a', 'b', 'c', 'd', 'e']
def middle(list_name):
    del list_name[0]
    del list_name[-1]
    return list_name
d = middle(letters)
print(d)