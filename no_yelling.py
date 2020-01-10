def filter_words(st):
    st=st.lower()
    st=st.strip()
    st=st.replace('  ', ' ')
    st=st.replace('  ', ' ')
    first=st[0].upper()
    return first+st[1:]

filter_words('HELLO CAN YOU HEAR ME')