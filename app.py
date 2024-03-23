import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def load_data():
    data = pd.read_csv('data/train.csv')
    return data

st.markdown('# Анализ качества вина')
data = load_data()

quality = tuple(np.unique(data['quality']))
option = st.sidebar.selectbox(
    "Уровень качества вина:",
    quality, placeholder="Выберите уровень качества..."
)

nrows = st.sidebar.slider("Количество отображаемых строк",value=5, min_value=0, max_value=len(data['Id'].loc[data['quality'] == option]))

df_show = st.sidebar.checkbox("Показать таблицу с данными")

if df_show:
    st.write(data.loc[data['quality'] == option].head(nrows))

if st.sidebar.button('Описательная статистика'):
    st.markdown("### Сводная таблица параметров вина по уровню качества")
    describe = data.drop(['Id', 'quality'], axis=1).loc[data['quality'] == option].describe()
    st.write(describe)

hist_on = st.sidebar.toggle('Показать гистограмму')

if hist_on:
    columns = tuple(np.unique(data.drop(['Id', 'quality'], axis=1).columns))
    hist_parameter = st.selectbox("Параметр:", columns, placeholder="Выбрать параметр")
    x = data[hist_parameter].loc[data['quality'] == option]
    fig, ax = plt.subplots()
    ax.hist(x, bins=25)
    st.pyplot(fig)
