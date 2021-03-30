# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:53:41 2021

author: AMS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_json("data/MBene.txt")
df.set_index("rIndex", inplace = True)
df[pd.isnull(df["rValue"])]
df[pd.isnull(df["rTagName"])]
df[pd.isnull(df["rTimestamp"])]
df[pd.isnull(df["rConfidence"])]

df = df.astype({'rTimestamp': 'datetime64[ns]'})

descriptivo_basico = df.describe(percentiles=[.01,.05, 0.1, .25,.5,.75,.90, .95, .99])
cotas= descriptivo_basico.loc[["1%","99%"]]
datamin = df[df> cotas.loc["1%"]]
datamin.fillna(value = cotas.loc["1%"], inplace=True)
datamin = datamin[datamin< cotas.loc["99%"]]
datamin.fillna(value = cotas.loc["99%"], inplace=True)


potencia0 = df[(df["rValue"]<11147.5)]

potencia0Ind = potencia0.index

TiempoDesfase = []
potenciaH = []
for i in range(len(potencia0Ind)-1):
    if ((potencia0Ind[i+1]-potencia0Ind[i])==1):
        print(potencia0.iloc[i]["rValue"])
        if(potencia0.iloc[i]["rValue"]>0):
            delta = potencia0.iloc[i+1]["rTimestamp"]-potencia0.iloc[i]["rTimestamp"]
            value = potencia0.iloc[i]["rValue"]
            TiempoDesfase.append(delta.total_seconds()/3600)
            potenciaH.append(value*delta.total_seconds()/3600)
        else: 
            TiempoDesfase.append(0)
            potenciaH.append(0)
    else:
        TiempoDesfase.append(0)
        potenciaH.append(0)
        
        
analisisPotencia = pd.DataFrame(columns = ["Desfase", "Potencia Hora"])
analisisPotencia["Desfase"] = TiempoDesfase
analisisPotencia["Potencia Hora"] = potenciaH
analisisPotencia.sum()

potenciaPromedioEnc= 5200
DuracionPromedio = 2.1

df.iloc[:80]["rValue"].plot()