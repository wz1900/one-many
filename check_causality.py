from TargetProvenance import TargetProvenance, readProvenance ;
from BasicFunction import get_targets_karate, get_edge_list ;

def build_path_dict(targetlist):
    tracedict = {} ;
    for tp in targetlist:
        for trace in tp.tracelist:
            tracedict[trace] = 1 ;

    return tracedict ;

# meliou's method
def remove_redundant(pathdict):
    allpaths = list(pathdict.keys()) ;

    for path in allpaths:
        for key in pathdict.keys():
            flag = True ;
            if( path != key ):
                pathset = set( get_edge_list(path) ) ;
                keyset =  set( get_edge_list(key) ) ;
                if( pathset.issubset(keyset) ):
                    print "-----redundant trace-------"
                    del pathdict[key] ;
    return pathdict ;


filename = "karate_provenance.txt";
targetnodelist = get_targets_karate() ;
targetlist = readProvenance(filename, targetnodelist) ;

tracedict = build_path_dict(targetlist) ;

usefuldict = remove_redundant(tracedict) ;
print "trace num:", len( usefuldict.keys() ) ;
