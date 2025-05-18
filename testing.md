# Testing

## User Stories
### Read an article
* When the title is clicked, the whole article is shown

This has passed

### Register
* The ability to register
* The ability to log in
* Access to post comments

These have passed

### Manage Articles
* If logged in as a superuser, I can create, update and delete articles.
* If logged in as a user, can read articles.

These have passed. In addition, non-registered users can also read articles, however can not post comments.

### Create Drafts
* Superuser can draft articles, that can be accessed later

This has passed

### View Wanted Page
* User able to view the page and know who is being looked for.

This has passed

### Edit Wanted Page
* Ability to add new entries
* Ability to delete entries

This has passed

### Social Feed
* The ability to post
* The ability to delete or edit posts later

The first passes. The latter has not been implimented for the social feed, however is available on the comments on artciles. This was due to time restraints, and would be a future addition.

### Like or dislike a comment
* A fully functional like button
* A fully functional dislike button
* Comments show how many likes or dislikes they have received

This has not been implimented. This would be a future addition.

## JavaScript Testing
### Update button
![Screenshot of comment add to page](/static/images/comment%20test%20basic.png)
![Screenshot of comment edit button](/static/images/comment%20test%20edit.png)

If the edit button is clicked, the contents are available in the comment form. The user can then edit the comment. The edit and delete buttons are not visible if the logged in user, is not the user that made the post.

![Screenshot of updated comment](/static/images/comment%20updated.png)

After update is clicked, the comment content updates.
### Delete button
![Screenshot of delete message](/static/images/comment%20deleted.png)

If the delete button is clicked, a warning message appears asking if the user is certain they wish to delete their comment.

![Screenshot of deleted message removed](/static/images/comment%20deleted%20confirmed.png)

If the user clicks the delete, the comment is immedietly removed.

## Lighthouse checks
The Lighthouse test for mobile

![Screenshot of Lighthouse mobile test](/static/images/lighthouse%20mobile.png)


The Lighthouse test for desktop

![Screenshot of Lighthouse mobile test](/static/images/lighthouse%20desktop.png)

## Code Validation
### HTML
Home Page
![Screenshot of HTML validation for home page](/static/images/html%20test%20home.png)

News Page
![Screenshot of HTML validation for news page](/static/images/html%20news%20page%20test.png)#

Article Detail
![Screenshot of HTML validation for article detail](/static/images/html%20article%20detail%20test.png)

Wanted Page
![Screenshot of HTML validation for wanted page](/static/images/html%20test%20wanted.png)

Social Feed
![Screenshot of HTML validation for social feed page](/static/images/html%20test%20social%20feed.png)

Contact Us
![Screenshot of HTML validation for contact page](/static/images/html%20test%20contact.png)

Register
![Screenshot of HTML validation for register page](/static/images/html%20test%20register%20page.png)

Sign In
![Screenshot of HTML validation for sign in page](/static/images/html%20test%20sign%20in.png)

Sign Out
![Screenshot of HTML validation for sign out page](/static/images/html%20test%20sign%20out.png)

### CSS
![Screenshot of CSS validation](/static/css/style.css)
### Python
Home Page

![Screenshot of python validation for home page](/static/images/python%20testing%20home%20admin.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20models.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20urls.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20views.png)

News

![Screenshot of python validation for news page](/static/images/python%20testing%20news%20admin.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20forms.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20models.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20urls.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20views.png)

Wanted (app name currently 'menu')

![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20admin.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20models.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20urls.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20views.png)

Social Feed (app name currently 'reviews')

![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20admin.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20models.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20urls.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20views.png)

Contact

![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20admin.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20models.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20urls.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20views.png)

### JavaScript
![Screenshot of JavaScript validation for contact page](/static/images/javascript%20testing.png)

One unnamed variable shows here. However as this is connected to the html where bootstrap is used, I have no concerns.

## Bugs
### Resolved Bugs
#### Bug 1
On the Social Media page, the social feed and the ability to post would not align. The "align-items-start" was present, however the form to post a message continously was pushed down. This was finally located as some previously applied CSS styling which pushed all forms with the class 'form' down. Once this was removed, the two lined up.

#### Bug 2
The CSS did not update properly on the deployed version on Heroku. This was eventually located as being due to the collectstatic not having been run. Once this was done, the CSS was applied.

#### Bug 3
![Screenshot of sign up page](/static/images/sign%20up%20page.png)
On the register page, the form continues bullet points next to the criteria for the password. The section has been centered to align with the rest of the site, however the bullet points have not moved. In the end, I was able to break the form down to html, and paste this back into the file. At this point, I was then able to remove the bulletpoints. The website still works with this.

### Unresolved Bugs

#### Bug 1
On desktop, whilst the footer does sit at the bottom of the page, it goes slightly below, meaning a scroll bar is always visible. I have tried many ways of rectifying this, which has ended up with the bar directly below the content, even if this is halfway up the page. As this does currently work succesfully but with a minor bug, I have applied this styling, though hope to resolve soon.