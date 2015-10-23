import numpy as np ;
import timeit
import random ;
from BasicFunction import get_random_p, get_targets_karate, get_mc_result_list ;
from TargetProvenance import get_tuple_list, get_connected_num, readProvenance ;

def effect(targetlist, edge_value_dict):
    connect_num = get_connected_num(targetlist, edge_value_dict) ;
    res_k_list = [] ;
    # calculate 10% ---- 100%
    for k in range(1, 11):
        temp = int(len(targetlist)*k/10.0) ;
        if( connect_num>= temp ): res_k_list.append(True) ;
        else: res_k_list.append(False) ;
    return res_k_list ;

def assign_edge_value(tuplelist, go_1=0.5):
    edge_value_dict = {} ;
    mylist = [] ;
    for i in range(len(tuplelist)):
        temp = random.random() ;
        if( temp >= go_1 ): edge_value_dict[tuplelist[i]] = False ;
        else: edge_value_dict[ tuplelist[i] ] = True ;
    return edge_value_dict ;

def assign_edge_value_opposite(edge_value_dict):
    res_dict = {} ;
    for key in edge_value_dict.keys():
        if( edge_value_dict[key] == True ): res_dict[key]=False ;
        else: res_dict[key]=True ;
    return res_dict ;

def run_mc(targetlist, mc_num, k):
    target_num = len(targetlist) ;
    tuplelist = get_tuple_list(targetlist) ;
    #print "tuple num:", len(tuplelist) ;
    go_1 = 0.5 # get_random_p(target_num, k) ;
    #print "p is: ", go_1 ;

    tuple_dict_true = {} ;
    flag_dict_true = {} ;
    flag_dict_false = {} ;
    for key in tuplelist:
        tuple_dict_true[key] = 0 ; 
        for i in range(1, 11):
            temp = int(target_num*i/10.0) ;
            mytuple = (key, temp) ;
            flag_dict_true[mytuple] = 0 ;
            flag_dict_false[mytuple] = 0 ;

    for t in range(mc_num):
        #if(t%1000 ==0 ): print "--------mc_num:", t, "-------------"
        edge_value_dict = assign_edge_value(tuplelist, go_1) ;
        res_effect_list = effect(targetlist, edge_value_dict) ;
        for edge in edge_value_dict.keys():
            if( edge_value_dict[edge] == True ): tuple_dict_true[edge] += 1 ;
            for i in range(1, 11):
                temp = int(target_num*i/10.0) ;
                mytuple = (edge, temp) ;
                if( res_effect_list[i-1] == True ):
                    if( edge_value_dict[edge] == True ): flag_dict_true[mytuple] += 1 ;
                    else: flag_dict_false[mytuple] += 1 ;

        edge_value_dict = assign_edge_value_opposite(edge_value_dict.copy()) ;
        res_effect_list = effect(targetlist, edge_value_dict) ;
        for edge in edge_value_dict.keys():
            if( edge_value_dict[edge] == True ): tuple_dict_true[edge] += 1 ;
            for i in range(1, 11):
                temp = int(target_num*i/10.0) ;
                mytuple = (edge, temp) ;
                if( res_effect_list[i-1] == True ):
                    if( edge_value_dict[edge] == True ): flag_dict_true[mytuple] += 1 ;
                    else: flag_dict_false[mytuple] += 1 ;
    mc_num = mc_num * 2 ;    
    res_dict = {} ;
    for edge in tuplelist:
        for i in range(1, 11):
            temp = int(target_num*i/10.0) ;
            mytuple = (edge, temp) ;
            res_dict[mytuple] = flag_dict_true[mytuple]/float(tuple_dict_true[edge]) - flag_dict_false[mytuple]/(mc_num-float(tuple_dict_true[edge])) ;

    return res_dict ;

if __name__ == "__main__":
    filename = "provenance_dataset/karate_provenance.txt";
    targetnodelist = get_targets_karate() ;
    targetlist = readProvenance(filename, targetnodelist) ;

    start = timeit.default_timer() ;
    res_dict = run_mc(targetlist, mc_num=100, k=5) ;
    stop = timeit.default_timer() ;
    print stop-start ;

    lines = get_mc_result_list(res_dict, targetlist, get_tuple_list(targetlist)) ; 
    for line in lines:
        print line ;
