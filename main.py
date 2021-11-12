import streamlit as st
import time

st.title('Streamlit 入門')
st.write('Showing progress bar')

'Start!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done.'

# left_column,right_column=st.beta_columns(2)
# btn=left_column.button('右コラムに文字を表示')

# if btn:
#     right_column.write('This is right column.')

# exp=st.beta_expander('問い合わせ')
# exp.write('書く')
# text = st.sidebar.text_input('あなたの趣味は？')

# condition=st.sidebar.slider('あなたの調子は？',0,100,50)

# 'あなたの趣味は、',text,'です。'

# 'Condition:',condition



# option = st.selectbox(
#     'Select your fovorite number',
#     list(range(1,11))
# )
# 'Selected number is ',option,'.'


# if st.checkbox('Show Image'):
#     img=Image.open('sample.jpg')
#     st.image(img,caption='あゆすけ', use_column_width=True)





