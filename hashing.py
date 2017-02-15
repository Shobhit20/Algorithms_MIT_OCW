
class HashTable:

    hashTable    = []
 
    def __init__(self, size):
        self.tableSize = size
        self.hashTable = [[] for i in range(size)]
 
         
    def hashing(self,key):
        hash = key
        return hash%self.tableSize
 
    def insert(self,item):
        hash = self.hashing(item)
        # print(hash)
        for i,j in enumerate(self.hashTable[hash]):
            if j == item:
                del self.hashTable[hash][i]
        self.hashTable[hash].append(item)

 
    def delete(self,key):
        print ("Deleting item with key " , key )
        hash = self.hashing(key)
        for i,j in enumerate(self.hashTable[hash]):
            if j== key:
                del self.hashTable[hash][i]
                return
        print (" Entry not available in the table")            
             
    def printtable(self):
        print ( "-------------------Hash Table------------------" )
        for i in range(self.tableSize):
            print ( " [" + str(i) + "]" ,end=" ")
            for j in range(len(self.hashTable[i])):
                print("->", end=" ")
                print(self.hashTable[i][j],end=" ")
            print()
 
 
if __name__ == "__main__":
    hs = HashTable(10)
 
    item = 1
    hs.insert(item)
 
    item = 2
    hs.insert(item)
 
    item = 3
    hs.insert(item)
    item=11
    hs.insert(item)
    hs.delete(1)
    hs.printtable()