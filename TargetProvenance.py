from BasicFunction import get_edge_list, get_targets_karate ;

class TargetProvenance:
    def __init__(self, nodeId):
        self.nodeId = nodeId ;
        self.prolist = [] ;
        self.tracelist = [] ;

        self.edgedict = {} ;
        self.degreedict = {} ;
        self.upsetdict = {} ; # if a trace is upperset of another trace

    def add_provenance(self, mystr):
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
                self.add_provenance(line.strip());

    def if_connected(self, all_edge_value):
        for edgelist in self.prolist:
            res = True ;
            for temp in edgelist:
                if(all_edge_value[temp] == False):
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

    '''
    tProvenance = TargetProvenance('T1') ;
    s1 = "A,B,T1" ;
    s2 = "A,C,T1" ;
    tProvenance.add_provenance(s1) ;
    tProvenance.add_provenance(s2) ;

    print tProvenance.prolist ;
    print tProvenance.edgedict ;
    '''
