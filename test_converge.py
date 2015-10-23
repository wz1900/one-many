from main_ndcg import perm_rank, get_ground_truth_dict ;
import os ;

def test(final_mc_file, filelist, k):
    ground_truth_lines = [x.strip() for x in open(final_mc_file).readlines()] ;
    gold_dict = get_ground_truth_dict(ground_truth_lines, k) ;#print G ;
    
    for myfile in filelist:
        testG = get_ground_truth_dict(open(myfile).readlines(), k) ;
        res = perm_rank(testG, gold_dict, 1000) ;
        print myfile ;
        print res ;

if __name__ == "__main__":
    k = 1 ;

    #final_mc_file = "res_1000000.txt" ; 
    #filelist=['res_100.txt', 'res_1000.txt', 'res_2000.txt', 'res_5000.txt', 'res_10000.txt', 'res_50000.txt', 'res_100000.txt'] ;
    final_mc_file = "res_1000000.txt" ; 
    filelist=['res_100.txt', 'res_1000.txt', 'res_5000.txt', 'res_10000.txt', 'res_100000.txt'] ;
    #filelist=['res_100.txt', 'res_1000.txt', 'res_10000.txt', 'res_100000.txt', 'res_1000000.txt'] ;
    main_path = "converge_file" ;
    final_mc_file = os.path.join(main_path, final_mc_file) ;
    for i in range(len(filelist)):
        filelist[i] = os.path.join(main_path, filelist[i]) ;

    test(final_mc_file, filelist, k) ;
