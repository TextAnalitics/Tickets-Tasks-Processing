#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter.filedialog import *
from tkinter.messagebox import *
import chardet
from gensim import corpora, models
#from settings import stopwords
import codecs
import sys, os
import os.path
import nltk
import re
import requests
import numpy
from numpy import *
import nltk
import scipy
from tkinter import Tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from settings import stem
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer
import re
stemmer = SnowballStemmer(stem)
import matplotlib.pyplot as plt
import matplotlib as mpl
stopwords1=['the', 'a', 'in ', 'for', 'to', 'of', 'and', 'ABC', 'of', 'on', 'at', 
         'or', 'if', 'end', 'were','each', 'was', 'as','has', 'how', 'it', 
           'may', 'often', 'be',  'done', 'these', 'all', 'etc', 'made',
          'make', ' the', 'about', 'also', 'always', 'as', 'can',
           'but', 'do', 'get', 'go', 'how', 'is', 'it',  'just', 'lot', 'able',
           'off', 'them', 'they', 'this', 'thus',  'up', 'us', 'very',
           'why', 'your', 'need', ' must', 'now', 'so', 'some',
           'became', 'still', 'stay', 'take', 'took', 'want', 'say',
           'while', 'who', 'you', 'thank', 'new', 'psi', 'busy', 'any',
           'only','a','about','above','after','again','against','all','am','an',
           'and','any','are','aren’t','as','at','be','because','been','before',
           'being','below','between','both','but','by','can’t','cannot','could',
           'couldn’t','did','didn’t','do','does','doesn’t','doing','don’t','down','during',
           'each','few','for','from','further','had','hadn’t','has','hasn’t','have','haven’t',
           'having','he','he’d','he’ll','he’s','her','here','here’s','hers','herself','him','himself',
           'his','how','how’s','i','I’d','I’ll','I’m','I’ve','if','in','into','is','isn’t','it','it’s','its','itself',
           'let’s','me','more','most','mustn’t','my','myself','no','nor','not','of','off','on','once',
           'only','or','other','ought','our','ours','ourselves','out','over','own','same','shan’t',
           'she','she’d','she’ll','she’s','should','shouldn’t','so','some','such','than','that','that’s',
           'the','their','theirs','them','themselves','then','there','there’s','these','they','they’d',
           'they’ll','they’re','they’ve','this','those','through','to','too','under','until','up','very',
           'was','wasn’t','we','we’d','we’ll','we’re','we’ve','were','weren’t','what','what’s','when',
           'when’s','where','where’s','which','while','who','who’s','whom','why','why’s','with','won’t',
           'would','wouldn’t','you','you’d','you’ll','you’re','you’ve','your','yours','yourself','yourselves'
           'get', 'our', 'out', 'set', 'such', 'take', 'have', 'did',
           'than', 'their', 'then', 'well', 'in', 'when', 'his', 'even',
           'what', 'due', 'via', 'from', 'do', 'does', 'thus', 'sit',
           'he', 'an', 'over', 'had', 'would', 'whoever', 'after',
           'with', 'which', 'within', 'where', 'come', 'more',
           'there', 'their', 'be', 'between', 'been',  'through',
           'can', 'is', 'this', 'we', 'will', 'give', 'without', 'by',  'itself', 'http'
           'about', 'does', 'not', 'that', 'no', 'but', 'are', 'keep','mr', 'ms', 'ayakkab', 'allah', 'bunyamin', '\ufeff']
stem='english'



def word_count(stopword):
   
   
   
   
   #_________________________________________________________ 
   k_b=0
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Texts'
   k=0
   
   fb1=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Tasks_Types_1.doc', 'wb')
   a=sorted(os.listdir(path))
   
   #k_w=0
   #k_o=0
   
   #fb1.write(bytes('"File"."Task"."length"'+'\n', 'UTF-8'))
   fb1.write(bytes('"File"."QS"."QA"."PSO"."Install"."4EP"."Implementation"."Infotask"."Support"."Execution"."Four eyes principle"'+'\n', 'UTF-8'))
   #print(Fa_stem)
   for i in a[0:9084]:
   #for i in a[0:5]:
      print('# Doc'+str(i))
      e=[]
      enc=0
      filename1=str(i)
      filename=path+'/'+str(i)
      #print('')
      #print('_______________________________________________________')
      #print('# doc:'+str(i))
      #print('_______________________________________________________')

      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         #fb.write(bytes(str(i)+', ', 'UTF-8')) 
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
  
            #Tasks

            #text1 = re.findall(r"(?:[a-zA-Z'-]+[^a-zA-Z'-]+){0,5}task(?:[^a-zA-Z'-]+[a-zA-Z'-]+){0,5}", a)
            text2 = re.findall(r'QS', a)
            text3 = re.findall(r'QA', a)
            text4 = re.findall(r'PSO', a)
            text5 = re.findall(r'Install', a)
            text6 = re.findall(r'4EP', a)
            text7 = re.findall(r'Implementation', a)
            text8 = re.findall(r'Infotask', a)
            text9 = re.findall(r'Support', a)
            text10 = re.findall(r'Execution', a)
            text11 = re.findall(r'Four eyes principle', a)
            text12 = re.findall(r'DB isntance', a)
            text13 = re.findall(r'Stop application', a)
            text14 = re.findall(r'Start application', a)
            text15 = re.findall(r'Quality Assurance', a)
            text16 = re.findall(r'Downtime', a)
            text17 = re.findall(r'Stop database', a)
            text18 = re.findall(r'Start database', a)
            text19 = re.findall(r'installation', a)
            text21 = re.findall(r'Application stop ', a)
            text22 = re.findall(r'Stop the application', a)
            text24 = re.findall(r'Application start ', a)
            text25 = re.findall(r'Start the application', a)
            text23 = re.findall(r'4 EP', a)
                
                         
            fb1.write(bytes(str(filename1)+'. '+str(text2)+'.'+str(text3)+'.'+str(text4)+'.'+str(text5)+'.'+str(text6)+'.'+str(text7)+'.'+str(text8)+'.'+str(text9)+'.'+str(text11)+'.'+str(text12)+'.'+str(text13)+'.'+str(text14)+'.'+str(text15)+'.'+str(text16)+'.'+str(text17)+'.'+str(text18)+'.'+str(text19)+'.'+str(text21)+'.'+str(text22)+'.'+str(text24)+'.'+str(text25)+'.'+str(text23), 'UTF-8'))
            fb1.write(bytes('\n', 'UTF-8'))
                     
                 

   
   
   fb1.close()
   



word_count(stopwords)
