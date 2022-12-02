
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/<isChat>")
def index(isChat):
    return render_template('home.html', chatIsActive = (isChat!=None), path="/")


@app.route("/forum")
def forum():
   con = sqlite3.connect("databases/bd.sqlite")
   
   cur = con.cursor()
   rowMsg = None
   cur.execute("select * from channel")
   rows = cur.fetchall()
   return render_template('forum.html', rows = rows)

@app.route("/forum/<subject>")
def subject(subject):
    con = sqlite3.connect("databases/bd.sqlite")

    message = con.cursor()
    message.execute(f"select * from msg where channel_id={subject} ")
    rowMsg = message.fetchall()

    message.execute(f"select nom from channel where id = {subject}")
    name = message.fetchone()[0]

    rowMsg.reverse()

    return render_template('subject.html',rowMsgs = rowMsg, id =subject, name= name)

@app.route('/addmsg',methods = ['POST' ])
def addmsg():
   if request.method == 'POST':
        msg = request.form['message']
        id = request.form['id']
    
        con = sqlite3.connect("databases/bd.sqlite")
        cur = con.cursor()
        cur.execute("INSERT INTO msg (msgContent,isAdmin,channel_id) VALUES (?,?,?)",(msg,0,id) )

        con.commit()
        con.close()

        # return render_template("subject.html")
        return redirect('/forum/'+id)

@app.route("/jeu")
def game(): 
    return render_template('game.html')


@app.route("/enquete")
def enquete():
    return render_template('enquete.html')


@app.route("/enquete/easterEgg")
def easterEgg():
    return render_template('easterEgg.html')
