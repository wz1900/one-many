import networkx as nx ;
import numpy as np ;
import timeit
from ctypes import c_int
import random ;
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
        result_k_list = effect(term, targetlist, edge_value_dict.copy()) ;
        term_dict[term] = result_k_list ;
    return term_dict ;

def get_random_list(mylen, go_1=0.5):
    random_list = np.random.random(size=mylen) ;
    for i in range(mylen):
        if( random_list[i]>= go_1 ): random_list[i] = 0 ;
        else: random_list[i] = 1 ;
    #random_list = np.random.randint(2, size=len(tuplelist)) ;
    '''
    edge_value_dict = {} ;
    for i in range(len(tuplelist)):
        temp = random.random() ;
        if( temp >= go_1 ): edge_value_dict[tuplelist[i]] = False ;
        else: edge_value_dict[ tuplelist[i] ] = True ;
    '''
    return random_list ;

def run_mc(tuplelist, targetlist, mc_num):
    sum_term_dict = {} ;
    for term in tuplelist:
        sum_term_dict[term] = [0]*len(targetlist) ;

    #mc_num = mc_num/2 ;
    for i in range(mc_num):
        if(i%1000 ==0 ): print "--------mc_num:", i, "-------------"
        edge_value_dict = get_random_list(len(tuplelist), go_1=0.9) ;
        term_dict = run_once(tuplelist, targetlist, edge_value_dict) ;
        for term in tuplelist:
            temp = [ x + y for x, y in zip(term_dict[term], sum_term_dict[term]) ] ;
            sum_term_dict[term] = temp ;
        ''' 
        one_matrix = np.ones((len(random_list_1),), dtype=np.int) ;
        random_list_2 = np.subtract( one_matrix, random_list_1) ;
        term_dict = run_once(tuplelist, targetlist, random_list_2) ;
        for term in tuplelist:
            temp = [ x + y for x, y in zip(term_dict[term], sum_term_dict[term]) ] ;
            sum_term_dict[term] = temp ;
        '''
    return sum_term_dict ;

filename = "provenance_dataset/karate_provenance.txt";
targetnodelist = get_targets_karate() ;
targetlist = readProvenance(filename, targetnodelist) ;
tuplelist = get_tuple_list(targetlist) ;
print "tuple num:", len(tuplelist) ;
start = timeit.default_timer() ;
sum_term_dict = run_mc(tuplelist, targetlist, mc_num=100) ;
stop = timeit.default_timer() ;
print stop-start ;
for term in sum_term_dict.keys():
    #print term, " ".join(sum_term_dict[term]) ;
    print term, str(sum_term_dict[term]).strip('[]')
