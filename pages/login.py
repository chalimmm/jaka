import streamlit as st

check_u = 'admin'
check_p = 'admin'

def auth(username, password):
    if username == check_u and password == check_p:
        st.success('Login Successful')
    else:
        st.warning('Login Unsuccessful')
    return True

def app():
    st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
    st.markdown("<a style='text-align: center;'>Sign in to your JAKA account.</a>", unsafe_allow_html=True)
    with st.form('login_form', clear_on_submit=True):
        u = st.text_input('Username', max_chars=30)
        p = st.text_input('Password', type='password', max_chars=30)
        with st.expander("See explanation"):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
        is_agree = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        col1, col2, col3  = st.columns((3,1,3))
        with col1:
            pass
        with col3:
            pass
        with col2 :
            is_login = st.form_submit_button('Login')
    if is_agree and is_login:
        return auth(u, p)
    else:
        return False
