
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import *
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


master = tk.Tk()
global quick_sort_start_time
global quick_sort_total_time
quick_sort_total_time=0
global time_dict
time_dict={'Insertion Sort':0 , 'Selection Sort':0, 'Regular Quick Sort':quick_sort_total_time, 'Merge Sort':0, 'Heap Sort':0, 'Bubble Sort':0,
                  '3 Median Quick Sort':0}

# insertion sort will be called
def insertion_sort():
    global num_list, time_dict
    # start time will start calculating the time as the function starts
    start_time = time.time()
    for index in range(len(num_list)):
        # this will store the right and left element
        right_element=num_list[index]
        left_element=index-1
        # this will check if the left element is greater than 0 and if it is it will go isnide the loop
        while left_element>=0:
            if right_element<num_list[left_element]:
                num_list[left_element+1]=num_list[left_element]
                num_list[left_element]=right_element
                left_element=left_element-1
            else:
                break
    # this will calculate the total time required
    time_calculate=time.time() - start_time
    time_dict['Insertion Sort'] = time_calculate
    # this will return the total time and sorted list
    return num_list,time_calculate

# selection sort will be called from here
def selection_sort():
    # declared global list and time dictionary
    global num_list, time_dict
    # start time will get started from here as the function starts
    start_time = time.time()
    size_of_elements=len(num_list)
    for i in range(size_of_elements):
        min_index=i
        for j in range(min_index+1,size_of_elements):
            if num_list[j]<num_list[min_index]:
                min_index=j
        if i!=min_index:
            num_list[i],num_list[min_index]=num_list[min_index],num_list[i]
    # time_calculate will store the whole time calculated for the function
    time_calculate = time.time() - start_time
    time_dict['Selection Sort'] = time_calculate
    # this will return the list and the total time taken for the function
    return num_list,time_calculate

# start time for quick sort is set to 0 initially
quick_sort__start_time_flag = 0
# regular quick sort
def regular_quick_sort(num_list):
    # global variables are declared time_dict, start time and total time
    global time_dict
    global quick_sort_start_time
    global quick_sort_total_time
    if quick_sort__start_time_flag==0:
        # start time will get started from here
        quick_sort_start_time=time.time()
    length = len(num_list)
    if length <= 1:
        return num_list
    else:
        # pivot is last elemment
        pivot = num_list.pop()
    elements_greater = []
    elements_lower = []
    for element in num_list:
        # if the elements are greater than pivot it will go to the right of the pivot
        if element > pivot:
            elements_greater.append(element)
        else:
            # else the element will be on the left side of the pivot
            elements_lower.append(element)
    quick_sort_total_time = time.time() - quick_sort_start_time
    # this will return the sorted quick sort list
    return regular_quick_sort(elements_lower) + [pivot] + regular_quick_sort(elements_greater)

# merge sort
def merge_sort(list_of_elements):
    global time_dict
    # start_time will get started from here when the function is called
    start_time=time.time()
    # if the length of the list is 1 then it will return the list
    if len(list_of_elements)==1:
        return list_of_elements
    else:
        # else it will get the middle elements, left elements and right elements
        mid_elements=len(list_of_elements)//2
        left_elements=list_of_elements[:mid_elements]
        right_elements=list_of_elements[mid_elements:]
        # left and right elements are passed to the merge sort function
        merge_sort(left_elements)
        merge_sort(right_elements)
        left_pointer=right_pointer=merge_pointer=0
        # this will check the elements from left and right side to merge into one sorted list
        while left_pointer<len(left_elements) and right_pointer<len(right_elements):
            if left_elements[left_pointer]<right_elements[right_pointer]:
                list_of_elements[merge_pointer]=left_elements[left_pointer]
                left_pointer=left_pointer+1
            else:
                list_of_elements[merge_pointer]=right_elements[right_pointer]
                right_pointer=right_pointer+1
            merge_pointer=merge_pointer+1
        # this will sort the list on the left side of the elements
        while left_pointer<len(left_elements):
            list_of_elements[merge_pointer]=left_elements[left_pointer]
            left_pointer=left_pointer+1
            merge_pointer=merge_pointer+1
        # this will sort the list on right side of the elemets
        while right_pointer<len(right_elements):
            list_of_elements[merge_pointer]=right_elements[right_pointer]
            right_pointer=right_pointer+1
            merge_pointer=merge_pointer+1
    # total time is calculated
    total_time=time.time() - start_time
    time_dict['Merge Sort'] = total_time
    # this will return total time and list of elements
    return list_of_elements,total_time

# heap sort function will be called from here
def heap_sort(num_list,length,i):
    largest_element=i
    left_elemet=2*i+1
    right_element=2*i+2
    # if largest element is less than left element then the largest element will be left element
    if left_elemet<length and num_list[largest_element]<num_list[left_elemet]:
        largest_element=left_elemet
    # if largest element is less than right element then the largest element will be right element
    if right_element<length and num_list[largest_element]<num_list[right_element]:
        largest_element=right_element
    if largest_element!=i:
        num_list[i],num_list[largest_element]=num_list[largest_element],num_list[i]
        heap_sort(num_list,length,largest_element)

# heap build function is called
def heap_build(num_list):
    global time_dict
    # start time is calculated from here when the function is called
    start_time = time.time()
    length_element=len(num_list)
    for i in range(length_element//2-1,-1,-1):
        # heap sort function is called from here
        heap_sort(num_list,length_element,i)
    for i in range(length_element-1,0,-1):
        num_list[i],num_list[0]=num_list[0],num_list[i]
        heap_sort(num_list,i,0)
    total_time = time.time() - start_time
    time_dict['Heap Sort'] = total_time
    # this will return the total time and list
    return num_list, total_time

# bubble sort function is called
def bubble_sort():
    global num_list, time_dict
    # start time is calculated from here when the function is called
    start_time=time.time()
    length_pointer = len(num_list) - 1
    # check sorted list is set initially to false
    check_sorted_list = False
    # if not check sorted list then it will go inside the while
    while not check_sorted_list:
        check_sorted_list = True
        for i in range(0, length_pointer):
            if num_list[i] > num_list[i + 1]:
                check_sorted_list = False
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    total_time = time.time() - start_time
    time_dict['Bubble Sort'] = total_time
    # this will return the sorted list and total time taken
    return num_list,total_time

# median of 3 function is called
def median_from_elements(first, second, third):
        # this function will calculate the median
        if first > second:
            if first < third:
                median_value = first
            elif second > third:
                median_value = second
            else:
                median_value = third
        else:
            if first > third:
                median_value = first
            elif second < third:
                median_value = second
            else:
                median_value = third
        # this will return the median value
        return median_value

# partition function is called where the first element, lower and higher element are passes as parameter
def partition(num_list, lower_element, higher_element):
    first_element = num_list[random.randint(lower_element, higher_element)]
    second_element = num_list[random.randint(lower_element, higher_element)]
    third_element = num_list[random.randint(lower_element, higher_element)]
    median = median_from_elements(first_element, second_element, third_element)
    index_pivot = num_list.index(median)
    num_list[lower_element], num_list[index_pivot] = num_list[index_pivot], num_list[lower_element]
    pivot_to_be = num_list[lower_element]
    i = lower_element
    for j in range(lower_element + 1, higher_element + 1):
        if (num_list[j] < pivot_to_be):
            i = i + 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
    num_list[i], num_list[lower_element] = num_list[lower_element], num_list[i]
    return i

# this will call the quick sort median function
def quick_sort_median(num_list, low_element, high_element):
    global time_dict
    # start time will get started from here
    start_time=time.time()
    if low_element < high_element:
        middle = partition(num_list, low_element, high_element)
        quick_sort_median(num_list, low_element, middle - 1)
        quick_sort_median(num_list, middle + 1, high_element)
    total_time = time.time() - start_time
    time_dict['3 Median Quick Sort'] = total_time
    # this will return the list and total time taken
    return num_list , total_time


# show entry fields will show the output
def show_entry_fields():
    global num_list
    print("First Name: %s\nLast Name: %s\nLast Name: %s" % (combo.get(), e2.get(),e3.get().split(",")))
    selected_algorithm=combo.get()
    e2_int=int(e2.get())
    num_list=e3.get().split(",")
    num_list=list(map(int,num_list))
    # this will check if the user has enter the elements more than data size
    if(e2_int<len(num_list)):
        messagebox.showinfo("Title", "You have entered more number of element than expected")
    # this will check if the user has enter the elements less than data size
    elif(e2_int>len(num_list)):
        messagebox.showinfo("Title", "You have entered less number of element than expected")
    else:
    # it will go inside else if the user has enter the correct elements
        messagebox.showinfo("Title", "All good")
        # if the selected algorithm is insertion sort then it will call insertion sort function
        if selected_algorithm=='Insertion Sort':
            lst,_=insertion_sort()
            label = Label(master, text='\nThe sorted list using insertion sort:' + str(num_list) + '\n')
            label.grid()
        # if the selected algorithm is selection sort then it will call selection sort function
        elif selected_algorithm=='Selection Sort':
            lst,_=selection_sort()
            label = Label(master, text='\nThe sorted list using selection sorted:' + str(num_list) + '\n')
            label.grid()
        # if the selected algorithm is regular quick sort then it will call regular quick sort function
        elif selected_algorithm=='Regular Quick Sort':
            lst=regular_quick_sort(num_list)
            quick_sort__start_time_flag=0
            label = Label(master, text='\nThe sorted list using regular quick sort:' + str(lst) + '\n')
            label.grid()
        # if the selected algorithm is merge sort then it will call merge sort function
        elif selected_algorithm == 'Merge Sort':
            lst,_=merge_sort(num_list)
            label = Label(master, text='\nThe sorted list using merge sort:' + str(num_list) + '\n')
            label.grid()
        # if the selected algorithm is heap sort then it will call heap sort function
        elif selected_algorithm=='Heap Sort':
            lst,_=heap_build(num_list)
            label = Label(master, text='\nThe sorted list using heap sort:' + str(num_list) + '\n')
            label.grid()
        # if the selected algorithm is bubble sort then it will call bubble sort function
        elif selected_algorithm=='Bubble Sort':
            lst,_=bubble_sort()
            label = Label(master, text='\nThe sorted list using bubble sort:' + str(num_list) + '\n')
            label.grid()
        # if the selected algorithm is 3 median quick sort then it will call 3 median quick sort function
        elif selected_algorithm == '3 Median Quick Sort':
            n=len(num_list)
            lst, _ = quick_sort_median(num_list, 0, n-1)
            label = Label(master, text='\nThe sorted list using 3 Median Quick Sort:' + str(num_list) + '\n')
            label.grid()

# this function will compare the two algorithm and will show which one is more efficient
def compare_algorithm():
    selected_algorithm = combo1.get()
    selected_algorithm_next = combo2.get()
    t1=show_time(selected_algorithm)
    t2=show_time(selected_algorithm_next)
    if t1<t2:
        label = Label(master, text=selected_algorithm + " is more efficient than  " + selected_algorithm_next)
        label.grid()
    else:
        label = Label(master, text=selected_algorithm_next + " is more efficient than  " + selected_algorithm)
        label.grid()

# show time function will show the total time taken for each algorithm
def show_time(selected_algorithm):
    # if selected algorithm is insertion sort then it will call insertion sort function
    if selected_algorithm=='Insertion Sort':
        # insertion sort function is called
        _,t1=insertion_sort()
        # this will print the time required for insertion sort
        label = Label(master, text="Time required to sort using insertion sort:  %s seconds "   % (t1) )
        label.grid()

    # if selected algorithm is selection sort then it will call selection sort function
    elif selected_algorithm=='Selection Sort':
        # selection sort function is called
        _,t1=selection_sort()
        # this will print the time required for selection sort
        label = Label(master, text="Time required to sort using selection sort:  %s seconds " % (t1))
        label.grid()

    # if selected algorithm is regular quick sort then it will call regular quick sort function
    elif selected_algorithm == 'Regular Quick Sort':
        t1=quick_sort_total_time
        # regular quick sort function is called
        regular_quick_sort(num_list)
        quick_sort__start_time_flag=0
        # this will print the time required for regular quick sort
        label = Label(master, text="Time required to sort using regular quick sort:  %s seconds " % (t1))
        label.grid()

    # if selected algorithm is merge sort then it will call merge sort function
    elif selected_algorithm == 'Merge Sort':
        # merge sort function is called
        _,t1 = merge_sort(num_list)
        # this will print the time required for merge sort
        label = Label(master, text="Time required to sort using merge sort:  %s seconds " % (t1))
        label.grid()

    # if selected algorithm is heap sort then it will call heap sort function
    elif selected_algorithm == 'Heap Sort':
        # heap build function is called
        _,t1 = heap_build(num_list)
        # this will print the time required for heap sort
        label = Label(master, text="Time required to sort using heap sort:  %s seconds " % (t1))
        label.grid()

    # if selected algorithm is bubble sort then it will call bubble sort function
    elif selected_algorithm == 'Bubble Sort':
        # bubble sort function is called
        _,t1 = bubble_sort()
        # this will print the time required for bubble sort
        label = Label(master, text="Time required to sort using bubble sort:  %s seconds " % (t1))
        label.grid()

    # if selected algorithm is 3 median quick sort then it will call 3 median quick sort function
    elif selected_algorithm == '3 Median Quick Sort':
        n = len(num_list)
        # quick sort median function is called
        _, t1 = quick_sort_median(num_list, 0, n-1)
        # this will print the time required for 3 median quick sort
        label = Label(master, text="Time required to sort using 3 Median Quick Sort:  %s seconds " % (t1))
        label.grid()
    # this will return the time from each sorting algorithm
    return t1

# plot function is called to plot the time taken by algorithm
def plot():
    insertion_sort()
    selection_sort()
    regular_quick_sort(num_list)
    quick_sort__start_time_flag=0
    merge_sort(num_list)
    heap_build(num_list)
    bubble_sort()
    n=len(num_list)
    quick_sort_median(num_list,0,n-1)
    # x axis values
    x = ["Insertion Sort", "Selection Sort", "Regular Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort",
         "3 Median Quick Sort"]
    # corresponding y axis values
    y = [time_dict['Insertion Sort'], time_dict['Selection Sort'], time_dict['Regular Quick Sort'],
         time_dict['Merge Sort'],
         time_dict['Heap Sort'], time_dict['Bubble Sort'], time_dict['3 Median Quick Sort']]

    plt.xticks(np.arange(7), ("Insertion Sort", "Selection Sort", "Regular Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort",
         "3 Median Quick Sort"))
    plt.plot(y, 'bs', y, 'g')
    plt.show()

combo = Combobox(master)
combo1 = Combobox(master)
combo2 = Combobox(master)


tk.Label(master,
         text="Enter size of the list: ").grid(row=2)

tk.Label(master,
         text="Enter the element: ").grid(row=3)


e2 = tk.Entry(master)
e3 = tk.Entry(master)


e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

from functools import partial
from tkinter import *

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=4,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

combo['values']= ("Insertion Sort", "Selection Sort", "Regular Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort", "3 Median Quick Sort")
print(combo.get())
combo.current(1) #set the selected item

combo.grid(column=0, row=1)

combo1['values']= ("Insertion Sort", "Selection Sort", "Regular Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort", "3 Median Quick Sort")
print(combo1.get())
combo1.current(1) #set the selected item

combo1.grid(column=0, row=6)

combo2['values']= ("Insertion Sort", "Selection Sort", "Regular Quick Sort", "Merge Sort", "Heap Sort", "Bubble Sort", "3 Median Quick Sort")
print(combo2.get())
combo2.current(1) #set the selected item

combo2.grid(column=1, row=6)

tk.Button(master,
          text='Compare Algorithm', command=compare_algorithm).grid(row=7,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=3)

tk.Button(master,
          text='Plot for all Algorithm', command=plot).grid(row=8,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=3)

tk.mainloop()


# References -
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# https://stackabuse.com/insertion-sort-in-python/
# https://realpython.com/sorting-algorithms-python/
# https://docs.python.org/3/library/tk.html
# https://realpython.com/python-gui-tkinter/

