fopen = open("access.log","r")
fget = open("get.log","w")
fpost = open("post.log","w")
fput = open("put.log","w")
fdelete = open("delete.log","w")
for fpe in fopen:
  if "GET /" in fpe:
    fget.write(fpe)
  elif "POST /" in fpe:
    fpost.write(fpe)
  elif "PUT /" in fpe:
    fput.write(fpe)
  else:
    fdelete.write(fpe)

def topip():m
  mydict = dict()
  fopen = open("access.log","r")
    for fop in fopen:
      if "GET /" in fop or "POST /" in fop:
        ip = fop.split('-')[0]
          if ip not in mydict:
            mydict[ip] = 1
          else:
            mydict[ip] += 1
    sorted_x = sorted(mydict, key=mydict.get, reverse=True)[:20]
    return sorted_x


print(topip())