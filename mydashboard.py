import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

mydf = pd.read_csv("Dataframe Dashboard.csv")
print(mydf)
mydf['Date'] = pd.to_datetime(mydf['Date'])


# Subsetting Data by Station
dongsi_daily = mydf.query("station == 'Dongsi'")
guanyuan_daily = mydf.query("station == 'Guanyuan'")
gucheng_daily = mydf.query("station == 'Gucheng'")
shunyi_daily = mydf.query("station == 'Shunyi'")
wanliu_daily = mydf.query("station == 'Wanliu'")

# Kondisi Pencemaran Udara oleh PM2.5 dan PM10
bystation_df = mydf.groupby(by='station').agg({
    'PM2.5' : 'mean',
    'PM10' : 'mean',
})

# Correlation Plot
mycol = ['PM2.5', 'PM10','CO']
subset_df = mydf[mycol]

mycor = subset_df.corr()

# plt.figure(figsize=(10, 8))
# sns.heatmap(mycor, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Plot Korelasi')
# plt.show()


# # Barplot
# Dongsi
dongsi_monthly = dongsi_daily.copy()
dongsi_monthly['Date'] = pd.to_datetime(dongsi_monthly['Date'])
dongsi_monthly.set_index('Date', inplace=True)
dongsi_monthly = dongsi_monthly.resample(rule='M').agg({
    'PM2.5': 'mean',
    'PM10': 'mean',
    'CO': 'mean'
}).reset_index()

pm25_monthly1 = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

for idx, month in enumerate(months, start=1):
    pm25_month = dongsi_monthly[dongsi_monthly['Date'].dt.month == idx]
    pm25_monthavg = pm25_month['PM2.5'].mean()
    pm25_monthly1[month] = pm25_monthavg
pm25_dongsi = pd.DataFrame(list(pm25_monthly1.items()), columns=['Month', 'PM2.5 AVG'])

print(pm25_dongsi)

# Guanyuan
guanyuan_monthly = guanyuan_daily.copy()
guanyuan_monthly['Date'] = pd.to_datetime(guanyuan_monthly['Date'])
guanyuan_monthly.set_index('Date', inplace=True)
guanyuan_monthly = guanyuan_monthly.resample(rule='M').agg({
    'PM2.5': 'mean',
    'PM10': 'mean',
    'CO': 'mean'
}).reset_index()

pm25_monthly2 = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
for idx, month in enumerate(months, start=1):
    pm25_month = guanyuan_monthly[guanyuan_monthly['Date'].dt.month == idx]
    pm25_monthavg = pm25_month['PM2.5'].mean()
    pm25_monthly2[month] = pm25_monthavg
pm25_guanyuan = pd.DataFrame(list(pm25_monthly2.items()), columns=['Month', 'PM2.5 AVG'])

# Gucheng
gucheng_monthly = gucheng_daily.copy()
gucheng_monthly['Date'] = pd.to_datetime(gucheng_monthly['Date'])
gucheng_monthly.set_index('Date', inplace=True)
gucheng_monthly = gucheng_monthly.resample(rule='M').agg({
    'PM2.5': 'mean',
    'PM10': 'mean',
    'CO': 'mean'
}).reset_index()

pm25_monthly3 = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
for idx, month in enumerate(months, start=1):
    pm25_month = gucheng_monthly[gucheng_monthly['Date'].dt.month == idx]
    pm25_monthavg = pm25_month['PM2.5'].mean()
    pm25_monthly3[month] = pm25_monthavg
pm25_gucheng = pd.DataFrame(list(pm25_monthly3.items()), columns=['Month', 'PM2.5 AVG'])

# Shunyi
shunyi_monthly = shunyi_daily.copy()
shunyi_monthly['Date'] = pd.to_datetime(shunyi_monthly['Date'])
shunyi_monthly.set_index('Date', inplace=True)
shunyi_monthly = shunyi_monthly.resample(rule='M').agg({
    'PM2.5': 'mean',
    'PM10': 'mean',
    'CO': 'mean'
}).reset_index()

pm25_monthly4 = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
for idx, month in enumerate(months, start=1):
    pm25_month = shunyi_monthly[shunyi_monthly['Date'].dt.month == idx]
    pm25_monthavg = pm25_month['PM2.5'].mean()
    pm25_monthly4[month] = pm25_monthavg
pm25_shunyi = pd.DataFrame(list(pm25_monthly4.items()), columns=['Month', 'PM2.5 AVG'])

# Wanliu
wanliu_monthly = wanliu_daily.copy()
wanliu_monthly['Date'] = pd.to_datetime(wanliu_monthly['Date'])
wanliu_monthly.set_index('Date', inplace=True)
wanliu_monthly = wanliu_monthly.resample(rule='M').agg({
    'PM2.5': 'mean',
    'PM10': 'mean',
    'CO': 'mean'
}).reset_index()

pm25_monthly5 = {}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
for idx, month in enumerate(months, start=1):
    pm25_month = wanliu_monthly[shunyi_monthly['Date'].dt.month == idx]
    pm25_monthavg = pm25_month['PM2.5'].mean()
    pm25_monthly5[month] = pm25_monthavg
pm25_wanliu = pd.DataFrame(list(pm25_monthly5.items()), columns=['Month', 'PM2.5 AVG'])

# DASHBOARD ============================================================================================================

min_date = mydf["Date"].min()
max_date = mydf["Date"].max()

with st.sidebar:
    st.image("https://th.bing.com/th/id/OIP.mTUkzo2AYlvwZoiqKK4rKgHaED?rs=1&pid=ImgDetMain")

    start_date, end_date = st.date_input(
        label='Range Time', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    station = st.radio(
        label = "Select The Station Below : ",
        options = ("Dongsi", "Guanyuan", "Gucheng", "Shunyi", "Wanliu"),
        horizontal = False
    )

df = mydf[(mydf["station"]==station)]
df = df[(df["Date"] >= str(start_date)) & (df["Date"] <= str(end_date))]

st.header('Air Pollution Dashboard')
st.subheader(f'PM2.5 Quality')

col1, col2 = st.columns(2)
with col1:
    st.metric("City", value=station)
with col2:
    pm25 = df["PM2.5"]
    avgpm25 = round(sum(pm25) / len(pm25), 2)
    st.metric("Average PM2.5", value=avgpm25)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    df["Date"],
    df["PM2.5"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("PM2.5 Distribution Plot")

col1, col2, col3 = st.columns(3)
with col1:
    fig, ax = plt.subplots(figsize=(15,15))
    dongsi_daily['PM2.5'].hist()
    ax.set_title("Dongsi", loc = "center", fontsize=45)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(15,15))
    guanyuan_daily['PM2.5'].hist()
    ax.set_title("Guanyuan", loc="center", fontsize=45)
    st.pyplot(fig)
with col3:
    fig, ax = plt.subplots(figsize=(15,15))
    gucheng_daily['PM2.5'].hist()
    ax.set_title("Gucheng", loc="center", fontsize=45)
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(15, 15))
    shunyi_daily['PM2.5'].hist()
    ax.set_title("Shunyi", loc="center", fontsize=45)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(15, 15))
    wanliu_daily['PM2.5'].hist()
    ax.set_title("Wanliu", loc="center", fontsize=45)
    st.pyplot(fig)

st.subheader("PM2.5, PM10, and CO Assosiation")
mycol = ['PM2.5', 'PM10','CO']
subset_df = mydf[mycol]
mycor = subset_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(mycor, annot=True, cmap='coolwarm', fmt=".2f")
plt.tight_layout()
st.pyplot()

st.subheader("Monthly PM2.5 Condition")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        pm25_dongsi["Month"],
        pm25_dongsi["PM2.5 AVG"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.set_title("Dongsi", loc="center", fontsize=45)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        pm25_guanyuan["Month"],
        pm25_guanyuan["PM2.5 AVG"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.set_title("Guanyuan", loc="center", fontsize=45)
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        pm25_gucheng["Month"],
        pm25_gucheng["PM2.5 AVG"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.set_title("Gucheng", loc="center", fontsize=45)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        pm25_shunyi["Month"],
        pm25_shunyi["PM2.5 AVG"],
        marker='o',
        linewidth=2,
        color="#90CAF9"
    )
    ax.set_title("Shunyi", loc="center", fontsize=45)
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    pm25_wanliu["Month"],
    pm25_wanliu["PM2.5 AVG"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.set_title("Wanliu", loc="center", fontsize=45)
st.pyplot(fig)




st.caption('Copyright (c) ML-15 | Muhammad Iqbal')