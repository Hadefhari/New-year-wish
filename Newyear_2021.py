import time
from random import randint
import os

start=5

for i in range(1,45):
	print('')

s=' '

for i in range(1,1000):
	count = randint(1,100)
	while(count>0):
		s+=' '
		count-=1

	if(i % 10 == 0):
		print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
		print("<     					   >")
		print("<   'Happy New Year 2021'   >")
		print("<                           >")
		print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
		
		
	else:
		print(s + '*')

	s = ''
	time.sleep(0.3)