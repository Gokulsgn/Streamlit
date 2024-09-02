import streamlit as st

st.title("Hello streamlit")

st.header("Header")

st.subheader("Sub Header")

st.text("Gokulnath Renuka")

st.markdown("""
# H1
## H2
### H3
#### H4
##### H5
###### H6

:heart:<br>
:smile:            
                                    
**Gokul(Bold)**  
_italic_                     

""",True           )

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
''')


d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 

st.write(d)