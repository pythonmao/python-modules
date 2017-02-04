import zipfile

fp = zipfile.ZipFile("./zipfile.zip", "r")

for filename in fp.namelist():
    print filename
    file = fp.read(filename)
    print len(file)
