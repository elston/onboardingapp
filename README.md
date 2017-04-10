
OOPJavaScript & RPC-django & Django 1.9.5  & python3 & sqlite & bootstrap 
==================


COMPLETED
==================
##### 1. Team Owner Membership:
When a team is created, the team owner is asked if they need to be added to the team as a member [with a checkbox], if so, they are added to the team, and should show up in the members list.

##### 2. Team Invitation status:
A teamuser should be placed in invitation status until they reach the team_invitation_step2 endpoint.  Until then, they are marked as invited, but not added.

##### 3. Service links:
All service icons should be clickable, open in a new tab, and should take the user to the logon page for the service.

##### 4. Team Ownership transfer:
A team owner should be able to transfer ownership to another teamuser.  This action must be confirmed.

##### 5. Empty Account Dashboard:
If the user has no teams, they should be instructed to create a team, and provided with a link.  

##### 6. Team Dashboard Creation link:
The team dashboard, and the regular dashboard should have a link to create a new team.

##### 7. Team Information edit:
The team should have editable information: Description and Team Name.

NOT COMPLETED
==================

##### 1. Error Log:
This log should look a little nicer, but should also include all actions that the software performs.  We should show the most recent 10 actions, with a date.  The actions include: “Added Team Member {} to Service {}”, “Removed Team Member {} from service {}”.  It should also indicate success or failure.

##### 2. Team member status:
The team page should list [in a collapsible div, default closed], the services the user is a member of.  This should be represented with a red/green light icon, and a link to re-invite if they are not a member, and a link to remove if they are.


##### 3. Username and password authentication:
For the services that require a token, we should change the template to request a username/email address [depending on the service], and a password.  The software will use the username and password to log into the service, navigate to the token pages, and capture the tokens.  Ideally this would happen client side.  The user should only see a loading icon.
For cases where a more secure method of capturing the token is available [oauth2, for example], this should be used.


##### 4. Billing change:
The account levels should be changed to cap on a number of users - in addition to a number of teams and orgs.