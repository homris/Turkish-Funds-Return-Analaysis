# import matplotlib.pyplot as plt
import pandas as pd
import os

# Convert CSV into DataFrame
directory_path = "static/files/"
most_recent_file = None
most_recent_time = 0

for entry in os.scandir(
    directory_path
):  # iterate over the files in the directory using os.scandir
    if entry.is_file():
        # get the modification time of the file using entry.stat().st_mtime_ns
        mod_time = entry.stat().st_mtime_ns
        if mod_time > most_recent_time:
            # update the most recent file and its modification time
            most_recent_file = entry.name
            most_recent_time = mod_time

df = pd.read_csv(directory_path + most_recent_file)
print(df.to_string())

# Parse float from string and turn into US decimal points(.)
df["Getiri (%)"] = pd.to_numeric(df["Getiri (%)"].str.replace(",", "."))


# Max Return Percentage + convert back to TR decimal points(,)
def get_max():
    max_return = df.loc[:, "Getiri (%)"].max()
    max_return_string = str(max_return).replace(".", ",")

    print("\nMaksimum Fon Getirisi: %" + max_return_string)


# Min Return Percentage + convert back to TR decimal points(,)
def get_min():
    min_return = df.loc[:, "Getiri (%)"].min()
    min_return_string = str(min_return).replace(".", ",")

    print("\nMinimum Fon Getirisi: %" + min_return_string)


# Calculate Return Mean
def calc_mean(tr):
    mean = df.loc[:, "Getiri (%)"].mean()
    mean_tr = str(round(mean, 4)).replace(".", ",")

    if tr == True:
        return mean_tr
    else:
        return mean


# Calculate Return Standard Deviation Population
def calc_std(tr, type):
    if type == "sample":
        std_type = 1
    else:
        std_type = 0

    std = df.loc[:, "Getiri (%)"].std(ddof=std_type)  # ddof=1 for sample std
    std_tr = str(round(std, 4)).replace(".", ",")

    if tr == True:
        return std_tr
    else:
        return std


# Başarılı, Nötr, Başarısız Fonlar
def egm_ranking():
    basarili_count = 0
    basarisiz_count = 0
    nötr_count = 0

    for getiri in df["Getiri (%)"]:
        row = df[df["Getiri (%)"] == getiri].index

        fund_code_temp = df.iloc[row]["Fon Adı"]
        print(fund_code_temp)

        if getiri > calc_mean(False) + calc_std(False, "population"):
            print("Başarılı\n")
            basarili_count += 1
        elif getiri > calc_mean(False) - calc_std(False, "population"):
            print("Nötr\n")
            nötr_count += 1
        else:
            print("Başarısız\n")
            basarisiz_count += 1

    print(str(basarili_count) + " Başarılı")
    print(str(nötr_count) + " Nötr")
    print(str(basarisiz_count) + " Başarısız")


# Making graphs/charts
"""ax = df.sort_values("Getiri (%)").plot.bar(x="Fon Kodu", y="Getiri (%)")
# bx = df.sort_values("Getiri (%)").plot.box(x="Fon Kodu", y="Getiri (%)", ax=ax)

df.sort_values("Getiri (%)").plot.line(x="Fon Kodu", y="Getiri (%)", rot=90, ax=ax)

plt.show()"""

get_max()
get_min()
print("\nOrtalama Fon Getirisi: %" + calc_mean(True))
print("\nStandart Sapma: %" + calc_std(True, "population"))
egm_ranking()
