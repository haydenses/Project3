import csv
import timeit
import matplotlib.pyplot as plt

# csv functions from python documentation https://docs.python.org/3/library/csv.html
# timeit timer from python documentation https://docs.python.org/3/library/timeit.html
# quicksort function help from sorting slides from class powerpoint slide 121 and 122 https://ufl.instructure.com/courses/500074/files/84164662?wrap=1
# matplot library for graph https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py


# print(start)
housing_prices_lst = []
first = True
with open("HPI_master.csv") as housing_prices:
    # this will convert the csv file into something python can read
    prices_to_python = csv.reader(housing_prices, delimiter=',')
    # we iterate over each house in the csv document to append it to the housing prices list
    for curr_house in prices_to_python:
        if first:
            first = False
            continue
        # here was the only point in the entire list where it did not have an nsa value which made this very difficult to debug
        if curr_house == ['non-metro', 'all-transactions', 'quarterly', 'State', 'Massachusetts', 'MA', '2022', '4', '', '']:
            continue
        housing_prices_lst.append(curr_house)


# print(len(housing_prices_lst))

quicksort_lst = [7, 4, 9, 3, 2, 8, 6, 5]
def cut(lst, low_num, high_num, col):
    # here up is the value that will move up, and down is the value that will move down
    up_val = low_num
    down_val = high_num
    # we choose our pivot position to be the first value in the list
    pivot_pt = float(lst[low_num][col])

    while (up_val < down_val):
        # move the up val up until the value is above the pivot pt value
        # also it should be noted that you can not do while loops no matter how much I tried because it reaches the max recursion depth
        # whenever I tried
        for i in range(up_val, high_num):
            if(float(lst[up_val][col]) > pivot_pt):
                break
            up_val += 1
        for i in range(high_num, low_num, -1):
            if(float(lst[down_val][col]) < pivot_pt):
                break
            down_val -= 1



        # if the up value is still lower than the down value when we move the up and down values respectively, we need to swap the values 
        # at those positions since the values at that positon are higher or lower than the pivot respecitvely
        if (up_val < down_val):
            temp_val = lst[up_val]
            lst[up_val] = lst[down_val]
            lst[down_val] = temp_val
            
    # swap the values where we replaces the lowest number that was in the partition (since we are choosing our partition to be pt 1) with where
    # the value is supposed to be in the list
    temp_val = lst[low_num]
    lst[low_num] = lst[down_val]
    lst[down_val] = temp_val
    # here we need to return what will be the next pivot point since we are always choosing the first position as the pivot
    return down_val

# quicksort function
def quicksort_func(lst, low_num, high_num, col):
    # each time we recursively call the quicksort function, we need to see if the low number is still less than the high number because we 
    # do not need to recursively call the function if these values are the same
    if (low_num < high_num):
        pivot_pt = cut(lst, low_num, high_num, col)
        quicksort_func(lst, low_num, pivot_pt-1, col)
        quicksort_func(lst, pivot_pt+1, high_num, col)

choice = input("Click 1 to sort the data by house prices. ")
start = timeit.default_timer()
time_to_sort = 0
if (choice == '1'):
    quicksort_func(housing_prices_lst, 0, len(housing_prices_lst)-1, 8)
    time_to_sort = timeit.default_timer()-start
else:
    print("invalid choice")

print("This data took " + str(time_to_sort) + " seconds to sort.\n")

year_dict_lst = {1975: [], 1976: [], 1977: [], 1978: [], 1979: [], 1980: [], 1981: [], 1982: [], 1983: [], 1984: [], 1985: [], 1986: [],
            1987: [], 1988: [], 1989: [], 1990: [], 1991: [], 1992: [], 1993: [], 1994: [], 1995: [], 1996: [], 1997: [], 1998: [],
            1999: [], 2000: [], 2001: [], 2002: [], 2003: [], 2004: [], 2005: [], 2006: [], 2007: [], 2008: [], 2009: [], 2010: [], 
            2011: [], 2012: [], 2013: [], 2014: [], 2015: [], 2016: [], 2017: [], 2018: [], 2019: [], 2020: [], 2021: [], 2022: [],
            2023: []}
for i in range(0, len(housing_prices_lst)-1):
    # 2024 has bad data so far because there are such few values to resonably compare to
    if (int(housing_prices_lst[i][6]) == 2024):
        continue
    year_dict_lst[int(housing_prices_lst[i][6])].append(float(housing_prices_lst[i][8]))

avg_price = {}
for key, value in year_dict_lst.items():
    total_val = 0
    curr_lst = year_dict_lst[key]
    for i in range(0, len(curr_lst) - 1):
        total_val += curr_lst[i]
    avg_price[key] = total_val/len(curr_lst)

years = []
prices = []


print("Here are the actual average prices of homes across the years: ")
for key, value in avg_price.items():
    print(str(key) + ": $" + str(value))
    years.append(key)
    prices.append(value)
    

inflation_dict = {1976: 1.058, 1977: 1.065, 1978: 1.076, 1979: 1.113, 1980: 1.135, 1981: 1.103, 1982: 1.062, 1983: 1.032, 
            1984: 1.043, 1985: 1.036, 1986: 1.019, 1987: 1.036, 1988: 1.041, 1989: 1.048, 1990: 1.054, 1991: 1.042, 1992: 1.03, 
            1993: 1.03, 1994: 1.026, 1995: 1.028, 1996: 1.03, 1997: 1.023, 1998: 1.016, 1999: 1.022, 2000: 1.034, 2001: 1.028, 
            2002: 1.016, 2003: 1.023, 2004: 1.027, 2005: 1.034, 2006: 1.032, 2007: 1.028, 2008: 1.038, 2009: 0.96, 2010: 1.016, 
            2011: 1.032, 2012: 1.021, 2013: 1.015, 2014: 1.016, 2015: 1.001, 2016: 1.013, 2017: 1.021, 2018: 1.024, 2019: 1.018, 
            2020: 1.012, 2021: 1.047, 2022: 1.08, 2023: 1.041}

inflation_adj_values = {1975: 58.124136690647504, 1976: 0, 1977: 0, 1978: 0, 1979: 0, 1980: 0, 1981: 0, 1982: 0, 1983: 0, 
            1984: 0, 1985: 0, 1986: 0, 1987: 0, 1988: 0, 1989: 0, 1990: 0, 1991: 0, 1992: 0, 1993: 0, 1994: 0, 1995: 0, 1996: 0, 
            1997: 0, 1998: 0, 1999: 0, 2000: 0, 2001: 0, 2002: 0, 2003: 0, 2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 
            2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0, 2023: 0}


for key, value in inflation_dict.items():
    inflation_adj_values[key] = inflation_adj_values[key-1]*value

prices2 = []
print("\nHere are the inflation adjusted values of home prices across the years: ")
for key, value in inflation_adj_values.items():
    print(str(key) + ": $" + str(value))
    prices2.append(value)


inflation_calculated_val = ((avg_price[2023]-inflation_adj_values[2023])/inflation_adj_values[2023])*100
print("If we look at the data we can see that home prices have outpaced inflation by about " +str(inflation_calculated_val) + "% since 1975.")

fig, ax = plt.subplots()
ax.scatter(years, prices)
ax.scatter(years, prices2)


decision = input("Press 1 if you want to visualize the data. ")
if (decision == '1'):
    plt.show()
