# AstroShare Blog

"Discover the cosmos with AstroShare, the ultimate online community for astronomy enthusiasts! Our blog is a hub where you can sign up, collaborate, and interact with fellow stargazers. Share stunning photos, insightful articles, and engaging discussions about all things astronomical. Whether you're a novice star-watcher or a seasoned astronomer, AstroShare makes it easy to connect, learn, and grow. Join us today and be a part of a vibrant community that’s exploring the universe, one post at a time!"

A live version of the project can be accessed here: 

(responsiveness image)


# Table Of Contents
  - [AstroShare Blog](#astroshare-blog)
  
  - User Experience Design
    - [User Experience (UX)](#ux)    
    - [User Demographic](#user-demographic-table-of-contents)
    - [User Stories & Epics](#user-stories-and-epics)
    - [Flowchart](#flowchart)
    - [Entity Relationship Diagram](#entity-relationship-diagram)

    - [Agile User Stories Epics Milestones](#agile)
    - Wireframes
    - Images
    - Logo
    - Favicon
    - Colour scheme
    - Fonts
    - [Database](#database)
    - Features
    - Bugs
    - Testing
    - Deployment
    - Credits

  # UX  


## User Experience

A user story is an explanation of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories were created with the help of GitHub issues. Each user story contains:
* Title - Short description of the user story. 
* Description - As a **role** i can **capability** so that **received benefit**.
* Acceptance criteria - A set of conditions that a feature must meet to be accepted by the user. 
* Unit tasks - A break down of each task needed to complete user story. 
* A MoSCoW label - To prioritise tasks. 
* Assignee -  Who the user store is assigned too. 
* Milestone - Which epic this user store is associated with.
<br/>


I used an Agile methodology approach to plan this project. This was implemented through the GitHub Project board with milestones, epics, user stories and tasks.
Each user story was classified with a label according to MoSCoW prioritization.<br>
The Kanban board can be seen [here](https://github.com/users/Harmonica-Men/projects/10).

### Milestones

The project was divided into three milestones, each containing the corresponding epics and user stories:<br>
1. [Setting Up The Project @ Bear minimums](https://github.com/Harmonica-Men/AstroShare-Blog/milestone/1)
- Task: Set up the project repository and initialize Django project.
  - Create a new repository on GitHub, GitLab
  - Set up the virtual environment and install Django.
  - Initialize a new Django project and create a base application.
  - Configure settings for the project  static files, static and README.md
  - Deploy early to a hosting platform Heroku

<details>
<summary></summary>
<br>

</details>

2. [Basic Blog Functionality]()
  - Task: Implement basic blog functionality including models, views, and templates.
    - Define the models for blog posts (e.g., Post, Category, Tag).
    - Create views to list all posts, view individual posts, and manage categories/tags.
    - Design templates for the blog homepage, individual post pages, and category/tag pages.
    - Implement URL routing for the blog.

3. User Authentication
  - Task: Add user authentication to allow for author logins and secure post management.
    - Set up Django’s built-in authentication system.
    - Create registration, login, and logout views and templates.
    - Implement user-specific actions, such as creating, editing, and deleting blog posts.

4. Admin Interface
  - Task: Set up the Django admin interface for managing blog content.
    - Register blog models with the Django admin.
    - Customize the admin interface for better usability (e.g., list displays, search fields).

5. Commenting System
  - Task: Implement a commenting system for blog posts.
    - Create models for comments linked to blog posts.
    - Create views and templates for adding and displaying comments.
    - Implement moderation features for comments (e.g., approval workflow).

6. Styling and Frontend
  - Task: Apply CSS and JavaScript to enhance the look and feel of the blog.
    - Use a CSS framework like Bootstrap for basic styling.
    - Customize templates to ensure a consistent and responsive design.
    - Add JavaScript for interactive elements (e.g., comment submission, post likes).

7. Search and Filtering
  - Task: Implement search and filtering capabilities.
    - Add a search bar to allow users to search for posts.
    - Implement filtering by categories, tags, and publication dates.
    - Optimize search and filter queries for performance.

8. SEO and Performance Optimization
  - Task: Optimize the blog for search engines and improve performance.
    - Implement SEO best practices (e.g., meta tags, sitemap, robots.txt).
    - Optimize images and static files for faster loading.
    - Use caching to improve page load times.

9. Testing and Deployment
  - Task: Write tests and deploy the project.
    - Write unit tests and integration tests for critical functionality.
    - Set up continuous integration (CI) to automate - and/or manual testing




## User stories 

A user story is an explanation of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories were created with the help of GitHub issues. Each user story contains:
* Title - Short description of the user story. 
* Description - As a **role** i can **capability** so that **received benefit**.
* Acceptance criteria - A set of conditions that a feature must meet to be accepted by the user. 
* Unit tasks - A break down of each task needed to complete user story. 
* A MoSCoW label - To prioritise tasks. 
* Assignee -  Who the user store is assigned too. 
* Milestone - Which epic this user store is associated with.

Below is an example of how the user stories where structured for this project.

<br/>






  #### The UX Table of Contents
  1. [Welcome and Introduction](#1-welcome-and-introduction)
  2. [Sign-Up Process](#2-sign-up-process)
  3. [Navigation and Exploration](#3-navigation-and-exploration)
  4. [Creating and Sharing Content](#4-creating-and-sharing-content)
  5. [Interaction and Collaboration](#5-interaction-and-collaboration)
  6. [Profile and Community Building](#6-profile-and-community-building)
  7. [Ease of Use and Accessibility](#7-ease-of-use-and-accessibility)
  8. [Continuous Engagement](#8-continuous-engagement)
  9. [Conclusion](#9-conclusion)
  ## 1. Welcome and Introduction
  **User opens the blog website:**

  - **Landing Page:**
    - A visually appealing landing page with a background image of the night sky or a space theme.
    - A welcoming headline: "Welcome to AstroShare - Your Space for Astronomical Insights and Community".
    - Brief introduction: "Join our community of astronomy enthusiasts, share your insights, post photos, and engage in enlightening discussions."

  - **Call to Action:**
    - Prominent "Sign Up" and "Log In" buttons.
    - Short introductory video or animation showcasing the features of the blog.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)


  ## 2. Sign-Up Process
  **User clicks on "Sign Up":**

  - **Sign-Up Form:**
    - Simple form requesting essential information: Username, Email, Password, and Confirm Password.
    - Option to sign up using social media accounts (Google, Facebook).

  - **Profile Setup:**
    - After signing up, the user is prompted to complete their profile:
      - Upload a profile picture.
      - Write a short bio.
      - Add links to personal websites or social media profiles (optional).

  [Back to UX Table of Contents](#the-ux-table-of-contents)
  
  [Back to Top](#astroshare-blog)


  ## 3. Navigation and Exploration
  **User completes sign-up and is directed to the main dashboard:**

  - **Main Dashboard:**
    - Personalized greeting: "Hello, [Username]! Welcome to AstroShare."
    - Easy-to-navigate menu with options: Home, Explore, Create Post, My Profile, Notifications, Settings, and Log Out.

  - **Home Feed:**
    - A feed of the latest posts from users, featuring photos, articles, and discussions about various astronomical topics.
    - Each post includes the author’s profile picture, name, post title, content preview, and interaction buttons (Like, Comment, Share).

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 4. Creating and Sharing Content
  **User clicks on "Create Post":**

  - **Create Post Page:**
    - Simple and intuitive editor for creating posts:
      - Title field.
      - Content field with rich text formatting options.
      - Option to add photos (drag and drop or upload from device).
      - Tags field for categorizing the post (e.g., Planets, Stars, Telescopes, Space Missions).
    - "Post" button to publish the content.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 5. Interaction and Collaboration
  **User interacts with a post:**

  - **Commenting:**
    - Users can leave comments on posts.
    - Comment section with a clear text field, and an "Add Comment" button.
    - Ability to reply to comments and like/dislike comments.

  - **Collaborative Features:**
    - Option to invite other users to collaborate on a post.
    - Real-time collaboration with a shared editor for multiple contributors.

  - **Notifications:**
    - Users receive notifications for new comments, likes, and collaboration invites.
    - Notification bell icon in the menu bar with a dropdown list of recent notifications.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 6. Profile and Community Building
  **User explores their profile and connects with others:**

  - **User Profile:**
    - Profile page displaying user information: profile picture, bio, posts, and activity.
    - Edit Profile button for updating information and settings.

  - **Community Engagement:**
    - Explore page with user search functionality.
    - Follow other users to receive updates on their posts and activities.
    - Direct messaging feature for private conversations.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 7. Ease of Use and Accessibility
  **User enjoys a seamless experience:**

  - **Responsive Design:**
    - Blog is fully responsive and works seamlessly on desktop, tablet, and mobile devices.
    - Fast loading times and smooth transitions between pages.

  - **Accessibility:**
    - High contrast mode and text resizing options for visually impaired users.
    - Keyboard navigable interface and screen reader compatibility.

  - **Help and Support:**
    - Easily accessible help section with FAQs and tutorials.
    - Contact support option for direct assistance.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 8. Continuous Engagement
  **User stays engaged and returns to the blog:**

  - **Content Recommendations:**
    - Personalized content recommendations based on user’s interests and activity.
    - Regular email updates with highlights from the blog and upcoming astronomical events.

  - **Events and Challenges:**
    - Community events such as virtual star-gazing sessions, photo contests, and Q&A sessions with astronomy experts.
    - Interactive challenges and quizzes to keep users engaged and learning.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 9. Conclusion
  AstroShare offers a user-friendly, engaging, and collaborative platform for astronomy enthusiasts to share knowledge, interact with the community, and enjoy a seamless and enriching experience.

  [Back to UX Table of Contents](#the-ux-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## User Demographic Table of Contents
  1. [Age Group](#1-age-group)
  2. [Interest](#2-interest)
  3. [Education Level](#3-education-level)
  4. [Technological Proficiency](#4-technological-proficiency)
  5. [Geographic Location](#5-geographic-location)
  6. [Behavioral Traits](#6-behavioral-traits)
  7. [Accessibility Needs](#7-accessibility-needs)
  
  ## 1. Age Group
  - Primarily adults and young adults (18-45 years old) who have a keen interest in astronomy and space exploration.
  - This demographic is likely to be tech-savvy and comfortable using digital platforms for both learning and social interaction.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 2. Interest
  - Individuals who are passionate about astronomy, including amateur astronomers, space enthusiasts, students studying astronomy or related sciences, and professionals working in the field.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 3. Education Level
  - Varied, but likely to include individuals with at least a high school education and a strong interest in science, particularly astronomy and space sciences.
  - Some users may have advanced degrees or be pursuing careers in astronomy or related fields.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 4. Technological Proficiency
  - Users who are comfortable with technology, including social media platforms, online communities, and content creation tools.
  - They are likely to engage actively in online discussions, share content, and collaborate with others on the platform.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 5. Geographic Location
  - The platform may attract users globally, given the universal interest in astronomy.
  - However, regions with active amateur astronomy communities, space research institutes, or strong educational programs in astronomy may have a higher concentration of users.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 6. Behavioral Traits
  - Users who enjoy sharing knowledge, participating in discussions, and engaging with multimedia content such as photos and videos related to astronomy.
  - They may also value community building, collaborative projects, and staying updated with the latest astronomical discoveries and events.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## 7. Accessibility Needs
  - While primarily targeting users comfortable with digital platforms, efforts should be made to ensure accessibility features such as high contrast mode, text resizing, and screen reader compatibility to accommodate users with visual impairments or disabilities.

  [Back to User Demographic Table of Contents](#user-demographic-table-of-contents)

  [Back to Top](#astroshare-blog)

## User Stories and Epics
Astro Blog Share is for those who are interested in Astronomical subjects and like to share there toughs in a deticated blog. The blog can be used as a discussion platform for anybody who have a special affliation whit astronomy.
 <br>

List of Epics: <br>
- [EPIC 1: Repository and agile tool]()
- [EPIC 2: Basic Website and Database Structure]()
- [EPIC 3: User authentication]()
- [EPIC 4: Blog Post Management]()
- [EPIC 5: Testing]()
- [EPIC 6: Validation]()

User Stories with their id:  <br>
- As a new website user, I am able to identify the website's goal so that I can decide whether to continue or leave. [#9]()
- As a new user, I can register an account so that I can create and manage wish lists or items of other wish lists. [#12](ht)
- As a registered user, I want to log in to my account so that I can create, read, update and delete my wish list(s) [#13]()
- As a registered user, I want to manage my profile so that I can update my account. [#13]()
- As a registered user, I want to edit my wishlist so that I can update its details. [#16]()
- As a registered user, I want to be able to delete a wishlist so that I can remove outdated or unnecessary lists. [#17]()
- As a registered user, I want to edit items in my wishlist so that I can update their details.[#19]()
- As a registered user, I want to be able to delete items from my wishlist so that I can remove unwanted items.[#20]()
- As a registered user, I want to reserve an item of a wishlist, so that no other user will purchase this. [#23]()
- As a registered user, I want to be able to collaborate on a wishlist with others so that we can collectively manage it. [#24]()
- As a logged-in user, I want to update my profile information so that my account details are current. [#14]()
- As a frequent website user, I can easily login to my account so that I have access to my wish lists and items I want to purchase. [#9]()
- As a user of the website I want to create a wish list for a specific occasion so that I can organize my desired items. [#15]()
- As a user, I want to add items to my wishlist so that I can keep track of things I want. [#18]()
- As a user, I want to share my wishlist with others so that they can see my wishlist and know what I want to have. [#22]()
<br>

- As a developer, I want to define a database structure so that it matches the objectives of the project. [#10])
- As a developer I want to set up and configure a database so that I can store and manage the application data securely and efficiently. [#11]()
- As a developer, I need to verify that all html files pass the W3C validation so that the code is executed correctly. [#25](https://github.com/Harmonica_men/wishlist/issues/25)
- As a developer, I need to verify that my css files pass the W3C validation so that the code is executed correctly. [#26](https://github.com/Harmonica_men/wishlist/issues/26)
- As a developer, I need to verify that my JavaScript files pass the jshint validation so that the code is executed correctly. [#27](https://github.com/Harmonica_men/wishlist/issues/27)
- As a developer, I need to verify that my python files pass the pep8 validation so that the code is executed correctly. [#28](https://github.com/Harmonica_men/wishlist/issues/28)
- As a developer, I want to implement python test procedures so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#29](https://github.com/Harmonica_men/wishlist/issues/29)
- As a developer, I want to implement JavaScript test procedures so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#30](https://github.com/Harmonica_men/wishlist/issues/30)
- As a developer, I want to implement manual test cases so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#31](https://github.com/Harmonica_men/wishlist/issues/31)
<br>

- As an admin, I want to access the site's administrative features so that I have access to the admin panel. [#8](https://github.com/Harmonica_men/wishlist/issues/8)



## User Stories Table of Contents
  1. [Welcome and Introduction](#welcome-and-introduction)
  2. [Sign-Up Process](#sign-up-process)
  3. [Navigation and Exploration](#navigation-and-exploration)
  4. [Creating and Sharing Content](#creating-and-sharing-content)
  5. [Interaction and Collaboration](#interaction-and-collaboration)
  6. [Profile and Community Building](#profile-and-community-building)
  7. [Ease of Use and Accessibility](#ease-of-use-and-accessibility)
  8. [Continuous Engagement](#continuous-engagement)
  9. [Epics]()

  ## Welcome and Introduction
  **As a user:**
  - I want to see a visually appealing landing page with a space theme and a welcoming headline.
  - I want to read a brief introduction about the community and its features.
  - I want to have prominent "Sign Up" and "Log In" buttons to easily join or access the blog.
  - I want to watch a short introductory video or animation showcasing the blog's features.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Sign-Up Process
  **As a user:**
  - I want to click on "Sign Up" and fill out a simple form with my Username, Email, Password, and Confirm Password.
  - I want to have the option to sign up using my social media accounts (Google, Facebook).
  - I want to be prompted to complete my profile by uploading a profile picture, writing a short bio, and optionally adding links to personal websites or social media profiles after signing up.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Navigation and Exploration
  **As a user:**
  - I want to be directed to the main dashboard with a personalized greeting after completing the sign-up.
  - I want an easy-to-navigate menu with options like Home, Explore, Create Post, My Profile, Notifications, Settings, and Log Out.
  - I want to see a home feed with the latest posts from users, including photos, articles, and discussions about various astronomical topics.
  - I want each post to include the author’s profile picture, name, post title, content preview, and interaction buttons (Like, Comment, Share).

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)


  # Database
    PostgreSQL uitleg psycopg2  (pip install) 2.9.6
    Cloudinary werking generate new API-key ... (pip install)


  ## Creating and Sharing Content
  **As a user:**
  - I want to click on "Create Post" and access a simple and intuitive editor.
  - I want to have a title field, content field with rich text formatting options, and the ability to add photos either by dragging and dropping or uploading from my device.
  - I want to add tags to categorize my post and a "Post" button to publish my content.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Flowchart

  This flowchart was created to determine the flow of the website. It shows which pages are available to the user. It takes into account if the user is logged in to the website or not.

  ![Flow Chart](static/images/readme-images/006_flowchart.jpg)

  [Back to Top](#astroshare-blog)

  ## Entity Relationship Diagram
  
  The database design for this project includes Four tables. The first table is a review table. This table houses all the data associated with making a review on the site. There is a customer table, which houses the details of the customer and this is linked to a booking table via a foreign key relationship. The booking table contains the information needed in order for users to make a booking. The last table present is the user table. This table has the information necessary for users to have an account on the website and has a foreign key relationship with the customer table.
  ![ERD](static/images/readme-images/005_ERD_diagram.jpg)

  [Back to Top](#astroshare-blog)

  ## Interaction and Collaboration
  **As a user:**
  - I want to leave comments on posts with a clear text field and an "Add Comment" button.
  - I want to be able to reply to comments and like or dislike them.
  - I want to invite other users to collaborate on a post.
  - I want real-time collaboration with a shared editor for multiple contributors.
  - I want to receive notifications for new comments, likes, and collaboration invites, with a notification bell icon in the menu bar showing a dropdown list of recent notifications.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Profile and Community Building
  **As a user:**
  - I want to explore my profile page that displays my information, including my profile picture, bio, posts, and activity.
  - I want an "Edit Profile" button to update my information and settings.
  - I want to use the Explore page to search for other users.
  - I want to follow other users to receive updates on their posts and activities.
  - I want to use a direct messaging feature for private conversations.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Ease of Use and Accessibility
  **As a user:**
  - I want the blog to be fully responsive and work seamlessly on desktop, tablet, and mobile devices.
  - I want fast loading times and smooth transitions between pages.
  - I want high contrast mode and text resizing options for better accessibility if I am visually impaired.
  - I want a keyboard navigable interface and screen reader compatibility.
  - I want an easily accessible help section with FAQs and tutorials, along with a contact support option for direct assistance.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

  ## Continuous Engagement
  **As a user:**
  - I want personalized content recommendations based on my interests and activity.
  - I want regular email updates with highlights from the blog and information about upcoming astronomical events.
  - I want to participate in community events such as virtual star-gazing sessions, photo contests, and Q&A sessions with astronomy experts.
  - I want to engage in interactive challenges and quizzes to keep learning and stay engaged with the blog.

  [Back to User Stories Table of Contents](#user-stories-table-of-contents)

  [Back to Top](#astroshare-blog)

## Deployment

### Heroku Deployment
This site was deployed to and is currently [hosted on the Heroku platform](https://mysimpleblog-1c6e9d449421.herokuapp.com/). The steps for deploying to Heroku, using PostgreSQL as the database host, are as follows:

#### Create a new PostgreSQL Code Institute database.

From codeinstitute every student can maintain up to eight databases to run there projects. Here is a step by step guide to install PostgreSQL from Code Institute to the cloud!

  1. Navigate to [PostgreSQL from Code Institute](https://dbs.ci-dbs.net//) and input with your LMS account
  ![PostgreSQL database creation step1](static/images/readme-images/001.png)

  2. After you filled in your LMS account the PostgresSQL database manager will automatically generate a new database for you.
  ![PostgreSQL database creation step2](static/images/readme-images/002.png)

  3. You now have a brand new PostgreSQL Code Institute database
  The link to this database and how to manage all your other databases will be sent to my email. 
  ![PostgreSQL database creation step3](static/images/readme-images/003.png)
  4. **Note:** These databases are limited in time and have a life time of operation of 18 months after the date of creation.
  ![PostgreSQL database creation step4](static/images/readme-images/004.png)
  5. infoknop
  6. copy/paste url-link
  7. paste this in  your env.py & heroku varibles.
 
#### Deploy the project 
  In the previous topic, I have created a PostgreSQL database. In this topic, you are challenged to deploy your project to Heroku.
  First you go to the Heroku website and login whit your credentials. 

  0. Set up your Heroku account 
  ...



  
  Part 1 - Create the Heroku app:
  1. Navigate to your Heroku dashboard and create a new app with a unique name in a GDPR region Europe 
  Note: No Django static file collection will be required during the build.
  2. In your new app’s settings tab, ensure the **Config Vars** click on **Reveal Config Vars** button to define new variables in the inputs fields: 
    
    "DATABASE_URL", "<your-database-URL>"

    "SECRET_KEY", "<secret-key>"

    "CLOUDINARY_URL", "<cloudinary-URL>"


  Part 2 - Update your code for deployment:

  1. Use **pip3** to install ```gunicorn~=20.1``` and **freeze** it to the **requirements.txt** file.
  The commands at the terminal are:

    pip3 install gunicorn~=20.1 
    pip3 freeze --local > requirements.txt

  2. In the **Procfile**, add a command using **gunicorn** and **myblog wsgi** file to start the webserver.

  3. In the **myblog/settings.py** file, set the **DEBUG** constant to False and append the **'.herokuapp.com'** hostname to the **ALLOWED_HOSTS** list. 
  
    web: gunicorn myblog.wsgi

  **Note:** There is a space after the colon.
  **Note:** The Procfile has no file extension.

  **Top tip!** It's a good habit to always set **DEBUG** to **False** before any deployment. Once you have completed deployment, you can set it back to True locally to continue development.
  **Double check**
    Have you changed DEBUG to False and added , **'.herokuapp.com'** to the **ALLOWED_HOSTS**?
      
      DEBUG = False
      ,'.herokuapp.com'
    
  4. Git add, commit and push the code to your GitHub repo.

    git add .
    git commit -m "readies code for deploy"
    git push origin main


Part 3 - Deploy to Heroku:

  1. In your new app’s **Deploy** tab, search for your GitHub repo and connect it to the Heroku app. Manually deploy the **main** branch of this GitHub repo is also the prefered method.
  **Note:** Start typing your project repo name into the search box and click on the GitHub repo you want to deploy from.
  After manually deploying the main branch, you can view the build output in the application’s **Activity** tab in the dashboard.

  In your new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on.

  2. Click **Open app** buttin to see your deployed app. 
  If everythings goes well you on the frontpage of myblog.

  **Note:** The build must be complete before you can open the app.

import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>")
os.environ.setdefault(
    "SECRET_KEY", "(j(j_+@%s$a955-5gw=m@b-%#$slmv$0aixrck&odnq*h+ig@0")
os.environ.setdefault(
    "CLOUDINARY_URL", "<cloudinary-URL>")






## Credits

### w3 schools

> Used to reference Python Structure

### Stack Overflow

> Used to reference different syntax issues from existing older boards. Also used to query clear function issues when I ran into them as referenced in the bug section.

## Acknowledgements

### Daisy McGirr

- My Mentor with Code Institute who has provided me with excellent feedback and guidance through this project.


Bootstrap


describe  Frontpage & Homepage

3 way proces , urls , views , html

widgets in forms

LOGIN_RREDIRECT_URL & LOGOUT


sluggyfy could have (maybe)