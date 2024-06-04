from streamlit import st
import pandas as pd
import numpy as np

# Vo, Da, Viの%を入力する欄
st.write('Vo, Da, Viのレッスンボーナス%を入力してください')

vo = st.number_input('Vo (%)', 0, 100, 30)
da = st.number_input('Da (%)', 0, 100, 30)
vi = st.number_input('Vi (%)', 0, 100, 30)

st.write('レッスンの表')

# レッスンの表を作成

df = pd.DataFrame(
    data = [
        ["1回目", 60, 0, np.NaN],
        ["2回目", 60, 90, np.NaN],
        ["追い込み", 180, np.NaN, 90],
        ["中間", 20, np.NaN, 20],
        ["3回目", 110, 170, np.NaN],
        ["授業", 70, np.NaN, np.NaN],
        ["4回目", 120, 200, np.NaN],
        ["5回目", 150, 220, np.NaN],
        ["追い込み2", 330, np.NaN, 165],
        ["期末", 30, np.NaN, 30]
    ],
    columns = ["レッスン回数", "ノーマル", "SP", "未選択"]
).set_index("レッスン回数")

df_Da = df.copy(deep=True).drop(columns=["ノーマル", "SP", "未選択"])
df_Da["Da_N"] = df["ノーマル"] * (1 + da / 100)
df_Da["Da_SP"] = df["SP"] * (1 + da / 100)
df_Da["Vo"] = df["未選択"] * (1 + vo / 100)
df_Da["Vi"] = df["未選択"] * (1 + vi / 100)

df_Vo = df.copy(deep=True)
df_Vo["Vo_N"] = df["ノーマル"] * (1 + vo / 100)
df_Vo["Vo_SP"] = df["SP"] * (1 + vo / 100)
df_Vo["Da"] = df["未選択"] * (1 + da / 100)
df_Vo["Vi"] = df["未選択"] * (1 + vi / 100)

df_Vi = df.copy(deep=True)
df_Vi["Vi_N"] = df["ノーマル"] * (1 + vi / 100)
df_Vi["Vi_SP"] = df["SP"] * (1 + vi / 100)
df_Vi["Da"] = df["未選択"] * (1 + da / 100)
df_Vi["Vo"] = df["未選択"] * (1 + vo / 100)

# checkboxで選択肢を表示
if st.checkbox('Voのみ表示'):
    tgt = df_Vo
    col_N = ["Vo_N", "Da", "Vi"]

if st.checkbox('Daのみ表示'):
    tgt = df_Da
    col_N = ["Vo", "Da_N", "Vi"]

if st.checkbox('Viのみ表示'):
    tgt = df_Vi
    col_N = ["Vo", "Da", "Vi_N"]

goal1 = [400 - tgt["追い込み"][i] for i in col_N]
goal2 = [1000 - tgt["追い込み"][i] for i in col_N]


st.write(tgt)

# 中間前追い込み後に400を越えるための条件
st.write('中間前追い込み後に400を越えるための条件')
st.write(pd.DataFrame(
    data = [goal1],
    columns = col_N
))

# 期末前追い込み後に1000を越えるための条件
st.write('期末前追い込み後に1000を越えるための条件')
st.write(pd.DataFrame(
    data = [goal2],
    columns = col_N
))