# The Green Gastronomes
Welcome to The Green Gastronomes - a multiauthor vegan recipe blog! This website is designed with a user-friendly and visually appealing interface, ensuring an enhanced user experience. From exploring a diverse list of vegan recipes to viewing detailed preparation guides, the site caters to all culinary enthusiasts. Registered users can not only interact with content, leaving comments and likes, but also share their own delightful creations with the community.
## User Experience - UX
### Site Aims
The site aims to achieve the following:
- **Promote Vegan Lifestyle:** The primary goal of the website is to promote and encourage a vegan lifestyle by offering a wide variety of delicious and nutritious vegan recipes. By showcasing the diverse and exciting options available, the aim is to inspire people to adopt a plant-based diet.
- **Community Engagement:** The website aims to build a thriving community of food lovers, bloggers, and vegan enthusiasts. Through user interaction features like comments, likes, and user-submitted recipes, the platform fosters a sense of belonging and collaboration among our users.
- **User-Friendly Experience:** The goal has been to provide a seamless and enjoyable user experience through an intuitive and visually appealing interface. The website aims to be easy to navigate, making it effortless for users to explore recipes and engage with the content.
- **Quality Content Curation:** Ensuring the highest quality of content is crucial. The site administrators review and approve user-submitted recipes and comments to maintain the platform's integrity and present the community with valuable, reliable, and safe information.
- **Empower Users:** The website aims to empower users by allowing them to share their own recipes and have control over their content. A platform has been provided where users can showcase their culinary creativity and expertise, contributing to the growth of the vegan community.
### Agile Methodology
Agile Methodology has been used to plan this project. This was implemented through Github and the Project Board. Through the use of the board in the projects view in Github, the project was divided into the following three sections: 
- **To Do:** All the User stories were initially entered in the *To Do* column.
- **In Progress:** During the development phase, the stories were moved into the *In Progress* column.
- **Done:** In the final stage, they were moved into *Done* as the development on the respective stories was completed.
### Epics & User Stories
The following epics were created which were further developed into 16 specific User Stories.
#### Epic 1: Recipe Management
This epic focuses on all aspects related to managing recipes on the platform. It includes providing an admin interface for administrators to post recipes with necessary details and enabling users to submit their own recipes. The epic also covers the functionality for administrators to review and approve user-submitted recipes to ensure content quality and appropriateness. Additionally, users should be able to edit or delete their own recipes as needed.
##### Related User Stories
- As an administrator I can have an admin interface where I can post recipes with all the necessary details so that I can share them with users.
- As a user I can submit my own recipes so that I can share my recipes with others.
- As an administrator I can review and approve user-submitted recipes before they are published so that quality and appropriateness of the content can be ensured.
- As a user I can edit and delete my own recipes so that I can make modifications or remove them if needed.
#### Epic 2: User Authentication and Profile
The second epic deals with user authentication and profile management. It encompasses user registration, allowing users to create accounts to access the application's features. The epic also covers secure login and authentication mechanisms to protect user accounts. Furthermore, it involves providing users with the ability to manage their personal information through their profiles.
##### Related User Stories
- As a user I can register an account so that I can access the features of the application.
- As a user I can log in to my account securely so that I can access my personalized content and perform actions that require authentication.
- As a user I can have a user profile so that I can view and update my personal information.
#### Epic 3: User Interaction with Recipes
This epic revolves around user interaction with recipes on the platform. It includes enabling users to view a list of available recipes, detailed views for individual recipes, and the ability to leave comments on recipes. Additionally, users and administrators can view the number of likes and comments on each post, allowing them to gauge popularity and engagement.
##### Related User Stories
- As a user I can view a list of recipes so that I can explore the available options.
- As a user I can view the details of a specific recipe so that I can follow the recipe to prepare the dish.
- As a user I can leave comments on recipes so that I can share my feedback or ask questions.
- As a user / administrator I can view the number of likes on each post so that I can see which is the most popular or viral.
- As a user/ administrator I can view comments on an individual post so that I can read the conversation.
- As a user I can like a post so that I can interact with the content.
#### Epic 4: User Interface and User Experience
The fourth epic focuses on enhancing the user interface and overall user experience of the application. It includes designing a user-friendly and visually appealing interface with proper styling and responsive design.
##### Related User Stories
- As an administrator I can provide a user-friendly and visually appealing interface, with proper styling and responsive design so that user experience can be enhanced.
#### Epic 5: Comment Moderation for a Safe User Environment
This epic centers around enabling administrators to review and manage comments for the purpose of filtering out objectionable content and maintaining a secure user environment. It includes the implementation of an efficient comment approval process that empowers administrators to approve or disapprove comments. By doing so, the platform ensures that objectionable content is effectively filtered out, creating a safe and welcoming space for users.
##### Related User Stories
- As an administrator I can approve or disapprove comments so that I can filter out objectionable comments.
#### Epic 6: Drafts and Unpublished Content
The final epic deals with the management of drafts and unpublished content. It includes providing administrators with the ability to create draft posts and save them for completion at a later time. This functionality can be useful for preparing content without immediately publishing it to the public.
##### Related User Stories
- As an administrator I can create draft posts so that I can finish writing the content later.
## Design
## Features
## Technologies Used
## Testing
## Bugs
## Deployment
##### 1. Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`(note: this must be either removed or set to 0 for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.
##### 2. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.
##### 3. Setting up settings.py
* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku, click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: 
```ALLOWED_HOSTS = ['<Heroku_app_name>.herokuapp.com', 'localhost']```
* Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Commit and push the code to the GitHub Repository.
##### 4. Heroku Deployment: 
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.
##### 5. Final Deployment
In the IDE:
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.
### Cloning
To create a clone of the repository within your local development environment which makes it easier to fix merge conflicts, add or remove files, and push larger commits, follow these steps:
- Log in to GitHub, access the specific GitHub Repository [The Green Gastronomes](https://github.com/FarehaSi/The-Green-Gastronomes)
- Above the file list on the repository page locate and click the 'Code' button (beside the 'Add file' button)
- Copy the provided link depending on your desired option for either 'HTTPS', 'SSH key' or 'GitHub CLI.
- Open Git Bash and change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the specific URL you copied in Step 3.
### Forking
Forking enables a third party to create a copy of the repository in order to view and/or make changes without affecting the original. To Fork this repositary:
- Navigate to GitHub project repositary [The Green Gastronomes](https://github.com/FarehaSi/The-Green-Gastronomes)
- In the right hand corner see the "Fork" section and click on it.
- Select an owner for the forked repository.
- Click Create fork button.
## Credits
#### Code
- The Code Institute <a href="https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/" target="_blank">I Think Therefore I Blog</a> walkthrough project assisted and guided in the setup and basic structure of this project
- <a href="https://docs.djangoproject.com/en/3.2/" target="_blank">Django Documentaion</a> was used to assist in multiple queries
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a> has been instrumental in helping resolve bugs
- The Code Institute <a href="https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/" target="_blank">Hello Django</a> helped with writing tests for the python code
#### Media
- The fonts were sourced using <a href="https://fonts.google.com/" target="_blank">Google Fonts</a>
- All icons were taken from <a href="https://www.fontawesome.com/" target="_blank">Font Awesome</a>
- All images have been obtained from <a href="https://www.pexels.com/" target="_blank">Pexels</a>
## Acknowledgement
I am grateful to my mentor Akshat Garg for his guidance and support.
