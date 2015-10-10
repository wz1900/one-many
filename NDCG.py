import random ;
import math ;

def get_discount_list(G, ranklist, step):
    mysum = float( G[ranklist[0]] ) ;
    res_list = [] ;
    for i in range(1, len(ranklist)):
        temp = ranklist[i] ;
        mysum = mysum + float(G[temp])/math.log(i+1, 2) ;
        if( (i+1)%step == 0 ): 
            res_list.append(mysum) ;
    return res_list ;

def _get_gold_discount_list(gdict, step):
    ranklist = sorted(gdict, key=gdict.get, reverse=True) ;
    res = get_discount_list(gdict, ranklist, step) ;
    return res ;

def NDCG(gold_dict, rank_list, step=5):
    gold_discount_list = _get_gold_discount_list(gold_dict, step) ;
    res = [0]*len(gold_discount_list) ;

    rank_discount_list = get_discount_list(gold_dict, rank_list, step) ;
    #print rank_discount_list ;
    res = [] ;
    for temp, groundtruth in zip(rank_discount_list, gold_discount_list):
        value = temp/groundtruth ;
        #print value ;
        res.append(value) ;
    return res ;

def get_ground_truth(lines):
    G = {} ;
    for line in lines:
        temp = [ x.strip() for x in line.split(" ") ];
        G[temp[0]] =  temp[1] ;
    return G ;

'''def get_ndcg_ground_truth(G, ndcglines):
    ground_truth_ndcg_list = NDCG(G, ndcglines);
    return ground_truth_ndcg_list ; 
'''

if __name__ == "__main__":
    ground_truth_file = "value1052/1052pns_value.txt" ;#"value/0-197-pns.txt" ; 
    #ground_truth_file = "value/0-197-pns.txt" ;
 
    lines = [x.strip() for x in open(ground_truth_file).readlines()] ;
    G = get_ground_truth( lines ) ;

    ground_truth_ndcg_list = NDCG(G, lines);
    print ground_truth_ndcg_list ;

    j = 0 ;
    res = [0]*len(ground_truth_ndcg_list) ;
    for ndcg, groundtruth in zip(ground_truth_ndcg_list, ground_truth_ndcg_list):
        value = ndcg/groundtruth ;
        res[j] = res[j] + value ;
        j = j + 1 ;
    print res ;
