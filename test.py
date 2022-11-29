import streamlit as st
import pandas as pd
from database import get_schedule_skill,get_user_id,get_skill_training,get_emp_schedule,update_emp_skill,get_par_score

# question_list=[
# ["Which one is NOT a legal variable name?", "my_var", "_myvar", "my-var", "my_var"],
# ["How do you create a variable with the numeric value 5?", "x=5", "x=int(5)", "Both the other answer are correct","x = 5"],
# ["What is the correct way to create a function in Python?", "Def myFunction():", "create myFunction():", "function myFunction():", "Def myFunction():"],
# ["What is a correct syntax to return the first character in a string?", "x = 'Hello'.sub(0,1)", "x = sub('Hello', 0, 1)", "x = 'Hello'[0]", "x = 'Hello[0]'"],
# ["Which collection is ordered, changeable, and allows duplicate members?", "Set", "Dictionary", "List", "List"] 
# ]

def get_score(emp_id,courses):
    # question=[]
    # for i in range(len(question_list)):
    #     question[i] = st.radio(question_list[i][0], (question_list[i][1], question_list[i][2], question_list[i][3]))
   
    ans1 = st.radio("Which one is NOT a legal variable name?",('my_var', '_myvar', 'my-var'))
    ans2 = st.radio("How do you create a variable with the numeric value 5?",('x=5', 'x=int(5)', 'Both the other answer are correct'))
    ans3 = st.radio("What is the correct way to create a function in Python?",('Def myFunction():', 'create myFunction():', 'Def myFunction():'))
    ans4 = st.radio("What is a correct syntax to return the first character in a string? ",("x = 'Hello'.sub(0,1)", "x = sub('Hello', 0, 1)", "x = 'Hello'[0]"))
    ans5 = st.radio("Which collection is ordered, changeable, and allows duplicate members? ",('Set', 'Dictionary', 'List'))

    score=0
    if st.button("Submit"):
        if ans1=='my_var':
            score+=1
        if ans2=='x=5':
            score+=1
        if ans3=='Def myFunction():':
            score+=1
        if ans4=='x=Hello[0]':
            score+=1
        if ans5=='List':
            score+=1

    return score 
    
def get_courses(u_id):
    n = get_emp_schedule(u_id)
    m=[]
    for ele in n:
        m.append(ele)
    return m    
    
def Take_test():
    u_id = get_user_id()
    m = get_courses(u_id)
    # st.write(m)
    choice = st.selectbox("taken Courses",m)
    score =  get_score(u_id,choice)
    skill,p_score = get_par_score(choice)
    if score >= p_score:
        update_emp_skill(u_id ,skill)