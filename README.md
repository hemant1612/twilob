# twilob
### Installation Instructions
#

#### 1.	Use git clone to clone this repository to your local machine: 
```sh 
$ git clone https://github.com/anurag-bug/twitter.git

```
#### 2. Navigate to Source Directory
```sh 
$ cd twitter-master
```

#### 3.Create a virtualenv
In windows
```sh
C:\Users\Name\twitter-master> python -m venv myvenv 
```
In Linux
```sh
$ python3 -m venv myvenv
```

#### 4. Start your virtual environment by running:
In windows
```sh
C:\Users\Name\twitter-master> myvenv\Scripts\activate
```
In ubuntu
```sh
$ source/myvenv/bin/activate
```
#### 5. Installing packages with requirements
Ubuntu
```sh
pip install -r requirements.txt
```
Windows
```sh
C:\Users\Name\twitter-master> python -m pip install -r requirements.txt
  ```
  
#### 6. Apply migrations
```sh
(myvenv) ~/twitter-master$ python manage.py makemigrations
(myvenv) ~/twitter-master$ python manage.py migrate
```
#### 7. Run server
```sh
(myvenv) ~/twitter-master$ python manage.py runserver
```
 App will run on http://127.0.0.1:8000/twitter/search/

### Todos

 - Create twitter account specific feedback
 
