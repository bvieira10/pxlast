#!/usr/bin/env python
# coding: utf-8

# In[1]:


import blpapi
from xbbg import blp

blp.bdp(tickers='NVDA US Equity', flds=['Security_Name', 'GICS_Sector_Name',''])


# In[2]:


time = blp.bdp('AAPL US Equity','LOCAL_TIME')
print(time)


# In[3]:


blp.bdp(['AAPL US Equity','TSLA US Equity','F US Equity','AMZN US Equity','NVDA US Equity'],['SECURITY_NAME','INDUSTRY_SECTOR','PX_LAST','CHG_PCT_1D','CHG_PCT_1M'])


# In[4]:


blp.bds(['LEVE3 BZ Equity ' ,
 'RENT3 BZ Equity ' ,
 'FESA4 BZ Equity ' ,
 'MDIA3 BZ Equity ' ,
 'VIVT3 BZ Equity ' ,
 'GGBR4 BZ Equity ' ,
 'BRML3 BZ Equity ' ,
 'GFSA3 BZ Equity ' ,
 'GOAU4 BZ Equity ' ,
 'SBSP3 BZ Equity ' ,
 'JBSS3 BZ Equity ' ,
 'ALSO3 BZ Equity ' ,
 'VLID3 BZ Equity ' ,
 'BBDC4 BZ Equity ' ,
 'CMIG4 BZ Equity ' ,
 'CYRE3 BZ Equity ' ,
 'ENGI3 BZ Equity ' ,
 'NEOE3 BZ Equity ' ,
 'PCAR3 BZ Equity ' ,
 'ECOR3 BZ Equity ' ,
 'IGTI3 BZ Equity ' ,
 'LREN3 BZ Equity ' ,
 'CPLE6 BZ Equity ' ,
 'VALE3 BZ Equity ' ,
 'BBAS3 BZ Equity ' ,
 'EMBR3 BZ Equity ' ,
 'ENAT3 BZ Equity ' ,
 'EZTC3 BZ Equity ' ,
 'BRFS3 BZ Equity ' ,
 'USIM5 BZ Equity ' ,
 'ITUB4 BZ Equity ' ,
 'SCAR3 BZ Equity ' ,
 'VIIA3 BZ Equity ' ,
 'UGPA3 BZ Equity ' ,
 'LOGN3 BZ Equity ' ,
 'RADL3 BZ Equity ' ,
 'CCRO3 BZ Equity ' ,
 'KEPL3 BZ Equity ' ,
 'AMER3 BZ Equity ' ,
 'GOLL4 BZ Equity ' ,
 'DXCO3 BZ Equity ' ,
 'DIRR3 BZ Equity ' ,
 'ENBR3 BZ Equity ' ,
 'AGRO3 BZ Equity ' ,
 'CSAN3 BZ Equity ' ,
 'MGLU3 BZ Equity ' ,
 'BRAP4 BZ Equity ' ,
 'CPFE3 BZ Equity ' ,
 'TAEE11 BZ Equity ' ,
 'BEEF3 BZ Equity ' ,
 'SYNE3 BZ Equity ' ,
 'TCSA3 BZ Equity ' ,
 'JHSF3 BZ Equity ' ,
 'SULA11 BZ Equity ' ,
 'LPSB3 BZ Equity ' ,
 'MRVE3 BZ Equity ' ,
 'CIEL3 BZ Equity ' ,
 'KLBN4 BZ Equity ' ,
 'EGIE3 BZ Equity ' ,
 'ODPV3 BZ Equity ' ,
 'MRFG3 BZ Equity ' ,
 'MEAL3 BZ Equity ' ,
 'ELET3 BZ Equity ' ,
 'FLRY3 BZ Equity ' ,
 'STBP3 BZ Equity ' ,
 'TIMS3 BZ Equity ' ,
 'MILS3 BZ Equity ' ,
 'DASA3 BZ Equity ' ,
 'BRSR6 BZ Equity ' ,
 'BPAN4 BZ Equity ' ,
 'DEXP3 BZ Equity ' ,
 'CVCB3 BZ Equity ' ,
 'ARZZ3 BZ Equity ' ,
 'B3SA3 BZ Equity ' ,
 'AMAR3 BZ Equity ' ,
 'TEND3 BZ Equity ' ,
 'SANB11 BZ Equity ' ,
 'MYPK3 BZ Equity ' ,
 'ENEV3 BZ Equity ' ,
 'CSMG3 BZ Equity ' ,
 'PRIO3 BZ Equity ' ,
 'TOTS3 BZ Equity ' ,
 'CARD3 BZ Equity ' ,
 'YDUQ3 BZ Equity ' ,
 'EVEN3 BZ Equity ' ,
 'TRIS3 BZ Equity ' ,
 'ABCB4 BZ Equity ' ,
 'ROMI3 BZ Equity ' ,
 'PTBL3 BZ Equity ' ,
 'RAPT4 BZ Equity ' ,
 'POMO4 BZ Equity ' ,
 'ITSA4 BZ Equity ' ,
 'OIBR4 BZ Equity ' ,
 'TUPY3 BZ Equity ' ,
 'SAPR4 BZ Equity ' ,
 'COGN3 BZ Equity ' ,
 'TASA4 BZ Equity ' ,
 'GUAR3 BZ Equity ' ,
 'VULC3 BZ Equity ' ,
 'WEGE3 BZ Equity ' ,
 'PETR4 BZ Equity ' ,
 'MULT3 BZ Equity ' ,
 'EQTL3 BZ Equity ' ,
 'ABEV3 BZ Equity ' ,
 'TRPL4 BZ Equity ' ,
 'LIGT3 BZ Equity ' ,
 'PSSA3 BZ Equity ' ,
 'PFRM3 BZ Equity ' ,
 'QUAL3 BZ Equity ' ,
 'GRND3 BZ Equity ' ,
 'SMTO3 BZ Equity ' ,
 'ALPA4 BZ Equity ' ,
 'HBOR3 BZ Equity ' ,
 'TGMA3 BZ Equity ' ,
 'SLCE3 BZ Equity ' ,
 'RECV3 BZ Equity ' ,
 'CAML3 BZ Equity ' ,
 'CSNA3 BZ Equity ' ,
 'BRKM5 BZ Equity ' ,
 'GPAR3 BZ Equity ' ,
 'POSI3 BZ Equity ' ,
 'BRPR3 BZ Equity ' ,
 'HYPE3 BZ Equity ' ,
 'MDNE3 BZ Equity ' ,
 'SQIA3 BZ Equity ' ,
 'CBAV3 BZ Equity ' ,
 'ASAI3 BZ Equity ' ,
 'OFSA3 BZ Equity ' ,
 'ALUP11 BZ Equity ' ,
 'HBSA3 BZ Equity ' ,
 'IRBR3 BZ Equity ' ,
 'MLAS3 BZ Equity ' ,
 'PGMN3 BZ Equity ' ,
 'LJQQ3 BZ Equity ' ,
 'INTB3 BZ Equity ' ,
 'JALL3 BZ Equity ' ,
 'PARD3 BZ Equity ' ,
 'MATD3 BZ Equity ' ,
 'ALPK3 BZ Equity ' ,
 'RDOR3 BZ Equity ' ,
 'BBSE3 BZ Equity ' ,
 'SEER3 BZ Equity ' ,
 'ANIM3 BZ Equity ' ,
 'WIZS3 BZ Equity ' ,
 'CXSE3 BZ Equity ' ,
 'ONCO3 BZ Equity ' ,
 'CSED3 BZ Equity ' ,
 'VVEO3 BZ Equity ' ,
 'AALR3 BZ Equity ' ,
 'MOVI3 BZ Equity ' ,
 'BPAC11 BZ Equity ' ,
 'CRFB3 BZ Equity ' ,
 'RAIL3 BZ Equity ' ,
 'AZUL4 BZ Equity ' ,
 'BKBR3 BZ Equity ' ,
 'SUZB3 BZ Equity ' ,
 'BLAU3 BZ Equity ' ,
 'VBBR3 BZ Equity ' ,
 'SMFT3 BZ Equity ' ,
 'HAPV3 BZ Equity ' ,
 'LOGG3 BZ Equity ' ,
 'VAMO3 BZ Equity ' ,
 'SBFG3 BZ Equity ' ,
 'NTCO3 BZ Equity ' ,
 'VIVA3 BZ Equity ' ,
 'CEAB3 BZ Equity ' ,
 'MTRE3 BZ Equity ' ,
 'LWSA3 BZ Equity ' ,
 'SOMA3 BZ Equity ' ,
 'TFCO4 BZ Equity ' ,
 'AMBP3 BZ Equity ' ,
 'DMVF3 BZ Equity ' ,
 'PLPL3 BZ Equity ' ,
 'LAVV3 BZ Equity ' ,
 'GMAT3 BZ Equity ' ,
 'PETZ3 BZ Equity ' ,
 'SEQL3 BZ Equity ' ,
 'CURY3 BZ Equity ' ,
 'JSLG3 BZ Equity ' ,
 'BRBI11 BZ Equity ' ,
 'BOAS3 BZ Equity ' ,
 'SIMH3 BZ Equity ' ,
 'MELK3 BZ Equity ' ,
 'CASH3 BZ Equity ' ,
 'ENJU3 BZ Equity ' ,
 'AERI3 BZ Equity ' ,
 'CMIN3 BZ Equity ' ,
 'BMOB3 BZ Equity ' ,
 'RRRP3 BZ Equity ' ,
 'VITT3 BZ Equity ' ,
 'NGRD3 BZ Equity ' ,
 'ORVR3 BZ Equity ' ,
 'ESPA3 BZ Equity ' ,
 'MBLY3 BZ Equity ' ,
 'OPCT3 BZ Equity ' ,
 'WEST3 BZ Equity ' ,
 'ELMD3 BZ Equity ' ,
 'HBRE3 BZ Equity ' ,
 'AGXY3 BZ Equity ' ,
 'AESB3 BZ Equity ' ,
 'IFCM3 BZ Equity ' ,
 'DOTZ3 BZ Equity ' ,
 'GGPS3 BZ Equity ' ,
 'SOJA3 BZ Equity ' ,
 'KRSA3 BZ Equity ' ,
 'ALLD3 BZ Equity ' ,
 'NINJ3 BZ Equity ' ,
 'FIQE3 BZ Equity ' ,
 'TRAD3 BZ Equity ' ,
 'RAIZ4 BZ Equity ' ,
 'ARML3 BZ Equity ' ,
 'DESK3 BZ Equity ' ,
 'TTEN3 BZ Equity ' ,
 'CLSA3 BZ Equity ' ,
 'LVTC3 BZ Equity ' ,
 'BRIT3 BZ Equity ' ,
 'MEGA3 BZ Equity ' ,
 'GETT11 BZ Equity ' ,
 'PORT3 BZ Equity ' ,
 'AURE3 BZ Equity '],['BEST_ANALYST_RECS_BULK'])


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[161.28,159.78,165.90,165.58,165.35,164.87,164.92,169.24,168.49,172.10,173.19,173.03]
plt.plot(x,y)
plt.show()


# In[21]:


aapl_last = blp.bdh('AAPL US Equity','PX_LAST','08/01/2022','08/16/2022')
print(aapl_last)


# In[8]:


blp.bdp( 'LEVE3 BZ Equity ','EBITDA')

blp.bdp('EC527035 Corp',['SECURITY_NAME','YAS_BOND_PX'])

# In[9]:


blp.beqs("rock.py")


# In[10]:


blp.bdp('AAPL US Equity','PX_LAST')


# In[11]:


blp.bds('YCGT0025 Index','CURVE_TENOR_RATES')


# In[12]:


blp.bdp('DAX Index','LAST_PRICE')


# In[13]:


blp.bdp('SPX Index','PCT_MEMB_ABOVE_MOV_AVG_200D')


# In[22]:


curve_tenor = blp.bds('YCSW0023 Index','CURVE_TENOR_RATES')
print(curve_tenor)


# In[15]:


#import psutil

#while True:
    #print(psutil.cpu_percent(interval=1.))


# In[16]:


disc = blp.bds('YCSW0023 Index','SW_CRV_DISCOUNT_FACTORS')
print(disc)


# In[17]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[18]:


blp.bdh(
tickers='SPX Index', flds=['High', 'Low', 'Last_Price'],
start_date='2018-10-10', end_date='2018-10-20',
)

blp.bdh(
tickers = 'LEVE3 BZ Equity ' ,
flds = 'Last_Price',
start_date ='2022-08-01',
end_date ='2022-09-01')

# In[19]:


blp.bdh(['LEVE3 BZ Equity ' ,
 'RENT3 BZ Equity ' ,
 'FESA4 BZ Equity ' ,
 'MDIA3 BZ Equity ' ,
 'VIVT3 BZ Equity ' ,
 'GGBR4 BZ Equity ' ,
 'BRML3 BZ Equity ' ,
 'GFSA3 BZ Equity ' ,
 'GOAU4 BZ Equity ' ,
 'SBSP3 BZ Equity ' ,
 'JBSS3 BZ Equity ' ,
 'ALSO3 BZ Equity ' ,
 'VLID3 BZ Equity ' ,
 'BBDC4 BZ Equity ' ,
 'CMIG4 BZ Equity ' ,
 'CYRE3 BZ Equity ' ,
 'ENGI3 BZ Equity ' ,
 'NEOE3 BZ Equity ' ,
 'PCAR3 BZ Equity ' ,
 'ECOR3 BZ Equity ' ,
 'IGTI3 BZ Equity ' ,
 'LREN3 BZ Equity ' ,
 'CPLE6 BZ Equity ' ,
 'VALE3 BZ Equity ' ,
 'BBAS3 BZ Equity ' ,
 'EMBR3 BZ Equity ' ,
 'ENAT3 BZ Equity ' ,
 'EZTC3 BZ Equity ' ,
 'BRFS3 BZ Equity ' ,
 'USIM5 BZ Equity ' ,
 'ITUB4 BZ Equity ' ,
 'SCAR3 BZ Equity ' ,
 'VIIA3 BZ Equity ' ,
 'UGPA3 BZ Equity ' ,
 'LOGN3 BZ Equity ' ,
 'RADL3 BZ Equity ' ,
 'CCRO3 BZ Equity ' ,
 'KEPL3 BZ Equity ' ,
 'AMER3 BZ Equity ' ,
 'GOLL4 BZ Equity ' ,
 'DXCO3 BZ Equity ' ,
 'DIRR3 BZ Equity ' ,
 'ENBR3 BZ Equity ' ,
 'AGRO3 BZ Equity ' ,
 'CSAN3 BZ Equity ' ,
 'MGLU3 BZ Equity ' ,
 'BRAP4 BZ Equity ' ,
 'CPFE3 BZ Equity ' ,
 'TAEE11 BZ Equity ' ,
 'BEEF3 BZ Equity ' ,
 'SYNE3 BZ Equity ' ,
 'TCSA3 BZ Equity ' ,
 'JHSF3 BZ Equity ' ,
 'SULA11 BZ Equity ' ,
 'LPSB3 BZ Equity ' ,
 'MRVE3 BZ Equity ' ,
 'CIEL3 BZ Equity ' ,
 'KLBN4 BZ Equity ' ,
 'EGIE3 BZ Equity ' ,
 'ODPV3 BZ Equity ' ,
 'MRFG3 BZ Equity ' ,
 'MEAL3 BZ Equity ' ,
 'ELET3 BZ Equity ' ,
 'FLRY3 BZ Equity ' ,
 'STBP3 BZ Equity ' ,
 'TIMS3 BZ Equity ' ,
 'MILS3 BZ Equity ' ,
 'DASA3 BZ Equity ' ,
 'BRSR6 BZ Equity ' ,
 'BPAN4 BZ Equity ' ,
 'DEXP3 BZ Equity ' ,
 'CVCB3 BZ Equity ' ,
 'ARZZ3 BZ Equity ' ,
 'B3SA3 BZ Equity ' ,
 'AMAR3 BZ Equity ' ,
 'TEND3 BZ Equity ' ,
 'SANB11 BZ Equity ' ,
 'MYPK3 BZ Equity ' ,
 'ENEV3 BZ Equity ' ,
 'CSMG3 BZ Equity ' ,
 'PRIO3 BZ Equity ' ,
 'TOTS3 BZ Equity ' ,
 'CARD3 BZ Equity ' ,
 'YDUQ3 BZ Equity ' ,
 'EVEN3 BZ Equity ' ,
 'TRIS3 BZ Equity ' ,
 'ABCB4 BZ Equity ' ,
 'ROMI3 BZ Equity ' ,
 'PTBL3 BZ Equity ' ,
 'RAPT4 BZ Equity ' ,
 'POMO4 BZ Equity ' ,
 'ITSA4 BZ Equity ' ,
 'OIBR4 BZ Equity ' ,
 'TUPY3 BZ Equity ' ,
 'SAPR4 BZ Equity ' ,
 'COGN3 BZ Equity ' ,
 'TASA4 BZ Equity ' ,
 'GUAR3 BZ Equity ' ,
 'VULC3 BZ Equity ' ,
 'WEGE3 BZ Equity ' ,
 'PETR4 BZ Equity ' ,
 'MULT3 BZ Equity ' ,
 'EQTL3 BZ Equity ' ,
 'ABEV3 BZ Equity ' ,
 'TRPL4 BZ Equity ' ,
 'LIGT3 BZ Equity ' ,
 'PSSA3 BZ Equity ' ,
 'PFRM3 BZ Equity ' ,
 'QUAL3 BZ Equity ' ,
 'GRND3 BZ Equity ' ,
 'SMTO3 BZ Equity ' ,
 'ALPA4 BZ Equity ' ,
 'HBOR3 BZ Equity ' ,
 'TGMA3 BZ Equity ' ,
 'SLCE3 BZ Equity ' ,
 'RECV3 BZ Equity ' ,
 'CAML3 BZ Equity ' ,
 'CSNA3 BZ Equity ' ,
 'BRKM5 BZ Equity ' ,
 'GPAR3 BZ Equity ' ,
 'POSI3 BZ Equity ' ,
 'BRPR3 BZ Equity ' ,
 'HYPE3 BZ Equity ' ,
 'MDNE3 BZ Equity ' ,
 'SQIA3 BZ Equity ' ,
 'CBAV3 BZ Equity ' ,
 'ASAI3 BZ Equity ' ,
 'OFSA3 BZ Equity ' ,
 'ALUP11 BZ Equity ' ,
 'HBSA3 BZ Equity ' ,
 'IRBR3 BZ Equity ' ,
 'MLAS3 BZ Equity ' ,
 'PGMN3 BZ Equity ' ,
 'LJQQ3 BZ Equity ' ,
 'INTB3 BZ Equity ' ,
 'JALL3 BZ Equity ' ,
 'PARD3 BZ Equity ' ,
 'MATD3 BZ Equity ' ,
 'ALPK3 BZ Equity ' ,
 'RDOR3 BZ Equity ' ,
 'BBSE3 BZ Equity ' ,
 'SEER3 BZ Equity ' ,
 'ANIM3 BZ Equity ' ,
 'WIZS3 BZ Equity ' ,
 'CXSE3 BZ Equity ' ,
 'ONCO3 BZ Equity ' ,
 'CSED3 BZ Equity ' ,
 'VVEO3 BZ Equity ' ,
 'AALR3 BZ Equity ' ,
 'MOVI3 BZ Equity ' ,
 'BPAC11 BZ Equity ' ,
 'CRFB3 BZ Equity ' ,
 'RAIL3 BZ Equity ' ,
 'AZUL4 BZ Equity ' ,
 'BKBR3 BZ Equity ' ,
 'SUZB3 BZ Equity ' ,
 'BLAU3 BZ Equity ' ,
 'VBBR3 BZ Equity ' ,
 'SMFT3 BZ Equity ' ,
 'HAPV3 BZ Equity ' ,
 'LOGG3 BZ Equity ' ,
 'VAMO3 BZ Equity ' ,
 'SBFG3 BZ Equity ' ,
 'NTCO3 BZ Equity ' ,
 'VIVA3 BZ Equity ' ,
 'CEAB3 BZ Equity ' ,
 'MTRE3 BZ Equity ' ,
 'LWSA3 BZ Equity ' ,
 'SOMA3 BZ Equity ' ,
 'TFCO4 BZ Equity ' ,
 'AMBP3 BZ Equity ' ,
 'DMVF3 BZ Equity ' ,
 'PLPL3 BZ Equity ' ,
 'LAVV3 BZ Equity ' ,
 'GMAT3 BZ Equity ' ,
 'PETZ3 BZ Equity ' ,
 'SEQL3 BZ Equity ' ,
 'CURY3 BZ Equity ' ,
 'JSLG3 BZ Equity ' ,
 'BRBI11 BZ Equity ' ,
 'BOAS3 BZ Equity ' ,
 'SIMH3 BZ Equity ' ,
 'MELK3 BZ Equity ' ,
 'CASH3 BZ Equity ' ,
 'ENJU3 BZ Equity ' ,
 'AERI3 BZ Equity ' ,
 'CMIN3 BZ Equity ' ,
 'BMOB3 BZ Equity ' ,
 'RRRP3 BZ Equity ' ,
 'VITT3 BZ Equity ' ,
 'NGRD3 BZ Equity ' ,
 'ORVR3 BZ Equity ' ,
 'ESPA3 BZ Equity ' ,
 'MBLY3 BZ Equity ' ,
 'OPCT3 BZ Equity ' ,
 'WEST3 BZ Equity ' ,
 'ELMD3 BZ Equity ' ,
 'HBRE3 BZ Equity ' ,
 'AGXY3 BZ Equity ' ,
 'AESB3 BZ Equity ' ,
 'IFCM3 BZ Equity ' ,
 'DOTZ3 BZ Equity ' ,
 'GGPS3 BZ Equity ' ,
 'SOJA3 BZ Equity ' ,
 'KRSA3 BZ Equity ' ,
 'ALLD3 BZ Equity ' ,
 'NINJ3 BZ Equity ' ,
 'FIQE3 BZ Equity ' ,
 'TRAD3 BZ Equity ' ,
 'RAIZ4 BZ Equity ' ,
 'ARML3 BZ Equity ' ,
 'DESK3 BZ Equity ' ,
 'TTEN3 BZ Equity ' ,
 'CLSA3 BZ Equity ' ,
 'LVTC3 BZ Equity ' ,
 'BRIT3 BZ Equity ' ,
 'MEGA3 BZ Equity ' ,
 'GETT11 BZ Equity ' ,
 'PORT3 BZ Equity ' ,
 'AURE3 BZ Equity '],'PX_LAST','2000-01-01','2022-09-01')


# In[20]:


print ('DONE')


# In[ ]:




