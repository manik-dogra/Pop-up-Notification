# Popup - Notifications Sender

## Working Video <br/>

https://user-images.githubusercontent.com/74672126/182908827-021845ba-c54f-4a0b-a5ab-dfef5f41367f.mp4

## About <br/>

>* A Software which sends notifications on email, text message and on whatsapp to the users whenever a new product is added into the database. <br/>
>* Sending notification automatically will save a lot of time, manpower and money. <br/>
>* Technologies used to built this software are: **Python, Django, API, MySQL**. <br/>
>* A Webpage is also created to add the products, and also that will show whether the notifications have been sent or not. <br/>
>* User can select whether to get messages on email/SMS/whatsapp. <br/>

## How to run <br/>

>* Install python, django and neccesaary packages/libraries. <br/>
>* Libraries must be installed in the python eniornment. You can create a virtual enviornment usning the below command. <br/>

###### To create a new python enviornment: <br/>
          virtualenv -p python3 envname <br/>

>* Create a twilio account. <br/>
>* From twilio Get the API Keys and Phone numbers of whatsapp and SMS respectively and paste them in the code as shown below. <br/>

>* <img width="590" alt="image" src="https://user-images.githubusercontent.com/74672126/182889199-65f18dc8-9fb9-4022-ad04-cf0ee49e62f3.png">
>* Create a database in XAMPP for products having attributes id (primary key and auto increment), name, availability, date. <br/>
>* Create a user in django admin, and the number of subscribed user should be verified by twilio. <br/>  

###### To go inside virtual enviornment: <br/>
          .\env\Scripts\activate <br/>

###### To run: <br/>
          python .\manage.py runserver <br/>

>* You're ready to go. <br/>
