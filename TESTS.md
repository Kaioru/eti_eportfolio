# tests [![CircleCI](https://github.com/Kaioru/eti_eportfolio/workflows/Python%20CI/badge.svg)](https://github.com/Kaioru/eti_eportfolio/actions) [![codecov](https://codecov.io/gh/Kaioru/eti_eportfolio/branch/master/graph/badge.svg?token=p4ZqZcLLTM)](https://codecov.io/gh/Kaioru/eti_eportfolio)
this file documents all the test cases for this project.

## testing 🧪
1. Install Google Chrome and Chrome Driver
2. `pip install -r requirements-test.txt`
3. `pytest`

## cases 🗃
*no model tests were done as it is assumed that Django has the proper validations in place and is already tested.*

### route tests
| description | values | expected |
|:----------- |:------ |:-------- |
| to test the route of the blogs index page | `/blogs/` | `status_code: 200`
| to test the route of the blogs detail page | `/blogs/1/` | `status_code: 200`
| to test the route of the category index page | `/blogs/Rants/` | `status_code: 200`
| to test the route of the projects index page | `/projects/` | `status_code: 200`
| to test the route of the projects detail page | `/projects/1` | `status_code: 200`
| to test the default fallback page of the site | `/randomurl123!` | redirect to `/projects/`

### backend tests
| description | values | expected |
|:----------- |:------ |:-------- |
| to test the http post route of a valid comment | ```{ "author": "Keith", "body": "Hello hello!" }``` | a comment is created
| to test the http post route of a empty comment body | *empty* | comment is not created
| to test the http post route of a comment with a long author name | ```{ "author": "x" * 61, "body": "Hello hello!" }``` | comment is not created

### browser tests
*all browser tests are run in Google Chrome in headless mode. this ensures that all tests can be run on any platform even when there is no GUI available.*

#### admin
| description | values | expected |
|:----------- |:------ |:-------- |
| to test a valid admin login | ```{ "username": "admin", "password": "password" }``` | validation success; redirect to admin page
| to test a invalid password admin login | ```{ "username": "admin", "password": "abc" }``` | validation fail; show error note
| to test a invalid username admin login | ```{ "username": "gfds", "password": "password" }``` | validation fail; show error note
| to test the changing of password with valid credentials | ```{ "old_password": "password", "new_password1": "abdzxc123", "new_password2": "abdzxc123"}``` | change password successfully
| to test the changing of password with wrong old password | ```{ "old_password": "wrongOldPassword", "new_password1": "abdzxc123", "new_password2": "abdzxc123"}``` | validation fail; show error note
| to test the changing of password with mistmatched passwords | ```{ "old_password": "password", "new_password1": "mismatchPassword1", "new_password2": "mismatchPassword2"}``` | validation fail; show error note
| to test the changing of password with short new password | ```{ "old_password": "password", "new_password1": "abdzxc1", "new_password2": "abdzxc1"}``` | validation fail; show error note

##### category / comment / post
*for the sake of redundancy and as these 3 types have similar tests, the tests will be consolidated in 1 section. the values can be found in the test files*

| description | values | expected |
|:----------- |:------ |:-------- |
| to test a valid creation of type | *varies* | new type created; success message shown
| to test creation of type with empty fields | *empty* | validation fail; show error note
| to test creation of type with too long fields | *varies* | as field does not allow data to be out of its bounds, it will be truncated and then created; new type created; success message shown
| to test a valid edit of type | *varies* | new type created; success message shown
| to test editting of type with too long fields | *varies* | as field does not allow data to be out of its bounds, it will be truncated and then created; type editted; success message shown
| to test deletion of a type | the type is selected | type deleted; success message shown
| to test deletion of a type without selecting | *empty* | show error note

#### blog
| description | values | expected |
|:----------- |:------ |:-------- |
| to test the blogs index page | `/blogs/`, *at least 1 blog post* | show all the blog posts
| to test the blogs index page when there is no posts | `/blogs/`, *empty* | shows a error note
| to test the category index page | `/blogs/Rants/`, *at least 1 blog post in category* | show all the blog posts
| to test the category index page when there is no posts | `/blogs/Rants/`, *empty* | shows a error note
| to test if blogs with long bodies are being truncated | `/blogs/`, ```{ "body": "x" * 450 }``` | the body of the blog is truncated to "x" * 400 + "..."
| to test the blog detail page | `/blogs/1/` | shows the blog details
| to test the blog detail page with invalid post | `/blogs/100/` | does not show any blog details
| to test the creation of comment | `/blogs/1/`; ```{ "author": "x" * 60, "body": "Cool blog post!" }``` | new comment created; new comment shown
| to test the creation of comment with too long author | `/blogs/1/`; ```{ "author": "x" * 61, "body": "Cool blog post!" }``` | as field does not allow data to be out of its bounds, it will be truncated and then created; new comment created; new comment shown
| to test the creation of comment with empty fields | `/blogs/1/`; *empty* | show error note; not created
| to test if comments allow for cross-site scripting | `/blogs/1/`; ```{ "author": "Keith", "body": "<script>alert('hello world!')</script>" }``` | new comment created; new comment shown; script does not execute

#### project
| description | values | expected |
|:----------- |:------ |:-------- |
| to test the projects index page | `/projects/`, *at least 1 project* | show all the blog posts
| to test the projects index page when there is no posts | `/projects/`, *empty* | shows a error note
| to test the projects detail page | `/projects/1/` | shows the project details
| to test the projects detail page with invalid project | `/projects/100/` | does not show any project details