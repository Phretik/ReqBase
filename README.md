# ReqBase
A web app for my software engineering and agile module

This is a web app that is designed to be relevant to my current job role. Applications packaging.
Reqbase is a web app that allows users to log on, register requests they have received for packaged apps and update their team with a team log that they can use to update their team and log their progress and activities. There exists 2 types of users for Reqbase, admin and and standard. Standard users may sign up and create, read, update and delete their own requests. They may also create their own and read the posts of other users on the team log webpage. However, they are unable to edit or delete posts. 
Admin users however can create, read and update all requests, but only delete their own. Admin users can also create, read, update and delete all posts on the team log. 
Both types of users are able to change their own passwords, but not the passwords of others.
Of course, you cannot sign up as an admin. There is only one admin account, which I have listed the details of below. I have also created a standard account for use if signing up another is not preffered. 

Their are 2 users created:
1) Email: Admin@admin.com    password: password
2) Email: Test@test.com      password: password

User 1 is of course an admin account, however the second and all subsequent users will be standard accounts

This app's dependencies from pip freeze:
-click==8.1.3
-colorama==0.4.6
-Flask==2.2.2
-Flask-Login==0.6.2       
-Flask-SQLAlchemy==3.0.3  
-greenlet==2.0.2
-importlib-metadata==6.0.0
-itsdangerous==2.1.2      
-Jinja2==3.1.2
-MarkupSafe==2.1.2        
-pipdeptree==2.7.0        
-SQLAlchemy==2.0.7
-typing_extensions==4.5.0
-Werkzeug==2.2.2
-zipp==3.12.1
