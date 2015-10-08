from BasicFunction import get_edge_list ;

file_path = "karate_provenance.txt"# "4-1alk.txt" 
pathlist = [x.strip() for x in open(file_path).readlines()] ;

def build_path_dict(allpaths):
    pathdict = {} ;
    for path in allpaths:
        pathdict[path] = 1 ;

    return pathdict ;

def find_redudant(allpaths, pathdict):
    for path in allpaths:
        for key in pathdict.keys():
            flag = True ;
            if( path!=key ):
                pathset = set( get_edge_list(path) ) ;
                keyset =  set( get_edge_list(key) ) ;
                if( pathset.issubset(keyset) ):
                    print "-----redundant trace-------"
                    print path ;
                    print key ;
                    del pathdict[key] ;

    f = open("test-walk_checked_causality.txt", 'w')
    for path in pathdict.keys():
        f.write(path+"\n")  ;
    f.close() ;
    #for key in pathdict.keys():
    #    print key ;

    print len(pathdict) ;

if __name__ == "__main__":
    pathdict = build_path_dict(pathlist) ;
    find_redudant(pathlist, pathdict) ;
    #print path.strip() ;
