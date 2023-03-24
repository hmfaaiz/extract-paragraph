#requirements
#1 django
#2 bs4
#3 request
#4 aspose-words
import aspose.words as aw
from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    return render(request,'base.html')

def extract(request):

    weburl="https://www.microsoft.com/en-pk"
    
    r=requests.get(weburl)
    htmlContent=r.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    f=open('extractfile.txt', 'w') 
    for i in (soup.find_all('p')):  
        para=i.get_text()
        f.write(f"{para}\n")
    
    f.close()
 
    return render(request,'extract.html')

    
def show(request):
     try:
        f=open('extractfile.txt','r')
        lines = f.readlines()
    
        data={"paragraph":lines}
        f.close()

        return render(request,'show.html',data)

     except:
         return render(request,'sorry.html')


    
def download(request):
    try:

        doc = aw.Document("extractfile.txt")
        doc.save("docformat.docx")
        return render(request,'download.html')
    except:
         return render(request,'sorry.html')

    

    