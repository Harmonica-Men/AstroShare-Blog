# Agile

# Table Of Contents

- Agile
- Table Of Contents
    - [Introduction](#introduction)
    - [Benefits of agile development](#benefits-of-agile-development)
    - [MoSCoW](#moscow)
    - [User Story Points Score](#user-story-points-score)
    - [Milestones](#milestones)
    - [User Stories and Epics](#user-stories-and-epics)
    - [User Stories](#user-stories)
    - [List Of Epics](#list-of-epics)
  - [UX Table Of Contents](#the-ux-table-of-contents)
    - [Welcome and Introduction](#1-welcome-and-introduction)
    - [Frontpage of the Blogpost](#2-frontpage-of-the-blogpost)
    - [Nav-bar](#3-nav-bar)
    - [Sign-Up Process](#4-sign-up-process)
    - [Creating and Sharing Content](#5-creating-and-sharing-content)
    - [Interaction and Collaboration](#6-interaction-and-collaboration)
    - [Profile and Community Building](#7-profile-and-community-building)
    - [Ease of Use and Accessibility](#8-ease-of-use-and-accessibility)
    - [Continuous Engagement](#9-continuous-engagement)
    - [Conclusion](#10-conclusion)
  - [User Demographic Table of Contents](#user-demographic-table-of-contents)
    - [Age Group](#1-age-group)
    - [Interest](#2-interest)
    - [Education Level](#3-education-level)
    - [Technological Proficiency](#4-technological-proficiency)
    - [Geographic Location](#5-geographic-location)
    - [Behavioral Traits](#6-behavioral-traits)
    - [Accessibility Needs](#7-accessibility-needs)
  - [User Stories Table of Contents](#user-stories-table-of-contents)
    - [Welcome and Introduction](#welcome-and-introduction)
    - [Sign-Up Process](#sign-up-process)
    - [Navigation and Exploration](#navigation-and-exploration)
    - [Creating and Sharing Content](#creating-and-sharing-content)
    - [Interaction and Collaboration](#interaction-and-collaboration)
    - [Profile and Community Building](#profile-and-community-building)
    - [Ease of Use and Accessibility](#ease-of-use-and-accessibility)
    - [Continuous Engagement](#continuous-engagement)

## Introduction

Agile planning methodology was used to create the site Astro Blog. GitHub projects was used to organise the development process into sprints, epics, Kanban boards and issues. This was the first time I have undertaken a project that was driven by the agile development process and a learning curve was associated with the development of this project, however the benefits of an agile approach soon outweighed the learning curve associated. I first started by creating issues. These where user stories that had a detailed acceptance criteria and unit tasks associated with each issue. These issues where also labelled using the MoSCoW technique. Each issue was then sorted into the epic in which it belonged. This project was completed over three Milestones of work.

## Benefits of agile development

As mentioned in the introduction there was a learning curve associated with using agile development for the first time, however there was a received number of benefits associated as well. These benefits include:

 1. Having a plan in place. It was easier to know which task I was working on and found myself getting less distracted as I was carrying out the work associated with the project.
 2. Having a dedicated timeframe for issues to be done. This helped me stay on track in terms of timeframe for the project.
 3. Initial overall planning of the project. As a lot of thought went into the user stories I was able to have a better picture of the overall project before starting the work. This sped up production and definitely felt more organised.
 4. Easily see the benefits of collaboration. As I was working on this project on my own it was easy to see how the use of agile would benefit collaboration if multiple people where working on a project together. Especially with the Kanban board, being able to see what is being worked on and the status of the work and also being able to assign this work to individual developers.

## MoSCoW

MoSCoW analysis helps developers understand which tasks to prioritise. It is a process by which labels are added to issues. These labels include 'Must-have', 'Could-have', 'Should-have' and ' Wont-have'. In my project I tried to ensure 'Should-have' prioritised user stories was not more than 60% of total. On reflection I should have prioritised more 'Must-have'. I also did not use 'Wont-have' and 'Could-have' in this project and this is something I would considering using more of in future projects as I found this technique useful to determine important work to be carried out. The image below shows a portion of the issues associated with this project and their labels in place.

## User Story Points Score
For this project I have caculated that for the Fibonacci User Story Points Score:
- **Must Have:** #3 +3, #8 +8, #20 +5, #25 +13, #16 +5, #23 +2, #15 +8, #4 +2, #15 +8, #4 +2, #17 +13, #28 +5,  #32 +8, #26 +8, #5 +2, #21 +3, #33 +5, #22 +3, #39 +5, #19 +2, #37 +2, #38 +5 = Total of 122 points
- **Should Have:** #41 +8, #31 +5, #30 +8, #43 +13, #35 +8 = Total of 42 points
- **Could Have:** #13 +8, #36 +8 = Total of 16 points
- **Wont Have:** 0

[Table Of Contents](#table-of-contents)

## The UX Table Of Contents
  1. [Welcome and Introduction](#1-welcome-and-introduction)
  2. [Frontpage of the Blogpost](#2-frontpage-of-the-blogpost)
  3. [Nav-bar](#3-nav-bar)
  4. [Sign-Up Process](#4-sign-up-process)
  5. [Creating and Sharing Content](#5-creating-and-sharing-content)
  6. [Interaction and Collaboration](#6-interaction-and-collaboration)
  7. [Profile and Community Building](#7-profile-and-community-building)
  8. [Ease of Use and Accessibility](#8-ease-of-use-and-accessibility)
  9. [Continuous Engagement](#9-continuous-engagement)
  10. [Conclusion](#10-conclusion)

### 1. Welcome and Introduction
**User opens the blog website:**

- **Landing Page:**
  - A visually appealing landing page with a background video of the night sky or a space theme.
  - A welcoming headline: "Share the latest space news - Welcome to Cosmic Chronicles, your gateway to the wonders of the universe!".
  - On the landing page there is no nav-bar but only "Go The Blog" button to navigate to the blogpost.
  - There extra features build in like a "Astronomy Picture of the Day"  whit a link to NASA APODs.
  - Subscribtion section for newsletter sign up.
  - A snap of the most popular categories of this blog.
  - The most recent contributors are displayed in the homepage.
  - A widget that tracks the International Space Station whit a redirect link that actual plot the ISS in real time on a map.

- **Call to Action:**
  - "Go To The Blog" button leads you the blogpost frontpage.
  - There are links where you interact whit API of "Astronomy Picture of the Day" and the International Space Station or ISS worldmap plotter.
  - Fill in the subscription and a confirmation mail will be sent.
  - Subscription is no registration to the blogpost.

### 2. Frontpage of the Blogpost
- **User clicks on "Go To The Blog":**
  - All registered users can add post on the blog.
  - All post listed at there post date and shows a short list of text.
  - On "Read more" hyperlinks there is redirect to blog post details where every aspect of the post can be read.

- **Call to Action:**
  - All non-autheticad users can access the blog post, but can not add posts.
  - All autheticad users can add posts, they can also delete or edit there posts.
  - Pagination to easy access other blog post.

[Table Of Contents](#table-of-contents)

### 3. Nav-bar 
- **User clicks access to Navigation Bar"**
  - The users can see any time login status in right upper corner.
  - The users can access if logged in there creditials.
  - The users can easy search trougout the blogpost.
  - Categories lists feature to display post per category.
  - Content of the categories.
  - Arrow icon left redirect always the blogpost frontpage.
  - House icon redirect always to the landing page.

- **Call to Action**
  - The users can easy login or logout.
  - The users can update and/or manipulate there profile.    
  - The users can search for certain key words to access and find posts.
  - Display all posts relevant to the category.
  - Show all categories and there content in Blog Post Categories.
  - Subpage of the blogpost is the frontpage of the blogpost.
  - Mainpage of the blogpost is the homepage of the blogpost.

### 4. Sign-Up Process
**User clicks on "Sign Up":**

- **Sign-Up Form:**
  - On the blog frontpage there is on the right upper corner a "Register" button.
  - Simple form requesting essential information: Username, Email, Password, and Confirm Password.
  - Optional feature is to sign up using social media accounts (Google, Facebook). 

- **Profile Setup:**
  - After signing up, there is the possibility to complete their profile "Create Profile Page" button:
    - Write a short bio.
    - Upload a profile picture.      
    - Add links to personal websites or social media profiles (optional).
  - If needed the user can always update there profile afterwards.

### 5. Creating and Sharing Content
**User clicks on "Add Post":**

- **Add Post Page:**
  - Simple and intuitive editor for creating posts:
    - Title field.
    - Content field with rich text formatting options.
    - Option to add photos (drag and drop or upload from device).
    - Tags field for categorizing the post (e.g., Planets, Stars, Telescopes, Space Missions).
  - "Post" button to publish the content.

[Table Of Contents](#table-of-contents)

### 6. Interaction and Collaboration
**User interacts with a post:**

- **Commenting:**
  - Users can leave comments on posts.
  - Comment section with a clear text field, and an "Add Comment" button.
  - Ability to reply to comments and like/dislike comments.

- **Collaborative Features:**
  - Option to invite other users to collaborate on a post.
  - Real-time collaboration with a shared editor for multiple contributors.

### 7. Profile and Community Building
**User explores their profile and connects with others:**

- **User Profile:**
  - Profile page displaying user information: profile picture, bio, posts, and activity.
  - Edit Profile button for updating information and settings.

- **Community Engagement:**
  - Explore page with user search functionality.
  - Follow other users on their posts and activities.
  - Direct messaging feature for private conversations.

### 8. Ease of Use and Accessibility
**User enjoys a seamless experience:**

- **Responsive Design:**
  - Blog is fully responsive and works seamlessly on desktop, tablet, and mobile devices.
  - Fast loading times and smooth transitions between pages.

- **Accessibility:**
  - High contrast mode and text resizing options for visually impaired users.
  - Keyboard navigable interface and screen reader compatibility.

### 9. Continuous Engagement
**User stays engaged and returns to the blog:**

- **Content Recommendations:**
  - Personalized content recommendations based on user’s interests and activity.
  - Regular email updates with highlights from the blog and upcoming astronomical events.

- **Events and Challenges:**
  - Community events such as virtual star-gazing sessions, photo contests, and Q&A sessions with astronomy experts.
  - Interactive challenges and quizzes to keep users engaged and learning.

### 10. Conclusion
AstroShare offers a user-friendly, engaging, and collaborative platform for astronomy enthusiasts to share knowledge, interact with the community, and enjoy a seamless and enriching experience.

[Table Of Contents](#table-of-contents)

## User Demographic Table of Contents
1. [Age Group](#1-age-group)
2. [Interest](#2-interest)
3. [Education Level](#3-education-level)
4. [Technological Proficiency](#4-technological-proficiency)
5. [Geographic Location](#5-geographic-location)
6. [Behavioral Traits](#6-behavioral-traits)
7. [Accessibility Needs](#7-accessibility-needs)

### 1. Age Group
- Primarily adults and young adults (18-65 years old) who have a keen interest in astronomy and space exploration.
- This demographic is likely to be tech-savvy and comfortable using digital platforms for both learning and social interaction.

### 2. Interest
- Individuals who are passionate about astronomy, including amateur astronomers, space enthusiasts, students studying astronomy or related sciences, and professionals working in the field.

### 3. Education Level
- Varied, but likely to include individuals with at least a high school education and a strong interest in science, particularly astronomy and space sciences.
- Some users may have advanced degrees or be pursuing careers in astronomy or related fields.

### 4. Technological Proficiency
- Users who are comfortable with technology, including social media platforms, online communities, and content creation tools.
- They are likely to engage actively in online discussions, share content, and collaborate with others on the platform.

### 5. Geographic Location
- The platform may attract users globally, given the universal interest in astronomy.
- However, regions with active amateur astronomy communities, space research institutes, or strong educational programs in astronomy may have a higher concentration of users.

### 6. Behavioral Traits
- Users who enjoy sharing knowledge, participating in discussions, and engaging with multimedia content such as photos and videos related to astronomy.
- They may also value community building, collaborative projects, and staying updated with the latest astronomical discoveries and events.

### 7. Accessibility Needs
- While primarily targeting users comfortable with digital platforms, efforts should be made to ensure accessibility features such as high contrast mode, text resizing, and screen reader compatibility to accommodate users with visual impairments or disabilities.

[Table Of Contents](#table-of-contents)

## User Stories and Epics
Astro Blog Share is for those who are interested in Astronomical subjects and like to share there toughs in a deticated blog. The blog can be used as a discussion platform for anybody who have a special affliation whit astronomy.

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
Each user story was classified with a label according to MoSCoW prioritization.
<br>
The Kanban board can be seen [here](https://github.com/users/Harmonica-Men/projects/10).

## Milestones 

The project was divided into three milestones, each containing the corresponding epics and user stories: [Milestone in Projects](https://github.com/Harmonica-Men/AstroShare-Blog/milestones)
<br>

1. [Setting Up The Project @ Bear minimums](https://github.com/Harmonica-Men/AstroShare-Blog/milestone/1)
- Task: The goal is to set up the project at its bare minimum.
  - EPIC 1 (Repository and Deploy Early)

2. [Basic Blog Functionality](https://github.com/Harmonica-Men/AstroShare-Blog/milestone/2)
- Task: Implement basic blog functionality including models, views, and templates.
  - EPIC 2 (Basic Blog Functionality)
  - EPIC 3 (User Authentication) 
  - EPIC 4 (Admin Interface)
  - EPIC 5 (Commenting System) 
  - EPIC 6 (Styling and Frontend) 
  - EPIC 7 (Search and Filtering) 
  - EPIC 8 (SEO and Performance Optimization) 

3. [Testing and Validation](https://github.com/Harmonica-Men/AstroShare-Blog/milestone/3)
- Task: test & validate
  - EPIC 9 (Testing and Validations) 
  
### User stories 

A user story is an explanation of a software feature written from the perspective of the end user. Its purpose is to articulate how a software feature will provide value to the customer. User stories were created with the help of GitHub issues. Each user story contains:
* Title - Short description of the user story. 
* Description - As a **role** i can **capability** so that **received benefit**.
* Acceptance criteria - A set of conditions that a feature must meet to be accepted by the user. 
* Unit tasks - A break down of each task needed to complete user story. 
* A MoSCoW label - To prioritise tasks. 
* Assignee -  Who the user store is assigned too. 
* Milestone - Which epic this user store is associated with.

Below is an example of how the user stories where structured for this project.

[Table Of Contents](#table-of-contents)

### List of Epics

- [EPIC 1: Repository and Deploy Early](https://github.com/users/Harmonica-Men/projects/10?pane=issue&itemId=70098431)
- [EPIC 2: Basic Blog Functionality](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70117569)
- [EPIC 3: User authentication](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70121138)
- [EPIC 4: Admin Interface](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70123718)
- [EPIC 5: Commenting System](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70128247)
- [EPIC 6: Styling and Frontend](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70208718)
- [EPIC 7: Search and Filtering](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70129504)
- [EPIC 8: SEO and Performance Optimization](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70129811)
- [EPIC 9: Testing and Validations](https://github.com/users/Harmonica-Men/projects/10/views/1?filterQuery=label%3AEPICS&pane=issue&itemId=70130186)

User Stories with their id:  <br>
- As a software developer,I can to set up the VS Code IDE on my local machine,so that I can efficiently develop and debug my projects. [#37](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70364129)
- As a software developer, I want to set up a GitHub repository for our new project, so that the team can collaborate on the codebase efficiently and maintain version control. [#2](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70098555)
- As a software developer, I can to create a working Django app, so that I can build and deploy a web application efficiently. [#3](https://github.com/users/Harmonica-Men/projects/10?pane=issue&itemId=70105394)
- As a software developer, I want to deploy our application to Heroku, so that it is accessible to users and can be tested in a live environment. [#4](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70105449)
- As a software developer, I want to set up a GitHub repository for our new project, so that the team can collaborate on the codebase efficiently and maintain version control.[#5](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70109025)
- As a software developer, I want to define the models for blog posts, so that the application can store and manage blog post data efficiently.[#15](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70132743)
- As a software developer, I can to create views to list all posts, view individual posts, and manage categories and profiles, so that users can easily navigate and interact with the blog content and manage their profiles.[#16](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70135804)
- As a software developer, I can to design templates for the blog, so that the blog has a consistent and visually appealing layout.[#17](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70138078)
- As a software developer, I can to implement URL routing for the blog, so that users can navigate to different parts of the blog application.[#18](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70139779)
- As a frontend developer, I want to set up Django’s built-in authentication system, so that users can securely register, log in, and manage their accounts.[#19](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70201797)
- As a software developer, I can to create registration, login, and logout views and templates, so that users can securely register, log in, and log out of the application.[#20](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70203518)
- As a software developer, I can to implement user-specific actions for creating, editing, and deleting blog posts,
so that users can manage their own blog content.[#21](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70204403)
- As a software developer, I want to register the blog models with the Django admin, so that I can manage blog content through the Django admin interface.[#22](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70205152)
- As an admin user, I can to customize the admin interface to improve usability, so that I can efficiently manage data and perform administrative tasks.[#23](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70205593)
- As a software developer, I can to create models for comments linked to blog posts, so that users can add comments to blog posts and manage them efficiently.[#24](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70206168)
- As a user, I can to add comments to blog posts and view comments on blog posts, so that I can engage with the content and other users.[#25](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70206850)
- As a software developer, I can to implement moderation features for comments, so that comments can be reviewed and approved before being displayed publicly.[#26](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70207750)
- As a software developer, I want to use a CSS framework like Bootstrap for basic styling, so that the application has a consistent and responsive design with minimal effort.[#28](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70210752)
- As a user, I can to customize templates so that I can ensure a consistent and responsive design across all devices and platforms.[#29](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=70211351)
- As a software developer, I want to add JavaScript for interactive elements such as comment submission and post likes, so that users can interact with the blog posts dynamically without page reloads.[#30](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70211925)
- As a user, I can to have a search bar on the blog, so that I can easily search for posts by keywords.[#31](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70212442)
- As a user, I can to filter blog posts by categories, tags, and publication dates, so that I can easily find the content that interests me.[#32](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70212964)
- As a software developer, I can to implement SEO best practices, so that the application ranks higher in search engine results and attracts more organic traffic.[#34](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70213733)
- As a front-end developer, I want to optimize images and static files, so that the application loads faster and provides a better user experience.[#35](https://github.com/users/Harmonica-Men/projects/10/views/2?pane=issue&itemId=70214000)
- As a software developer, I want to write unit tests and integration tests for critical functionality, So that I can ensure the reliability and correctness of the application and catch issues early in the development cycle. [#38](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=79390026) 
- As a software developer, I want to set up continuous integration (CI), So that I can automate tests and streamline manual testing processes to improve software quality and reduce the time spent on manual checks. [#39](https://github.com/users/Harmonica-Men/projects/10/views/1?pane=issue&itemId=79390026)
- As a software developer, I want to set up continuous integration (CI), So that I can automate tests and streamline manual testing processes to improve software quality and reduce the time spent on manual checks. 

[Table Of Contents](#table-of-contents)

## User Stories Table of Contents
1. [Welcome and Introduction](#welcome-and-introduction)
2. [Sign-Up Process](#sign-up-process)
3. [Navigation and Exploration](#navigation-and-exploration)
4. [Creating and Sharing Content](#creating-and-sharing-content)
5. [Interaction and Collaboration](#interaction-and-collaboration)
6. [Profile and Community Building](#profile-and-community-building)
7. [Ease of Use and Accessibility](#ease-of-use-and-accessibility)
8. [Continuous Engagement](#continuous-engagement)

### Welcome and Introduction
**As a user:**
- I want to see a visually appealing landing page with a space theme and a welcoming headline.
- I want to read a brief introduction about the community and its features.
- I want to have prominent "Sign Up" and "Log In" buttons to easily join or access the blog.
- I want to watch a short introductory video or animation showcasing the blog's features.

### Sign-Up Process
**As a user:**
- I want to click on "Sign Up" and fill out a simple form with my Username, Email, Password, and Confirm Password.
- I want to have the option to sign up using my social media accounts (Google, Facebook).
- I want to be prompted to complete my profile by uploading a profile picture, writing a short bio, and optionally adding links to personal websites or social media profiles after signing up.

### Navigation and Exploration
**As a user:**
- I want to be directed to the main dashboard with a personalized greeting after completing the sign-up.
- I want an easy-to-navigate menu with options like Home, Explore, Create Post, My Profile, Notifications, Settings, and Log Out.
- I want to see a home feed with the latest posts from users, including photos, articles, and discussions about various astronomical topics.
- I want each post to include the author’s profile picture, name, post title, content preview, and interaction buttons (Like, Comment, Share).

### Creating and Sharing Content
**As a user:**
- I want to click on "Create Post" and access a simple and intuitive editor.
- I want to have a title field, content field with rich text formatting options, and the ability to add photos either by dragging and dropping or uploading from my device.
- I want to add tags to categorize my post and a "Post" button to publish my content.

[Table Of Contents](#table-of-contents)

### Interaction and Collaboration
**As a user:**
- I want to leave comments on posts with a clear text field and an "Add Comment" button.
- I want to be able to reply to comments and like or dislike them.
- I want to invite other users to collaborate on a post.
- I want real-time collaboration with a shared editor for multiple contributors.
- I want to receive notifications for new comments, likes, and collaboration invites, with a notification bell icon in the menu bar showing a dropdown list of recent notifications.

### Profile and Community Building
**As a user:**
- I want to explore my profile page that displays my information, including my profile picture, bio, posts, and activity.
- I want an "Edit Profile" button to update my information and settings.
- I want to use the Explore page to search for other users.
- I want to follow other users to receive updates on their posts and activities.
- I want to use a direct messaging feature for private conversations.

### Ease of Use and Accessibility
**As a user:**
- I want the blog to be fully responsive and work seamlessly on desktop, tablet, and mobile devices.
- I want fast loading times and smooth transitions between pages.
- I want high contrast mode and text resizing options for better accessibility if I am visually impaired.
- I want a keyboard navigable interface and screen reader compatibility.
- I want an easily accessible help section with FAQs and tutorials, along with a contact support option for direct assistance.

### Continuous Engagement
**As a user:**
- I want personalized content recommendations based on my interests and activity.
- I want regular email updates with highlights from the blog and information about upcoming astronomical events.
- I want to participate in community events such as virtual star-gazing sessions, photo contests, and Q&A sessions with astronomy experts.
- I want to engage in interactive challenges and quizzes to keep learning and stay engaged with the blog.

[Table Of Contents](#table-of-contents)