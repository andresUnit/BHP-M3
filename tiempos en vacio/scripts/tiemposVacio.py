# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 02:08:56 2021

author: AMS
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

files = list()
for file in os.listdir(r"D:/GIT/BHP/tiempos en vacio/data"):
    if file.startswith('data'):
        files.append(file)
df = pd.concat([pd.read_excel(f"data/{f}", header=5) for f in files]).reset_index(drop=True)
df["Inicio"] = pd.to_datetime(df.Inicio, dayfirst=True)

df["Fin"] = pd.to_datetime(df.Fin, dayfirst=True)
df['Inicio Turno'] = pd.to_datetime(df['Inicio Turno'], dayfirst=True)

categorias = ["Detención Equipo No Programada", "Detención Proceso No Programada"]
df = df[df["TUM"].isin(categorias)]
dataMolinoSAG = df[df["Desc. Equipo"] == "Molino Sag MSAG5"]
dataMolinoSAG.reset_index(drop=True, inplace=True)

molinosBolas = ['Molino Bolas MB5','Molino Bolas MB6', 'Molino Bolas MB7', 'Molino Bolas MB8']

dataMolinoBolas = df[df["Desc. Equipo"].isin(molinosBolas)]

dataMolinoBolas.reset_index(drop=True, inplace=True)

dataMolinoSAG["Duración (hrs)"].describe(percentiles=[.01,.05, 0.1, .25,.5,.75,.90, .95, .99])

dataMolinoSAG_ago = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-08-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-09-2020", dayfirst=True))]

dataMolinoSAG_jul = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-07-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-08-2020", dayfirst=True))]

dataMolinoSAG_sep = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-09-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-10-2020", dayfirst=True))]

dataMolinoSAG_oct = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-10-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-11-2020", dayfirst=True))]


dataMolinoSAG_nov = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-11-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-12-2020", dayfirst=True))]


dataMolinoSAG_dic = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-12-2020", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-01-2021", dayfirst=True))]

dataMolinoSAG_ene = dataMolinoSAG[(dataMolinoSAG["Inicio"] > pd.to_datetime("01-01-2021", dayfirst=True)) & (dataMolinoSAG["Inicio"] < pd.to_datetime("01-02-2021", dayfirst=True))]

dataMolinoBolas_ago = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-08-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-09-2020", dayfirst=True))]

dataMolinoBolas_jul = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-07-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-08-2020", dayfirst=True))]

dataMolinoBolas_sep = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-09-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-10-2020", dayfirst=True))]

dataMolinoBolas_oct = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-10-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-11-2020", dayfirst=True))]


dataMolinoBolas_nov = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-11-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-12-2020", dayfirst=True))]


dataMolinoBolas_dic = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-12-2020", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-01-2021", dayfirst=True))]

dataMolinoBolas_ene = dataMolinoBolas[(dataMolinoBolas["Inicio"] > pd.to_datetime("01-01-2021", dayfirst=True)) & (dataMolinoBolas["Inicio"] < pd.to_datetime("01-02-2021", dayfirst=True))]
# graficos

plt.hist(dataMolinoSAG["Duración (hrs)"])
plt.title("Distribucion Horas detención Molino SAG")
plt.xlabel("Horas")
plt.ylabel("N° de detenciones")
plt.show()


mesesVar = [dataMolinoSAG_jul, dataMolinoSAG_ago, dataMolinoSAG_sep, dataMolinoSAG_oct, dataMolinoSAG_nov, dataMolinoSAG_dic, dataMolinoSAG_ene]
meses = ["jul","ago", "sep", "oct", "nov", "dic", "ene"]
cantidad = []
for i in mesesVar:
    cantidad.append(len(i))
    
plt.plot(meses, cantidad)
plt.title("Distribucion Horas detención Molino SAG Mensual")
plt.xlabel("Mes")
plt.ylabel("N° de detenciones")
plt.grid()
plt.show()

cantidadMean = []
for i in mesesVar:
    cantidadMean.append(i["Duración (hrs)"].mean())
    
cantidadVar = []
for i in mesesVar:
    cantidadVar.append(i["Duración (hrs)"].std())
    
plt.scatter(meses, cantidadMean, label = "Promedio Horas")
plt.scatter(meses, cantidadVar, label = "Desviación Estandar Horas")
plt.title("Distribucion Horas detención Molino SAG Mensual")
plt.xlabel("Mes")
plt.ylabel("Promedio Horas de Detención")
plt.legend()
plt.grid()
plt.show()

plt.hist(dataMolinoBolas["Duración (hrs)"])
plt.title("Distribucion Horas detención Molino Bolas Total")
plt.xlabel("Horas")
plt.ylabel("N° de detenciones")
plt.show()


mesesVar = [dataMolinoBolas_jul, dataMolinoBolas_ago, dataMolinoBolas_sep, dataMolinoBolas_oct, dataMolinoBolas_nov, dataMolinoBolas_dic, dataMolinoBolas_ene]
meses = ["jul","ago", "sep", "oct", "nov", "dic", "ene"]
cantidad = []
for i in mesesVar:
    cantidad.append(len(i))
    
plt.plot(meses, cantidad)
plt.title("Distribucion Horas detención Molino Bolas Mensual Total")
plt.xlabel("Mes")
plt.ylabel("N° de detenciones")
plt.grid()
plt.show()

cantidadMean = []
for i in mesesVar:
    cantidadMean.append(i["Duración (hrs)"].mean())
    
cantidadVar = []
for i in mesesVar:
    cantidadVar.append(i["Duración (hrs)"].std())
    
plt.scatter(meses, cantidadMean, label = "Promedio Horas")
plt.scatter(meses, cantidadVar, label = "Desviación Estandar Horas")
plt.title("Distribucion Horas detención Molino Bolas Mensual Total")
plt.xlabel("Mes")
plt.ylabel("Promedio Horas de Detención")
plt.legend()
plt.grid()
plt.show()

labels = ["MB5", "MB6", "MB7", "MB8"]


MB5 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB5']["Duración (hrs)"].values
MB6 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB6']["Duración (hrs)"].values
MB7 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB7']["Duración (hrs)"].values
MB8 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB8']["Duración (hrs)"].values

plt.hist([MB5, MB6, MB7, MB8], label=labels, histtype = 'step')

plt.legend()
plt.title("Distribucion Horas detención Molino Bolas por Tipo")
plt.xlabel("Horas")
plt.ylabel("N° de detenciones")
plt.show()


cantidadMB5 = []
cantidadMB6 = []
cantidadMB7 = []
cantidadMB8 = []

for i in mesesVar:
    MB5 = i[i["Desc. Equipo"]=='Molino Bolas MB5']
    MB6 = i[i["Desc. Equipo"]=='Molino Bolas MB6']
    MB7 = i[i["Desc. Equipo"]=='Molino Bolas MB7']
    MB8 = i[i["Desc. Equipo"]=='Molino Bolas MB8']
    cantidadMB5.append(len(MB5))
    cantidadMB6.append(len(MB6))
    cantidadMB7.append(len(MB7))
    cantidadMB8.append(len(MB8))
    
plt.plot(meses, cantidadMB5, label = "MB5")
plt.plot(meses, cantidadMB6, label = "MB6")
plt.plot(meses, cantidadMB7, label = "MB7")
plt.plot(meses, cantidadMB8, label = "MB8")
plt.title("Distribucion Horas detención Molino Bolas Mensual Por Tipo")
plt.xlabel("Mes")
plt.ylabel("N° de detenciones")
plt.legend()
plt.grid()
plt.show()

cantidadMeanMB5 = []
cantidadMeanMB6 = []
cantidadMeanMB7 = []
cantidadMeanMB8 = []
for i in mesesVar:
    MB5 = i[i["Desc. Equipo"]=='Molino Bolas MB5']
    MB6 = i[i["Desc. Equipo"]=='Molino Bolas MB6']
    MB7 = i[i["Desc. Equipo"]=='Molino Bolas MB7']
    MB8 = i[i["Desc. Equipo"]=='Molino Bolas MB8']
    cantidadMeanMB5.append(MB5["Duración (hrs)"].mean())
    cantidadMeanMB6.append(MB6["Duración (hrs)"].mean())
    cantidadMeanMB7.append(MB7["Duración (hrs)"].mean())
    cantidadMeanMB8.append(MB8["Duración (hrs)"].mean())
    
cantidadVarMB5 = []
cantidadVarMB6 = []
cantidadVarMB7 = []
cantidadVarMB8 = []

for i in mesesVar:
    MB5 = i[i["Desc. Equipo"]=='Molino Bolas MB5']
    MB6 = i[i["Desc. Equipo"]=='Molino Bolas MB6']
    MB7 = i[i["Desc. Equipo"]=='Molino Bolas MB7']
    MB8 = i[i["Desc. Equipo"]=='Molino Bolas MB8']
    cantidadVarMB5.append(MB5["Duración (hrs)"].std())
    cantidadVarMB6.append(MB5["Duración (hrs)"].std())
    cantidadVarMB7.append(MB7["Duración (hrs)"].std())
    cantidadVarMB8.append(MB8["Duración (hrs)"].std())
    
plt.scatter(meses, cantidadMeanMB5, label = "MB5")
plt.scatter(meses, cantidadMeanMB6, label = "MB6")
plt.scatter(meses, cantidadMeanMB7, label = "MB7")
plt.scatter(meses, cantidadMeanMB8, label = "MB8")
plt.title("Promedio Horas detención Molino Bolas Mensual Por Tipo")
plt.xlabel("Mes")
plt.ylabel("Promedio Horas de Detención")
plt.legend()
plt.grid()
plt.show()


plt.scatter(meses, cantidadVarMB5, label = "MB5")
plt.scatter(meses, cantidadVarMB6, label = "MB6")
plt.scatter(meses, cantidadVarMB7, label = "MB7")
plt.scatter(meses, cantidadVarMB8, label = "MB8")
plt.title("STD Horas detención Molino Bolas Mensual Total")
plt.xlabel("Mes")
plt.ylabel("STD Horas de Detención")
plt.legend()
plt.grid()
plt.show()


#-------------- medicion de desviacion tiempo de parada -------------------#
MB5 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB5'].sort_values(by = "Inicio").reset_index(drop = True)
MB6 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB6'].sort_values(by = "Inicio").reset_index(drop = True)
MB7 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB7'].sort_values(by = "Inicio").reset_index(drop = True)
MB8 = dataMolinoBolas[dataMolinoBolas["Desc. Equipo"]=='Molino Bolas MB8'].sort_values(by = "Inicio").reset_index(drop = True)

MolinoSAG = dataMolinoSAG.sort_values(by = "Inicio").reset_index(drop = True)
diffMolinoSAG = []
for i in range(len(MolinoSAG)-1):
    auxDiff = MolinoSAG["Inicio"].iloc[i+1]-MolinoSAG["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffMolinoSAG.append(auxDiff)


diffMolinoSAG = pd.DataFrame(diffMolinoSAG, columns=["Diff"])

diffMolinoSAG["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones Molino SAG")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()

diffMB5 = []
for i in range(len(MB5)-1):
    auxDiff = MB5["Inicio"].iloc[i+1]-MB5["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffMB5.append(auxDiff)


diffMB5 = pd.DataFrame(diffMB5, columns=["Diff"])

diffMB5["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones MB5")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()

diffMB6 = []
for i in range(len(MB6)-1):
    auxDiff = MB6["Inicio"].iloc[i+1]-MB6["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffMB6.append(auxDiff)


diffMB6 = pd.DataFrame(diffMB6, columns=["Diff"])

diffMB6["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones MB6")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffMB7 = []
for i in range(len(MB7)-1):
    auxDiff = MB7["Inicio"].iloc[i+1]-MB7["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffMB7.append(auxDiff)


diffMB7 = pd.DataFrame(diffMB7, columns=["Diff"])

diffMB7["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones MB7")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffMB8 = []
for i in range(len(MB8)-1):
    auxDiff = MB8["Inicio"].iloc[i+1]-MB8["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffMB8.append(auxDiff)


diffMB8 = pd.DataFrame(diffMB8, columns=["Diff"])

diffMB8["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones MB8")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()

# ------------------------- Relacion MolinoSAG MB --------------------------#

MolinoSAGFallaEquipo = MolinoSAG[MolinoSAG["TUM"]=="Detención Equipo No Programada"].reset_index(drop = True)
MB5FallaProces = MB5[MB5["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
MB6FallaProces = MB6[MB6["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
MB7FallaProces = MB7[MB7["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
MB8FallaProces = MB8[MB8["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
MB5FallaProcesSAG = MB5FallaProces[MB5FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
MB6FallaProcesSAG = MB6FallaProces[MB6FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
MB7FallaProcesSAG = MB7FallaProces[MB7FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
MB8FallaProcesSAG = MB8FallaProces[MB8FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)


def cruceData(data1, data2):
    iDetenCruce = pd.DataFrame(columns=["SAG_ini","SAG_fin", "SAG_hrs", "MB_ini", "MB_fin", "MB_hrs", "diff_ini", "diff_fin"])
    indices = []
    diff = 0
    for j in range(len(data2)):
        for i in range(len(data1)):
            timeSAG = data1["Inicio"].iloc[i]
            timeMB = data2["Inicio"].iloc[j]
            diffaux = timeMB- timeSAG
            if diffaux >=pd.Timedelta(0, unit="m"):
                diff = diffaux
                tupla = (i,j, diffaux)
            else:
                break
        indices.append(tupla)
        iDetenCruce.loc[j,:] = [data1["Inicio"].iloc[i-1], data1["Fin"].iloc[i-1], data1['Duración (hrs)'].iloc[i-1],data2["Inicio"].iloc[j],data2["Fin"].iloc[j],data2['Duración (hrs)'].iloc[j], diff,data1["Fin"].iloc[i-1]- data2["Fin"].iloc[j]]
    iDetenCruce = iDetenCruce.astype({'SAG_ini': 'datetime64[ns]','SAG_fin': 'datetime64[ns]','SAG_hrs': 'float','MB_ini': 'datetime64[ns]','MB_fin': 'datetime64[ns]','MB_hrs': 'float','diff_ini': 'timedelta64[ns]','diff_fin': 'timedelta64[ns]'})
    return iDetenCruce, indices

cruceMB5, indMB5 = cruceData(MolinoSAG, MB5FallaProcesSAG)
cruceMB6, indMB6 = cruceData(MolinoSAG, MB6FallaProcesSAG)
cruceMB7, indMB7 = cruceData(MolinoSAG, MB7FallaProcesSAG)
cruceMB8, indMB8 = cruceData(MolinoSAG, MB8FallaProcesSAG)

ComparativeIni = pd.DataFrame(index=(["count","mean", "std", "min", "25%", "50%", "75%","max"]))
ComparativeIni["MB5"]=cruceMB5.describe(percentiles=[])["diff_ini"]
ComparativeIni["MB6"]=cruceMB6.describe()["diff_ini"]
ComparativeIni["MB7"]=cruceMB7.describe()["diff_ini"]
ComparativeIni["MB8"]=cruceMB8.describe()["diff_ini"]

ComparativeFin = pd.DataFrame(index=(["count","mean", "std", "min", "25%", "50%", "75%","max"]))
ComparativeFin["MB5"]=cruceMB5.describe()["diff_fin"]
ComparativeFin["MB6"]=cruceMB6.describe()["diff_fin"]
ComparativeFin["MB7"]=cruceMB7.describe()["diff_fin"]
ComparativeFin["MB8"]=cruceMB8.describe()["diff_fin"]


auxMB5 = cruceMB5.sort_values(by = "SAG_hrs",ascending=True)
auxMB6 = cruceMB6.sort_values(by = "SAG_hrs",ascending=True)
auxMB7 = cruceMB7.sort_values(by = "SAG_hrs",ascending=True)
auxMB8 = cruceMB8.sort_values(by = "SAG_hrs",ascending=True)

plt.plot(auxMB5["SAG_hrs"], auxMB5["diff_ini"]/(10**9*60))
plt.title("Relación Duración detenimiento SAG con Delay detenimiento MB5")
plt.xlabel("Horas de detención")
plt.ylabel("Minutos de Delay")
plt.grid()
plt.show()

plt.plot(auxMB6["SAG_hrs"], auxMB6["diff_ini"]/(10**9*60))
plt.title("Relación Duración detenimiento SAG con Delay detenimiento MB6")
plt.xlabel("Horas de detención")
plt.ylabel("Minutos de Delay")
plt.grid()
plt.show()

plt.plot(auxMB7["SAG_hrs"], auxMB7["diff_ini"]/(10**9*60))
plt.title("Relación Duración detenimiento SAG con Delay detenimiento MB7")
plt.xlabel("Horas de detención")
plt.ylabel("Minutos de Delay")
plt.grid()
plt.show()

plt.plot(auxMB8["SAG_hrs"], auxMB8["diff_ini"]/(10**9*60))
plt.title("Relación Duración detenimiento SAG con Delay detenimiento MB8")
plt.xlabel("Horas de detención")
plt.ylabel("Minutos de Delay")
plt.grid()
plt.show()


def recInd(ind):
    indaux=[]
    for i in range(len(ind)):
        indaux.append(ind[i][0])
    return indaux

recIndMB5 = recInd(indMB5)
recIndMB6 = recInd(indMB6)
recIndMB7 = recInd(indMB7)
recIndMB8 = recInd(indMB8)

IndMBTotal = recIndMB5+recIndMB6+recIndMB7+recIndMB8

IndMBTotal = list(set(IndMBTotal))
IndSAG = list(range(0,59))
IndSAGSinMB = [ind for ind in IndSAG if ind not in IndMBTotal]

DetenSAGSinMB = MolinoSAG.iloc[IndSAGSinMB]
DetenSAGConMB = MolinoSAG.iloc[IndMBTotal]

detencionesExternasSAG = ["Indisponibilidad de Correa","Indisponibilidad de Bomba", "Indisponibilidad de Molinos Bola"]
DetenSAGSinMB.describe()
DetenSAGConMB.describe()

DetencionSAGInternas = DetenSAGSinMB[~DetenSAGSinMB["MDD"].isin(detencionesExternasSAG)]
DetencionSAGInternas.describe()

DetenSAGConMB["MDD"].hist()
plt.xticks(rotation='vertical')
plt.title("Detenciones Con Delay a MB")
plt.ylabel("N° de Detenciones")
plt.show()

DetenSAGSinMB["MDD"].hist()
plt.xticks(rotation='vertical')
plt.title("Detenciones Sin Delay a MB")
plt.ylabel("N° de Detenciones")
plt.show()

DetenSAGConMB.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas Con Delay MB")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

DetenSAGSinMB.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas Sin Delay MB")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

MB5.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas de detencion por tipo MB5")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

MB6.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas de detencion por tipo MB6")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

MB7.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas de detencion por tipo MB7")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

MB8.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Horas de detencion por tipo MB8")
plt.grid()
plt.ylabel("Total de Horas")
plt.show()

cruceTotal = pd.concat([cruceMB5,cruceMB6, cruceMB7, cruceMB8])



cruceTotal['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB, No programado")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()


cruceMB5['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB5")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

cruceMB6['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB6")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()


cruceMB7['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB7")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

cruceMB8['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB8")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

tiemposVacioConDesfase = DetenSAGSinMB[(DetenSAGSinMB["Duración (hrs)"]-0.75)>0]

TotalHorasVacio1Des = (tiemposVacioConDesfase["Duración (hrs)"]-0.75).sum()


def Ahorro1(PotenciaMediaVacio,CostoMw, TotalHorasVacio1Des):
    ahorroPrevisto1 = PotenciaMediaVacio*CostoMw*TotalHorasVacio1Des
    return ahorroPrevisto1

def Ahorro2(potenciaPromedioEnc,CostoMw, DuracionPromedioMarcha):
    HorasAhorroPuestaMarcha = len(DetenSAGSinMB)*DuracionPromedioMarcha
    ahorroPrevisto2 = (15.145-potenciaPromedioEnc)*CostoMw*HorasAhorroPuestaMarcha
    return ahorroPrevisto2


def Ahorro3(potenciaPromedioEnc, CostoMw):
    crucetotalDesface = cruceTotal[cruceTotal["diff_ini"]>pd.Timedelta(45, "m")]["diff_ini"]
    promedioHorasDesfase = 24/60
    cantidad=len(crucetotalDesface)
    ahorroPrevisto3 = (15.145-potenciaPromedioEnc)*CostoMw*cantidad*promedioHorasDesfase
    return ahorroPrevisto3


def AhorroTotal(PotenciaMediaVacio,CostoMw,TotalHorasVacio1Des,potenciaPromedioEnc, DuracionPromedioMarcha):
    ahorro1 = Ahorro1(PotenciaMediaVacio, CostoMw, TotalHorasVacio1Des)
    ahorro2 = Ahorro2(potenciaPromedioEnc, CostoMw, DuracionPromedioMarcha)
    ahorro3 = Ahorro3(potenciaPromedioEnc, CostoMw)
    return ahorro1+ahorro2+ahorro3

ahorroMB5 = AhorroTotal(10.691, 109, TotalHorasVacio1Des,5.381, 2.1 )
ahorroMB6 = AhorroTotal(11.004, 109, TotalHorasVacio1Des,5.761, 2.5 )
ahorroMB7 = AhorroTotal(10.174, 109, TotalHorasVacio1Des,5.221, 3.1 )
ahorroMB8 = AhorroTotal(10.250, 109, TotalHorasVacio1Des,4.704, 2.2 )

ahorroTotal = ahorroMB5+ ahorroMB6+ ahorroMB7+ ahorroMB8

import numpy as np

DetenSAGSinMB["Duración (hrs)"].hist()
plt.title("Distribución Detención SAG y MB Trabajo en Vacio No Program.")
plt.ylabel("N° de Detenciones")
plt.xlabel("Horas")
plt.xticks(np.arange(0, 12, step=1))
plt.show()

(DetenSAGSinMB.groupby(["MDD"])["Duración (hrs)"].sum()/DetenSAGSinMB["MDD"].value_counts()).plot(kind='bar')
plt.title("Distribución Detención SAG y MB Trabajo en Vacio No Program. Mean")
plt.grid()
plt.ylabel("Horas Promedio")
plt.xlabel("Horas")
plt.show()

DetenSAGSinMB["MDD"].hist()
plt.title("Distribución Detención SAG y MB Trabajo en Vacio No Program. Count")
plt.ylabel("N° de Detenciones")
plt.xticks(rotation= "vertical")
plt.show()

DetenSAGSinMB.groupby(["MDD"])["Duración (hrs)"].sum().plot(kind='bar')
plt.title("Distribución Detención SAG y MB Trabajo en Vacio No Program.")
plt.grid()
plt.ylabel("Total Horas")
plt.xlabel("Horas")
plt.show()


CountaDataTrabajosVacio = np.array([59-len(cruceMB5),59-len(cruceMB6),59-len(cruceMB7),59-len(cruceMB8)])

auxCount = pd.DataFrame(CountaDataTrabajosVacio.reshape((1,4)), columns= ["MB5","MB6", "MB7", "MB8"])
auxCount.sum().plot(kind="bar")
plt.title("Cantidad de Trabajos en Vacio Por Equipo, No program.")
plt.xlabel("equipo")
plt.ylabel("N° de Trabajos en Vacio")
plt.grid()
plt.show()