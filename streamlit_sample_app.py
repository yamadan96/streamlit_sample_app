import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ダミーデータをDataFrameに変換
data = {'日付': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    '体重': [70, 71, 70.5, 70.2, 70.8],
    '体脂肪率': [20, 19.5, 19, 18.5, 18]}
df = pd.DataFrame(data)

# グラフの描画
fig, ax1 = plt.subplots()

# 体重の推移を折れ線グラフで表示
ax1.plot(df['日付'], df['体重'], color='tab:blue')
ax1.set_xlabel('日付')
ax1.set_ylabel('体重', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# 体脂肪率を棒グラフで表示
ax2 = ax1.twinx()
ax2.bar(df['日付'], df['体脂肪率'], color='tab:orange', alpha=0.5)
ax2.set_ylabel('体脂肪率', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# グラフのタイトルと軸の回転
plt.title('体重と体脂肪率の推移')
plt.xticks(rotation=45)

# グラフを表示
st.pyplot(fig)
