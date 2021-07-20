from .lms_child import lms_engine as l1
import sys
import os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Python Template
def loan_app(request,in_cust_name,in_credit_score,in_loan_amt):
    template = loader.get_template(r'C:\DjangoLabs\training\tinitiate\loan_mgt\templates\loan_template1.html')
    
    l_cust_name =in_cust_name
    l_cust_creditscore = in_credit_score
    l_cust_requestedloanamount = in_loan_amt
    lms_obj = l1(l_cust_name, l_cust_creditscore, l_cust_requestedloanamount)
    outfile = lms_obj.engine()
    context = {}
    context['name']= l_cust_name
    context['credit_score']= l_cust_creditscore
    context['loan_amt']= l_cust_requestedloanamount
    context['status']= outfile['status']
    context['message']= outfile['message']

        # if l_cust_creditscore < 0:
                # context = 'Error : Invalid Credit score'
            
            # elif l_cust_creditscore > 400:   
                # context = 'Error : Maximum allowed credit score is 400'
            
            # else:
                # lms_obj = l1(l_cust_name, l_cust_creditscore, l_cust_requestedloanamount)
                # context = lms_obj.engine() 
    
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END

