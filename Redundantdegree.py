from TargetProvenance import readProvenance ;
from BasicFunction import get_tuplelist_traces, get_edge_list, get_targets_karate ;

# raw method
def get_redundant_degree(mytrace, otherTargets):
    degree = 0 ;
    for target in otherTargets:
        flag = 0 ;
        for temp in target.prolist:
            mytraceset = set( get_edge_list(mytrace) ) ;
            tempset = set( get_edge_list(temp) ) ;
            if( mytraceset.isuperset(tempset) ):
                flag = 1 ;
                break ;
        degree = degree + flag ;
    return degree ;

def cal_outer_degree(myTarget, targetnodelist):
    targetset = set(targetnodelist) ;
    targetset.remove(myTarget.nodeId) ;
    #print myTarget.nodeId ;
    for trace in myTarget.tracelist:
        myset = set( trace.split(",")[:-1] ) ;
        #print "trace:", mytrace, myset ;
        intersec = myset.intersection(targetset) ;
        #print intersec ;
        myTarget.degreedict[trace] = len(intersec) ;

def cal_inner_degree(myTarget):
    allpaths = list(myTarget.tracelist) ;

    for path in allpaths:
        for key in allpaths:
            flag = True ;
            if( path != key ):
                pathset = set( get_edge_list(path) ) ;
                keyset =  set( get_edge_list(key) ) ;
                if( pathset.issubset(keyset) ):
                    #print "-----redundant trace-------"
                    myTarget.upsetdict[key] = 1 ;


# my method for speed up
def speed_redundant_degree(myTarget, targetnodelist):
    cal_outer_degree(myTarget, targetnodelist) ;
    cal_inner_degree(myTarget) ;

def cal_k_redundant(k):
    all_traces = [] ;
    num = 0 ;
    for target in targetlist:
        speed_redundant_degree(target, targetnodelist) ;
        for trace in target.tracelist:
            if( target.degreedict[trace] <= k and target.upsetdict.has_key(trace) is False):
                num = num + 1 ;
                all_traces.append(trace) ;
    [nouse, edgedict] = get_tuplelist_traces(all_traces) ;
    print "trace num:", num ;
    print "tuple num:", len(edgedict) ;
    for key in edgedict.keys():
        print key ;

filename = "karate_provenance.txt";
targetnodelist = get_targets_karate() ;
targetlist = readProvenance(filename, targetnodelist) ;
for k in range(5,6):
    print "k=", k, ;
    cal_k_redundant(k) ;
