# Testing

## User Stories
### Read an article

* When the title is clicked, the whole article is shown

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| The full article showing when the title is clicked | On the list of articles, clicked onto the title | Pass, the full artcile was opened  |


This has passed

### Register
* The ability to register
* The ability to log in
* Access to post comments

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| When a username and password is entered as directed, the user can make an account | On the register page, a username and a password meeting critera was entered | Pass, an account was created |
| If a username is not entered, an account cannot be created | On the register page, an email address and a password was entered, however a username was not | Pass, the user is unable to create an account without a username |
| If a password is not entered, an account cannot be created | On the register page, an email address and a username was entered, however a password was not | Pass, the user is unable to create an account without a password |
| If the password does not meet the criteria, an account cannot be created | On the register page, the password entered did not meet the stated requirements | Pass, the user is unable to create an account if the password does not meet criteria |
| If the password and the password confirmation aren't the same, the user cannot make an account | On the register page, two different passwords were entered | Pass, the user is unable to create an account if the password and password confirmation do not match.
| On the log in page, when the username and password are entered correctly, the user can log in | On the log in page, the username and password are entered correctly | Pass, the user is able to log in. |
| On the log in page, when the username is entered incorrectly, the user cannot log in | On the log in page, the username is entered incorrectly | Pass, the user is unable to log in. |
| On the log in page, when the password is entered incorrectly, the user cannot log in | On the log in page, the password is entered incorrectly | Pass, the user is unable to log in. |

These have all passed

### Manage Articles
* If logged in as a superuser, I can create, update and delete articles.
* If logged in as a user, can read articles.

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| As the superuser, I can create an article | On the admin page, the plus sign was clicked to create a new post. Then the CHECK THIS was changed to published, and the post was visable on the blog | Pass, a post was created. |
| As the superuser, I can update an article | On the admin page, I can view the list of articles, and click the edit button to update them. | Pass, a post can be updated. |
| As the superuser, I can delete an article | On the admin page, I can view the list of articles, and click the delete button to remove them. | Pass, a post was deleted. |
| As a user, I can read an article | On the frontend, I could click onto an article's title and read the post. | Pass, the post can be read. |

These have passed. However the superuser's abilitiy to create and delete articles is only available in admin mode. Making this available on the front end would be a future feature to impliment. In addition, non-registered users can also read articles, however can not post comments.

### Create Drafts
* Superuser can draft articles, that can be accessed later

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| As the superuser, I can draft an article | On the admin page, the plus sign was clicked to create a new post. Then the CHECK THIS was changed to draft, and the post was saved. | Pass, a post was created and saved. |

This has passed, however this is currently only available in admin mode. Making this available on the front end would be a future feature to impliment.

### View Wanted Page
* User able to view the page and know who is being looked for.

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| As a user, I am able to see the content on the wanted page | Clicking onto the wanted page shows the required images. | Pass, the images are visable. |

This has passed

### Edit Wanted Page
* Ability to add new entries
* Ability to delete entries

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| As the superuser, I can create new entries on the wanted page | On the admin page, the plus sign was clicked to create a new entry. Then the CHECK THIS was changed to published, and the post was visable on the blog | Pass, an entry was created. |
| As the superuser, I can delete an entry | On the admin page, I can view the list of entries, and click the delete button to remove them. | Pass, an entry was deleted. |

This has passed, however is only available to the superuser on the admin page.

### Social Feed
* The ability to post
* The ability to delete or edit posts later

| Test | What was Carried Out | Result |
| ---- | ---- | ---- |
| As a user, I can read the comments | I could click onto an social feed and read the posted comments. | Pass, the comments can be read. |
| As a user, I can create a comment | On the social feed, I can type a comment and post it | Pass, a comment was created. |
| A empty comment cannot be posted | On the social feed page, if the text field has not been filled out, a comment is not posted. | Pass, a warning comes up advising the text field cannot be left empty. |


The ability to delete or edit a comment has not been implimented for the social feed, however is available on the comments on articles. This was due to time restraints, and would be a future addition.

### Like or dislike a comment
* A fully functional like button
* A fully functional dislike button
* Comments show how many likes or dislikes they have received

This has not been implimented. This would be a future addition.

## Python Testing
All forms and models provided have been manually tested.
* Home page - the object is visible. Pass
* News page - the articles show up in a list order. They have the user-input title and except. Pass
* Article detail - When clicked, the correct article is displayed in full - pass
  * Comments - the form can be filled in, and posts immedietly to the page. The comment shows the logged in user correctly. The range function works for the rating. Pass
* Wanted - The objects show correctly on the page. Pass
* Social Feed - the form can be filled in, and posts immedietly to the page. The message shows the logged in user correctly. Pass
* Contact page - The form can be filled in. Once sent, this is received on the admin page. This is not shown to other users. Pass
* Account
  * Register - this successfully lets a user create an account. Pass
  * Sign in - this succesfully lets a user log in. Pass
  * Sign out - this succesfully lets a user log out. Pass

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
<details>
<summary>
The Lighthouse test for mobile
</summary>

![Screenshot of Lighthouse mobile test](/static/images/lighthouse%20mobile.png)
</details>

<details>
<summary>
The Lighthouse test for desktop
</summary>

![Screenshot of Lighthouse mobile test](/static/images/lighthouse%20desktop.png)
</details>

## Code Validation
### HTML
<details>
<summary>
Home Page
</summary>

![Screenshot of HTML validation for home page](/static/images/html%20test%20home.png)
</details>

<details>
<summary>
News Page
</summary>

![Screenshot of HTML validation for news page](/static/images/html%20news%20page%20test.png)#
</details>

<details>
<summary>
Article Detail
</summary>

![Screenshot of HTML validation for article detail](/static/images/html%20article%20detail%20test.png)
</details>

<details>
<summary>
Wanted Page
</summary>

![Screenshot of HTML validation for wanted page](/static/images/html%20test%20wanted.png)
</details>

<details>
<summary>
Social Feed
</summary>

![Screenshot of HTML validation for social feed page](/static/images/html%20test%20social%20feed.png)
</details>

<details>
<summary>
Contact Us
</summary>

![Screenshot of HTML validation for contact page](/static/images/html%20test%20contact.png)
</details>

<details>
<summary>
Register
</summary>

![Screenshot of HTML validation for register page](/static/images/html%20test%20register%20page.png)
</details>

<details>
<summary>
Sign In
</summary>

![Screenshot of HTML validation for sign in page](/static/images/html%20test%20sign%20in.png)
</details>

<details>
<summary>
Sign Out
</summary>

![Screenshot of HTML validation for sign out page](/static/images/html%20test%20sign%20out.png)
</details>

### CSS
<details>
<summary>
CSS Testing
</summary>

![Screenshot of CSS validation](/static/images/css%20test.png)
</details>

### Python
<details>
<summary>
Home Page
</summary>

![Screenshot of python validation for home page](/static/images/python%20testing%20home%20admin.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20models.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20urls.png)
![Screenshot of python validation for home page](/static/images/python%20testing%20home%20views.png)
</details>

<details>
<summary>
News
</summary>

![Screenshot of python validation for news page](/static/images/python%20testing%20news%20admin.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20forms.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20models.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20urls.png)
![Screenshot of python validation for news page](/static/images/python%20testing%20news%20views.png)
</details>

<details>
<summary>
Wanted (app name currently 'menu')
</summary>

![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20admin.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20models.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20urls.png)
![Screenshot of python validation for wanted page](/static/images/python%20testing%20menu%20views.png)
</details>

<details>
<summary>
Social Feed (app name currently 'reviews')
</summary>

![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20admin.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20models.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20urls.png)
![Screenshot of python validation for social feed page](/static/images/python%20testing%20reviews%20views.png)
</details>

<details>
<summary>
Contact
</summary>

![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20admin.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20models.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20urls.png)
![Screenshot of python validation for contact page](/static/images/python%20testing%20contact%20views.png)
</details>

### JavaScript
<details>
<summary>
JavaScript validation
</summary>

![Screenshot of JavaScript validation for contact page](/static/images/javascript%20testing.png)
</details>

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