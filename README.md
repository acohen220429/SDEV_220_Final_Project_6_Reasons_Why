## Quickstart

1. Clone the repo:

   ```git clone https://github.com/acohen220429/SDEV_220_Final_Project_6_Reasons_Why.git```

   ```cd SDEV_220_Final_Project_6_Reasons_Why```

2. Create visual environment and install dependencies (Windows):

   ```py -m venv venv```

   ```venv\Scripts\activate```

   ```pip install -r requirements.txt```

3. Run the server

   ```python manage.py runserver```

   Close server with ctrl/cmd + c

4. If you go to the URL and put /admin at the end, you can log in with your superuser credentials (the first part of your email + the password "mypassword")

## Workflow

Before doing any work, make sure you are on your own personal branch by using the ```git checkout (branch_name)``` command. Each branch is named after your first name.
Also, make sure to merge any new changes that have been made with the following commands:

```git checkout main```

```git pull origin main```

```git checkout (your_branch)```

```git merge main```

When you are finished for the time being, do the following:

```git status``` shows you what you changed

```git add .```

```git commit -m "Put clear message of what you did here"```

```git push```


