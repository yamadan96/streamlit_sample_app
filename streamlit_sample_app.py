import streamlit as st
import pandas as pd
import numpy as np

# データの読み込み
# データの作成
data = pd.DataFrame({
    'A': np.random.randint(0, 100, 10),
    'B': np.random.randint(0, 100, 10),
    'C': np.random.randint(0, 100, 10)
})

# データの表示
st.dataframe(data)

# データの統計情報の表示
st.write(data.describe())

# グラフの表示
st.line_chart(data)


# ランダムな場所のマップ表示
random_lat = np.random.uniform(-90, 90)
random_lon = np.random.uniform(-180, 180)
data['LAT'] = random_lat
data['LON'] = random_lon
st.map(data)
