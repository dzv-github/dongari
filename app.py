import streamlit as st
import pandas as pd


def initialize_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'get_start' not in st.session_state:
        st.session_state.get_start = 0


def update_score(player_choice, correct_answer):
    if player_choice == correct_answer:
        st.session_state.player_score += 1

st.title("Quiz Game")
initialize_session_state()

def calculate_score(player_choice):
    ind=st.session_state.current_question
    c_q=df.loc[ind]
    correct_answer = c_q['correct_answer']
    update_score(player_choice, correct_answer)
    st.session_state.current_question += 1


first=pd.read_csv('problem.csv')
second=pd.read_csv('problem2.csv')
third=pd.read_csv('third_problem.csv')


if st.session_state.get_start==0:
    player_c=st.selectbox('Select categori:',options=['Problem','Problem2'])
    if st.button('Start'):
        if player_c=='Problem':
            st.session_state.get_start+=1
        if player_c=='Problem2':
            st.session_state.get_start+=2
        st.experimental_rerun()

else:
    if st.session_state.get_start==1:
        df=first
    
    if st.session_state.get_start==2:
        df=second
    quiz_questions=df['question']
    

    if st.session_state.current_question >= len(quiz_questions):
        st.success("Quiz Finished!")
        st.write(f"Your Score: {st.session_state.player_score}")
        if st.session_state.player_score==7:
            st.success('You get a perfect score!!!')
        st.write('program ended')

    else:

        ind = st.session_state.current_question
        c_q=df.loc[ind]
        st.write(c_q['question'])

        player_choice = st.selectbox("Select your answer:",
                                 options=[c_q['option 1'],c_q['option 2'],c_q['option 3'],c_q['option 4'],c_q['option 5']],
                                 key=f"question_{ind}") 
        if st.button("Submit", key=f"submit_{ind}"):   
            calculate_score(player_choice)
            if st.session_state.current_question < len(quiz_questions):
                st.experimental_rerun()
        
            if st.session_state.current_question >= len(quiz_questions):
            
                st.experimental_rerun()
