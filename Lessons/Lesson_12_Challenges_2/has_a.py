def in_function(l):
	def contains(e):
		if e in l:
			return True
		else:
			return False
	return contains

def contains(self,e):
    return e in self

class mylist(list):
	pass


a = mylist((1,2,3))
# a.has_a = in_function(a)
a.has_a = contains
# mylist.has_a = in_function

print(a.has_a(a,2))
print(a.has_a(a,4))
