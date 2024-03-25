# The Study Portal:



The project aims to ease the work of students. Instead of visiting several sites, 'The Study Portal' is a one-stop solution for it. Containing several features and a user-friendly UI.
The student portal can bring all the tabs to a single site. From homework to to-do list to getting YouTube videos and making notes and making list of blogs/articles/books that you want to read, everything will be saved in one place. With a fully flexible authentication system.


** The live application can be viewed here : **

[https://study-portal-1ae4e787ae9c.herokuapp.com/](https://study-portal-1ae4e787ae9c.herokuapp.com/)

## Purpose and Target Audience:


### Problem Statement:

As a student, we usually logged In to many sites, open ChatGPT simultaneously, watch videos on some other tab and the browser gets filled with all the unnecessary tabs.

### Purpose: 

The study portal application will help students to manage their study and achieve their goals by not only managing their homework’s and creating notes but along with that managing their day-to-day tasks, so they never miss any opportunity.

### Target Audience:

The primary target audience include students who wants to manage their studies/tasks as well as individuals learners who want to learn new things while balancing their work by prioritizing the tasks.

## Persona and User Stories:

Piya is a curious and passionate student who loves to plan and prioritize her task beforehand so she never miss any deadline. She likes to read books/articles so, she makes an list of articles she wants to read whenever she had time. Along with this she likes to take notes and save it. 

### User Stories :

-	As a Site User I can create/update/delete my homework so that I can manage my task.
*	As a site user, I can view a list of features so that I can select which feature to manage my studies.
+	As a Site User, I can click on notes so that I can create new notes.
-	As a Site User / Admin I can view Notes I already created so that I can read whenever I want.
*	As a Site User I can delete my notes so that I can manage my notes.
+	As a Site User I can register an account so that I can use app features to manage my studies.
-	As a Site User I can create/update/delete to-do list so that I can manage my task.
*	As a Site User I can search content on youtube so that I can fully understand new concepts.
+	As a Site User I can see my progress so that I can achieve my goals.
-	As a Site User I can ask question to copilot/chatbot so that I get clear understanding.


## Wireframe & Initial Design:

### HomePage:


 ![home](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/37ac38b5-ed77-4b36-bff8-5dcb0b5c97ce)
 

### Homework(LoggedIn user):


 ![Homework](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/20f4fcd3-3df1-47fc-a81a-681ab025a50c)

 

### Register New User:


 ![register](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/158afa0c-8ec9-4a63-92f9-355da03d1a78)

 

### User Profile :


![Profile](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/e2eaa7ef-1f8f-492e-a736-6f7e801df530)



## Log In :

 
![login](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/7dddb4bb-9da4-4f07-92ab-979d0207b2cd)




## Agile:


This project was created using Agile principles via a project board on GitHub. This is the first time I have implemented Agile as an individual developer. However, creating user stories and identifying acceptance criteria acted as a roadmap to target the various features and functionalities of the application. It helped me stay on track and reduced distractions.

 

## Database:


### ER Diagram :


![erd](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/120bd727-1bf1-4f44-b2fe-ba646bcc6b94)

 

### Flowchart:

 
![flowchart](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/d7d38c1e-4b8b-4b90-a402-88b4f4b2eb67)



## Priority Features:

### HomePage:


The landing page provides an introduction to the website with all the features listed with responsive nav bar showcasing existing user can login or new user can register to the application. The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Home, Profile Register/Logout and Log In.


![home](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/1702a066-3197-431c-bbb9-072ce4507358)

 

### Registration:


Registration will allow new user to register to the application which will give user rights to create notes, add homework, add todo list and create profile to watch progress etc.


![register](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/49624308-127f-4bda-9c79-e95e2c605403)

 
### Login :


Login will allow existing user to login to the application and see profile and user study portal feature to manage study.

 
![login](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/ae8f991d-3e40-4eaf-98fe-934aa7f011ac)



### Notes:


Logged In user can user notes to create new notes or see existing added notes. User can delete note as well when done and user can have detail view of existing note.


 ![notes](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/c3dc8d6f-43e8-40fd-b8b6-0e7337a3fc93)



### Detail view Note:
 

![detailnotes](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/01d9507c-95bc-4469-a548-08184887f712)



### Books:

Books page will display list of books/blogs user has added to read along with the status of finished or not. User can add more ebooks just by providing link to the book.


![books](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/89dfbc85-2dad-4723-b98d-c412e5ed3211)


### HomeWork :

Homework page will display users homework. User can delete homework from the list of table when its finished.
 

![homework](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/336ad105-d8e6-42a7-a7a5-6453e032fa5e)



### Todo : 

To-do page will display list of todos for user. User can update the list when the task in the list is finished.



![todo](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/6bc5174a-ca72-42a6-95da-59ea8d1469e9)



### Youtube:

Youtube page will display list of 10 videos for searched content. User can watch any video from result it will display on another tab.


 
![youtube](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/c42b2031-a67a-4b67-9b93-2eaecae69ff8)




## Future Features:


-	Implement Ask me chatbot feature for user.
*	Allow user to add profile picture and more user specific information.
+	Display user progress using material design like charts.


## Challenges/Issues we ran into:


-	Merging the frontend part with the Django backend was messy
*	Due to lack of time i had to rush up my work (Time management was a huge problem)
+	Using Django defined user model for user registration I found quite confusing.
-	Deployment with Heroku was also quite challenging .

 

## How I Solve It:

-	Solved most of the CSS issues with Bootstrap.
*	Made a lot of error while developing and deploying, got over with some hit and trails.
+	Learning from previous experience specially hackathon helped a lot from model creation to deployment.



## Links :

| Link | ExpectedOutcome | Grade |
| --- | --- | ---|
| Logo | Navigates to the home page when clicked | Pass |
| Home | Navigates to the home page when clicked | Pass |
| Register | Navigates to a registration form when clicked  | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |
| Notes | Navigates to the notes page when clicked  | Pass |
| Homework | Navigates to the homework page when clicked  | Pass |
| Todo | Navigates to the todo page when clicked  | Pass |
| Youtube | Navigates to the youtube page when clicked | Pass |
| Askme | Navigates to the askme page when clicked | Fail |


## Testing :

| Feature | Expected Outcome | Grade |  Screenshot |
| --- | --- | --- | --- |
| Log in | Users can log in using a form after clicking "Log in"  | Pass |  ![login](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/f3d52e52-d04a-4a20-9f34-2e842f255964) |
| Log Out  | Users get logged out after clicking "Log out" | Pass |  ![logout](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/2ec68ff9-c9d1-45fe-a294-12c6d62f0bd2)  |
| Register | New users can access a registration form from the "Register" link |  Pass | ![register](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/16969cec-c3ef-4742-90ce-c1f269c3c208) |
| View Notes | Users can see available notes which have been added | Pass | ![notes](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/38f11476-af5c-4141-be2d-f13c99284aa2) |
| Add Note | Add a new note to the notes collection that will be available to read later | Pass |  ![notes](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/61eb518d-c995-4efa-821e-8300a099d539) |
| Edit homework | A user can edit the status of homework when its finished. It will update the is_finished value | Pass |  ![homework](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/03b4c3bb-e834-4257-9940-e6a1022b8516) |
| Delete task from todo | A user who added a todo OR an admin can delete a todo. It will then be deleted from the DB | Pass  |  ![todo](https://github.com/piya-ds/StudyPortal_Django/assets/86950823/528dde64-698f-48b1-a7ea-40e3f54301cc)|


## Tools and Technologies Used:

The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

- Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
+ GitHub used for secure online code storage.
- GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
+ Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
- ElephantSQL used as the Postgres database.
* Heroku used for hosting the deployed back-end site.

## Credit:

- Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by following along with django projects on YouTube. One of the vidoes I found especially helpful was : [https://www.youtube.com/watch?v=XvU0QXqDQ1Y&t=13269s](https://www.youtube.com/watch?v=XvU0QXqDQ1Y&t=13269s)
* tack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.
+ Font Awesome was used for icons and the fonts used were derived from Google Fonts.
- ERD & flowcharts were created using draw.io.

