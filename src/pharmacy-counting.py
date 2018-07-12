with open('../input/itcont.txt') as datafile:
    D=[line.rstrip('\n').split(',') for line in datafile]
datafile.close()

D=D[1:len(D)]
names = list(set([data[3] for data in D]))

drug_name_count_cost = [[name, 0, 0] for name in names]
for data in D:
    idx=names.index(data[3])
    drug_name_count_cost[idx][1] += 1
    drug_name_count_cost[idx][2] = drug_name_count_cost[idx][2]+float(data[-1])


drug_name_count_cost.sort(key = lambda x: (x[-1],x[0]), reverse=True)
#print drug_name_count_cost
t1=time.time()
f=open('output.txt', 'w')
f.write('drug_name, count, total_cost')
f.close()
for data in drug_name_count_cost:
    f = open('top_cost_drug.txt','a')
    f.write('\n'+str(data[0])+','+str(data[1])+','+str(data[2]))
f.close()
