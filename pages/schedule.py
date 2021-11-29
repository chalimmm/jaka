import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def FilterCourse():
    cred = credentials.Certificate("pages/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    for course in courses:
        getData = db.collection('courses').document(course).get()
        if getData.exists:
            getData = getData.to_dict()
            if courses[course] != getData:
                print("UPDATE : " + str(course))
                db.collection('courses').document(course).update(courses[course])
        else:
            db.collection('courses').document(course).set(courses[course])
    
    c1, c2 = st.columns((3, 1))
    with c1:
        course_list = []
        for course in courses:
            course_list.append(course['name']+' ('+str(course['sks'])+' SKS)') 
        st.subheader('Select Course(s)')
        course_selected = st.multiselect('', options=course_list)
    with c2:
        for i in range(4):
            st.write(' ')
        
        st.markdown("""
        <style>
        div.stButton > button {
            background-color: #f72585;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #f8f8f8;
            box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 10px 20px 0 rgba(0,0,0,0.19);
        }
        </style>""", unsafe_allow_html=True)
        
        if st.button('Create Plan'):
            for course_name in course_selected:
                for course in courses:
                    if course['name'] == course_name[:-4]:
                        course['selected'] = 'Yes'
                        break
            return True
    
def SelectSchedule():
    c1, c2 = st.columns ([3,1])
    
    with c1:
        with st.expander("Course 1"):
            course1_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours1 = st.radio('Pilih Kelas yang Diinginkan:', course1_sched, key='cours1')
    
        with st.expander("Course 2"):
            course2_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours2 = st.radio('Pilih Kelas yang Diinginkan:', course2_sched, key='cours2')
        
        with st.expander("Course 3"):
            course3_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours3 = st.radio('Pilih Kelas yang Diinginkan:', course3_sched, key='cours3')
    
        with st.expander("Course 4"):
            course4_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours4 = st.radio('Pilih Kelas yang Diinginkan:', course4_sched, key='cours4')
    
        with st.expander("Course 5"):
            course5_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours5 = st.radio('Pilih Kelas yang Diinginkan:', course5_sched, key='cours5')
    
        with st.expander("Course 6"):
            course6_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours6 = st.radio('Pilih Kelas yang Diinginkan:', course6_sched, key='cours6')
    
        with st.expander("Course 7"):
            course7_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours7 = st.radio('Pilih Kelas yang Diinginkan:', course7_sched, key='cours7')
    
        with st.expander("Course 8"):
            course8_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours8 = st.radio('Pilih Kelas yang Diinginkan:', course8_sched, key='cours8')
    
    with c2:
        st.write("Jadwal yang telah dipilih per matkul")
        st.write("")
        st.write("")
        st.write("Course 1:", cours1)
        st.write("Course 2:", cours2)
        st.write("Course 3:", cours3)
        st.write("Course 4:", cours4)
        st.write("Course 5:", cours5)
        st.write("Course 6:", cours6)
        st.write("Course 7:", cours7)
        st.write("Course 8:", cours8)

def app():
    return FilterCourse()
