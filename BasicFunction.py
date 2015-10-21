#from TargetProvenance import TargetProvenance ;

'''
def get_target_provenance(filename):
    target_dict = {} ;
    for line in open(filename).readlines():
        mylist = line.strip().split(",") ;
        targetId = mylist[-1] ;
        if(target_dict.has_key(targetId) == False):
            targetPro = TargetProvenance(targetId) ;
            target_dict[targetPro] = True ;
        else:
            targetPro = target_dict[targetId] ;
        targetPro.add_provenance(line.strip());
    return target_dict ;
'''

def get_mc_result_list(mydict, targetlist, tuplelist):
    lines = [] ;
    for edge in tuplelist:
        line = [] ;
        line.append(edge) ;
        #print edge ,
        for i in range(1, 11):
            temp = int(len(targetlist)*i/10.0) ;
            mytuple = (edge, temp) ;
            #print round(mydict[mytuple],8),
            line.append(str(mydict[mytuple])) ;
        #print ""
        lines.append( " ".join(line) ) ;
    return lines ;

def get_random_p(num, k):
    p = 0.5 ;
    myvalue = float(k)/num ;
    mylist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] ;
    min_value = 10000000000 ;
    for term in mylist:
        temp = abs( myvalue - term ) ;
        if( temp < min_value ): 
            min_value = temp ;
            p = term ; 
    return p ;


def get_targets_karate():
    end_list = ["29", "10", "4", "24", "27", "32", "2", "21", "16", "6"] ;
    return end_list ;

def get_edge_list(line):
    mylist = line.strip().split(",") ;
    res = [] ;
    for i in range(len(mylist)-1):
        edge = mylist[i] + "-" + mylist[i+1] ;
        res.append(edge) ;

    return res ;


def get_tuplelist(file_name):
    tuplelist = [] ;
    mydict = {} ;
    lines = open(file_name).readlines() ;
    for line in lines:
        edgelist = get_edge_list(line) ;
        for edge in edgelist:
            mydict[edge] = True ;
        tuplelist.append( edgelist ) ;
    return [tuplelist, mydict] ;


def get_tuplelist_traces(lines):
    tuplelist = [] ;
    mydict = {} ;
    for line in lines:
        edgelist = get_edge_list(line) ;
        for edge in edgelist:
            mydict[edge] = True ;
        tuplelist.append( edgelist ) ;
    return [tuplelist, mydict] ;


def get_value(tuplelist, mydict, term, kType=1):
    for mylist in tuplelist:
        res = True ;
        for temp in mylist:
            if( mydict[temp] == False):
                res = False ;
                break;
        if (res == True): return True ;
        
    return False ;

if __name__ == "__main__":
    p = get_random_p(100, 99) ;
    print p ;
    filename = "data.txt" ;
    #target_dict = get_target_provenance(filename) ;
    #print target_dict ; 
