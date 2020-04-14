import json 
import csv 
import pandas as pd 
import numpy as np
from scipy.optimize import curve_fit
from array import array
import matplotlib.pyplot as plt

def Json_to_csv(Json_filename,CSV_filename):
    with open(Json_filename) as json_file: 
        data = json.load(json_file) 
    
    employee_data = data['raw_data'] 
    
    data_file = open(CSV_filename, 'w') 
    csv_writer = csv.writer(data_file) 

    count = 0  
    for emp in employee_data: 
        if count == 0: 
            # Writing headers of CSV file 
            header = emp.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(emp.values()) 
    
    data_file.close() 


def clean_data(csv_file):
    data = pd.read_csv(csv_file)
    clean_data_df = data[['dateannounced','gender','detectedstate']]
    
    dates_df = data[['dateannounced']].drop_duplicates()

    summary = dates_df

    dates_all = data[['dateannounced']].values

    dates = dates_df.values
    date_count_list = []
    count_cumulative_list = [0]

    for date in dates:
        count=0
        if (date != ""):
            # print(date[0])
            for row in dates_all:
                if (date[0]==row[0]):
                    count +=1
        date_count_list.append(count)


    #culumative cases

    for i in range(len(dates)-1):
        count_cumulative_list.append( count_cumulative_list[i] + date_count_list[i] )
    
    summary["count"] = date_count_list
    summary["cumulative"] = count_cumulative_list

    print (summary.values)
    return summary

    # print(summary)

    # summary.to_csv("clean.csv")



def curve(x, a, b,c):
    return a *(b ** x) + c
    # return x*a  +b +c

def sigmoid(x,a,b,c):
    return  a *(1/( 1 + b^(-x-c) ))
    

raw_data_json ="raw_data.json"
raw_data_csv = "raw_data.csv"


# Json_to_csv(raw_data_json ,raw_data_csv)
data = clean_data(raw_data_csv)
data.drop(data.tail(1).index,inplace=True)

y = data['count'].values

x =  np.arange(0,len(y))

# print (len(y))
# print (len(x))

popt, pcov = curve_fit(curve, x, y)

print ( curve(50, *popt))

plt.plot(x, curve(x, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.bar(x, y)



plt.plot(x, data["cumulative"].values, 'g--')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()