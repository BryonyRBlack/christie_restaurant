# The HoloNet

![Image of the website from AmIResponsive, showing how this is displayed on mobile, tablet and desktop](/static/images/Am%20I%20Responsive.png)

A website based in the Star Wars universe, which gives updates on events taking place in particular years. 

The aim of the website is to provide news updates, as well as allow reigstered users to take part in the conversation by comments or on the social feed.

## Contents

## Overview
The HoloNet is a way to publish news articles that can be commented on, as well as a social feed for users to use at will. The website is based within the Star Wars universe, and the news articles focus on this.

### Development Story
Initially, this project was going to be a website for a restaurant and a show. The user would be able to book seats on a particular day, view the menu available, read and post reviews, and contact the site owners. However during this, I was unhappy with the results. I could not find a design I liked for the website. I also could not make a successful booking page, as the date input would not work. As such, I amended this to a news site. Although this did require creating a news app and models, I was able to reuse many of the models already created. The menu became the wanted page, the reviews became the social feed. Though I did try and change the app name, django currently does not have a succesful way to do this completely, and as such the names have remained the same. The contact page, and home page remained the same. The booking app was deleted.

### Project Goals
* Engaging user experience: Allows a user to read news they are interested in, comment and rate articles, post on the social feed, and contact the site owner.
* Ability to easily navigate: Allows the user to find what they are looking for easily.
* Users able to participate: Allows the user to comment on posts, and post on the social feed so that they are part of the conversation.
* Responsive design: Allows for the website to load smoothly on whichever device is used.

### First time users
* Home: When the site is loaded, there is an explanation as to what The HoloNet is, and what each individual page is for. There is a navigation bar along the top for ease. 
* News: The News page shows the list of articles with the newest first. If the user clicks on this, they can read the full article and any comments left. They are unable to comment.
* Social Feed: A first-time user is able to view the comments, however they cannot leave one.
* Contact: This page allows for first-time users to send a message without having an account. They have to provided a name and email address.

### Existing users
* News: With an account, the user is able to leave comments on articles.
* Social Feed: With an account, a user can leave messages on the feed.

### Admin
Those with admin privellages are the only ones able to post articles, and on the wanted page. This is to mirror a real news site. They also are able to view and delete comments or posts on the social feed. They can also read any messages sent through the contact page.

## Original Design

### Original WireFrames
![Image of a WireFrame designed for a restaurant. Shows the home page, and the booking page](/static/images/restaurant%20wireframe.png)
![Image of a WireFrame designed for a restaurant. Shows the menu page, and the review page](/static/images/restaurant%20wireframe%202.png)

### Original Website Design
![Screenshot of the original website design. Shows the home page](/static/images/AC%20index%20page.png)
![Screenshot of the original website design. Shows the booking page](/static/images/AC%20Booking.png)
![Screenshot of the original website design. Shows the menu page](/static/images/AC%20menu.png)
![Screenshot of the original website design. Shows the reviews page](/static/images/AC%20reviews.png)
![Screenshot of the original website design. Shows the contact page](/static/images/AC%20Contact%20Us.png)

The above is the original planning and design used when this was a restaurant website. Some of these I have kept, as detailed below.

## Features
### Overview
![Screenshot of the home page](/static/images/home%20page.png)
* Shows TheHolonet icon
* Explains what the site is, and what each individual page does
* This is the same page as created for the original restaurant layout.

![Screenshot of the news page](/static/images/news%20page.png)
* Lists each news article, showing only the title and the slug. These are shown in descending order
* If the title is clicked, this links to the article page.

![Screenshot of the article page](/static/images/article%20detail%20page.png)
* If the title was clicked on the news page, this page is brought up
* Shows the full selected article.
* Comments for the article are shown below the article.
* If signed in, the user has the ability to leave a comment.
* If the user has previously left a comment, they can edit or delete these.

![Screenshot of the wanted page](/static/images/wanted%20page.png)
* Users are able to see who is a wanted criminal.
* Only the admin can post to this page
* This is the same layout as created for the original restaurant layout.

![Screenshot of the social feed page](/static/images/social%20feed%20page.png)
* Users are able to view over messages that users have posted.
* If logged in, users are able to make their own posts, which immedietly show to the feed.
* This is the same form as created for the original review layout.

![Screenshot of contact us page](/static/images/contact%20us%20page.png)
* Users are able to send a message to the site owners.
* This form does not require the user to be logged in.
* This is the same form as created for the original restaurant layout.

## All pages
### Navigation bar
![Screenshot of the full width navigation bar](/static/images/navbar%20full%20width.png)
On desktop this is the navigation bar. It is sticky to the top of the screen, making it always visible even if scrolled down. The current page is visible as a different colour to the rest.

![Screenshot of the navigation bar if logged in](/static/images/nav%20bar%20logged%20in.png) ![Screenshot of the navigation bar if logged out](/static/images/navbar%20logged%20out.png)
On the right side of the navigation bar, a message is displayed depending on if the user has an account. If the user has an account then they are welcomed back. If not, they are advised they aren't logged in and won't have access to social features.

![Screenshot of the navigation bar for mobile](/static/images/navbar%20mobile.png) ![Screenshot of the uncollapsed mobile navigation bar](/static/images/navbar%20mobile%20full.png)
For smaller devices, the navigation shrinks into a burger icon, rather than take up space on the page. The user can click this for access to the full navigation.

### Footer
![Screenshot of the footer](/static/images/footer.png)
The footer sits along the bottom of all of the pages. It shows the copyright.

## Testing
Please see the testing documentation here

## Technologies used
Fontend: HTML, CSS, JavaScript, Bootstrap
Backend: Python, Django, Summernote
Liberies and dependecies:
* Django
* Cloudinary
* Crispy-Bootstrap
* Django-Allauth
* Gunicorn
* WhiteNoise

## Deployment
* Created the site within VS
* Linked the VS code, to a repository on GitHub
* In Heroku, created a new app
* Set the app to have a unique name, and a region of Europe
* Linked the Heroku app, and GitHub repository together
* Manually ran deployment

## Credits
* Bootstrap Documentation
* Code Institute's codestar blog tutorial
* Django 5 By Example by Antonio Mele
* Slack Overflow

### Acknowledgements
* My mentor Spencer who offered insight on what was required, and inspiration on how to resolve.
* peer-code-review on Slack, for giving me advice on some elements that could be added to the project
