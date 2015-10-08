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
    filename = "data.txt" ;
    #target_dict = get_target_provenance(filename) ;
    #print target_dict ; 
