from NDCG import NDCG ;
import random

def get_ground_truth_dict(lines, k):
    G = {} ;
    for line in lines:
        temp = line.strip().replace(",","").split(" ") ;
        mytuple = temp[0] ;
        values = temp[1:] ;
        G[mytuple] = float(values[k-1]) ;
    return G ;

def perm_rank(G, num=1):
    reslist = [] ;
    for i in range(num):
        for key in testG.keys():
            testG[key] = testG[key] + random.random()/10000000 ;
        rank_list = sorted(testG, key=testG.get, reverse=True) ;
        #print rank_list ;
        temp = NDCG(gold_dict, rank_list);
        reslist.append(temp) ;
    #print reslist ;
    avg = [float(sum(col))/len(col) for col in zip(*reslist)] ;
    return avg ;

k = 9 ;

final_mc_file = "res_100000.txt" ;
ground_truth_lines = [x.strip() for x in open(final_mc_file).readlines()] ;
gold_dict = get_ground_truth_dict(ground_truth_lines, k) ;#print G ;

#print ground_truth_ndcg_list ;

test_mc_file = "res_1000.txt" ;
testG = get_ground_truth_dict(open(test_mc_file).readlines(), k) ;

res = perm_rank(testG, 10000) ;
print res ;
res = perm_rank(testG, 10000) ;
print res ;
