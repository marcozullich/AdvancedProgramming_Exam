import datetime  # use this module to deal with dates:  https://docs.python.org/3/library/datetime.html
import re

class PostcardList(object): 
    ########################
    # define attributes here
    #pass
    ########################
    
    
    def __init__(self):
        self._file = None
        self._postcards = []
        self._date = {}
        self._from = {}
        self._to = {}
        #pattern that an import line should match
            #date: year (at least one digit) - month (1 to 2 digits) -
            #      day (1 to 2 digits)
            #from: mixture of chars and dollar signs (e.g. $crooge)
            #to: as above
        self._linePattern = re.compile("date:(\d+-[\d+]{1,2}-[\d+]{1,2}); "+
                                  "from:([\w\$]+); to:([\w\$]+);")
        
    def _appendToDict(self, myDict, key, value):
        if key in myDict.keys():
            myDict[key].append(value)
        else:
            myDict[key] = [value]
    
    def readFile(self, fileToRead):
        if self._file != None:
            raise ImportError("PostcardList already associated with a file. " +
                              "Create a new one to proceed.")
        file = open(fileToRead, 'r')
        lineNumber = 0
        for line in file:
            lineMatch = self._linePattern.match(line)

            self._appendToDict(self._date, lineMatch.group(1), lineNumber)
            self._appendToDict(self._from, lineMatch.group(2), lineNumber)
            self._appendToDict(self._to, lineMatch.group(3), lineNumber)
            
            self._postcards.append(line)

            lineNumber += 1
            
    def getPostcardsBySender(self, sender):
        if sender in self._from:
            return [self._postcards[i] for i in self._from[sender]]
        else:
            return []
        
#a = PostcardList()
#a.readFile('exam_postcard_list0.txt')

#a._from['Sneezy']
#a._postcards
#a.getPostcardsBySender('Sneezy')
