from BasicFunction import get_edge_list ;

class TargetProvenance:

    def __init__(self, nodeId):
        self.nodeId = nodeId ;
        self.prolist = [] ;
        self.edgedict = {} ;

    def add_provenance(self, mystr):
        edgelist = get_edge_list( mystr ) ;
        for edge in edgelist:
            self.edgedict[edge] = True ;

        self.prolist.append( edgelist ) ;

    def if_connected(self, all_edge_value):
        for edgelist in self.prolist:
            res = True ;
            for temp in edgelist:
                if(all_edge_value[temp] == False):
                    res = False ;
                    break ;
                if(res == True): return True ;
        return False ;

def get_target_provenance(filename):
    target_dict = {} ;
    for line in open(filename).readlines():
        mylist = line.strip().split(",") ;
        targetId = mylist[-1] ;
        print targetId ;
        if(target_dict.has_key(targetId) == False):
            print "----new target----"
            target = TargetProvenance(targetId) ;
            target_dict[targetId] = target ;

        target = target_dict[targetId] ;
        target.add_provenance(line.strip());
    return target_dict ;

if __name__ == "__main__":
    filename = "data.txt"
    target_dict = get_target_provenance(filename) ;
    for t in target_dict.keys():
        print t ;
        print target_dict[t].prolist ;
        print target_dict[t].edgedict ;

    '''
    tProvenance = TargetProvenance('T1') ;
    s1 = "A,B,T1" ;
    s2 = "A,C,T1" ;
    tProvenance.add_provenance(s1) ;
    tProvenance.add_provenance(s2) ;

    print tProvenance.prolist ;
    print tProvenance.edgedict ;
    '''
