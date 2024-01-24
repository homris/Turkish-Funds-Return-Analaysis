import matplotlib.pyplot
import pandas as pd

#Convert CSV into DataFrame
df = pd.read_csv("CSV Files/baslangic.csv")
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
for getiri in df['Getiri (%)']:
    if getiri > mean_return + std_return:
        print("Başarılı")
    elif getiri > mean_return - std_return:
        print("Nötr")
    else:
        print("Başarısız")


#Making graphs/charts
"""ax = df.sort_values("Getiri (%)").plot.bar(x="Fon Kodu", y="Getiri (%)")
#bx = df.sort_values("Getiri (%)").plot.box(x="Fon Kodu", y="Getiri (%)", ax=ax)

df.sort_values("Getiri (%)").plot.line(x="Fon Kodu", y="Getiri (%)", rot=90, ax=ax)

matplotlib.pyplot.show()"""