import MapReduce
import sys
import collections

friends=collections.defaultdict(list)

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    #value = record[1]
    #a=raw_input()
    friends[record[0]].append(record[1])

    mr.emit_intermediate(record[0], record[1])
    #mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for person in list_of_values:
        if key not in friends[person]:
            mr.emit((key,person))
            mr.emit((person,key))
        
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
