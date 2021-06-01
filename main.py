from typing import List
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)



st.write('DataFrame')

df = pd.DataFrame({
  '1列目': [1,2,3,4],
  '2列目': [10,20,30,40],
})

# st.write(df)
# axis=1 列
# axis=0 行

# 動的な表
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# 静的な表
st.table(df.style.highlight_max(axis=0))
# cf. https://docs.streamlit.io/en/stable/api.html#display-data

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# 折線グラフ
st.title('折線グラフ')
df1 = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a','b','c']
)
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

#map 経度、緯度 新宿周辺
df2 = pd.DataFrame(
  np.random.rand(100,2)/[50,50] + [35.69,139.70],
  columns=['lat','lon']
)
st.map(df2)

# 画像
st.write('Display Image')
if st.checkbox('Show Image'):
  img = Image.open('/Users/yusuke.tokuda/Downloads/image_python.jpeg')
  st.image(img, caption='あくまでもイメージです',use_column_width=True)

option = st.selectbox(
  'あなたが好きな数字を教えてください',
  list(range(1,11))
)
# st.write('あなたが好きな数字は、',option,'です。')
'あなたが好きな数字は、',option,'です。'

st.sidebar.write('Interactive Widget')
option2 = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味は、',option2,'です。'

condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'コンディション：', condition

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容１')
expander.write('問い合わせ内容２')
expander.write('問い合わせ内容３')