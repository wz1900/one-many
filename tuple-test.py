from BasicFunction import getTargetListKarate, get_edge_list, get_tuplelist ;

targetlist = getTargetListKarate() ;

write_file = "data_file/why-1_checked_causality.txt" ;
[prolist, mydict] = get_tuplelist(write_file) ;

lenlist = [] ;
for pro in prolist:
    lenlist.append( len(pro) ) ;

print min(lenlist), max(lenlist) ;

print "edge num: ",len(mydict) ;
nodeset = set() ;
for key in mydict.keys():
    temp = key.split("-") ;
    nodeset.add(temp[0]) ;
    nodeset.add(temp[1]) ;
    print ",".join(temp) ;

print len(nodeset) ;
print set(targetlist) & nodeset ;
