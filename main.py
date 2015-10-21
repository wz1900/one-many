import timeit
from random_causal_test import run_mc ;
from TargetProvenance import get_tuple_list, readProvenance ;
from BasicFunction import get_targets_karate, get_mc_result_list ;
from main_ndcg import evaluate ;

def causal_test(pro_file_name, mc_num, k):
    targetnodelist = get_targets_karate() ;
    targetlist = readProvenance(filename, targetnodelist) ;
    res_dict = run_mc(targetlist, mc_num, k) ;
    return get_mc_result_list(res_dict, targetlist, get_tuple_list(targetlist)) ; 

if __name__ == "__main__":
    filename = "provenance_dataset/karate_provenance.txt";
    mc_num = 100 ;
    k = 1 ;
    start = timeit.default_timer() ;
    lines = causal_test(filename, mc_num, k) ;
    stop = timeit.default_timer() ;
    print stop-start ;
    #for line in lines:
        #print " ".join(line) ;

    final_mc_file = "converge_file_better/res_1000000.txt" ;
    ground_truth_lines = [x.strip() for x in open(final_mc_file).readlines()] ;
    res = evaluate(ground_truth_lines, lines, k, perm_num=1000) ;
