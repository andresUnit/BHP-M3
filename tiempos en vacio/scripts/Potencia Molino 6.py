# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:19:04 2021

author: AMS
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_json("data/PMB6.json")
df.set_index("rIndex", inplace = True)
df[pd.isnull(df["rValue"])]
df[pd.isnull(df["rTagName"])]
df[pd.isnull(df["rTimestamp"])]
df[pd.isnull(df["rConfidence"])]

df = df.astype({'rTimestamp': 'datetime64[ns]'})

descriptivo_basico = df.describe(percentiles=[.01,.05, 0.1, .25,.5,.75,.90, .95, .99])

df = df[df["rConfidence"]==100].reset_index(drop=True)

TrabajoVacio = pd.DataFrame(data[1:], columns=data[0])
TrabajoVacio = TrabajoVacio.astype({'Inicio': 'datetime64[ns]', 'Fin': 'datetime64[ns]'})
TrabajoVacio.drop(columns="")

iteracionMB5 = []
iteracionTiempoMB5 = []
for i in range(len(TrabajoVacio)):
    print(i)
    inicio = TrabajoVacio.iloc[i]["Inicio"]
    Fin = TrabajoVacio.iloc[i]["Fin"]
    aux = df[(df["rTimestamp"]>=(inicio)+pd.Timedelta(45,"m")) & (df["rTimestamp"]<=(Fin+pd.Timedelta(45,"m")))].reset_index(drop = True)
    PotenciaVacio = 0
    TiempoVacio = 0
    if len(aux)>1:
        for j in range(len(aux)-1):
            delta = aux.iloc[j+1]["rTimestamp"]-aux.iloc[j]["rTimestamp"]
            value = aux.iloc[j]["rValue"]
            TiempoDesfase = delta.total_seconds()
            potenciaH = value*TiempoDesfase
            PotenciaVacio += potenciaH
            TiempoVacio += TiempoDesfase
        iteracionMB5.append(PotenciaVacio/TiempoVacio)
        iteracionTiempoMB5.append(TiempoVacio)
    else:
        continue

meanPotenciaVacio = np.array(iteracionMB5).mean()
varPotenciaVacio = np.array(iteracionMB5).std()


potencia0 = df[(df["rValue"]<(meanPotenciaVacio+varPotenciaVacio/3))]

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
            potenciaH.append(value)
        else: 
            TiempoDesfase.append(0)
            potenciaH.append(0)
    else:
        TiempoDesfase.append(0)
        potenciaH.append(0)
        
        
analisisPotencia = pd.DataFrame(columns = ["Desfase", "Potencia Hora"])
analisisPotencia["Desfase"] = TiempoDesfase
analisisPotencia["Potencia Hora"] = potenciaH
analisisPotencia["multiplicacion"] = analisisPotencia["Desfase"]*analisisPotencia["Potencia Hora"]
potenciaMediaEnc = analisisPotencia["multiplicacion"].sum()/analisisPotencia.sum()["Desfase"]

DuracionPromedio = analisisPotencia["Desfase"].sum()/((analisisPotencia["Desfase"]==0).sum()*0.17)