import streamlit as st


def take_test(emp_id,courses):
    # u_id = get_user_id()
    # get_courses
    # col1,col2,col3,col4 = st.columns(4)
    # with col1:
        pass
    
    
def get_courses(u_id):
    n = get_emp_schecdule(u_id)
    m=[]
    for ele in n:
        m.append(n[1])
    return m    
    
def update_emp_skill(u_id,skill):
    c.execute(f"select distinct name,role from employee where emp_id = {u_id}")
    data=c.fetchall()
    (name , role) = (data[0][0],data[0][1])
    c.execute(f"insert into employee values({u_id},{name},{skill},{role});")
    
    
    
def test_options():
    u_id = get_user_id()
    m = get_courses(u_id)
    choice = st.selectbox("taken Courses",m)
    score =  take_test(u_id,choice)
    skill,p_score = get_par_score(choice)
    if(score > p_score):
        update_emp_skill(u_id ,skill)
        