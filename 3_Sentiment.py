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

stemmer = SnowballStemmer(stem)
import matplotlib.pyplot as plt
import matplotlib as mpl
stopwords1=['the', 'a', 'in ', 'for', 'to', 'of', 'and', 'ABC', 'of', 'on', 'at', 
         'or', 'if', 'end', 'were','each', 'was', 'as','has', 'how', 'it', 
           'may', 'often', 'be',  'done', 'these',  'etc', 'made',
          'make', ' the', 'about', 'also', 'always', 'as', 'can',
           'but', 'do', 'get', 'go', 'how', 'is', 'it',  'just', 'lot', 'able',
           'off', 'them', 'they', 'this', 'thus',  'up', 'us', 'very',
           'why', 'your', 'need', ' must', 'now', 'so', 'some',
           'became', 'still', 'stay', 'take', 'took', 'want', 'say',
           'while', 'who', 'you', 'thank', 'new', 'psi', 'any',
           'only','a','about','above','after','again','am','an',
           'and','any','are','aren’t','as','at','be','because','been','before',
           'being','below','between','both','but','by','can’t','cannot','could',
           'couldn’t','did','didn’t','do','does','doesn’t','doing','don’t','down','during',
           'each','few','for','from','further','had','hadn’t','has','hasn’t','have','haven’t',
           'having','he','he’d','he’ll','he’s','her','here','here’s','hers','herself','him','himself',
           'his','how','how’s','i','I’d','I’ll','I’m','I’ve','if','in','into','is','isn’t','it','it’s','its','itself',
           'let’s','me','mustn’t','my','myself','no','nor','not','of','off','on','once',
           'only','or','other','ought','our','ours','ourselves','out','over','own','same','shan’t',
           'she','she’d','she’ll','she’s','should','shouldn’t','so','some','such','than','that','that’s',
           'the','their','theirs','them','themselves','then','there','there’s','these','they','they’d',
           'they’ll','they’re','they’ve','this','those','through','to','too','under','until','up','very',
           'was','wasn’t','we','we’d','we’ll','we’re','we’ve','were','weren’t','what','what’s','when',
           'when’s','where','where’s','which','while','who','who’s','whom','why','why’s','with','won’t',
           'would','wouldn’t','you','you’d','you’ll','you’re','you’ve','your','yours','yourself','yourselves'
           'get', 'our', 'out', 'set', 'such', 'take', 'have', 'did',
           'than', 'their', 'then', 'in', 'when', 'his', 'even',
           'what', 'due', 'via', 'from', 'do', 'does', 'thus', 'sit',
           'he', 'an', 'over', 'had', 'would', 'whoever', 
           'with', 'which', 'within', 'where', 'come',  'there', 'their', 'be', 'between', 'been',  'through',
           'can', 'is', 'this', 'we', 'will', 'without', 'by',  'itself', 'http'
           'about', 'does', 'not', 'that', 'no', 'but', 'are', 'keep','mr', 'ms', ]
stem='english'

def word_count(stopword):
   
   
   #fw=open('App.doc', 'wb')
   #fo=open('Other.doc', 'wb')
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/Ticket_sentiment_pos'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Bo=s1
   
  #________________________________________________________
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/Ticket_sentiment_neu'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Re=s1
   #___________________________________________________________
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/Ticket_sentiment_neg'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Sc=s1
   #_________________________________________________________ 
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/ITIL_sentiment_neg'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Fa=s1
   #_________________________________________________________ 
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/ITIL_sentiment_neu'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Fa1=s1
   #_________________________________________________________
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/Paper_Sentiment/ITIL_sentiment_pos'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Fa2=s1
   #_________________________________________________________
   k_b=0
   #path='Tickets_separated'
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Texts'
   k=0
   fb=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Business_Sentiment.doc', 'wb')
   a=sorted(os.listdir(path))
   #k_w=0
   #k_o=0
   fb.write(bytes('num, length, lang, ticket_pos_Score, ticket_pos_Number, ticket_neu_Score, ticket_neu_Number,ticket_neg_Score,ticket_neg_Number, ITIL_neg_Score, ITIL_neg_Number,ITIL_neu_Score,ITIL_neu_Number,ITIL_pos_Score, ITIL_pos_Number, Expr_neg_Score, Expr_neg_Number,Expr_neu_Score, Expr_neu_Number, Expr_pos_Score, Expr_pos_Number, ITIL_neg_Score, ITIL_neg_Number,ITIL_neu_Score, ITIL_neu_Number'+'\n', 'UTF-8'))
   Bo_stem=[stemmer.stem(w).lower() for w in Bo if len(w) >1 and w.isalpha()]
   Re_stem=[stemmer.stem(w).lower() for w in Re if len(w) >1 and w.isalpha()]
   Sc_stem=[stemmer.stem(w).lower() for w in Sc if len(w) >1 and w.isalpha()]
   Fa_stem=[stemmer.stem(w).lower() for w in Fa if len(w) >1 and w.isalpha()]
   Fa1_stem=[stemmer.stem(w).lower() for w in Fa1 if len(w) >1 and w.isalpha()]
   Fa2_stem=[stemmer.stem(w).lower() for w in Fa2 if len(w) >1 and w.isalpha()]
   
   #print(Fa_stem)
   for i in a[0:9084]: 
   #for i in a[0:2]:   
      #print('# Doc'+str(i))
      e=[]
      enc=0
      
      filename=path+'/'+str(i)
      #print('')
      #print('_______________________________________________________')
      print('# doc:'+str(i))
      #print('_______________________________________________________')

      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         #fb.write(bytes(str(i)+', ', 'UTF-8')) 
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
            #print(a)
            
            if len(a)==0:
               enc=enc+1
            #print(len(line.strip()))
            #print(enc)
            if enc==0:
            
               if len(line.strip())!=0:
                  
                  k=k+1
                  text=line.strip()
                  #print(text)
                  text=re.sub(' +', ' ',text)
                  #print(text)
                  text_CAP=text
                  text=text.lower()
                  text = re.sub(r'\b[0-9]+\b\s*', '', text)
                  print(text)
                  #________________!!!!_________________________________________
                  #mm=re.match(r'\w+!',text)
                  mm_exl = re.findall("(\w+)!", text)
                  print(mm_exl)
                  mm_exl_stem=[stemmer.stem(w).lower() for w in mm_exl if len(w)>1 and w.isalpha()]
                  #print(mm_exl_stem)
                  #_________________######______________________________________
                  #your_string = text
                  #list_of_words = your_string.split()
                  #if "#" in list_of_words:
                  #   mm_ex2 = [list_of_words[list_of_words.index("#") + 1]]
                     #print(mm_ex2)
                  #   mm_ex2_stem=[stemmer.stem(w).lower() for w in mm_ex2 if len(w)>1 and w.isalpha()]
                  #else:
                  #   mm_ex2_stem=[]
                  mm_ex2_stem=[]
                     #print(mm_ex2_stem)
                  #_________________*******______________________________________
                  #your_string = text
                  #list_of_words = your_string.split()
                  #print(list_of_words)
                  #if "*" in list_of_words:
                  #   mm_ex3 = [list_of_words[list_of_words.index("*") + 1]]
                  #   print(mm_ex3)
                  #   mm_ex3_stem=[stemmer.stem(w).lower() for w in mm_ex3 if len(w)>1 and w.isalpha()]
                  #   #print(mm_ex3_stem)
                  #else:
                  mm_ex3_stem=[]
                  #_________________"-----"______________________________________
                  mm_ex4 = re.findall("-- . (\w+)",text)
                  print(mm_ex4)
                  mm_ex4_stem=[stemmer.stem(w).lower() for w in mm_ex4 if len(w)>1 and w.isalpha()]
                  #_________________"======"______________________________________
                  mm_ex5 = re.findall(r'=(\w+)', text)
                  print(mm_ex5)
                  mm_ex5_stem=[stemmer.stem(w).lower() for w in mm_ex5 if len(w)>1 and w.isalpha()]
                  #_________________"->"______________________________________
                  #your_string = text
                  #list_of_words = your_string.split()
                  #if "->" in list_of_words:
                     #mm_ex6 = [list_of_words[list_of_words.index("->") + 1]]
                     #print(mm_ex6)
                     #mm_ex6_stem=[stemmer.stem(w).lower() for w in mm_ex6 if len(w)>1 and w.isalpha()]
                     #print(mm_ex3_stem)
                  #else:
                     #mm_ex6_stem=[]
                  mm_ex6_stem=[]
                  #_________________"CAPS"______________________________________
                  #your_string_CAP = text_CAP
                  #list_of_words_CAP = your_string_CAP.split()
                  #mm_ex7 = filter(None, [x.strip() for x in re.findall(r"\b[A-Z\s]+\b", text_CAP)])
                  mm_ex7 = re.findall('([A-Z]+)', text_CAP)
                  #mm_ex7=map(text_CAP.isupper, text_CAP.split())
                  print(mm_ex7)
                  mm_ex7_stem=[stemmer.stem(w).lower() for w in mm_ex7 if len(w)>1 and w.isalpha()]
                  #print(mm_ex7_stem)
                  
                  #_________________Expressions Tickets______________________________________
                  #text=text.lower()
                  text1 = re.findall(r'big measure', text)
                  a1=len(text1)
                  aa1=a1*(-0.5)
                  text2 = re.findall(r'disaster recovery', text)
                  a2=len(text2)
                  aa2=a2*(0.0)
                  text3 = re.findall(r'set alarms warnings', text)
                  a3=len(text3)
                  aa3=a3*(0.0)
                  text4 = re.findall(r'poison attack vulnerability', text)
                  a4=len(text4)
                  aa4=a4*(0.0)
                  text5 = re.findall(r'critical security leaks', text)
                  a5=len(text5)
                  aa5=a5*(0.0)
                  text6 = re.findall(r'fan', text)
                  a6=len(text6)
                  aa6=a6*(0.0)
                  text7 = re.findall(r'outstanding windows updates', text)
                  a7=len(text7)
                  aa7=a7*(0.0)
                  text8 = re.findall(r'thank you', text)
                  a8=len(text8)
                  aa8=a8*(0.0)
                  text9 = re.findall(r'would like', text)
                  a9=len(text9)
                  aa9=a9*(0.0)
                  text11 = re.findall(r'kind regards', text)
                  a11=len(text11)
                  aa11=a11*(0.0)
                  text12 = re.findall(r'be so kind', text)
                  a12=len(text12)
                  aa12=a12*(0.5)
                  text16 = re.findall(r'best regards', text)
                  a16=len(text16)
                  aa16=a16*(0.0)
                  text13 = re.findall(r'would be nice', text)
                  a13=len(text13)
                  aa13=a13*(0.5)
                  text14 = re.findall(r'no risk', text)
                  a14=len(text14)
                  aa14=a14*(2.0)
                  text15 = re.findall(r'no outage', text)
                  a15=len(text15)
                  aa15=a15*(2.0)

                  exp_neg_num=a1
                  exp_neg_score=aa1
                  exp_neu_num=a2+a3+a4+a5+a6+a7+a8+a9+a11+a16
                  exp_neu_score=0
                  exp_pos_num=a12+a13+a14+a15
                  exp_pos_score=aa12+aa13+aa14+aa15
                  #print(str(exp_neg_score)+';'+str(exp_neg_num)+';'+str(exp_neu_score)+';'+str(exp_neu_num)+';'+str(exp_pos_score)+';'+str(exp_pos_num))

                  #_________________Expressions ITIL______________________________________
                  text16 = re.findall(r'projected service outage', text)
                  a16=len(text16)
                  aa16=a16*(-0.5)
                  text17 = re.findall(r'change advisory board', text)
                  a17=len(text17)
                  aa17=a17*(-0.5)
                  text18 = re.findall(r'high impact', text)
                  a18=len(text18)
                  aa18=a18*(-0.5)
                  text19 = re.findall(r'major change', text)
                  a19=len(text19)
                  aa19=a19*(-0.5)
                  text20 = re.findall(r'request for change', text)
                  a20=len(text20)
                  aa20=a20*(0.0)
                  ITIL_neg_num=a16+a17+a18+a19
                  ITIL_neg_score=aa16+aa17+aa18+aa19
                  ITIL_neu_num=a20
                  ITIL_neu_score=0
                  #print(str(ITIL_neg_score)+';'+str(ITIL_neg_num)+';'+str(ITIL_neu_score)+';'+str(ITIL_neu_num))
                  #print(str(text1)+'.'+str(text2)+'.'+str(text3)+'.'+str(text4)+'.'+str(text5)+'.'+str(text6)+'.'+str(text7)+'.'+str(text8)+'.'+str(text9)+'.'+str(text10)+'.'+str(text11)+'.'+str(text12)+'.'+str(text13)+'.'+str(text14)+'.'+str(text15)+'.'+str(text16)+'.'+str(text17)+'.'+str(text18)+'.'+str(text19) +'.'+str(text20))



                  
                  word=nltk.word_tokenize(text)
                  
                  ooo=len(word)
                  filename1=str(i)
                  fb.write(bytes(str(filename1)+', '+str(ooo)+',', 'UTF-8'))
                  word_stem=[stemmer.stem(w).lower() for w in word if len(w) >1 and w.isalpha()]
                  #print(word_stem)
                  stopWordsG = set(stopwords.words('english'))
                  stopword=[stemmer.stem(w).lower() for w in stopWordsG]

                  stopwords_e = [w for w in word_stem if w in stopword]
                  n_eng=len(stopwords_e) / len(word) * 100
                  #print(n_eng)
                  stopWordsG = set(stopwords.words('german'))
                  stopwords_g = [w for w in word_stem if w in stopWordsG]
                  n_ger=len(stopwords_g) / len(word) * 100
                  #print(n_ger)
                  if n_ger>n_eng:
                     kkk="German"
                  else:
                     kkk="English"
                  #print(kkk)
                  #if kkk!="German":
                     #print (word)
                     
                  word_stop=[ w for w in word_stem if w not in stopwords1]
                  
                  m=word_stop
                  print(m)
                  da={}
                  ds={}
                  dv={}
                  d={}
                  b=[]
                  b1=[]
                  b2=[]
                  b3=[]
                  b4=[]
                  b5=[]
                  b6=[]
                  b7=[]
                                    
                  yy=[]
                  #print('_______________________________________________________')
                  try:
                     
                     b.append(sum([B[Bo_stem.index(w)] for w in m  if w in Bo_stem]))
                     #print("b=",b)
                     b1.append(sum([B_E[Bo_stem.index(w)] for w in mm_exl_stem  if w in Bo_stem]))
                     b2.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex2_stem  if w in Bo_stem]))
                     b3.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex3_stem  if w in Bo_stem]))
                     b4.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex4_stem  if w in Bo_stem]))
                     b5.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex5_stem  if w in Bo_stem]))
                     b6.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex6_stem  if w in Bo_stem]))
                     b7.append(sum([B_E[Bo_stem.index(w)] for w in mm_ex7_stem  if w in Bo_stem]))
                     yy.append(sum([m.count(w) for w in  Bo_stem]))
                     #print("b1=",b1)
                     #print(Bo_stem)
                     #print(mm_exl_stem)
                     #print('T_pol=',  yy[0])
                  except:
                     pass
                  try:
                     b.append(sum([R[Re_stem.index(w)] for w in m if w in Re_stem]))
                     #print("b=",b)
                     b1.append(sum([R_E[Re_stem.index(w)] for w in mm_exl_stem  if w in Re_stem]))
                     b2.append(sum([R_E[Re_stem.index(w)] for w in mm_ex2_stem  if w in Re_stem]))
                     b3.append(sum([R_E[Re_stem.index(w)] for w in mm_ex3_stem  if w in Re_stem]))
                     b4.append(sum([R_E[Re_stem.index(w)] for w in mm_ex4_stem  if w in Re_stem]))
                     b5.append(sum([R_E[Re_stem.index(w)] for w in mm_ex5_stem  if w in Re_stem]))
                     b6.append(sum([R_E[Re_stem.index(w)] for w in mm_ex6_stem  if w in Re_stem]))
                     b7.append(sum([R_E[Re_stem.index(w)] for w in mm_ex7_stem  if w in Re_stem]))
                     yy.append(sum([m.count(w) for w in  Re_stem]))
                     #print("b1=",b1)
                     #print(Re_stem)
                     #print(mm_exl_stem)
                     #print('T_neu=', yy[1])
                  except:
                     pass
                  try:
                     b.append(sum([S[Sc_stem.index(w)] for w in m if w in Sc_stem]))
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  Sc_stem]))
                     b1.append(sum([S_E[Sc_stem.index(w)] for w in mm_exl_stem  if w in Sc_stem]))
                     b2.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex2_stem  if w in Sc_stem]))
                     b3.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex3_stem  if w in Sc_stem]))
                     b4.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex4_stem  if w in Sc_stem]))
                     b5.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex5_stem  if w in Sc_stem]))
                     b6.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex6_stem  if w in Sc_stem]))
                     b7.append(sum([S_E[Sc_stem.index(w)] for w in mm_ex7_stem  if w in Sc_stem]))
                     #print("b1=",b1)
                     #print(Sc_stem)
                     #print(mm_exl_stem)
                     #print('T_neg=',  yy[2])
                  except:
                     pass      
                  try:
                     b.append(sum([F[Fa_stem.index(w)] for w in m  if w in Fa_stem]))
                     print("b=",b)
                     yy.append(sum([m.count(w) for w in  Fa_stem]))
                     b1.append(sum([FF[Fa_stem.index(w)] for w in mm_exl_stem  if w in Fa_stem]))
                     b2.append(sum([FF[Fa_stem.index(w)] for w in mm_ex2_stem  if w in Fa_stem]))
                     b3.append(sum([FF[Fa_stem.index(w)] for w in mm_ex3_stem  if w in Fa_stem]))
                     b4.append(sum([FF[Fa_stem.index(w)] for w in mm_ex4_stem  if w in Fa_stem]))
                     b5.append(sum([FF[Fa_stem.index(w)] for w in mm_ex5_stem  if w in Fa_stem]))
                     b6.append(sum([FF[Fa_stem.index(w)] for w in mm_ex6_stem  if w in Fa_stem]))
                     b7.append(sum([FF[Fa_stem.index(w)] for w in mm_ex7_stem  if w in Fa_stem]))
                     #print("b1=",b1)
                     print(Fa_stem)
                     #print(mm_exl_stem)
                     print('ITIL_neg=', yy[3])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([Fa1_N[Fa1_stem.index(w)] for w in m  if w in Fa1_stem]))
                     print("b=",b)
                     yy.append(sum([m.count(w) for w in  Fa1_stem]))
                     b1.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_exl_stem  if w in Fa1_stem]))
                     b2.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex2_stem  if w in Fa1_stem]))
                     b3.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex3_stem  if w in Fa1_stem]))
                     b4.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex4_stem  if w in Fa1_stem]))
                     b5.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex5_stem  if w in Fa1_stem]))
                     b6.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex6_stem  if w in Fa1_stem]))
                     b7.append(sum([FFa1_N[Fa1_stem.index(w)] for w in mm_ex7_stem  if w in Fa1_stem]))
                     #print("b1=",b1)
                     print(Fa1_stem)
                     #print(mm_exl_stem)
                     print('ITIL_neu=', yy[4])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([Fa2_N[Fa2_stem.index(w)] for w in m  if w in Fa2_stem]))
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  Fa2_stem]))
                     b1.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_exl_stem  if w in Fa2_stem]))
                     b2.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex2_stem  if w in Fa2_stem]))
                     b3.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex3_stem  if w in Fa2_stem]))
                     b4.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex4_stem  if w in Fa2_stem]))
                     b5.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex5_stem  if w in Fa2_stem]))
                     b6.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex6_stem  if w in Fa2_stem]))
                     b7.append(sum([FFa2_N[Fa2_stem.index(w)] for w in mm_ex7_stem  if w in Fa2_stem]))
                     #print("b1=",b1)
                     #print(Fa2_stem)
                     #print(mm_exl_stem)
                     #print('ITIL_pol=', yy[5])
                     #print(yy)
                  except:
                     pass 
                  #if kkk!="German":
                     #print(b)
                     #print(b1)
                     #print(yy)
                  ee=max(b)
                  
                
                  fb.write(bytes(str(kkk)+','+str(b[0]+b1[0]+b2[0]+b3[0]+b4[0]+b5[0]+b6[0]+b7[0])+','+str(yy[0])
                                 +','+str(b[1]+b2[1]+b3[1]+b4[1]+b5[1]+b6[1]+b7[1]+b1[1])+','+str(yy[1])
                                 +','+str(b[2]+b1[2]+b2[2]+b3[2]+b4[2]+b5[2]+b6[2]+b7[2])+','+str(yy[2])
                                 +','+str(b[3]+b1[3]+b2[3]+b3[3]+b4[3]+b5[3]+b6[3]+b7[3]) +','+str(yy[3])
                                 +','+str(b[4]+b1[4]+b2[4]+b3[4]+b4[4]+b5[4]+b6[4]+b7[4])+','+str(yy[4])
                                 +','+str(b[5]+b1[5]+b2[5]+b3[5]+b4[5]+b5[5]+b6[5]+b7[5])+','+str(yy[5])
                                 +','+str(exp_neg_score)+','+str(exp_neg_num)
                                 +','+str(exp_neu_score)+','+str(exp_neu_num)
                                 +','+str(exp_pos_score)+','+str(exp_pos_num)
                                 +','+str(ITIL_neg_score)+','+str(ITIL_neg_num)
                                 +','+str(ITIL_neu_score)+','+str(ITIL_neu_num), 'UTF-8'))
                
                  fb.write(bytes('\n', 'UTF-8'))
 
                     
                 

                  #print('Nouns=',yy[0], '%=',yy[0]/k*100)
                  #print('Verbs=',yy[1], '%=',yy[1]/k*100)
                  #print('Adjectives=',yy[2], '%=',yy[2]/k*100)
                  #print('Adverbs=',yy[3], '%=',yy[3]/k*100)
   
   
   fb.close()
   
B=[0.5, 0.5, 0.5, 0.5, 0.5]
B_E=[0.5, 0.5, 0.5, 0.5, 0.5]
R=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
R_E=[-0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
   -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
   -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1 ]
S=[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.5, -0.5]
S_E=[-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5]


Fa2_N=[0.5, 0.5, 0.5]
FFa2_N=[0.5, 0.5, 0.5]
Fa1_N=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
FFa1_N=[-0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
       -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
       -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
       -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1,
       -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.10, -0.1, -0.1, -0.1,
       -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1]
F=[-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
   -0.5, -0.5, -0.5]
FF=[-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
   -0.5, -0.5, -0.5]

word_count(stopwords)
