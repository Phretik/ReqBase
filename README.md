# ReqBase
Reqbase: Web Application for Software Engineering and Agile Module
Reqbase is a web application tailored to my current job role in applications packaging. It facilitates the management of requests for packaged apps and enables team collaboration through a shared log. The application supports two types of users: admin and standard.

User Roles:

Standard Users: Standard users can register, log in, and manage their own requests. They have the following permissions:
- Create, read, update, and delete their own requests.
- View team log posts created by other users.
- Change their own passwords.
- Cannot edit or delete team log posts.

Admin Users: Admin users have broader privileges and responsibilities. They can perform the following actions:
- Create, read, update, and delete all requests.
- Create, read, update, and delete team log posts.
- Change their own passwords.
- Cannot change the passwords of other users.

User Accounts:
Two initial user accounts have been created for demonstration purposes:

Admin Account:

-Email: Admin@admin.com
-Password: Tester1995
This account has admin privileges and should be used for administrative tasks.

-Standard Account:

-Email: Test@test.com
-Password: Tester1995
This is a standard user account, suitable for regular use. Additional standard accounts can be created if needed.

Security Measures:
The application incorporates protections against common security vulnerabilities, including broken access control, broken authentication, SQL injection, XSS, and other OWASP Top 10 vulnerabilities.
Comments and indentation have been utilized throughout the code to enhance readability and maintainability.