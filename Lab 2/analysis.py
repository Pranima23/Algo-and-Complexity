import random, time
from matplotlib import pyplot as plt
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def exec_time(search, *args):

    start = time.time()
    search(*args)
    return (time.time() - start)

def sort():

    exec_records = {
        'input_size': [], 
        'insertion_sort': [],
        'merge_sort': [],
        }

    for size in range(1, 100000, 10000):
        randomInputs = random.sample(range(100000), size)
        
        exec_records['input_size'].append(size)

        # insertion sort
        exec_records['insertion_sort'].append(exec_time(insertion_sort, randomInputs))
      
        # merge sort
        exec_records['merge_sort'].append(exec_time(merge_sort, randomInputs, 0, len(randomInputs)-1))
        
    return exec_records

def plot_exec_records(plot_datas):
   
    fig, [insertion_sort_time, merge_sort_time] = plt.subplots(2, 1)

    # Insertion Sort Execution Times Plot
    insertion_sort_time.plot(plot_datas['input_size'], plot_datas['insertion_sort'], color='orange')    
    insertion_sort_time.set_title('Insertion Sort', loc='left')
    insertion_sort_time.set_xlabel('Input Sizes')
    insertion_sort_time.set_ylabel('Execution Times')

    # Merge Sort Execution Times Plot
    merge_sort_time.plot(plot_datas['input_size'], plot_datas['merge_sort'], color='blue')
    merge_sort_time.set_title('Merge Sort', loc='left')
    merge_sort_time.set_xlabel('Input Sizes')
    merge_sort_time.set_ylabel('Execution Times')

    plt.show()

if __name__ == "__main__":
    exec_records = sort()
    plot_exec_records(exec_records)