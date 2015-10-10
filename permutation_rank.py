from RankTerm import RankTerm 
from math import fabs ;
import math ;
import random ;
from NDCG import NDCG, get_ground_truth ;
from KendallTau import get_gold_list, Kendall ;
from MyPreason import my_preasonr
from mPrecision import mPrecision
min_float = 0.00000001 ;

#---------get the gound truth list of ndcg -----------
#ground_truth_file = "value_72-simple-paths/0-197-pns-small.txt" ;
ground_truth_file = "158-146/158-146-1024PNS.txt" 
#ground_truth_file = "0-197-1052/0-197-1052PNS.txt"
# "/home/pear/research/social_network/158-146/158-146-1035PNS.txt"
#ground_truth_file = "value/0-197-pns.txt" ; 
lines = [x.strip() for x in open(ground_truth_file).readlines()] ;
G = get_ground_truth( lines ) ;
ground_truth_ndcg_list = NDCG(G, lines);
#print ground_truth_ndcg_list ;

def rank_perm(file_path):
    lines = [x.strip() for x in open(file_path).readlines()] ;
    value = -1 ;
    i = 0 ;
    rTermList = [] ;

    while( i< len(lines) ):
        val_list = lines[i].split(" ") ;

        if( fabs(value-float(val_list[-1])) > min_float ):
            value = float(val_list[-1]) ;
            rTerm = RankTerm() ;
            #print "rank term: ", lines[i] ;
            rTerm.readRecord(lines[i]) ;
            i = i + 1 ;
            while( i<len(lines) ):     
                val_list = lines[i].split(" ") ;
                if( fabs(value-float(val_list[-1])) > min_float ): break ;
                rTerm.readRecord(lines[i]) ;
                i = i + 1 ;
        rTermList.append(rTerm) ;
    #for test in rTermList:
        #print test.rank_list ;
    return rTermList ;   

def rank_by_G(mylist, G):
    d = {} ;
    for temp in mylist:
        vallist = temp.split(" ") ;
        #print vallist ;
        d[vallist[0]] = G[vallist[0]] ;
        #list_of_dicts.sort(key=operator.itemgetter('name')) ;
    return sorted(d, key=d.get, reverse=True) ; 

'''def rank_randomly(mylist, G):
    return random.shuffle(mylist) ; 
'''

def getRanklist(G, random_flag):
    rank_list = [] ;
    file_name = "/home/pear/research/social_network/responsibility_ability_fixed/resp_ab_values_158-146/nresp-ability_158-146.txt"
    #file_name = "/home/pear/research/social_network/responsibility_ability_fixed/resp_ab_values_0-197-1052/appresp-ability_0-197.txt"
    #file_name = "/home/pear/research/social_network/responsibility_ability_fixed/resp_ab_values_0-197-70/appresp-ability_0-197.txt"
    #file_name = "value/0-197-nresp.txt" ;
    termlist = rank_perm( file_name ) ;
    #print "termlist length: ", len(termlist) ;
    for term in termlist:
        if(random_flag): 
            templist = sorted(term.rank_list, key=lambda *args: random.random()) ; #= term.rank_list.copy() ;
            #print templist ;
            #random.shuffle(templist) ;
        else: templist = rank_by_G(term.rank_list, G) ;
        #print "temp list: ", templist ;
        #rank_list.append(templist[0]) ;
        for temp in templist:
            rank_list.append( temp ) ;
    return rank_list ;

def randomNDCG(G, ground_truth_ndcg_list):
    num = 10000 ;
    res = [0]*len(ground_truth_ndcg_list) ;
    for i in range(num):
        rank_list = getRanklist(G, True) ;#------this is the key ---------
        ndcg_list = NDCG(G, rank_list) ;
        j = 0 ;
        for ndcg, groundtruth in zip(ndcg_list, ground_truth_ndcg_list):
            value = ndcg/groundtruth ;
            res[j] = res[j] + value ;
            j = j + 1 ;
    '''
    for i in range(len(res)):
        res[i] = res[i]/float(num) ;
        print res[i] ;
    #print res ;
    '''
    f = open("ndcg-ability-result.txt", "w") ;
    for i in range(len(res)):
        res[i] = res[i]/float(num) ;
        print res[i] ;
        print >>f, res[i] ;
    f.close() ;

def randomKendall(G, gold_list):
    num = 2000 ;
    nouse_list = Kendall(gold_list, gold_list) ;
    res = [0]*len(nouse_list) ;
    for tt in range(num):
        rank_list = getRanklist(G, True) ;
        templist = [] ;
        for temp in rank_list:
            templist.append( temp.split(" ")[0] ) ;
        #print templist ;
        kendall_list = Kendall(gold_list, templist) ;
        i = 0 ;
        for val in kendall_list:
            res[i] = res[i] + val ;
            i = i + 1 ;

    f = open("kt-nresp-ability-result.txt", "w") ;
    for i in range( len(res) ): 
        res[i] = res[i]/float(num) ;
        print res[i] ;
        print >>f, res[i] ;
    f.close() ;

def randomPearson(G, ground_truth_ndcg_list, gold_list):
    num = 2000 ;
    resPreason = [0]*len(ground_truth_ndcg_list) ;
    resPvalue = [0]*len(ground_truth_ndcg_list) ;
    
    for i in range(num):
        rank_list = getRanklist(G, True) ;
        preason_list = my_preasonr(G, gold_list, rank_list) ;
        #print preason_list ;
        for j in range( len(preason_list) ):
            resPreason[j] += preason_list[j][0] ;
            resPvalue[j] += preason_list[j][1] ;

    f = open("preason-nresp-ability-result.txt", "w") ;
    for i in range( len(resPreason) ): 
        resPreason[i] = resPreason[i]/float(num) ;
        resPvalue[i] = resPvalue[i]/float(num) ;
        print resPreason[i], resPvalue[i] ;
        print >>f, resPreason[i], resPvalue[i] ;
    f.close() ;

def randomPrecision(gold_list):
    num = 2000 ;
    nouse_list = mPrecision(gold_list, gold_list) ;
    res = [0]*len(nouse_list) ;
    
    for i in range(num):
        rank_list = getRanklist(G, True) ;
        templist = [] ;
        for temp in rank_list:
            templist.append( temp.split(" ")[0] ) ;
        precision_list = mPrecision( gold_list, templist) ;
        #print preason_list ;
        for j in range( len(precision_list) ):
            res[j] += precision_list[j] ;

    f = open("precision-result.txt", "w") ;
    for i in range( len(res) ): 
        res[i] = res[i]/float(num) ;
        print res[i] ;
        print >>f, res[i] ;
    f.close() ;


gold_list = get_gold_list(lines) ;
randomPrecision(gold_list) ;
#randomPearson(G, ground_truth_ndcg_list, gold_list) ;

#randomKendall(G, gold_list) ;
#randomNDCG(G, ground_truth_ndcg_list) ;
'''
rank_list =getRanklist(G, False) ;
#print len(rank_list) ;
ndcg_list = NDCG(G, rank_list) ;
for ndcg, groundtruth in zip(ndcg_list, ground_truth_ndcg_list):
    print ndcg/groundtruth ;
'''
