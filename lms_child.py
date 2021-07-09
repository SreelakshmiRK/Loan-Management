from MasterDataClass import master as m1

class lms_engine(m1):

    def __init__(self, p_cust_name, p_cust_creditscore, p_cust_requestedloanamount):
    
        self.cust_name = p_cust_name
        self.cust_creditscore = p_cust_creditscore
        self.cust_requestedloanamount = p_cust_requestedloanamount
        m1.__init__(self)
        #super().__init__()
        self.loan_application_data = {}

        
    def engine(self):
    
        #self.loan_masterdata = super().loandata()
        self.loan_masterdata = m1.loandata(self)

        for mdata in self.loan_masterdata : 
            if (self.cust_creditscore >= mdata['cs_start']) and (self.cust_creditscore <= mdata['cs_end']) and (self.cust_requestedloanamount >= mdata['LoanAmtStart']) and (self.cust_requestedloanamount <= mdata['LoanAmtEnd']):
                    self.loan_application_data['status'] = 'Approved'
                    self.loan_application_data['message'] = """Dear {cust},
                    We are pleased to inform that your requested loan amount of ${amt} has been approved with an 
                    interest rate of {rate}% for a duration of {dur} months.""".format(cust=self.cust_name, amt=self.cust_requestedloanamount, rate = mdata["Interest"], dur =mdata['Duration'])
                    self.loan_application_data['interest'] = mdata['Interest'] 
                    self.loan_application_data['duration'] = mdata['Duration']
        if self.cust_requestedloanamount> 40000:
            self.loan_application_data['status'] = 'Denied'
            self.loan_application_data['message'] ="""Dear {cust},
                      We regret to inform that your requested loan amount of ${amt} has been rejected 
                      since the maximum loan amount cannot exceed $40000""".format(cust=self.cust_name, amt=self.cust_requestedloanamount)
        elif self.cust_requestedloanamount < 10001 and self.cust_creditscore <101:
            self.loan_application_data['status'] = 'Denied'
            self.loan_application_data['message']="""Dear {cust},
                      We regret to inform that your requested loan amount of ${amt} has been rejected 
                      since the minimum loan amount cannot be less than $10000 if your credit score less than 101""".format(cust=self.cust_name, amt=self.cust_requestedloanamount)
        # elif self.cust_creditscore < 0:
            # self.loan_application_data['status'] = 'Error'
            # self.loan_application_data['message']= 'Invalid Credit score'
            
        # elif self.cust_creditscore > 400:
            # self.loan_application_data['status'] = 'Error'
            # self.loan_application_data['message']= 'Maximum allowed credit score is 400'
        return (self.loan_application_data) 


    # In[ ]:



