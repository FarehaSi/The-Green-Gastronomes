# The Green Gastronomes
Welcome to [The Green Gastronomes](https://green-gastronomes-1952abf961a7.herokuapp.com/) - a multiauthor vegan recipe blog! This website is designed with a user-friendly and visually appealing interface, ensuring an enhanced user experience. From exploring a diverse list of vegan recipes to viewing detailed preparation guides, the site caters to all culinary enthusiasts. Registered users can not only interact with content, leaving comments and likes, but also share their own delightful creations with the community.
![Mockup](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/fcabb011-0845-4864-b9a1-336f54384a17)
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
### Tasks
Building upon the insights gained in the preceding discovery phase, the tasks of the development phase were executed in the following order:
#### Before Project Inception
- Designing an Entity Releationship Diagaram and Wireframing
- Creating a Repository in GitHub
- Creating Project, Epics, User Stories and preparing the Project Board
#### Creation of Project in GitPod
- Creating the django project
- Deploying app to Heroku
- Creating Database Models
- Setting up models.py file in the 'blog' directory
- Building the Admin site
- Installing Allauth for sign in, sign up and sign out templates
- Installing crispy-forms to add styles to Django account templates
- Creating base.html - Navbar and Footer content, which extended to all the other template files
- Adding hero image & content
- Adding responsiveness to navigation and footer
- Creating index.html, view and styling
- Setting up templates for signup, login and logout 
- Setting up other template files with views.py and urls.py
- Allowing user's to like and comment
- recipe_detail.html (to view full posts)
- user_profile.html (for user's to manage their personal information and blog posts)
- add_recipe.html (to allow user's to share their own creations)
- edit_recipe.html (to allow user's to update their posts)
- delete_recipe.html (to allow user's to delete their posts)
- Writing scripts for automated testing
- Manual Testing was carried throughout the process
- Creating a custom 404 Error page
- Validation checks were carried for all the html files, css file and python code
- Final Deployment steps
## Design - UI
The design philosophy embodies the essence of a vibrant and conscious lifestyle. The blog is meticulously crafted to reflect the principles of plant-based living, sustainability, and visual harmony. Here's an overview of the design elements that come together to create a cohesive and captivating theme:
### Typography
#### Logo & Headings (Font: Lobster)
The curvy and playful lines of the Lobster font evoke a sense of warmth and approachability making the page inviting and enjoyable for everyone.
#### Body Text (Font: Quicksand)
Quicksand's clean and modern appearance aligns with focus on clarity and readability, allowing readers to effortlessly explore the recipes and content.
### Color Palette
#### Background (White)
A clean white background serves as a canvas, spotlighting our content and enhancing the overall readability of the blog.
#### Font Color (Black)
The black font color exudes elegance and timelessness, emphasizing the reliability.
#### Links (Green)
The vibrant green hue of the links not only adds a pop of color but also signifies the flourishing nature of plant-based living.
### Logo & Imagery
The website's logo, featuring the Lobster font, captures the dynamic energy of our blog, radiating a sense of enthusiasm for plant-based cooking.
While the imagery showcases vibrant vegetables, and delectable vegan dishes, resonating with the freshness and abundance of plant-based ingredients.
### Layout & Composition
Thoughtfully structured layouts guide the readers seamlessly through recipes, with ease of navigation. Whitespace is generously used to ensure a clutter-free experience, emphasizing the purity and simplicity of vegan cuisine.
### Visual Harmony & Theme
The combination of Lobster and Quicksand fonts creates a harmonious balance between playfulness and professionalism, mirroring the holistic approach of a vegan lifestyle. The color palette, with its calming white backdrop, grounding black text, and invigorating green accents, establishes a soothing yet invigorating visual rhythm. Collectively, these design choices synergize to encapsulate the essence of Vegan Vibes: a platform that promotes the joy of plant-based cooking, environmental consciousness, and overall well-being.
In essence, the design of The Green Gastronomes is a deliberate orchestration of fonts, colors, imagery, and layout, all meticulously chosen to mirror the core values of veganism and create an immersive experience that resonates with the readers.
## Features
### Home Page
On the landing page, the user is introduced to the vibrant atmosphere of the website – colorful, hip, and inviting. At the top, there's a header that features the logo and a navigation bar. Right below is the hero image accompanied by text that introduces the user to the purpose and content of the website.
<br>
<br>
![Home](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/436d4081-7c91-4342-819d-54b7bd6131e5)
<br>
<br>
As the user scrolls down, they encounter a list of blog posts/recipes accompanied by enticing pictures and excerpts designed to encourage users to click on them and delve deeper into the content.
<br>
<br>
![RecipeList](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/42f525d0-a07b-4f3e-9e6f-25d6d8516ca8)
![RecipeList2](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/7a684dd5-d5ec-4bed-b220-059dfef0bd67)
<br>
#### Navbar
The Navbar changes when th user logs in.
<br>
<br>
![NavbarLogin](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/6741cb84-ac56-4694-abba-e34439556e6f)
<br>
<br>
It collapses into a hamburger on smaller devices.
<br>
<br>
![NavbarSmall](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/bfd2f9bf-6715-4c93-8f7d-613c84c34a6a)
#### Footer
At the bottom of the page, user's will find the footer containing links to the blog's social media platforms.
<br>
<br>
![Footer](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/dd93c3f5-fa2b-4208-9aa6-40bf8b82633d)
### Registeration
Here, users create an account with the site and are able to post their own recipes. By registering with the site, users can also interact with others by leaving comments and liking posts.
<br>
<br>
![Screenshot (175)](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/4dcc0982-8207-4030-a012-f12ad6556960)
<br>
<br>
The login and logout pages carry a similar layout.
### Recipe Detail Page
When a user clicks on their chosen recipe from the home page, they are directed to the recipe detail page.
<br>
<br>
![RecipeDetail](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/6013c541-1411-438c-a6a5-20cabeb0abf5)
<br>
<br>
Beneath the post is the opportunity for users to interact with others by commenting or liking the post. A recipe can be liked by simply clicking on the heart icon. While a comment can be posted in the <i>'Leave a comment'</i> section.
<br>
<br>
![RecipeDetail2](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/6881af29-09d7-4518-a59a-37a7a451f575)
<br>
<br>
#### User Profile Page
This page displays the individual users' credentials. Users can choose to upload their profile picture. It also serves as a platform for users to manage their recipes.
<br>
<br>
![UserProfile](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/9d2d5d94-aeea-42bf-a181-be659772b0c8)
<br>
<br>
##### Add Recipe
In the last section of the user profile page, users can add, edit and/or delete their posts. When clicked on the relevant section, a page will be opened that would allow them to carry out their respctive task.
<br>
<br>
![AddRecipe](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/1978f60e-2de1-45d5-ac96-44814a7849a9)
<br>
<br>
The Edit Recipe carries a similar layout.
##### Delete Recipe
Users are asked to confirm before they want to delete a post. This minimizes the risk of accidental loss.
<br>
<br>
![Delete Recipe](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/bc969973-19f9-43c7-bf17-650fbfe36ef5)
<br>
<br>
## Technologies Used
### Languages Used
* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt
### Django Packages
* [Gunicorn](https://gunicorn.org/)- As the server for Heroku.
* [Cloudinary](https://cloudinary.com/)- Was used to host the static files and media for the site.
* [Dj_database_url](https://pypi.org/project/dj-database-url/)- To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Summernote](https://summernote.org/)- As a text editor.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.
### Frameworks - Libraries - Programs Used
* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [Heroku](https://id.heroku.com)- Used to deploy the live project.
* [PostgreSQL](https://www.postgresql.org/)- Database used through heroku.
* [Balsamiq](https://balsamiq.com/)- To build the wireframes for the project.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.
* [Google Fonts:](https://fonts.google.com/) used for the Roboto font
* [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
## Testing
Both manual and automated testing have been performed to maintain site integrity.
### Manual Testing
#### Validator Testing
The following validation tools have been used to test HTML, CSS, PYTHON codes. 
##### Python via [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)
Forms.py: ![forms py](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/95e8a8c6-527a-4a83-9d72-0c171064e0b0)
Models.py: ![models py](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/cfe2c457-d5eb-47b4-8402-2a784793eba0)
Signals.py: ![signals py](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/edf8c9b9-d975-464d-8eed-2d79fee96d6a)
URLs.py: ![urls py](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/c52097f7-8db5-4ce0-9234-5d2ef9063078)
Views.py: ![views py (2)](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/3cb89a93-9ea9-4949-93e2-9faa7d8e5ef2)
##### CSS using [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
Style.css: ![style css](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/729dc581-e8ea-415c-bcd5-928fd615be03)
##### HTML using [W3C HTML validator](https://validator.w3.org/)
![HomePage](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/f51a070a-294f-4647-8bb6-2d9b86d26e42)
<br>
<br>
Users can register with the website: 
![userRegisteration](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/cd447bbe-f830-4d2d-be31-f733b662fecd)
<br>
<br>
Their user profile is created:
![UserProfile](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/b9de2cfd-195c-45a5-8f8a-a0ec7b7afff9)
<br>
<br>
They can manage their recipes. Add new ones and update or delete old ones. When they do any of that, success messages are display on the screen.
![addRecioe](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/e237f9ac-a018-4001-9c9e-53bc599b08e1)
![deleteRecipe](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/f5d9c585-e685-4be2-bebe-2c56b36be44f)
![recipeDeleted](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/add501db-2b20-49aa-856b-f94b25a79804)
<br>
<br>
Users can also interact with recipes posted by others.
![comment](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/7985e86d-6dcb-422c-8d74-8d4cf2417a4a)
![comment2](https://github.com/FarehaSi/The-Green-Gastronomes/assets/116716786/0e44c4a7-9146-4d71-ad90-003db18e321a)
## Bugs
#### Solved Bugs
- There was an issue where a User Profile wasn't being created upon User registration on the website, contrary to the expected behavior. This problem was resolved by introducing a 'signals.py' file into the directory that used the 'post_save' signal for the 'User' model to create a 'UserProfile' and the signals were then imported to the apps.py file.
- The User Profile page was displaying all of django's default success messages including login and logout instead of solely displaying the ones specified in the views.py file. This was resolved by adding an extra_tag with each message that allowed for only those specific messages to be displayed while maintaining the styling associated with traditional Django success messages.
- On the Recipe Detail page, when a User attempted to post a comment, an error was appearing instead of the expected behavior, which was the page refreshing with a success message presented on the screen. The resolution for this issue involved implementation of a 'method_decorator(login_required)' on the comment post method within the RecipeDetail view.
- Automated tests were not working because of the Postgres database. This was resolved by temporarily establishing a connection with the local 'db.sqlite3' database while conducting unit tests.
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
- <a href="https://stackoverflow.com/" target="_blank">Stack Overflow</a> has been instrumental in guiding through differnet parts of code and helping resolve bugs
- The Code Institute <a href="https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/" target="_blank">Hello Django</a> helped with writing tests for the python code
#### Media
- The fonts were sourced using <a href="https://fonts.google.com/" target="_blank">Google Fonts</a>
- All icons were taken from <a href="https://www.fontawesome.com/" target="_blank">Font Awesome</a>
- All images have been obtained from <a href="https://www.pexels.com/" target="_blank">Pexels</a>
## Acknowledgement
I am grateful to my mentor Akshat Garg for his guidance and support.
