# spec sheet

## user

	- sqlite (username, password, email, userid, key)
	- login, logout, create, reset password, change password
	- non login user permission read/search
	- normal user permission write, edit own post
	- super user permission delete

## post

	- create
	- read
	- update
	- delete

## api

### user-related

	- login/logout
		- username, password
		- auth token, permission?, JWT
	- create account
		- username, password, email
		- email
	- reset password
		- username, password, email
		- reset password key
	- change password
		- username, password
	- super user access

### post related

	- get post by userid
		- automatically redirect upon login
		- JWT
	- get all post
		- homepage/mainpage
	- get post by title
		- title/any input
		- return post
	- post post
		- title, content, others, userid (separately for db), JWT
		- create post