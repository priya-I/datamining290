'''
Created on Feb 27, 2013

@author: priya, jim blomo
'''
#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.
Classes are strings."""

import fileinput
import csv
from collections import defaultdict
from collections import Counter
from decimal import Decimal

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)

def ginical(numer,denom):
    ginival=1-(Decimal(numer)/Decimal(denom**2))
    return ginival

############### Set up variables
cnames=Counter()
amount_names=defaultdict(Counter)
zipnames=defaultdict(Counter)
zipcodes=[]
steps=[1000,5000]
############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # Steps to calculate Gini Index by candidate names and candidate zip codes
        bracket=0
        name=row[cand_nm]
        cnames[name]+=1
        zipcode=row[contbr_zip]
        zipnames[zipcode][name]+=1
        contr_amt=float(row[contb_receipt_amt])
        if contr_amt>1000:
            amount_names["partition"][name]+=1
        else:
            amount_names["rest"][name]+=1
        ##/
###
#Current Gini Index using candidate name as the class
gini = 0
#Calculating the total number of records in the dataset  
sumcount=sum(cnames.values())

#Calculating the fraction of each class in the dataset
fraction=sum(each**2 for each in cnames.values())

#Part 1: Calculating the gini index of the dataset by candidate name
gini=ginical(fraction,sumcount)

#Part 2: Calculating the weighted average of the Gini Indexes using candidate names, split up by zip code
##/
split_gini = 0
numerator=0
#Iterating over the (Candidate Name, Count) pair for every zipcode
for record in zipnames.values():
    partialsum=sum(record.values())
    frac_zip=sum(each**2 for each in record.values())
    
    #Could move this computation to a separate method but not now !
    part_gini=ginical(frac_zip,partialsum)
    
    #Numerator calculated by taking the weighted sum of the partitions' gini indexes
    numerator+=part_gini*partialsum
    
#Calculating the weighted average of all the gini indexes
split_gini=Decimal(numerator)/Decimal(sumcount)

print "Gini Index: %s" % round(gini,3)
print "Gini Index after split: %s" % round(split_gini,3)

#Extra Credit
numerator=0
for record in amount_names.values():
    partialsum=sum(record.values())
    frac=sum(each**2 for each in record.values())
    part_gini=ginical(frac,partialsum)
    numerator+=part_gini*partialsum
cont_gini=Decimal(numerator)/Decimal(sumcount)
print "Gini Index for Thousand: %s" %round(cont_gini,3) 

'''
Gini Index: 0.291
Gini Index after split: 0.042
** Individual computation of continuous ranges: Extra Credit
Gini Index for Thousand: 0.284 (Best Score)
Gini Index for Zero: 0.291
Gini Index for Ten Thousand: 0.291
Gini Index for Twenty Thousand: 0.291
'''
