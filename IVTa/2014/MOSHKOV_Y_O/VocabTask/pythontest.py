
orig = open("eng.txt", 'r')
num = orig.readline()
d = {}
for line in orig:
	raw = line.strip().split(" - ")
	eng = raw[0]
	lat = raw[1].split(", ")
	for word in lat:
		if word in d:
			d[word].append(eng)
		else:
			d[word] = [eng]
orig.close()

new = open("lat.txt", 'w')
new.write(str(len(d)) + '\n')
for key in sorted(d):
	new.write(key + " - ")
	new.write(", ".join(d[key]) + '\n')
new.close()
input("Enter...")