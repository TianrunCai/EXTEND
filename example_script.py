import string,os
from extend import cleanreport,report_processor

def test():
    EXTEND_HOME=os.environ['EXTEND_HOME']
    path = os.path.join(EXTEND_HOME,'test_data.txt')
    def filter_content(data):
        printable = set(string.printable)
        return filter(lambda x: x in printable, data)
        
    
    def readstring_txt(path):
        file2=open(r'%s' %path,'r')
        data = file2.read()
        data = filter_content(data)
        file2.close()
        return data    
        
    report = readstring_txt(path)
    report_by_list=cleanreport.tokenized(report)
    itemlist = ['EF','HBA1C','Crn','VS']
    
    res= report_processor.process(report_by_list,itemlist)
    
    print res
    
test()