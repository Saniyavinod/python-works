placements={"django":2,"big data":8,"java":5 ,"testing":7}
def get_value(key):

    return placements.get(key)
srt=sorted(placements,key=get_value,reverse=True)
print(srt)