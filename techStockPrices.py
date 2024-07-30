"""
CÓDIGO QUE ESTUDIA LOS PRECIOS MÁXIMOS DE CIERRE DE VARIAS EMPRESAS, IMPRIME UNA LISTA CON EL PRECIO MÁXIMO DE CADA UNA Y EN LA FECHA EN LA QUE SE PRODUJO; TAMBIÉN IMPRIME UN \
GRÁFICO CON LOS PRECIOS DE CIERRES A FINAL DE MES PARA CADA EMPRESA A LO LARGO DEL PERIODO DE ESTUDIO. LOS DATOS DE ENTRADA SON ARCHIVOS CSV, IMPORTADOS EN DATAFRAMES, MEDIANTE \
EL USO DE LA LIBRERÍA PANDAS. LOS GRÁFICOS HACEN USO DE LA LIBRERÍA MATPLOTLIB.
"""
import pandas as pd
import matplotlib.pyplot as plt

#FUNCIÓN QUE DEVUELVE LOS PRECIOS DE CIERRE A FINAL DE CADA MES
def max_month(empresa):
    empresa['Date']=pd.to_datetime(empresa['Date'])
    fDates=pd.DataFrame({'Dates': empresa['Date']})
    gDates=fDates.groupby(pd.Grouper(key='Dates',freq='BME'))
    gM=[group for _, group in gDates]
    gMindex = [group.index.to_frame(index=False) for group in gM]
    indices_list=[group[0].tolist() for group in gMindex]
    close_list=[empresa.loc[indices,"Close"].tail(1) for indices in indices_list]
    return close_list

#FUNCIÓN QUE IMPRIME UN GRÁFICO CON TODOS LOS PRECIOS DE CIERRE A FINAL DE MES PARA CADA EMPRESA
def impr_graph(dictm): 
    mes=['07/23','08/23','09/23','10/23','11/23','12/23','01/24','02/24','03/24','04/24','05/24','06/24','07/24']
    fig,ax=plt.subplots()
    ax.set_title('Closing prices at the end of each month', loc = 'center', fontdict={'fontsize': 14, 'fontweight': 'bold'})
    for x in dictm:
        ax.plot(mes,dictm[x],marker='.', label=x)
    ax.legend(loc = 'upper left')
    ax.set_xlabel('Months', loc = 'right', fontdict={'fontsize': 11, 'fontweight': 'bold'})
    ax.set_ylabel('Closing price', loc = 'top', fontdict={'fontsize': 11, 'fontweight': 'bold'})
    ax.grid(axis= 'both', color = 'gray', linestyle = 'dashed')
    ax.set_yticks(range(0,500,20))
    plt.show()

#Histórico diario, en el intervalo de un año, del precio de mercado y volumen de 10 compañías tecnolóicas en el mercado de USA, en USD$.
#CSV obtenidos de Yahoo! finance del 28 de julio 2023 al 26 de julio de 2024
aapl = pd.read_csv("csv_stock_market/AAPL.csv") #Apple
amzn = pd.read_csv("csv_stock_market/AMZN.csv") #Amazon
baba = pd.read_csv("csv_stock_market/BABA.csv") #Alibaba
crm = pd.read_csv("csv_stock_market/CRM.csv") #Salesforce
goog = pd.read_csv("csv_stock_market/GOOG.csv") #Google
intc = pd.read_csv("csv_stock_market/INTC.csv") #Intel
meta = pd.read_csv("csv_stock_market/META.csv") #Meta
msft = pd.read_csv("csv_stock_market/MSFT.csv") #Microsoft
nvda = pd.read_csv("csv_stock_market/NVDA.csv") #Nvidia
tsla = pd.read_csv("csv_stock_market/TSLA.csv") #Tesla

#EMPRESAS CON LOS MAYORES PRECIOS DE CIERRE
#Serie con los máximos precios de cierre de cada empresa
maximos=pd.Series({"Apple": aapl["Close"].max(), "Amazon": amzn["Close"].max(), "Alibaba": baba["Close"].max(), "Salesforce": crm["Close"].max(), "Google": goog["Close"].max(), \
                   "Intel": intc["Close"].max(), "Meta": meta["Close"].max(), "Microsoft": msft["Close"].max(), "Nvidia": nvda["Close"].max(), "Tesla": tsla["Close"].max()})
#Lista con las fechas de los máximos precios de cierre de cada empresa
dates=[aapl.loc[aapl["Close"].idxmax(),"Date"],amzn.loc[amzn["Close"].idxmax(),"Date"],baba.loc[baba["Close"].idxmax(),"Date"],crm.loc[crm["Close"].idxmax(),"Date"], \
       goog.loc[goog["Close"].idxmax(),"Date"],intc.loc[intc["Close"].idxmax(),"Date"],meta.loc[meta["Close"].idxmax(),"Date"], msft.loc[msft["Close"].idxmax(),"Date"], \
        nvda.loc[nvda["Close"].idxmax(),"Date"],tsla.loc[tsla["Close"].idxmax(),"Date"]]
print("EMPRESAS ORDENADAS SEGÚN EL MAYOR PRECIO DE CIERRE EN EL ÚLTIMO AÑO:")
#DataFrame donde se muestra las fechas y los precios de cierre máximos de cada empresa en orden descendente según el precio de cierre
maxClose=pd.DataFrame({"Dates": dates, "Max Close":maximos}).sort_values(by=["Max Close"],ascending=False)
print(maxClose)
maxEmpresa=maxClose["Max Close"].idxmax()
print(f"La empresa con el mayor precio de cierre es {maxEmpresa}")

#DICCIONARIO CON LOS PRECIOS DE CIERRE A FINAL DE CADA MES
dictClose={'Apple': max_month(aapl), 'Amazon': max_month(amzn), 'Alibaba': max_month(baba), 'Salesforce': max_month(crm), 'Google': max_month(goog), 'Intel': max_month(intc), \
         'Meta': max_month(meta),'Microsoft': max_month(msft), 'Nvidia': max_month(nvda), 'Tesla': max_month(tsla)}
#GRÁFICO DE LOS PRECIOS DE CIERRE A FINAL DE CADA MES PARA CADA EMPRESA
impr_graph(dictClose)
