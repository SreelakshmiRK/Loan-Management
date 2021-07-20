from django.urls import path
from . import views

urlpatterns = [
    # For URL: http://localhost:8000/loan_mgt/st_loan/Sree/320/1000
    path('st_loan/<str:in_cust_name>/<int:in_credit_score>/<int:in_loan_amt>', views.loan_app, name='st_loan'),


]