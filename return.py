import matplotlib.pyplot
import pandas as pd

#Convert CSV into DataFrame
df = pd.read_csv("CSV Files/01.01.2023-02.01.2024-değişken.csv")
print(df.to_string())

#Parse float from string and turn into US decimal points(.)
df['Getiri (%)'] = pd.to_numeric(df['Getiri (%)'].str.replace(',', '.'))

#Max Return Percentage + convert back to TR decimal points(,)
max_return = df.loc[:, "Getiri (%)"].max()
max_return_string = str(max_return).replace('.', ',')

print("\nMaksimum Fon Getirisi: %" + max_return_string)

#Min Return Percentage + convert back to TR decimal points(,)
min_return = df.loc[:, "Getiri (%)"].min()
min_return_string = str(min_return).replace('.', ',')

print("\nMinimum Fon Getirisi: %" + min_return_string)

#Calculate Return Mean
mean_return = df.loc[:, "Getiri (%)"].mean()
mean_return_string = str(round(mean_return, 4)).replace('.', ',')

print("\nOrtalama Fon Getirisi: %" + mean_return_string)

#Calculate Return Standard Deviation Population
std_return = df.loc[:, "Getiri (%)"].std(ddof=0)#ddof=1 for sample std
std_return_string = str(round(std_return, 4)).replace('.', ',')

print("\nStandart Sapma (Popülasyon): %" + std_return_string)

#Başarılı, Nötr, Başarısız Fonlar
basarili_count = 0
basarisiz_count = 0
nötr_count = 0

for getiri in df['Getiri (%)']:
    if getiri > mean_return + std_return:
        print("Başarılı")
        basarili_count += 1
    elif getiri > mean_return - std_return:
        print("Nötr")
        nötr_count += 1
    else:
        print("Başarısız")
        basarisiz_count += 1

print(str(basarili_count) + " Başarılı")
print(str(nötr_count) + " Nötr")
print(str(basarisiz_count) + " Başarısız")



#Making graphs/charts
"""ax = df.sort_values("Getiri (%)").plot.bar(x="Fon Kodu", y="Getiri (%)")
#bx = df.sort_values("Getiri (%)").plot.box(x="Fon Kodu", y="Getiri (%)", ax=ax)

df.sort_values("Getiri (%)").plot.line(x="Fon Kodu", y="Getiri (%)", rot=90, ax=ax)

matplotlib.pyplot.show()"""