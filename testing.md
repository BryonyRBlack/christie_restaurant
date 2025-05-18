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

## Code Validation
### HTML
### CSS
### Python
### JavaScript

## Bugs
### Resolved Bugs
#### Bug 1
On the Social Media page, the social feed and the ability to post would not align. The "align-items-start" was present, however the form to post a message continously was pushed down. This was finally located as some previously applied CSS styling which pushed all forms with the class 'form' down. Once this was removed, the two lined up.

#### Bug 2
The CSS did not update properly on the deployed version on Heroku. This was eventually located as being due to the collectstatic not having been run. Once this was done, the CSS was applied.

### Unresolved Bugs
#### Bug 1
![Screenshot of sign up page](/static/images/sign%20up%20page.png)
On the register page, the form continues bullet points next to the criteria for the password. The section has been centered to align with the rest of the site, however the bullet points have not moved. I have also been unable to remove them at this time.

#### Bug 2
On desktop, whilst the footer does sit at the bottom of the page, it goes slightly below, meaning a scroll bar is always visible. I have tried many ways of rectifying this, which has ended up with the bar directly below the content, even if this is halfway up the page. As this does currently work succesfully but with a minor bug, I have applied this styling, though hope to resolve soon.