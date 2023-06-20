import numpy as np
import matplotlib.pyplot as plt


def remove_keys_with_less_than_three_elements(dict1, dict2):
    keys_to_remove = []

    for key in dict1.keys():
        if len(dict1[key]) != 3:
            keys_to_remove.append(key)

    for key in dict2.keys():
        if len(dict2[key]) != 3:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        dict1.pop(key)
        dict2.pop(key)

    return(dict1, dict2)


## DO THIS SEPERATELY FOR TCP AND UDP AND CHANGE LINE 51 and 55 for mb\kb and tcp\udp
path_maxflow="C:\\Users\\danny\\Desktop\\Courses\\fast networks\\MAXFLO\\results_parser\\udp_maxflow_final_res.txt"
path_dijkstra="C:\\Users\\danny\\Desktop\\Courses\\fast networks\\MAXFLO\\results_parser\\dijkstra_udp_result_final.txt"

maxflow_file=open(path_maxflow,'r')
dijkstra_file=open(path_dijkstra,'r')
mf_bw_dict=dict()
for line in maxflow_file:
    linesplit = line.split()
    samp_time = linesplit[0]
    bw = linesplit[1]
    if samp_time != 'sec' and bw!= 'received' :
        if float(samp_time)<=20:
            if samp_time not in mf_bw_dict.keys():
                mf_bw_dict.update({samp_time:[bw]})
            else:
                currbw=mf_bw_dict[samp_time]
                currbw.append(bw)
                mf_bw_dict.update({samp_time:currbw})

# print(maxflow_bws)


# NOW DIJKSTRA PARSING
dijkstra_bw_dict=dict()
for line in dijkstra_file:
    linesplit = line.split()
    samp_time = linesplit[0]
    bw = linesplit[1]
    if samp_time != 'sec' and bw!= 'received' :
        if float(samp_time)<=20:
            if samp_time not in dijkstra_bw_dict.keys():
                dijkstra_bw_dict.update({samp_time:[bw]})
            else:
                currbw=dijkstra_bw_dict[samp_time]
                currbw.append(bw)
                dijkstra_bw_dict.update({samp_time:currbw})


#mf_bw_dict,dijkstra_bw_dict = remove_keys_with_less_than_three_elements(mf_bw_dict,dijkstra_bw_dict)
time_vector=list(mf_bw_dict.keys())
time_vector=np.asarray(time_vector,dtype=float)

mf_values=list(mf_bw_dict.values())
maxflow_bws=np.asarray(mf_values,dtype=float)
maxflow_sum_bws=maxflow_bws.sum(axis=1)

dijkstra_values=list(dijkstra_bw_dict.values())
dijkstra_bws=np.asarray(dijkstra_values,dtype=float)
dijkstra_sum_bws=dijkstra_bws.sum(axis=1)

plt.plot(time_vector,maxflow_sum_bws,time_vector,dijkstra_sum_bws)
plt.legend(["Maxflow","Dijkstra"])
plt.xlabel(f"time[sec]")
plt.ylabel(f"Throughput[Mb/sec]")
plt.xticks(np.arange(1,21))
plt.yticks(np.arange(1,30,2))
plt.grid()
plt.title("Dijkstra vs Maxflow for UDP")
plt.show()

maxflow_file.close()
dijkstra_file.close()

