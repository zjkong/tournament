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

5 Find tournament file through git bash and run 'python tournament_test.py', you will find that all tests passed.

6 If you have installed python, you can open tournament.py and find what each function do to the database.
You could also find database schema from tournament.sql.
