import string, random, urllib, os, thread, array, sys

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python " + sys.argv[0] + " (Number of threads)")
threadAmount = int(sys.argv[1])

print ("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\nThis script is for educational purposes only! Use on your own responsibility!\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
raw_input("Press ENTER if you have read and accept that you are fully responsible for using this script!\n")

temp = 0
#while temp < 10:

noneWorking = [0, 503, 4939, 4940, 4941, 12003, 5556, 5082]

def scrapePictures():
	while True:
	#	N = int(''.join(random.choice('1' + '2') for _ in range(1)))
		amount = int(''.join(random.choice('5' + '6') for _ in range(1)))
		if amount == 6:
	#		N = int(''.join(random.choice('3') for _ in range(1)))
			N = 3
			#name = str(len([name for name in os.listdir('.') if os.path.isfile(name)]) - 1)

			###Generate the random url###
			picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(N)))
			picture2 = str(''.join(random.choice(string.digits + string.lowercase) for _ in range(N)))

			# printsc = "http://img.prntscr.com/img?url=http://i.imgur.com/" + "" + str(picture) + str(picture2) + ".jpg"
				# Trying to improve.
			name = picture + picture2

			printsc = "http://i.imgur.com/" + "" + str(picture) + str(picture2) + ".jpg"
			urllib.urlretrieve(""+ printsc, str(name) + ".jpg")
			file = os.path.getsize(str(name)+ ".jpg")

			# print printsc
				# original print file. Currently in maintance mode.
			# print str(file) + " file" #Used to DEBUG and find the none working pictures
			if file in noneWorking:
				print "[-] Invalid: " + picture + picture2
				os.remove(name + ".jpg")
			else:
				print "[+] Valid: " + printsc
			#temp += 1


		if amount == 5:
			N = 5
	#		N = int(''.join(random.choice('3') for _ in range(1)))
	#		N2 = int(''.join(random.choice('2') for _ in range(1)))
			#name = str(len([name for name in os.listdir('.') if os.path.isfile(name)]) - 1)
			picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(N)))
	#		picture2 = str(''.join(random.choice(string.digits + string.lowercase) for _ in range(N2)))
			# printsc = "http://img.prntscr.com/img?url=http://i.imgur.com/" + "" + str(picture) + ".jpg"
				# Trying to improve.
			printsc = "http://i.imgur.com/" + "" + str(picture) + ".jpg"
	#		printsc = "http://img.prntscr.com/img?url=http://i.imgur.com/" + "" + str(picture) + str(picture2) + ".jpg" #Porsiacaso necesito dividr 3 mixed y luego 2 numeros y minusculas
			name = picture
			urllib.urlretrieve(""+ printsc, str(name) + ".jpg")
			file = os.path.getsize(str(name)+ ".jpg")
			#print printsc
			# print str(file) + " file" #Used to DEBUG and find the none working pictures
			if file in noneWorking:
				print "[-] Invalid: " + picture
				os.remove(name + ".jpg")
			else:
				print "[+] Valid: " + printsc
			#temp += 1

tempVar2 = 1
#threadAmount = sys.argv[2]
while (tempVar2 <= threadAmount):
	try:
		print ("Starting thread #" + str(tempVar2))
		thread.start_new_thread(scrapePictures, ())
		tempVar2 += 1
	except:
		print "Error initializing thread...."

#Make threads never stop
while (True):
	temp = 1+1
