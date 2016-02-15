import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1][:-10]
    #print(record[0],record[1])
   # a=raw_input()
    mr.emit_intermediate(key, record[0])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(key)




# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
