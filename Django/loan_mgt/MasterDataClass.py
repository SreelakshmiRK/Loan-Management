
class master:

    def __init__(self):

        self.masterdata = ( {"cs_start":0  , "cs_end": 100, "LoanAmtStart": 10001,"LoanAmtEnd": 20000, "Interest": 8  , "Duration":72 }
                          ,{"cs_start":0  , "cs_end": 100, "LoanAmtStart": 20001,"LoanAmtEnd": 30000, "Interest": 8  , "Duration":72 }
                          ,{"cs_start":0  , "cs_end": 100, "LoanAmtStart": 30001,"LoanAmtEnd": 40000, "Interest": 9  , "Duration":72 }
                          ,{"cs_start":101, "cs_end": 201, "LoanAmtStart": 0    ,"LoanAmtEnd": 10000, "Interest": 6  , "Duration":72 }
                          ,{"cs_start":101, "cs_end": 201, "LoanAmtStart": 10001,"LoanAmtEnd": 20000, "Interest": 6  , "Duration":72 }
                          ,{"cs_start":101, "cs_end": 201, "LoanAmtStart": 20001,"LoanAmtEnd": 30000, "Interest": 6  , "Duration":72 }
                          ,{"cs_start":101, "cs_end": 201, "LoanAmtStart": 30001,"LoanAmtEnd": 40000, "Interest": 7  , "Duration":72 }
                          ,{"cs_start":201, "cs_end": 301, "LoanAmtStart": 0    ,"LoanAmtEnd": 10000, "Interest": 5.5, "Duration":72 }
                          ,{"cs_start":201, "cs_end": 301, "LoanAmtStart": 10001,"LoanAmtEnd": 20000, "Interest": 5.5, "Duration":72 }
                          ,{"cs_start":201, "cs_end": 301, "LoanAmtStart": 20001,"LoanAmtEnd": 30000, "Interest": 5.5, "Duration":72 }
                          ,{"cs_start":201, "cs_end": 301, "LoanAmtStart": 30001,"LoanAmtEnd": 40000, "Interest": 6  , "Duration":72 }
                          ,{"cs_start":301, "cs_end": 400, "LoanAmtStart": 0    ,"LoanAmtEnd": 10000, "Interest": 4  , "Duration":72 }
                          ,{"cs_start":301, "cs_end": 400, "LoanAmtStart": 10001,"LoanAmtEnd": 20000, "Interest": 4  , "Duration":72 }
                          ,{"cs_start":301, "cs_end": 400, "LoanAmtStart": 20001,"LoanAmtEnd": 30000, "Interest": 4  , "Duration":72 }
                          ,{"cs_start":301, "cs_end": 400, "LoanAmtStart": 30001,"LoanAmtEnd": 40000, "Interest": 5  , "Duration":72 }
                         )
                         
    def loandata(self):
    
        return(self.masterdata)
                         
    # def greetings(p_cust):
        # x =  print("Hello", p_cust)
        # return(x)
    

