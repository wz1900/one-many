import networkx as nx ;
import numpy as np ;
import timeit
from ctypes import c_int
from BasicFunction import get_targets_karate, get_tuplelist, get_value ;
from TargetProvenance import get_tuple_list, get_connected_num, readProvenance ;

def effect(term, targetlist, edge_value_dict):
    edge_dict = edge_value_dict.copy() ;

    #------- set edge true ----------
    edge_dict[term] = True ;
    set_true_num = get_connected_num(targetlist, edge_dict) ;

    #------- set edge false ---------
    edge_dict[term] = False ;
    set_false_num = get_connected_num(targetlist, edge_dict) ;

    result_k_list = [] ;
    for k in range(1,len(targetlist)+1):
        flag = 0 ;
        if( set_true_num>=k and set_false_num<k ): flag = 1 ;
        result_k_list.append(flag) ;

    return result_k_list ;

def run_once(tuplelist, targetlist, random_list):
    edge_value_dict = {} ;
    for i in range(len(tuplelist)):
        if( random_list[i] == 0 ): edge_value_dict[tuplelist[i]] = False ;
        else: edge_value_dict[ tuplelist[i] ] = True ;

    term_dict = {} ;
    for term in tuplelist:
        result_k_list = effect(term, targetlist, edge_value_dict) ;
        term_dict[term] = result_k_list ;
    return term_dict ;

def run_mc(tuplelist, targetlist, mc_num):
    sum_term_dict = {} ;
    for term in tuplelist:
        sum_term_dict[term] = [0]*len(targetlist) ;

    for i in range(mc_num):
        if(i%100 ==0 ): print "--------mc_num:", i, "-------------"
        random_list_1 = np.random.randint(2, size=len(tuplelist)) ;
        term_dict = run_once(tuplelist, targetlist, random_list_1) ;
        for term in tuplelist:
            #print "term", term_dict[term] ;
            #print "sum_term", term, sum_term_dict[term] ;
            temp = [ x + y for x, y in zip(term_dict[term], sum_term_dict[term]) ] ;
            #print "added:", temp ;
            sum_term_dict[term] = temp ;
    return sum_term_dict ;

filename = "provenance_dataset/karate_provenance.txt";
targetnodelist = get_targets_karate() ;
targetlist = readProvenance(filename, targetnodelist) ;
tuplelist = get_tuple_list(targetlist) ;
print "tuple num:", len(tuplelist) ;
sum_term_dict = run_mc(tuplelist, targetlist, mc_num=100000) ;
for term in sum_term_dict.keys():
    #print term, " ".join(sum_term_dict[term]) ;
    print term, str(sum_term_dict[term]).strip('[]')
