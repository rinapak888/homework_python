def gen_name(name, num):
    i= 1
    while i<num:
        yield name 
        i+=1
ranger= gen_name('Free', 0)
ranger2= gen_name('Maya', 40)
names= [x for x in ranger]
names2= [x for x in ranger2]
print(names)
print(names2)


