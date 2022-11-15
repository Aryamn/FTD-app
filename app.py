import os
from flask import Flask, session, render_template, url_for, redirect, request, flash
import sqlite3 as sql
from datetime import datetime
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)

#store path to images in the dictionary
questions_emotion = {
    '1':{'question':  'Surprise',
    'options':['surprise','happy','sad','disgust','silly','think'],
    'answer':'surprise'},

    '2':{'question': 'Angry',
    'options':['sad','surprise','think','happy','silly','angry'],
    'answer':'angry'},

    '3':{'question': 'Happiness',
    'options':['disgust','think','surprise','sad','happy','silly'],
    'answer':'happy'},

    '4':{'question': 'Sadness',
    'options':['disgust','surprise','think','sad','silly','angry'],
    'answer':'sad'},

    '5':{'question': 'Disgust',
    'options':['sad','disgust','happy','surprise','angry','silly'],
    'answer':'disgust'},

    '6':{'question': 'Fear',
    'options':['sad','disgust','happy','silly','surprise','angry'],
    'answer':'surprise'},

    '7':{'question': 'Think',
    'options':['disgust','surprise','think','sad','silly','angry'],
    'answer':'think'}
}

questions_emotion_2 = {
    '1':{'question':  'Surprise',
    'options':['surprise2','happy2','sad2','disgust2','worried2','fear2'],
    'answer':'surprise2'},

    '2':{'question': 'Fear',
    'options':['sad2','surprise2','fear2','happy2','disgust2','worried2'],
    'answer':'fear2'},

    '3':{'question': 'Happiness',
    'options':['disgust2','worried2','surprise2','sad2','happy2','fear2'],
    'answer':'happy2'},

    '4':{'question': 'Sadness',
    'options':['disgust2','surprise2','worried2','sad2','fear2','angry2'],
    'answer':'sad2'},

    '5':{'question': 'Disgust',
    'options':['sad2','disgust2','happy2','surprise2','worried2','fear2'],
    'answer':'disgust2'},

    '6':{'question': 'Fear',
    'options':['sad2','disgust2','happy2','fear2','surprise2','worried2'],
    'answer':'fear2'},

    '7':{'question': 'Angry',
    'options':['disgust2','surprise2','angry2','sad2','worried2','happy2'],
    'answer':'angry2'}
}

questions_emotion_3 = {
    '1':{'question': '',
    'options':['fear2','happy2','sad2','worried2'],
    'answer':'happy'},

    '2':{'question': '',
    'options':['surprise2','happy2','sad2','worried2'],
    'answer':'sad'},

    '3':{'question': '',
    'options':['disgust2','surprise2','fear2','worried2'],
    'answer':'surprise'},

    '4':{'question': '',
    'options':['fear2','happy2','surprise2','disgust2'],
    'answer':'disgust'},

    '5':{'question': '',
    'options':['angry2','happy2','sad2','worried2'],
    'answer':'angry'}
}

questions_visuo_spatial = {
    '1':{'question': 'Shape',
    'options':['star2','diamond2','triangle2','star','square','diamond2','triangle2','star2','semi'],
    'answer':'square2'},
   
    '2':{'question': 'Shape',
    'options':['circle','diamond','triangle','star','square','semi','diamond2','triangle2','star2'],
    'answer':'circle2'},

    '3':{'question': 'Shape',
    'options':['diamond2','square2','circle','diamond','triangle','star','square','semi','star2'],
    'answer':'triangle2'},

    '4':{'question': 'Shape',
    'options':['diamond','circle','diamond2','triangle2','triangle','star','square','semi','plus'],
    'answer':'star2'},

    '5':{'question': 'Shape',
    'options':['square','semi','plus','triangle2','star2','circle','diamond','triangle','star'],
    'answer':'circle2'},

    '6':{'question': 'Shape',
    'options':['circle','diamond','triangle','star','plus','triangle2','star2','square','semi'],
    'answer':'plus2'},

    '6':{'question': 'Shape',
    'options':['circle','triangle','diamond','star','square','semi','plus','diamond2','star2'],
    'answer':'triangle2'}
}

score_emotion = 0
score_visuo_spatial = 0
score_emotion_2 = 0
score_emotion_3 = 0
time_visuo = time.time()
time_emotion = time.time()
time_emotion_2 = time.time()
time_emotion_3 = time.time()
Name = ""
Age = ""
Sex = ""

def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


@app.route('/',methods=['GET','POST'])
def front():
    if request.method == 'POST':
        global Name
        global Age
        global Sex

        Name = request.form.get("name")
        Age = request.form.get("age")
        Sex = request.form.get("sex")
        print(Name)
        if Name=="" or not is_float(Age):
            flash("Invalid Name  or Age!")
        else:   
            print(Name)
            print(Age)
            print(Sex)
            return redirect(url_for('index'))
    return render_template("index.html")


@app.route('/emotion',methods=['GET','POST'])
def index():
    if request.method == "POST":
        entered_answer = request.form.get("answer")

        if not entered_answer:
            flash("Please choose an answer","error")
        
        else:
            global score_emotion
            global time_emotion

            curr_answer = request.form['answer']
            correct_answer = questions_emotion[session["current_question"]]["answer"] #change 

            if curr_answer==correct_answer:
                score_emotion+=1
            print(score_emotion)

            session["current_question"] = str(int(session["current_question"])+1)

            if session["current_question"] in questions_emotion:
                redirect(url_for('index'))

            else:
                time_emotion =  time.time()-time_emotion
                print(time_emotion)
                return render_template("end_quiz_emotion.html")

    if "current_question" not in session:
        score_emotion = 0
        time_emotion =  time.time()
        session["current_question"] = "1"

    elif int(session["current_question"]) > len(questions_emotion):
        session["current_question"] = "1"
        score_emotion = 0
        time_emotion =  time.time()-time_emotion
        print(time_emotion)
        return render_template("end_quiz_emotion.html")

    currentQ = questions_emotion[session["current_question"]]["question"]
    op1,op2,op3,op4,op5,op6 = questions_emotion[session["current_question"]]["options"]

    return render_template('ftd_emotion_quiz.html',num=int(session["current_question"]),question=currentQ,ans1=op1,ans2=op2,ans3=op3,ans4=op4,ans5=op5,ans6=op6)


@app.route('/emotion2',methods=['GET','POST'])
def page2():
    if request.method == "POST":
        entered_answer = request.form.get("answer")

        if not entered_answer:
            flash("Please choose an answer","error")
        
        else:
            global time_emotion_2
            global score_emotion_2
            
            curr_answer = request.form['answer']
            correct_answer = questions_emotion_2[session["current_question_2"]]["answer"] #change 

            if curr_answer==correct_answer:
                time_emotion_2 = time.time()
                score_emotion_2+=1
            print(score_emotion_2)

            session["current_question_2"] = str(int(session["current_question_2"])+1)

            if session["current_question_2"] in questions_emotion_2:
                redirect(url_for('page2'))

            else:
                time_emotion_2 =  time.time()-time_emotion_2
                print(time_emotion_2)
                return render_template("end_quiz_emotion_2.html")

    if "current_question_2" not in session:
        score_emotion_2 = 0
        time_emotion_2 = time.time()
        session["current_question_2"] = "1"

    elif int(session["current_question_2"]) > len(questions_emotion_2):
        score_emotion_2 = 0
        time_emotion_2 =  time.time()-time_emotion_2
        print(time_emotion_2)
        session["current_question_2"] = "1"
        return render_template("end_quiz_emotion_2.html")

    currentQ = questions_emotion_2[session["current_question_2"]]["question"]
    op1,op2,op3,op4,op5,op6 = questions_emotion_2[session["current_question_2"]]["options"]

    return render_template('ftd_emotion_quiz.html',num=int(session["current_question_2"]),question=currentQ,ans1=op1,ans2=op2,ans3=op3,ans4=op4,ans5=op5,ans6=op6)

@app.route('/emotion3',methods=['GET','POST'])
def page3():
    if request.method == "POST":
        entered_answer = request.form.get("answer")

        if not entered_answer:
            flash("Please choose an answer","error")
        
        else:
            global score_emotion_3
            global time_emotion_3
            
            curr_answer = request.form['answer']
            correct_answer = questions_emotion_3[session["current_question_3"]]["answer"] #change 

            if curr_answer[:-1]==correct_answer:
                time_emotion_3 = time.time()
                score_emotion_3+=1
            print(score_emotion_3)

            session["current_question_3"] = str(int(session["current_question_3"])+1)

            if session["current_question_3"] in questions_emotion_3:
                redirect(url_for('page3'))

            else:
                time_emotion_3 = time.time()-time_emotion_3
                print(time_emotion_3)
                return render_template("end_quiz_emotion_3.html")

    if "current_question_3" not in session:
        time_emotion_3 = time.time()
        session["current_question_3"] = "1"

    elif int(session["current_question_3"]) > len(questions_emotion_3):
        session["current_question_3"] = "1"
        time_emotion_3 = time.time()-time_emotion_3
        print(time_emotion_3)
        return render_template("end_quiz_emotion_3.html")

    currentQ = questions_emotion_3[session["current_question_3"]]["question"]
    op1,op2,op3,op4= questions_emotion_3[session["current_question_3"]]["options"]
    currentA = questions_emotion_3[session["current_question_3"]]["answer"]
    return render_template('ftd_emotion_quiz_3.html',num=int(session["current_question_3"]),question=currentQ,ans=currentA,ans1=op1,ans2=op2,ans3=op3,ans4=op4)


@app.route('/visuospatial',methods=['GET','POST'])
def visuospatial():
    if request.method == "POST":
        entered_answer = request.form.get("answer")

        if not entered_answer:
            flash("Please choose an answer","error")
        
        else:
            global score_visuo_spatial
            global time_visuo
            
            curr_answer = request.form['answer']
            correct_answer = questions_visuo_spatial[session["current_question_visuo"]]["answer"] #change 

            if curr_answer==correct_answer[:-1]:
                time_visuo = time.time()
                score_visuo_spatial+=1
            print(score_visuo_spatial)

            session["current_question_visuo"] = str(int(session["current_question_visuo"])+1)

            if session["current_question_visuo"] in questions_visuo_spatial:
                redirect(url_for('index'))

            else:
                print(Name)
                print(Age)
                print(Sex)
                print(score_emotion)
                print(score_emotion_2)
                print(score_emotion_3)
                time_visuo = time.time()-time_visuo
                print(time_visuo)

                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO FTD (Name,Age,Sex,EROG1_score,EROG2_score,\
                    EROG3_score,VISPA_score,EROG1_time , EROG2_time , EROG3_time ,\
                    VISPA_time ) VALUES (?,?,?,?,?,?,?,?,?,?,?)",\
                    (Name,Age,Sex,score_emotion,score_emotion_2,score_emotion_3,score_visuo_spatial,time_emotion
                    ,time_emotion_2,time_emotion_3,time_visuo) )
                
                    con.commit()
                    print("Record successfully added")
                return render_template("end_quiz_visuo.html")

    if "current_question_visuo" not in session:
        time_visuo = time.time()
        session["current_question_visuo"] = "1"

    elif int(session["current_question_visuo"]) > len(questions_visuo_spatial):
        session["current_question_visuo"] = "1"
        print(Name)
        print(Age)
        print(Sex)
        print(score_emotion)
        print(score_emotion_2)
        print(score_emotion_3)
        time_visuo = time.time()-time_visuo
        return render_template("end_quiz_visuo.html")

    currentQ = questions_visuo_spatial[session["current_question_visuo"]]["question"]
    op1,op2,op3,op4,op5,op6,op7,op8,op9 = questions_visuo_spatial[session["current_question_visuo"]]["options"]
    currentA = questions_visuo_spatial[session["current_question_visuo"]]["answer"]
    return render_template('ftd_visuo_quiz.html',num=int(session["current_question_visuo"]),question=currentQ,ans=currentA,ans1=op1,ans2=op2,ans3=op3,ans4=op4,ans5=op5,ans6=op6
    , ans7=op7,ans8=op8,ans9=op9)

    

