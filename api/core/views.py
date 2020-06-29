from django.shortcuts import render
# from . forms import MyForm
import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# from . models import approvals
from . models import Document
# from . serializers import approvalsSerializers
from . serializer import DocumentSerializar
# import pickle
# from sklearn.externals import joblib
# import json
# import numpy as np
# from sklearn import preprocessing
# import pandas as pd
import docx


class DocumentView(viewsets.ModelViewSet):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializar
		
@api_view(["POST"])
def prueba(request):
    try:
        mydata=request.FILES
        d = list(mydata.values())
        document = Document(archive=d[0])
        document.save()
        print(document.id)
        lastdocument = Document.objects.get(pk=document.id)
        print(lastdocument.archive)
        
        doc = docx.Document(lastdocument.archive)
        var = ""
        for i in doc.paragraphs:
            if i.text != "":
                var += i.text

        print(var)

        # mdl=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
        # #mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
        # mydata=request.data
        # unit=np.array(list(mydata.values()))
        # unit=unit.reshape(1,-1)
        # scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
        # X=scalers.transform(unit)
        # y_pred=mdl .predict(X)
        # y_pred=(y_pred>0.58)
        # newdf=pd.DataFrame(y_pred, columns=['Status'])
        # newdf=newdf.replace({True:'Approved', False:'Rejected'})
        # return JsonResponse('Your Status is {}'.format(newdf), safe=False)
        return JsonResponse('Your Status is F', safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
