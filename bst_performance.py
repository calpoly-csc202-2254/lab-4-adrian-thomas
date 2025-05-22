import random
import time
from bst import *


def ordering(a:float,b:float)->bool:
    return a<b

def random_nums(n:int)->list[float]:
    return [random.random() for num in range(n)]

def time_ops(tree_sizes:list[int])->None:
    print("Tree Size\tInsert Time(s)\tLookup Time(s)")
    for num in tree_sizes:
        data_set = random_nums(num)
        targets = random_nums(1000)
        bin_s_tree = frozenBinarySearchTree(ordering,None)
        start_insert_time = time.time()
        for data in data_set:
            bin_s_tree = frozenBinarySearchTree(
                bin_s_tree.comes_before,
                insert(bin_s_tree.tree,data,bin_s_tree.comes_before))
        end_insert_time=time.time()
        start_lookup_time = time.time()
        for target in targets:
            look_up=lookup(bin_s_tree.tree,target,bin_s_tree.comes_before)
        end_lookup_time=time.time()
        insert_time=round(end_insert_time - start_insert_time,4)
        lookup_time=round(end_lookup_time - start_lookup_time,4)
        print(f"{num}\t{insert_time}\t{lookup_time}")

if __name__ == "__main__":
    tree_sizes=[num for num in range(100000,1000001,100000)]
    time_ops(tree_sizes)




        
