import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
address = urllib.request.urlopen(url)
data = address.read()

total = 0

while True:
	if len(url)<1:
		break

	print("Retrieving: ", address)
	print("Retrieved ", len(data), "characters")

	info = json.loads(data)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
		# print("Sum: ", total)
	print("Final sum: ", total)
	break
