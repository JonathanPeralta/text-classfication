from django.shortcuts import render
# from . forms import MyForm
import json
import logging
import requests

from bs4 import BeautifulSoup
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
import nltk
import inflect
import re
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))

import docx
import tika
from tika import parser
from tika import detector

logger = logging.getLogger(__name__)



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

        lastdocument = Document.objects.get(pk=document.id)

        patharchive = str(lastdocument.archive)

        archivename = patharchive.split('/')[1]
        archivetype = archivename.split('.')[1]
        
        if archivetype=="pdf":
            text = textpdf(patharchive)
        else:
            text = textword(patharchive)

        words = nltk.word_tokenize(text)
        words = normalize(words)
        print(words)
        # datos = urllib.request.urlopen('https://pe.indeed.com/Empleos-de-desarrollador').read().decode()
        # print(datos)
        # URL = 'https://pe.indeed.com/Empleos-de-desarrollador'
        # page = requests.get(URL)
        # print(type(page.content.decode("utf-8")))
        # soup =  BeautifulSoup(page.content.decode("utf-8"),"html.parser")
        # results = soup.find(id='resultsCol')
        # tags = soup('a')
        # mydivs = soup.find_all("div")
        # mydivs = soup.div
        # mydivs =  soup.select('div#resultsCol')
        # mydivs = soup.find({"id": "resultsCol"})
        # mydivs = soup.find_all("div", class_="result")
        # print(type(results))
        # job_elems = results.find_all('div', class_='clickcard')
        # print(results.prettify())
        # print(type(job_elems))
        # print(job_elems)

        lista = []
        # lista = results.prettify()
        # if mydivs != None:
        #     for md in mydivs:
        #         # lista.append(md)
        #         print(md)
        
        
        
        
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
        return JsonResponse({'lista':lista,'res':'ok'}, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)




def textword(document):
    
    doc = docx.Document(document)
    text = ""
    for i in doc.paragraphs:
        if i.text != "":
            text += i.text

    return text




def textpdf(document):

    tika.initVM()
    parsed = parser.from_file(document.encode('utf-8'))
    return parsed["content"]




# print(words)


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    # words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words

# words = normalize(words)