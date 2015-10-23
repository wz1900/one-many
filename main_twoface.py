import timeit
import numpy as np
#from random_causal_test import run_mc ;
from random_causal_test_twoface import run_mc ;
from TargetProvenance import get_tuple_list, readProvenance ;
from BasicFunction import get_targets_karate, get_mc_result_list ;
from main_ndcg import evaluate ;

def causal_test(pro_file_name, mc_num, k):
    targetnodelist = get_targets_karate() ;
    targetlist = readProvenance(filename, targetnodelist) ;
    res_dict = run_mc(targetlist, mc_num, k) ;
    return get_mc_result_list(res_dict, targetlist, get_tuple_list(targetlist)) ; 

def test_converge(mc_num_list, profil, test_time):
    for mc_num in mc_num_list:
        reslist = [] ;
        for t in range(test_time):
            print "-------------mc num is:", mc_num , "----------------";
            line = [] ;
            lines = causal_test(filename, mc_num, 0) ;
            for k in range(1,11):
                print k, ;
                #lines = causal_test(filename, mc_num, k) ;
                final_mc_file = "converge_file_better/res_1000000.txt" ;
                ground_truth_lines = [x.strip() for x in open(final_mc_file).readlines()] ;
                res = evaluate(ground_truth_lines, lines, k, perm_num=10000) ;
                print res[0] ;
                line.append(float(res[0])) ;
            #print line ;
            reslist.append(line) ;
        print [float(sum(col))/len(col) for col in zip(*reslist)] ;
        #print np.mean(np.array(lines), axis=0) ;


if __name__ == "__main__":
    filename = "provenance_dataset/karate_provenance.txt";
    mc_num = 100 ;
    #mc_num_list = [100, 1000, 10000] ;
    mc_num_list = [50, 500, 5000] ;
    test_converge(mc_num_list, filename, 10) ; 
    '''k = 1 ;
    start = timeit.default_timer() ;
    lines = causal_test(filename, mc_num, k) ;
    stop = timeit.default_timer() ;
    print stop-start ;
    #for line in lines:
        #print " ".join(line) ;
    '''
