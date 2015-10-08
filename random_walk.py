import sys   
sys.setrecursionlimit(1000000);
import matplotlib.pyplot as plt ;
import networkx as nx;
import numpy as np ;
import random 
from BasicFunction import get_edge_list, get_tuplelist ;

degree_dict = {} ;
step = 0 ;
maxSteps = 0 ;
path = [] ;
provenance_dict = {} ;

def initStep():
    global step, maxSteps, path;
    step = 0 ;
    maxSteps = 12 ;
    path = [] ;

def walk(G, start):
    global step, maxSteps, degree_dict, path;
    
    #print type(nx.all_neighbors(G, start)) ; 

    node_dict = {} ;
    for node in nx.all_neighbors(G, start):
        #degree = str(G.degree(node)) ;
        node_dict[str(node)] = 1 ;

    step = step + 1 ;
    #if( step >= maxSteps or start == end_node ): return ;
    if( step >= maxSteps ):
        provenance_dict[",".join(path)] = 1 ;
        return ;

    stop_walk_pro = np.random.random_sample() ;
    if( stop_walk_pro <= 0.1 ): 
        walk(G, start) ; # it has the 10% rate to stop 
    else: 
        node = random.choice(node_dict.keys()) ;    
        #node = select_random(node_dict, 1)[0] ;
        path.append(node) ;
        #print "add edge %s %s" % (start, node) ;
        walk(G, node) ; 
    

def run_once(G, start_node):
    global provenance_dict ;
    print "-------------start walk------------"
    for i in range(200):
        if(i%100 == 0): print "-----walk %d ----"%i
        initStep() ;
        path.append(start_node) ;
        walk(G, start_node) ;


print "------------reading graph-----------"
file_name = "/home/pear/one_multi_pro_ranking/dataset/karate.txt" ;
G = nx.read_edgelist(file_name) ;
start_node = "1"
end_list = ["29", "10", "4", "24", "27", "32", "2", "21", "16", "6"] ;
    
run_once(G, start_node) ;

write_file = "test-walk.txt" ;
f = open(write_file, 'w') ;
for key in provenance_dict:
    print >>f, key ;
f.close() ;

[nouse, mydict] = get_tuplelist(write_file) ;
print "edge num: ",len(mydict) ;
