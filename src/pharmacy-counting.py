with open('./input/itcont.txt') as datafile:#reading in the data
    D=[line.rstrip('\n').split(',') for line in datafile]

D=D[1:len(D)]
names = list(set([data[3] for data in D]))#the list of unique drug names

drug_name_count_cost = {name:[0, 0] for name in names}
#drug_name_count_cost = [[name, 0, 0] for name in names]
for data in D:
    #idx=names.index(data[3])#index of drug in the name list
    #drug_name_count_cost[idx][1] += 1#counting ocurrance of each name
    drug_name_count_cost[data[3]][0] += 1
    #drug_name_count_cost[idx][2] = drug_name_count_cost[idx][2]+int(data[-1])#adding the price
    drug_name_count_cost[data[3]][1] += int(data[-1])#adding the price


#drug_name_count_cost.sort(key = lambda x: (x[-1],x[0]), reverse=True)#sorting by price and then name

f=open('./output/top_cost_drug.txt', 'w')
f.write('drug_name,num_prescriber,total_cost')
f.close()
for data in drug_name_count_cost.keys():#writing the data in a text file
    f = open('./output/top_cost_drug.txt','a')
    f.write('\n'+str(data)+','+str(drug_name_count_cost[data][0])+','+str(drug_name_count_cost[data][1]))
f.close()
