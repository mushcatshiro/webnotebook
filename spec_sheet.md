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

#### ETA 8/11 2359

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

#### ETA 9/11 2359

	- get post by userid ('/post/<int:userId>')
		- currently only grabs post based on user id provided
			- automatically redirect upon login
			- JWT
	- get all post 
		- homepage/mainpage
	- get post by title ('/post/<title>')
		- currently grabs post based on post title
			- title/any input
			- return post
	- post post ('/posts/<int:num>', '/posts/')
		- currently grabs post based on the number of post provided
		- if using 2nd route '/posts/', returns all post)
			- title, content, others, userid (separately for db), JWT
			- create post