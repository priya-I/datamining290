from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches, 
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/
    
    def extractUsers(self,_,record):
        if record['type'] == 'review':
            yield[record['user_id'],record['business_id']]
        
    def userBusiness(self,user_id,business_ids):
            business_id_list=list(business_ids)
            yield["ALL",[user_id,business_id_list]]
            
            
    def jaccard(self,all,entries):
        
        tuples=itertools.combinations(list(entries),2)
        for tuple in tuples:
            user1=tuple[0][0]
            user2=tuple[1][0]
            business1=set(tuple[0][1])
            business2=set(tuple[1][1])
            jvalue=len(business1.intersection(business2))/len(business1.union(business2))
            if(jvalue>=0.5):
                yield[user1,user2]
         

        
    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <user_id, business_id>
        reducer1: <user_id, [business_ids]> => <"ALL",[user_id,[business_ids]]>
        reducer2: <"ALL",[user_id,[business_ids]]> => list of all <user1,user2> 
        """
        return [self.mr(mapper=self.extractUsers, reducer=self.userBusiness),
                self.mr(reducer=self.jaccard)]               


if __name__ == '__main__':
    UserSimilarity.run()

