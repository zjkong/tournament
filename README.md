# tournament
1 You need to install vagrant, virtualBox and git.
you can download both of them from here:https://www.udacity.com/wiki/ud197/install-vagrant

2 Clone the fullstack-nanodegree-vm repository, just type the following in the Git Bash program:
git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack
Then in the file github, you can find that a file called fullstack is cloned for you.

3 Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), 
then type vagrant up to launch your virtual machine

4 Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, 
and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt.  
To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, 
you'll need to run vagrant up again before you can log into it.

5 Before running application, you could run "psql" command in gitbash and do some database operation in it.
"\c database_name" allows you to connect a database you want(in this project, database name is tournament)
"\dt" tells you the how many table in the database.
"\d+ table_name" tells you the schema of each table.
"psql -f <schema>.sql" allows you to import sql schema.
You can also use insert, select, delete and other operations to update database and tables.

6 Find tournament file through git bash and run 'python tournament_test.py', you will find that all tests passed.

7 If you have installed python, you can open tournament.py and find what each function do to the database.
You could also find database schema from tournament.sql.
