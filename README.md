# Zendesk_Assesment
Design and develop wrapper APIs for Zendesk ticket viewer.

## Setup
 1. Ensure you have Python 3.5+ on the system.
 2. Go to the Zendesk_Assessment folder from terminal, preferably setup a virtual env for the project
 3. Make a new file '.env' under the Zendesk_Assessment folder and add the following:
        `AGENT_EMAIL= {{email_id}}`
        `AGENT_PASSWORD = {{password}}`
         `ZENDESK_BASE_URL = {{subdomain/apiv2/}} ex: https://ak5146.zendesk.com/api/v2/`
 4. Now type `pip install .` 
  To finish the setup
 
 ## To run app
 Type `EXPORT FLASK_APP=app` followed by `flask run`
 
 Now if the setup was successful, you should see that the app is running on localhost:5000
 
 Open the browser and hit the URL
 
 ## APIs available:
 1. You can access the list of the tickets for the specific agent by clicking on `view all tickets` button from UI or
  http://localhost:5000/viewalltickets?page=1 
  note: the tickets per page is limited to 100. Change the page param in the URL or click on `next` button on UI to move to next page.
  
![Alt text](/snapshots/snap_allticketsVIEW.png)
  
  2. You can access the details of a specific ticket by the URL http://localhost:5000/viewticket?ticketId=1 
     where ticketId is the param, changing that you can access other ticket details or click on the id of a specific ticket on the viewalltickets page to request the details of that specfic ticket.
 
 ![Alt text](/snapshots/snap_ticketDetailsVIEW.png)
 
 ## To run test cases
 On the terminal from the Zendesk_Assessment folder type:
  `python setup.py test`
  



