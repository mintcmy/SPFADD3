import os,sys
import math
import random
import time 
def map_add(mp, key1,key2, value):
    if (key1 not in mp):
        mp[key1] = {}
    if (key2 not in mp[key1]):
        mp[key1][key2] = 0.0
    mp[key1][key2] += value
    

def map_add1(mp,key):
    if (key not in mp):
        mp[key] = 0
    mp[key]+=1


f = open("data/relation2id.txt","r")
relation2id = {}
id2relation = {}
relation_num = 0
for line in f:
    seg = line.strip().split()
    relation2id[seg[0]] = int(seg[1])
    id2relation[int(seg[1])]=seg[0]
    id2relation[int(seg[1])+1345]="~"+seg[0]
    relation_num+=1
f.close()
f = open("data/train.txt","r")
ok = {}
a ={}

num=0
step=0


for line in f:
    seg = line.strip().split()
    e1 = seg[0]
    e2 = seg[1]
    rel = seg[2]
    if (e1+" "+e2 not in ok):
        ok[e1+" "+e2]={}
    ok[e1+" "+e2][relation2id[rel]]=1
    if (e2+" "+e1 not in ok):
        ok[e2+" "+e1]={}
    ok[e2+" "+e1][relation2id[rel]+relation_num]=1
    if (e1 not in a):
        a[e1]={}
    if (relation2id[rel] not in a[e1]):
        a[e1][relation2id[rel]]={}
    a[e1][relation2id[rel]][e2]=1
    if (e2 not in a):
        a[e2]={}
    if ((relation2id[rel]+relation_num) not in a[e2]):
        a[e2][relation2id[rel]+relation_num]={}
    a[e2][relation2id[rel]+relation_num][e1]=1
f.close()


f = open("data/test.txt","r")
for line in f:
    seg = line.strip().split()
    if (seg[0]+" "+seg[1] not in ok):
        ok[seg[0]+' '+seg[1]]={}
    if (seg[1]+" "+seg[0] not in ok):
        ok[seg[1]+' '+seg[0]]={}
f.close()


f = open("data/e1_e2.txt","r")
for line in f:
    seg = line.strip().split()
    ok[seg[0]+" "+seg[1]] = {}
    ok[seg[1]+" "+seg[0]] = {}
f.close()


path_dict = {}
path_r_dict = {}

for e1 in a:
    for rel1 in a[e1]:
        e2_set = a[e1][rel1]
        for e2 in e2_set:
            map_add1(path_dict,str(rel1))
            for key in ok[e1+' '+e2]:
                map_add1(path_r_dict,str(rel1)+"->"+str(key))
            if (e2 in a):
                for rel2 in a[e2]:
                    e3_set = a[e2][rel2]
                    for e3 in e3_set:
                        map_add1(path_dict,str(rel1)+" "+str(rel2))
                        if (e1+" "+e3 in ok):
                            for key in ok[e1+' '+e3]:
                                map_add1(path_r_dict,str(rel1)+" "+str(rel2)+"->"+str(key))
 

g = open("data/path_1.txt","w")

for key in path_dict:
    g.write(key+" "+str(path_dict[key])+"\n")

g.close()

g = open("data/path_2.txt","w")

for key in path_r_dict:
    g.write(key+" "+str(path_r_dict[key])+"\n")

g.close()