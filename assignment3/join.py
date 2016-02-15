import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    #print(key,value)
    #a=raw_input()
    
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    orders=[]
    line_item=[]
    for v in list_of_values:
        if v[0]=='order':
            orders.append(v)
        else:
            line_item.append(v)
    for o in orders:
        for l in line_item:
            mr.emit((o+l))
            total.append(o+l)
        
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
