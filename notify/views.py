from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context
from .models import User
from twilio.rest import Client
import smtplib
import mysql.connector
from django.contrib import messages

def home(request):
    return render(request, "index.html")

def send_function(request):
    
    gmail_user = 'himanshudhar02@gmail.com'
    gmail_password = 'vmubyobwsjydgqot'
    my_db =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "edai"
    )
    mycursor = my_db.cursor()  
    name = request.GET['productName']
    availability = request.GET['productDetails']
    print(name," ", availability)
    sql = "INSERT INTO ga (id, product, availability, launch) VALUES (NULL, %s, %s, current_timestamp())"
    val = (name, availability)
    mycursor.execute(sql, val)
    my_db.commit()
    print(mycursor.rowcount, "record inserted.")
    mycursor.execute("Select * from ga")
    result = mycursor.fetchone()
    # #############
    allUsers = User.objects.all()
    body = 'Greetings from group 2\n This is the push notification project.\nThe latest entry is  --->' + result[1] + '\nthe availability staus of this product is  ---->' + result[2] + '\nThis product was launched on --->' + result[3].strftime('%d/%m/%Y')
    ####
    for user in allUsers:
        if user.userchoice_email:
            sent_from = gmail_user
            to = user.user_email
            subject = 'Automated Email'
    
            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)
            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print ("Email sent successfully!")
            except Exception as ex:
                print ("Something went wrong….",ex)
        if user.userchoice_message:
            client = Client('AC378aae47bb96762fdb82deb5b6444335', '3bbb3f12eca99f05ca34c24790529e93')
            client.messages.create(
	            body=body,from_='+19896440454',to=user.user_number)
            print("Message sent")
        if user.userchoice_whatsapp:
            client = Client('AC378aae47bb96762fdb82deb5b6444335', '3bbb3f12eca99f05ca34c24790529e93')
            client.messages.create(
	            body=body,from_='whatsapp:+14155238886',to=user.user_whatsapp)
            print("Whatsapp sent")
    
    messages.success(request, 'Notifications sent.')
    
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")