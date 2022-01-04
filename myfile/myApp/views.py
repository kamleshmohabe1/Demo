from django.shortcuts import render,redirect
from django.http import HttpResponse
import MySQLdb

# Create your views here.
def register(req):
	return render(req,"insert.html")
def Register(req):
	Fname=req.GET['Fname']
	Lname=req.GET['Lname']
	Email=req.GET['Email']
	Phone=req.GET['Phone']
	conn=MySQLdb.connect("localhost","root","","register")
	cur=conn.cursor()
	query="insert into registerdata(Fname,Lname,Email,Phone)values('{}','{}','{}','{}')".format(Fname,Lname,Email,Phone)
	cur.execute(query)
	conn.commit()
	cur.close()
	conn.close()
	return redirect("/ViewData")
def ViewData(req):
	conn=MySQLdb.connect("localhost","root","","register")
	cur=conn.cursor()
	query="select * from registerdata"
	cur.execute(query)
	res=cur.fetchall()
	conn.commit()
	cur.close()
	conn.close()
	return render(req,"views.html",{'data':res})

def edit(req):
	SerNo=req.GET['SerNo']
	conn=MySQLdb.connect("localhost","root","","register")
	cur=conn.cursor()
	query="select * from registerdata where SerNo={}".format(SerNo)
	cur.execute(query)
	result=cur.fetchone()
	conn.commit()
	cur.close()
	conn.close()
	return render(req,"edits.html",{'data':result})

def updateData(req):
	Ser=req.GET['SerNo']
	Fname=req.GET['Fname']
	Lname=req.GET['Lname']
	Email=req.GET['Email']
	Phone=req.GET['Phone']
	conn=MySQLdb.connect("localhost","root","","register")
	cur=conn.cursor()
	query="update registerdata set Fname='{}',Lname='{}',Email='{}',Phone='{}' where SerNo='{}'".format(Fname,Lname,Email,Phone,Ser)
	cur.execute(query)
	conn.commit()
	cur.close()
	conn.close()
	return redirect("/ViewData")

def delete(req):
	ser=req.GET['SerNo']
	conn=MySQLdb.connect("localhost","root","","register")
	cur=conn.cursor()
	query="delete from registerdata where SerNo={}".format(ser)
	cur.execute(query)
	conn.commit()
	cur.close()
	conn.close()
	return redirect("/ViewData")
