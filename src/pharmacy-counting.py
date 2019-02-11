with open('./input/itcont.txt') as datafile:#reading in the data
    D=[line.rstrip('\n').split(',') for line in datafile]

D=D[1:len(D)]
names = list(set([data[3] for data in D]))#the list of unique drug names

drug_name_count_cost = {name:[0, 0] for name in names}
#drug_name_count_cost = [[name, 0, 0] for name in names]
for data in D:
    drug_name_count_cost[data[3]][0] += 1
    drug_name_count_cost[data[3]][1] += int(data[-1])#adding the price

drug_name_count_cost_list = [[name, drug_name_count_cost[name][0] , drug_name_count_cost[name][1]]for name in drug_name_count_cost.keys()]
drug_name_count_cost_list.sort(key = lambda x: (x[-1],x[0]), reverse=True)#sorting by price and then name

f=open('./output/top_cost_drug.txt', 'w')
f.write('drug_name,num_prescriber,total_cost')
f.close()
for data in drug_name_count_cost_list:#writing the data in a text file
    f = open('./output/top_cost_drug.txt','a')
    f.write('\n'+str(data[0])+','+str(data[1])+','+str(data[2]))
f.close()
