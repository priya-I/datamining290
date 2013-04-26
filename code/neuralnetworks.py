'''
Created on Mar 4, 2013

@author: priya
'''
#Target
t_6=0

#Node weights
outputs={'w_6':[0.8387,0]}
hiddens={'w_5':0.9933,'w_4':0.0179,'w_3':0.7311}
inputs={'w_2':2,'w_1':1}

#Edge weights
hidden_out={'w_36':0.2,'w_46':0.7,'w_56':1.5}
in_hidden={'w_13':-3,'w_14':2,'w_15':4,'w_23':2,'w_24':-3,'w_25':0.5}
h_node_conn={'3':[6],'4':[6],'5':[6]}
i_node_conn={'1':[3,4,5],'2':[3,4,5]}
#TODO: Create a file that takes all of the above as input


def err_hidden(w_next,edges_list):
    sum_of_edges=0
    for err_next,w_edge in edges_list:
        sum_of_edges+=err_next*w_edge
    err_hid=w_next*(1-w_next)*sum_of_edges
    return err_hid



def err_output(w_j,t_j):
    err_op=w_j*(1-w_j)*(t_j-w_j)
    return err_op

def new_weight(w_ij,err_j,o_i,I=10):
    nw_ij=w_ij+I*err_j*o_i
    return nw_ij

#Find the error in weight of output node.
errOps={'err_1':0,'err_2':0}  

for output in outputs:
    node_id=output[2]
    w_j=outputs[output][0]
    t_j=outputs[output][1]
    errOps['err_'+node_id]=err_output(w_j, t_j)

#Find the error in weight of the hidden nodes
for node in hiddens:
    node_id=node[2]
    w_curr=hiddens[node]
    edge_list=[]
    for conn in h_node_conn[str(node_id)]:
        next_id=str(conn)
        err_next=errOps['err_'+next_id]
        edge_id='w_'+node_id+next_id
        w_edge=hidden_out[edge_id]
        edge_list.append((err_next,w_edge))
    errOps['err_'+node_id]=err_hidden(w_curr,edge_list)
    
    
#Find the new weight of the edges between hidden and output nodes
w_ho={}
for conn in h_node_conn:
    node_id='w_'+conn
    err_node_id='err_'+conn
    for node in h_node_conn[conn]:
        next_id=str(node)
        edge_id=node_id+next_id
        w_ij=hidden_out[edge_id]
        err_j=errOps['err_'+next_id]
        w_i=hiddens[node_id]
        w_ho[edge_id]=new_weight(w_ij, err_j, w_i, I=10)

#Find the new weight of the edges between input and hidden nodes
w_ih={}
for conn in i_node_conn:
    node_id='w_'+conn
    err_node_id='err_'+conn
    for node in i_node_conn[conn]:
        next_id=str(node)
        edge_id=node_id+next_id
        w_ij=in_hidden[edge_id]
        err_j=errOps['err_'+next_id]
        w_i=inputs[node_id]
        w_ih[edge_id]=new_weight(w_ij, err_j, w_i, I=10)

#Print error values
print "Error in the node outputs are:"
for value in errOps:
    print str(value)+" : "+str(round(errOps[value],5))
    
print "\n"
print "Error in the node weights are:"
for key in w_ho:
    print str(key)+" : "+str(round(w_ho[key],5))

for key in w_ih:
    print str(key)+" : "+str(round(w_ih[key],5))
    
    
    
'''Output:
Error in the node outputs are:
err_5 : -0.0011
err_4 : -0.0014
err_6 : -0.1135
err_1 : 0.0
err_3 : -0.0045
err_2 : 0.0


Error in the node weights are:
w_56 : 0.373
w_46 : 0.6797
w_36 : -0.6295
w_23 : 1.9108
w_24 : -3.0279
w_25 : 0.4773
w_13 : -3.0446
w_15 : 3.9887
w_14 : 1.986

'''