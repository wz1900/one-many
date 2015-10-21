from NDCG import NDCG ;
import random
# edge_tuple 10% 20% ... 100%
def get_ground_truth_dict(lines, k):
    G = {} ;
    for line in lines:
        temp = line.strip().replace(",","").split(" ") ;
        mytuple = temp[0] ;
        values = temp[1:] ;
        G[mytuple] = float(values[k-1]) ;
    return G ;

def perm_rank(testG, gold_dict, num=1):
    reslist = [] ;
    for i in range(num):
        for key in testG.keys():
            testG[key] = testG[key] + random.random()/10000000 ;
        rank_list = sorted(testG, key=testG.get, reverse=True) ;
        #print "\n".join(rank_list) ;
        temp = NDCG(gold_dict, rank_list);
        reslist.append(temp) ;
    #print reslist ;
    avg = [float(sum(col))/len(col) for col in zip(*reslist)] ;
    return avg ;

def evaluate(ground_truth_lines, test_mc_lines, k, perm_num=1):
    gold_dict = get_ground_truth_dict(ground_truth_lines, k) ;#print G ;
    testG = get_ground_truth_dict(test_mc_lines, k) ;
    
    res = perm_rank(testG, gold_dict, perm_num) ;
    print res ;


if __name__ == "__main__":
    k = 5 ;

    final_mc_file = "converge_file_better/res_1000000.txt" ;
    ground_truth_lines = [x.strip() for x in open(final_mc_file).readlines()] ;

    test_mc_file = "converge_file_better/res_100.txt" ;
    test_mc_lines = open(test_mc_file).readlines() ;
    res = evaluate(ground_truth_lines, test_mc_lines, k, perm_num=10000) ;
