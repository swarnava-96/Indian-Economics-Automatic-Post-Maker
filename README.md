# Indian Economy Automatic Post Maker

### Goal: The goal of this project is to create a post maker that will give the top six latest news of the Indian Economy so that one can download that image and upload it on instagram or linkedin stories.

### Project Outline:
1. Economic news are scrapped from [here](https://www.businesstoday.in/latest/economy) using BeautifulSoup.
2. Flask is used at the backend to create the web application.
3. Front end is created using HTML, CSS and Java Script. 
4. Application is run on local host(port: 5000)

### Installation:
The Code is written in Python 3.7.3 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

##### 1. First create a virtual environment by using this command:
```bash
conda create -n myenv python=3.7
```
##### 2. Activate the environment using the below command:
```bash
conda activate myenv
```
##### 3. Then install all the packages by using the following command
```bash
pip install -r requirements.txt
```
##### 4. Then, in cmd or Anaconda prompt write the following code:
```bash
python app.py
```
##### Make sure to change the directory to the root folder inside cmd/Anaconda prompt.  

### A glimpse of the application:

![image](https://user-images.githubusercontent.com/75041273/147985972-2939e2e7-43da-45f1-87d8-4b34b26300af.png)

### Further Changes to be Done:

- [ ] Deploying the Web Application on Cloud.
     - [ ] Google Cloud 
     - [ ] Azure
     - [ ] AWS EC2
     - [ ] Heroku
