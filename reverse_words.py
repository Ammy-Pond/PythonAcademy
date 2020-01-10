def reverse(st):
    st=st.strip()
    st=st.replace('  ', ' ')
    st=st.replace('  ', ' ')
    st=st.split(' ')
    st.reverse()
    st= ' '.join(st)
    return st