# Guidelines to contribute
There are two parts of the project frontend and backend development.

Understanding the working
---
Right now the project has a simple boilerplate. It takes any link 
which is referred to Groovy bot. This is done via Slack API. The
Slack API sends the text to our backend API server which then stores it
in a database. 
   
To retrieve these links in frontend, we send a request to our API endpoint
which sends in response an array of the links in the database, which can be shown 
and used in different components of the frontend.  
  
The backend endpoint is in Django and uses the rest_framework package. One instance of the 
master branch backend is hosted on my Heroku right now. 
The frontend is in React and at the moment it only shows the links in the database. The design is 
done using [Ant.d](https://ant.design/).  

Procedure to Contribute
---
1. Fork the repo
2. Clone the forked repo
3. Run the app.
4. Go to main [repo](https://github.com/Shashvat6264/Groovy-Slack).
5. Check out the issues in it.
6. See if any issue interests you and you want to work on it.
7. Put a comment on that issue saying you want to address it.
8. Wait for me to assign the issue to you. 
8. **_Assigning of issues is totally on first come - first serve basis but if you have an issue already assigned to you, you have to complete it to get a new issue._**
9. After being assigned the issue, work on the codebase to address the issue.
10. If you are not able to understand some part or want some resources to address the issue, you are always welcome to send me a DM on Slack or post your query in '#queries' channel.
10. After modifying the code accordingly, commit it and push it to your forked repo in a different brach.
11. Send a pull request of your modified branch to my main repo from your forked repo.
12. Sit back and relax, I will take it from here.

To create a new issue:
1. If you catch a bug in the code, report it in the '#issues' channel of Slack.
2. If I approve it, Go ahead and make an issue in my repo.
3. If you wish to address it too leave a comment below it saying so, I will assign it to you.


Handling Open Source
---

#### Getting Started
To get started with contributing you need to fork my [repo](https://github.com/Shashvat6264/Groovy-Slack). This 
would create a replica of my repo in your account. Then to make a local git of the forked repo in your machine, 
Clone your forked repo. **Note: You need to have Git installed in your OS, Git bash for Windows users**. This will create 
a local copy of the code in your machine. Then, you need to create an upstream remote to keep your code up to date.
You can do the following by running this command in git bash opened in the cloned repo.
```bash
    git remote add upstream https://github.com/Shashvat6264/Groovy-Slack.git
```
You can check if it worked by running:
```bash
    git remote -v
```
This will list all remotes present in the repo.

#### Sending a Pull request after work is completed
**Note: Please do all your work in a different branch. Don't do it in main branch**

To make a different branch use the command: 
```bash
    git checkout -b branchname
```

If you have completed the coding part, and wish to merge your addition to the main repo. You need to add all new files in your 
local repo and commit the changes. First push the branch in your forked repo using this command.
```bash
    git push origin branchname
```
Then go to your forked repo on github, where you can see the send pull request option. Click on it to send a Pull request successfully.
Now you just have to wait eagerly for me to merge your awesome work. 

#### Updating your repo to avoid merge conflicts
**Note: This is very important. Please do keep updating your repo. In case you get any merge conflict. You can contact me if there is problem in solving it**

Since, there are a lot of people working on the same codebase. There are chances that, I had merged someone's code in my main repo but the code on your local machine 
is still in it's previous version, which is obsolete now. This might lead you to wasting many precious hours on working on code which is no more being used. To avoid this 
you need to regularly keep updating your codebase in local machine. You can do this by running this command in git bash opened in your local code.
```bash
    git pull upstream main
``` 
This will update your main branch with the new codebase of the main repo.
**Note: Setting up upstream remote explained above is very important for this part**

How to run the project in your device
---
I prefer if you use PyCharm as your text editor for this project. If you 
don't have said software, you can download it's professional version from [here](https://www.jetbrains.com/pycharm/download/#section=windows) 
using your [institute](https://www.jetbrains.com/community/education/#students) ID. If you decide to use 
some other editor don't forget to turn on the virtual environment before working on the specified part of the project.

#### Running Backend
If you are using Pycharm:  
1. Open up your Pycharm Editor.
2. Open project using Open project option.
3. Open directly the Backend folder inside the cloned repo.
4. To run the program, click on **Run** option.
5. You have the Backend API running on the 127.0.0.1:8000 i.e. your localhost on port 8000.
6. You can work in the open Pycharm, then add, commit and send pull request to the main repo.  

If you are in some other editor:
1. Open the Backend folder inside the cloned repo directly.
2. Activate the virtual environment inside the folder. The command to activate it depends on 
the OS you are working on.
For ubuntu users:
    ```bash
        source venv/bin/activate
    ``` 
3. After activating the virtual environment, you can run the Backend server with the command
    ```bash
        python3 manage.py runserver 
    ```
4. You have the Backend API running on the 127.0.0.1:8000 i.e. your localhost on port 8000.
5. You can work in the open editor, then add, commit and send pull request to the main repo.

#### Running Frontend
If you are using Pycharm:  
1. Open up your Pycharm Editor.
2. Open project using Open project option.
3. Open directly the Frontend folder inside the cloned repo.
4. To run the program, click on **Run** option.
5. You have the Frontend running on the 127.0.0.1:3000 i.e. your localhost on port 3000.
6. You can work in the open Pycharm, then add, commit and send pull request to the main repo.  

If you are in some other editor:
1. Open the Frontend folder inside the cloned repo directly.
2. Activate the virtual environment inside the folder. The command to activate it depends on 
the OS you are working on.
For ubuntu users:
    ```bash
        source venv/bin/activate
    ``` 
3. After activating the virtual environment, you can run the Frontend server with the command
    ```bash
        npm start 
    ```
4. You have the Frontend running on the 127.0.0.1:3000 i.e. your localhost on port 3000.
5. You can work in the open editor, then add, commit and send pull request to the main repo.


**Note: I would really appreciate if you could make a separate branch for the work you do and then send that branch in the pull request instead of the main branch**

**_Cheers, Happy Coding!!!_** 