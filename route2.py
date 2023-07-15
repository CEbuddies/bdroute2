import streamlit as st

if __name__ == '__main__':

    st.text('I am the everlasting memory of unthinkable horror.\nWhat I am telling you is more than 100 years in the past!\n')
    st.text('Do not know where I am? Look where this city has its garden ;)')

    st.text('Do the math and tell me the result')

    num_eq = st.number_input('Result: ')

    

    if num_eq == 1896:
        


        st.text('I tell of great success and the birth of a nation.\nI am exposed to the elements and you may find me,\nwhere an entire continent has its >>place<<.')

        st.text('Find the numbers that are not arabic and sum them up to get the next hint.')

        num = st.number_input('Your number is: ')

        if num == 10:

            st.text('Seek the Alter Simon and ask the bartender for advice.')
            st.text('Your codeword is: Herrengedeck')
            st.text('Hint: Why not buy him a drink?')
