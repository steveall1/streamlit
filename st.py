import streamlit as st
import pandas as pd


st.set_page_config(
    page_title = "Streamlit Prototype",
    page_icon = "_",
    layout='wide'
)

st.text('Streamlit 프로토타입 만들기')

st.header('홍기범은.')
st.subheader('왜 홍범기인가?.')


st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')




st.title('홍기범 : Title을 입력하세요')



stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)



st.dataframe(df_index.style.highlight_max(axis=0))


symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')
st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])

