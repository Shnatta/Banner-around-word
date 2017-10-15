def banner(xy):
	x = ""
	for i in range(len(xy)+4):
		x+= "*"
	return x + "\n* " + xy + " * \n" + x

vy = input("Please enter a word you would've like to be bannered around # ")
print(banner(vy))