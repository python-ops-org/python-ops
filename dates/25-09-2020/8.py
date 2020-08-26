f1=open('f5',"r")
f2=open('f7',"w+")

i = 0
for fmr in f1:
    fmr=fmr.replace("\n","")
    f_id = i
    if i < 10:
        f_id = "0%s"%i
    new_name=""
    sliced = fmr.split("_")
    for q in sliced:
        if sliced.index(q) == 3:
            new_name=new_name+"_"+f_id
        else:
            new_name=new_name+"_"+q
    final_name = new_name[1:]
    print(final_name)
    f2.write("%s\n"%final_name)
    i=i+1
f2.close()
with open("f7","r") as f2_again:
    for line in f2_again:
        print(line)
