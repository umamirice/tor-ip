#!/usr/bin/python3
import argparse, os, time, sys, math
parser = argparse.ArgumentParser()

parser.add_argument('-t', '--time', help='Time (in seconds between IP changes)', default=10, type=int)
parser.add_argument('-c', '--count', help='Number of changes enter 0 to change until manually stopped', default=0, type=int)
parser.add_argument('-v', '--verbose', help='When used shows count every change', action='count', default=0)
args = parser.parse_args()

if args.time == 0:
	print(f'I don\'t think it\'ll work with time {args.time}')
	exit()
if args.count > 0:
        i=0
elif args.count < 0:
        print('Bro check -h option')
        exit()

if len(sys.argv) == 1:
	print(f'Running change every {args.time} and by default until killed')
	time.sleep(5)
else:
	print(f'Running change every {args.time} seconds') 
	time.sleep(3)


os.system('clear')

while True:
	
	if int(args.verbose) > 0:
                print(f'{i}. Changing...')

	os.system('killall -HUP tor')
	time.sleep(abs(args.time))
	
	if args.count != 0:
		i+=1
		if i == args.count:
			print('Done!')
			exit()
			
