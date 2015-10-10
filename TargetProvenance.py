from BasicFunction import get_edge_list, get_targets_karate ;

class TargetProvenance:
    def __init__(self, nodeId):
        self.nodeId = nodeId ;
        self.prolist = [] ;
        self.tracelist = [] ;

        self.edgedict = {} ;
        self.degreedict = {} ;
        self.upsetdict = {} ; # if a trace is upperset of another trace

    def _add_provenance(self, mystr):
        edgelist = get_edge_list( mystr ) ;
        for edge in edgelist:
            self.edgedict[edge] = True ;

        self.prolist.append( edgelist ) ;
        self.tracelist.append( mystr ) ;

    def read_provenance(self, lines):
        for line in lines:
            mylist = line.strip().split(",") ;
            targetId = mylist[-1] ;
            if(self.nodeId == targetId):
                self._add_provenance(line.strip());

    def if_connected(self, edge_value_dict):
        for edgelist in self.prolist:
            res = True ;
            for temp in edgelist:
                if(edge_value_dict[temp] == False):
                    res = False ;
                    break ;
            if(res == True): return True ;
        return False ;

def readProvenance(profilename, targetnodelist):
    prolist = open(profilename).readlines() ;
    targetProlist = [] ;
    for target in targetnodelist:
        targetPro = TargetProvenance(target) ;
        targetPro.read_provenance(prolist) ;
        #print targetPro.prolist ;
        #print targetPro.edgedict ;
        targetProlist.append(targetPro) ; 
    return targetProlist ;

def get_connected_num(targetlist, edge_dict):
    num = 0 ;
    for target in targetlist:
        if( target.if_connected(edge_dict) == True ): num = num + 1 ;
    return num ;

def get_tuple_list(targetlist):
    res = [] ;
    for target in targetlist:
        for edge in target.edgedict.keys(): res.append(edge) ;
    return list(set(res)) ;

if __name__ == "__main__":
    filename = "karate_provenance.txt"
    prolist = open(filename).readlines() ;
    targetlist = get_targets_karate() ;
    for target in targetlist:
        targetPro = TargetProvenance(target) ;
        targetPro.read_provenance(prolist) ;
        print targetPro.prolist ;
        print targetPro.edgedict ;
        print "------------ next target --------------" ;

