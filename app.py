import streamlit as st 
st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  result = -b/a
  st.success(f'Phương trình có 1 nghiệm {result}')