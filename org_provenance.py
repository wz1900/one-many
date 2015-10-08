start_node = "1"
end_list = ["29", "10", "4", "24", "27", "32", "2", "21", "16", "6"] ;

tracedict = {} ;
def get_trace(mylist, n):
    templist = mylist[0:n] ;
    trace = ",".join(templist) ;
    return trace ;

def get_provenance(line):
    line = line.strip() ;
    mylist = line.split(",") ;
    for i in range(len(mylist)):
        if( target_dict.has_key(mylist[i]) ):
            trace = ",".join(mylist[0:i+1]) ; 
            tracedict[ trace] = 1 ;

target_dict = {} ;
for item in end_list:
    target_dict[item] = True ;

filename = "karate_random.txt" ;
prolist =  open(filename).readlines() ;

num = 0 ;
for line in prolist:
    get_provenance(line) ;

for key in tracedict.keys():
    print key ;
    #num = num + 1 ;
    #if( num > 10 ): break ; 
    

