# In a party of N people, only one person is known to everyone.
# Such a person may be present in the party, if yes, (s)he doesn’t
# know anyone in the party. We can only ask questions like “does A know B? “.
# Find the stranger (celebrity) in minimum number of questions.

# consider has_heard_of(a, b) given -> return True/False as in a has heard/hasn't heard of b


n = int(input())
stack = []
stack.append(int(input()))

for i in range(1, n):
	p1 = stack[len(stack) - 1]
	p2 = int(input())
	
	if has_heard_of(p1, p2):
		# p1 knows p2, so p1 is clearly not the star
		stack.pop()
		stack.append(p2)
	else:
		# p1 doesn't know p2, so p2 is clearly not the star
		# don't do anything

if len(stack) != 1:
	print('Celebrity is missing')
else:
	print(stack[0])

