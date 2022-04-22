import pandas as pd
import time
import glob
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# mercek2_temp = pd.concat(map(pd.read_excel, glob.glob('//10.90.1.239/14 ic kontrol bas/Analitik/data/ioz/databank/mercek/mercek20' + "/*.xlsx")))
mercek21_temp = pd.concat(map(pd.read_excel, glob.glob('//10.90.1.239/14 ic kontrol bas/Analitik/data/ioz/databank/mercek/mercek21' + "/*.xlsx")))
mercek21 = mercek21_temp.copy()

mercek21.isnull().sum()

mercek21 = mercek21[mercek21["YIL ORT BAKIYE"] != 0]

musteri_adet = mercek21[["ANA ŞUBE", "MUST NO", "KISA ISIM"]].groupby(["ANA ŞUBE", "MUST NO"]).agg(["count"]).reset_index()
musteri_adet2 = musteri_adet.groupby(["ANA ŞUBE"]).count().reset_index()
musteri_adet3 = musteri_adet2.iloc[:,0:2]
musteri_adet3.columns = ["Şube No", "Müşteri Sayısı"]
musteri_adet3.to_excel("//10.90.1.239/14 ic kontrol bas/Analitik/data/ioz/databank/mercek/musteri_adet.xlsx", index =False)



