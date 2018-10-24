def function1(n, filenames) :
  for filename in filenames :
    f = open(filename, "r", encoding="utf-8")
    for line in f :
      if len(line) > n :
         print (line)
         yield line

def function2(filenames) :
  for filename in filenames :
    f = open(filename, "r", encoding="utf-8")
    lineCount = 0
    for line in f :
      if line not in ['\n', '\r\n'] :
        lineCount+=1
            
        yield lineCount

def function3(filenames) :
  lineCount = 0
  for filename in filenames :
    f = open(filename, "r", enconding="utf-8")
    yield sum(1 for line in f)

def enumerate_(listToEnumerate) :
  for i in range(0, len(listToEnumerate)) :
    yield (i, listToEnumerate[i])

print (list(enumerate_(["a", "b", "c"])))


for i,c in enumerate_(["a", "b", "c"]):
  print (i, c)
