import networkx as nx ;
import numpy as np ;
import timeit
from ctypes import c_int
from multiprocessing import Process, Queue, Pool, Value, Lock ;
from BasicFunction import get_tuplelist, get_value ;
from TargetProvenance import TargetProvenance, get_target_provenance ;

targetDict = {} ; # target->tarProvenance
at_least_k = 2 ;

counter = Value(c_int)  # defaults to 0
counter_lock = Lock() ;

def get_active_targets(all_edge_value):
    num = 0 ;
    for target in targetDict.keys():
        if( target.if_connected(all_edge_value) is True ): num = num + 1 ;
    return num ;

def do_PS(tuplelist, mydict, term, ps_num, ps_total_num):
    # ps = p(Y_x|x',y') ;
    if(mydict[term] == False and get_value(tuplelist, mydict, term)==False) : 
        # -------- set edge true ---------
        ps_total_num += 1 ;
        mydict[term] = True ;
        active_nums = get_active_targets(mydict) ; 
        if( active_nums > at_least_k ):
            ps_num = ps_num + 1 ;

    return [ps_num, ps_total_num] ;

def do_PN(tuplelist, mydict, term, pn_num, pn_total_num):
    # pn = p(y'_x'|x,y)
    if(mydict[term] == True and get_value(tuplelist, mydict, term)==True) :
        pn_total_num += 1 ;
        mydict[term] = False ;
        active_nums = get_active_targets(mydict) ;
        if( active_nums < at_least_k ):
            pn_num = pn_num + 1 ;
        
    return [pn_num, pn_total_num] ;

def random_pns(random_list, tuplelist, mydict, term, ps_num, ps_total_num, pn_num, pn_total_num):
    tempdict = mydict.copy() ;
    i = 0 ;
    for key in mydict:
        if( random_list[i] == 0 ):
            tempdict[key] = False ;
        else: tempdict[key] = True ;
        i = i + 1 ;
    [ps_num, ps_total_num] = do_PS(tuplelist, tempdict.copy(), term, ps_num, ps_total_num) ;
    [pn_num, pn_total_num] = do_PN(tuplelist, tempdict.copy(), term, pn_num, pn_total_num) ;
    return [ps_num, ps_total_num, pn_num, pn_total_num] ;

def mc_graph(args_list):
    #if counter.value > 100: return [0,0,0,0,0,0] ;
    [target_dict, term, mc_num] = args_list ;
    ps_num = 0 ;
    ps_total_num = 0.00001 ;
    pn_num = 0 ;
    pn_total_num = 0.00001 ;
    pslist = [] ;
    pnlist = [] ;
    for i in range(mc_num) :
        random_list_1 = np.random.randint(2, size=len(mydict)) ;
        one_matrix = np.ones((len(random_list_1),), dtype=np.int) ;
        random_list_2 = np.subtract( one_matrix, random_list_1) ;
        #-------------- twice ------------------
        [ps_num, ps_total_num, pn_num, pn_total_num] = random_pns(random_list_1, tuplelist, mydict, term, ps_num, ps_total_num, pn_num, pn_total_num) ;
        [ps_num, ps_total_num, pn_num, pn_total_num] = random_pns(random_list_2, tuplelist, mydict, term, ps_num, ps_total_num, pn_num, pn_total_num) ;
    #mc_num = i + 1 ;
    print "mc_num = ", mc_num ;
    prob_s = ps_num*1.0/(1.0*ps_total_num) ;
    prob_n = pn_num*1.0/(1.0*pn_total_num) ;

    pns = ps_num*2.0/(2.0*mc_num) ;

    print "finish ", term ;
    with counter_lock:
        counter.value += 1 ;

    print "counter id: ", counter.value ;
    templist = [term, prob_s, ps_total_num*1.0/(2*mc_num), prob_n, pn_total_num*1.0/(2*mc_num), pns] ;
    print templist ;

    f = open("ps_pn_temp.txt", "a") ; 
    print >> f, templist;
    f.close() ;

    return [term, prob_s, ps_total_num*1.0/(2*mc_num), prob_n, pn_total_num*1.0/(2*mc_num), pns] ;

def func():
    file_name = "data.txt"
    target_dict = get_target_provenance(file_name) ;
    tuplelist = get_tuplelist(file_name) ;

    mc_num = 1000 ;
    print "mc_num: %d", mc_num ;
 
    pool = Pool(1) ;
    tasks = [ [tuplelist, mydict, term, mc_num] for term in mydict ] ;
    #print tasks ;

    pool_outputs = pool.map(mc_graph, tasks)
    pool.close()
    pool.join()
    
    f = open("ps_pn_output.txt", "w") ; 
    print >> f, 'Pool:', pool_outputs;
    f.close() ;

if __name__ == "__main__":
    start_time = timeit.default_timer()

    func()

    stop_time = timeit.default_timer()
    print stop_time-start_time ;
