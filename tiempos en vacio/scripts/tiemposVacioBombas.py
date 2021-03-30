# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:31:08 2021

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

Bombas = ["Bomba PP-019","Bomba PP-020","Bomba bajo molino PP-021","Bomba bajo molino PP-022","Bomba bajo molino PP-023", "Bomba bajo molino PP-024" ]

dataBombas = df[df["Desc. Equipo"].isin(Bombas)]

dataBombas.reset_index(drop=True, inplace=True)

dataBombas["Duración (hrs)"].describe(percentiles=[.01,.05, 0.1, .25,.5,.75,.90, .95, .99])

dataBombas_ago = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-08-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-09-2020", dayfirst=True))]

dataBombas_jul = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-07-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-08-2020", dayfirst=True))]

dataBombas_sep = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-09-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-10-2020", dayfirst=True))]

dataBombas_oct = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-10-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-11-2020", dayfirst=True))]

dataBombas_nov = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-11-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-12-2020", dayfirst=True))]

dataBombas_dic = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-12-2020", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-01-2021", dayfirst=True))]

dataBombas_ene = dataBombas[(dataBombas["Inicio"] > pd.to_datetime("01-01-2021", dayfirst=True)) & (dataBombas["Inicio"] < pd.to_datetime("01-02-2021", dayfirst=True))]

# graficos

plt.hist(dataBombas["Duración (hrs)"])
plt.title("Distribucion Horas detención Bombas")
plt.xlabel("Horas")
plt.ylabel("N° de detenciones")
plt.show()


mesesVar = [dataBombas_jul, dataBombas_ago, dataBombas_sep, dataBombas_oct, dataBombas_nov, dataBombas_dic, dataBombas_ene]
meses = ["jul","ago", "sep", "oct", "nov", "dic", "ene"]
cantidad = []
for i in mesesVar:
    cantidad.append(len(i))
    
plt.plot(meses, cantidad)
plt.title("Distribucion Horas detención Bombas Mensual")
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
plt.title("Distribucion Horas detención Bombas Mensual")
plt.xlabel("Mes")
plt.ylabel("Promedio Horas de Detención")
plt.legend()
plt.grid()
plt.show()




labels = ["PP-019", "PP-020", "PP-021", "PP-022","PP-023","PP-024"]


pp19 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba PP-019']["Duración (hrs)"].values
pp20 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba PP-020']["Duración (hrs)"].values
pp21 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-021']["Duración (hrs)"].values
pp22 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-022']["Duración (hrs)"].values
pp23 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-023']["Duración (hrs)"].values
pp24 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-024']["Duración (hrs)"].values

plt.hist([pp19, pp20, pp21, pp22, pp23, pp24], label=labels, histtype = 'step')

plt.legend()
plt.title("Distribucion Horas detención  por Tipo")
plt.xlabel("Horas")
plt.ylabel("N° de detenciones")
plt.show()


cantidadpp19 = []
cantidadpp20 = []
cantidadpp21 = []
cantidadpp22 = []
cantidadpp23 = []
cantidadpp24 = []


for i in mesesVar:
    Bpp19 = i[i["Desc. Equipo"]=='Bomba PP-019']
    Bpp20 = i[i["Desc. Equipo"]=='Bomba PP-020']
    Bpp21 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-021']
    Bpp22 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-022']
    Bpp23 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-023']
    Bpp24 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-024']
    cantidadpp19.append(len(Bpp19))
    cantidadpp20.append(len(Bpp20))
    cantidadpp21.append(len(Bpp21))
    cantidadpp22.append(len(Bpp22))
    cantidadpp23.append(len(Bpp23))
    cantidadpp24.append(len(Bpp24))
    
plt.plot(meses, cantidadpp19, label = "B19")
plt.plot(meses, cantidadpp20, label = "B20")
plt.plot(meses, cantidadpp21, label = "B21")
plt.plot(meses, cantidadpp22, label = "B22")
plt.plot(meses, cantidadpp23, label = "B23")
plt.plot(meses, cantidadpp24, label = "B24")
plt.title("Distribucion Horas detención Bombas Mensual Por Tipo")
plt.xlabel("Mes")
plt.ylabel("N° de detenciones")
plt.legend()
plt.grid()
plt.show()

cantidadMeanpp19 = []
cantidadMeanpp20 = []
cantidadMeanpp21 = []
cantidadMeanpp22 = []
cantidadMeanpp23 = []
cantidadMeanpp24 = []


for i in mesesVar:
    Bpp19 = i[i["Desc. Equipo"]=='Bomba PP-019']
    Bpp20 = i[i["Desc. Equipo"]=='Bomba PP-020']
    Bpp21 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-021']
    Bpp22 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-022']
    Bpp23 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-023']
    Bpp24 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-024']
    cantidadMeanpp19.append(Bpp19["Duración (hrs)"].mean())
    cantidadMeanpp20.append(Bpp20["Duración (hrs)"].mean())
    cantidadMeanpp21.append(Bpp21["Duración (hrs)"].mean())
    cantidadMeanpp22.append(Bpp22["Duración (hrs)"].mean())
    cantidadMeanpp23.append(Bpp23["Duración (hrs)"].mean())
    cantidadMeanpp24.append(Bpp24["Duración (hrs)"].mean())
    
cantidadVarpp19 = []
cantidadVarpp20 = []
cantidadVarpp21 = []
cantidadVarpp22 = []
cantidadVarpp23 = []
cantidadVarpp24 = []

for i in mesesVar:
    Bpp19 = i[i["Desc. Equipo"]=='Bomba PP-019']
    Bpp20 = i[i["Desc. Equipo"]=='Bomba PP-020']
    Bpp21 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-021']
    Bpp22 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-022']
    Bpp23 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-023']
    Bpp24 = i[i["Desc. Equipo"]=='Bomba bajo molino PP-024']
    cantidadVarpp19.append(Bpp19["Duración (hrs)"].std())
    cantidadVarpp20.append(Bpp20["Duración (hrs)"].std())
    cantidadVarpp21.append(Bpp21["Duración (hrs)"].std())
    cantidadVarpp22.append(Bpp22["Duración (hrs)"].std())
    cantidadVarpp23.append(Bpp23["Duración (hrs)"].std())
    cantidadVarpp24.append(Bpp24["Duración (hrs)"].std())
    
plt.scatter(meses, cantidadMeanpp19, label = "Bpp19")
plt.scatter(meses, cantidadMeanpp20, label = "Bpp20")
plt.scatter(meses, cantidadMeanpp21, label = "Bpp21")
plt.scatter(meses, cantidadMeanpp22, label = "Bpp22")
plt.scatter(meses, cantidadMeanpp23, label = "Bpp23")
plt.scatter(meses, cantidadMeanpp24, label = "Bpp24")
plt.title("Promedio Horas detención Bombas Por Tipo")
plt.xlabel("Mes")
plt.ylabel("Promedio Horas de Detención")
plt.legend()
plt.grid()
plt.show()


plt.scatter(meses, cantidadVarpp19, label = "Bpp19")
plt.scatter(meses, cantidadVarpp20, label = "Bpp20")
plt.scatter(meses, cantidadVarpp21, label = "Bpp21")
plt.scatter(meses, cantidadVarpp22, label = "Bpp22")
plt.scatter(meses, cantidadVarpp23, label = "Bpp23")
plt.scatter(meses, cantidadVarpp24, label = "Bpp24")

plt.title("STD Horas detención Bombas Mensual Total")
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

pp19 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba PP-019'].sort_values(by = "Inicio").reset_index(drop = True)
pp20 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba PP-020'].sort_values(by = "Inicio").reset_index(drop = True)
pp21 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-021'].sort_values(by = "Inicio").reset_index(drop = True)
pp22 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-022'].sort_values(by = "Inicio").reset_index(drop = True)
pp23 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-023'].sort_values(by = "Inicio").reset_index(drop = True)
pp24 = dataBombas[dataBombas["Desc. Equipo"]=='Bomba bajo molino PP-024'].sort_values(by = "Inicio").reset_index(drop = True)

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


diffpp19 = []
for i in range(len(pp19)-1):
    auxDiff = pp19["Inicio"].iloc[i+1]-pp19["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp19.append(auxDiff)


diffpp19 = pd.DataFrame(diffpp19, columns=["Diff"])

diffpp19["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B19")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffpp20 = []
for i in range(len(pp20)-1):
    auxDiff = pp20["Inicio"].iloc[i+1]-pp20["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp20.append(auxDiff)


diffpp20 = pd.DataFrame(diffpp20, columns=["Diff"])

diffpp20["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B20")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffpp21 = []
for i in range(len(pp21)-1):
    auxDiff = pp21["Inicio"].iloc[i+1]-pp21["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp21.append(auxDiff)


diffpp21 = pd.DataFrame(diffpp21, columns=["Diff"])

diffpp21["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B21")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()



diffpp22 = []
for i in range(len(pp22)-1):
    auxDiff = pp22["Inicio"].iloc[i+1]-pp22["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp22.append(auxDiff)


diffpp22 = pd.DataFrame(diffpp22, columns=["Diff"])

diffpp22["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B22")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffpp23 = []
for i in range(len(pp23)-1):
    auxDiff = pp23["Inicio"].iloc[i+1]-pp23["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp23.append(auxDiff)


diffpp23 = pd.DataFrame(diffpp23, columns=["Diff"])

diffpp23["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B23")
plt.xlabel("Dias")
plt.ylabel("N° de detenciones")
plt.show()


diffpp24 = []
for i in range(len(pp24)-1):
    auxDiff = pp24["Inicio"].iloc[i+1]-pp24["Fin"].iloc[i]
    if auxDiff > pd.Timedelta(1, unit = "m"):
        diffpp24.append(auxDiff)


diffpp24 = pd.DataFrame(diffpp24, columns=["Diff"])

diffpp24["Diff"].dt.days.hist()
plt.title("Histograma de dias entre Detenciones B24")
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
pp19FallaProces = pp19[pp19["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp20FallaProces = pp20[pp20["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp21FallaProces = pp21[pp21["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp22FallaProces = pp22[pp22["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp23FallaProces = pp23[pp23["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp24FallaProces = pp24[pp24["TUM"]=="Detención Proceso No Programada"].reset_index(drop = True)
pp19FallaProcesSAG = pp19FallaProces[pp19FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
pp20FallaProcesSAG = pp20FallaProces[pp20FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
pp21FallaProcesSAG = pp21FallaProces[pp21FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
pp22FallaProcesSAG = pp22FallaProces[pp22FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
pp23FallaProcesSAG = pp23FallaProces[pp23FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)
pp24FallaProcesSAG = pp24FallaProces[pp24FallaProces["MDD"]=="Indisponibilidad de Molino SAG"].reset_index(drop = True)

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


crucepp19, indpp19 = cruceData(MolinoSAG, pp19FallaProcesSAG)
crucepp20, indpp20 = cruceData(MolinoSAG, pp20FallaProcesSAG)
crucepp21, indpp21 = cruceData(MolinoSAG, pp21FallaProcesSAG)
crucepp22, indpp22 = cruceData(MolinoSAG, pp22FallaProcesSAG)
crucepp23, indpp23 = cruceData(MolinoSAG, pp23FallaProcesSAG)
crucepp24, indpp24 = cruceData(MolinoSAG, pp24FallaProcesSAG)

crucepp19 = crucepp19[crucepp19["diff_ini"]<pd.Timedelta(1,"d")]
crucepp20 = crucepp20[crucepp20["diff_ini"]<pd.Timedelta(1,"d")]

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

ComparativeIniBomba = pd.DataFrame(index=(["count","mean", "std", "min", "25%", "50%", "75%","max"]))
ComparativeIniBomba["B19"]=crucepp19.describe(percentiles=[])["diff_ini"]
ComparativeIniBomba["B20"]=crucepp20.describe()["diff_ini"]
ComparativeIniBomba["B21"]=crucepp21.describe()["diff_ini"]
ComparativeIniBomba["B22"]=crucepp22.describe()["diff_ini"]
ComparativeIniBomba["B23"]=crucepp23.describe()["diff_ini"]
ComparativeIniBomba["B24"]=crucepp24.describe()["diff_ini"]

ComparativeFinBomba = pd.DataFrame(index=(["count","mean", "std", "min", "25%", "50%", "75%","max"]))
ComparativeFinBomba["B19"]=crucepp19.describe()["diff_fin"]
ComparativeFinBomba["B20"]=crucepp20.describe()["diff_fin"]
ComparativeFinBomba["B21"]=crucepp21.describe()["diff_fin"]
ComparativeFinBomba["B22"]=crucepp22.describe()["diff_fin"]
ComparativeFinBomba["B23"]=crucepp23.describe()["diff_fin"]
ComparativeFinBomba["B24"]=crucepp24.describe()["diff_fin"]


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

recIndpp19 = recInd(indpp19)
recIndpp20 = recInd(indpp20)
recIndpp21 = recInd(indpp21)
recIndpp22 = recInd(indpp22)
recIndpp23 = recInd(indpp23)
recIndpp24 = recInd(indpp24)

IndMBTotal = recIndMB5+recIndMB6+recIndMB7+recIndMB8

IndppTotal = recIndpp19+recIndpp20+ recIndpp21+recIndpp22+recIndpp23+recIndpp24

IndMBTotal = list(set(IndMBTotal))
IndSAG = list(range(0,59))
IndSAGSinMB = [ind for ind in IndSAG if ind not in IndMBTotal]

IndppTotal = list(set(IndppTotal))
IndSAG = list(range(0,59))
IndSAGSinpp = [ind for ind in IndSAG if ind not in IndppTotal]

DetenSAGSinMB = MolinoSAG.iloc[IndSAGSinMB]
DetenSAGConMB = MolinoSAG.iloc[IndMBTotal]

DetenSAGConpp = MolinoSAG.iloc[IndppTotal]
DetenSAGSinnpp = MolinoSAG.iloc[IndSAGSinpp]

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

cruceTotalpp = pd.concat([crucepp19,crucepp20, crucepp21, crucepp22, crucepp23,crucepp24])


cruceTotal['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a MB")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

cruceTotalpp['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a Bombas")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

crucepp19['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B19")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

crucepp20['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B20")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()


crucepp21['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B21")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

crucepp22['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B22")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

crucepp23['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B23")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

crucepp24['diff_ini'].astype('timedelta64[m]').plot.hist()
plt.title("Distribucion Desfase SAG a B24")
plt.ylabel("Numero de Detenciones")
plt.xlabel("Minutos")
plt.grid()
plt.show()

tiemposVacioConDesfasepp = DetenSAGSinnpp[(DetenSAGSinnpp["Duración (hrs)"]-0.75)>0]

TotalHorasVacio1Despp = (tiemposVacioConDesfasepp["Duración (hrs)"]-0.75).sum()


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