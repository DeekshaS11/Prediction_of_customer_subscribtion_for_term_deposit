

# Create your views here.

from django.shortcuts import render
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report



def result(request):
    if(request.method=='POST'):
        path = "C:\\Users\\user\\Downloads\\train.csv"
        data = pd.read_csv(path)
        data.isnull()
        data.isnull().sum()
        le = LabelEncoder()
        data['job_n'] = le.fit_transform(data['job'])
        data['marital_n'] = le.fit_transform(data['marital'])
        data['education_n'] = le.fit_transform(data['education'])
        data['default_n'] = le.fit_transform(data['default'])
        data['housing_n'] = le.fit_transform(data['housing'])
        data['loan_n'] = le.fit_transform(data['loan'])
        data['contact_n'] = le.fit_transform(data['contact'])
        data['month_n'] = le.fit_transform(data['month'])
        data['poutcome_n'] = le.fit_transform(data['poutcome'])
        inputs=data.drop(['job','marital','education','default','housing','loan','contact','month','poutcome','y_bool'],axis=1)
        output=data.drop(['age','balance','day','duration','campaign','pdays','previous','job','marital','education','default','housing','loan','contact','month','poutcome','job_n','marital_n','education_n','default_n','housing_n','loan_n','contact_n','month_n','poutcome_n'],axis=1)

        model=KNeighborsClassifier(n_neighbors=13)
        model.fit(inputs,output)

        data = request.POST
        age = int(data.get('age'))
        job_n= int(data.get('job'))
        marital_n = int(data.get('marital'))
        education_n = int(data.get('education'))
        default_n = int(data.get('default'))
        balance = int(data.get('balance'))
        housing_n = int(data.get('housing'))
        loan_n = int(data.get('loan'))
        contact_n = int(data.get('contact'))
        day = float(data.get('day'))
        month_n = int(data.get('month'))
        duration = int(data.get('duration'))
        campaign = int(data.get('campaign'))
        p_days = int(data.get('p_days'))
        previous = int(data.get('previous'))
        poutcome_n = int(data.get('poutcome'))
    

        result = model.predict([
            [age,job_n,marital_n,education_n,default_n,balance,housing_n,loan_n,contact_n,day,month_n,duration,campaign,p_days,previous,poutcome_n]
        ])

        if result[0] == 0:
            res = 'sub'
        else:
            res = 'unsub'

        return render(request, 'index.html',context={'result': res})
    return render(request, 'index.html')