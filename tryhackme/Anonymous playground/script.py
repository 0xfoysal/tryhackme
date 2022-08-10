string = "hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def order(char):
    for i in range(len(alphabet)):
	if alphabet[i] == char:
		return i
	return -1

def sumup(a,b):
	s = (a+1+b+1)%52
	return alphabet[s-1]

output = ""
for i in range(0, len(string), 2):
    if string[i] == ":":
	output += ":"
    else:
	output += sumup(order(string[i]), order(string[i+1]))

print(output)