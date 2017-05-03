Getting started with Python ... 
===============================

![python_logo](images/python_logo.png)

Nothing special here, just trying to learn some Python

### But why Python?
> Python community has its own unique character. Python has a culture which finds an ideal balance between fast-moving innovation and diligent caution. It emphasizes readability, minimizes "magic," treats documentation as a first-class concern, and has a traditon of well-tested, backward-compatible releases in both the core language and its ecosystem of libraries. It blends approachability for beginners with maintainability for large projects, which has enabled its presence in fields as diverse as scientific computing, video games, systems automation, and the web. (Source: [Heroku](https://blog.heroku.com/python_and_django))

Python Learning Path
====================

## PART I (beginner)
> For total beginners that have no previous programming experience.
> 


* [ ] [Google Python Class](https://youtu.be/tKTZoB2Vjuk?list=PLC8825D0450647509) (YouTube Video)
    * [Support materials and exercises](https://developers.google.com/edu/python/)
    * Additional stuff recommanded by Google: [Udacity - CS101](http://udacity.com/course/cs101)
* [ ] [How to Think Like a Computer Scientist](http://interactivepython.org/runestone/static/thinkcspy/index.html) (Interactive online)
* [ ] [A Byte of Python](https://python.swaroopch.com/first_steps.html) (Book online)
* [ ] [Python for You and Me - _PYM_ ](http://pymbook.readthedocs.io/en/latest/) (Book online)
* [ ] [CodeAcademy Python Course](https://www.codecademy.com/learn/python) (Interactive online)
* [ ] [Learn Python The Hard Way](https://learnpythonthehardway.org/book/) (Book online)
* [ ] [CS Principles: Big Ideas in Programming](http://interactivepython.org/runestone/static/StudentCSP/index.html) (Interactive online)
* [ ] http://www.pythonlearn.com/
* [ ] *Write automated tests right from the beginning!*
    * [ ] Write unit tests with py.test ([PyTest tutorial](https://github.com/keeppythonweird/catinabox))
    * ...


* [ ] **Want more? For free?**
  - https://checkio.org/ (GAME!!! Play & Learn!)
  - https://www.coursera.org/learn/python/
  - https://www.coursera.org/learn/learn-to-program/
  - http://www.afterhoursprogramming.com/tutorial/Python/Overview/
  - https://www.learnpython.org/
  - http://www.pyschools.com/
  - http://codingbat.com/python
  - http://www.markandclick.com/ (Interactive tutorial)
  - http://inventwithpython.com/ (4 online books)
    - [Automate The Boring stuff](http://automatetheboringstuff.com/)
    - Invent your own computer games with python
    - Making Games with Python & PyGame
    - Hacking Secret Ciphers with Python
    - http://www.singpath.com/#/paths (nice idea - unfotunatly buggy as sh**)
    - ...

* [ ] **Want even more? (Mostly paid stuff):**
  - https://realpython.com ($60)
  - https://www.codeschool.com/ ($20 - $30 /mo)
  - https://www.datacamp.com/
  - ...

```md
Use http://pythontutor.com to 'visualize' your code
```




## PART II (intermediate)
> For peope that have at least some previous programming experience even if it's from other languages.

* [ ] [Dive Into Python 3](http://www.diveintopython3.net/) (Book online)
* [ ] [Python for Computational Science and Engineering](http://www.southampton.ac.uk/~fangohr/training/python/pdfs/Python-for-Computational-Science-and-Engineering.pdf) (PDF)
* [ ] [Problem Solving with Algorithms and Data Structures](http://interactivepython.org/runestone/static/pythonds/index.html) (Interactive online)
* [ ] [Python How to Program] (Python How to Program) (Youtube)
* [ ] [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/) (Book online)
* [ ] [Python Challenge](http://www.pythonchallenge.com/) (Solve riddles!)
* [ ] [The Python (3.6.0) Tutorial](https://docs.python.org/3/tutorial/index.html) (python.org)
* [ ] http://pythonpracticeprojects.com/
* [ ] https://www.coursera.org/learn/interactive-python-1/
* [ ] https://www.coursera.org/learn/interactive-python-2/


## PART III (specialization)
> Where do you want to go after Part I and II? There are a lot of special areas and it is hard to master them all thus you should decide where you want to put your focus.

* [ ] Backend/API development
* [ ] Frontend/GUI development
* [ ] Web Application/Apps development (front- & backend)
    * [ ] [Django-Girls](https://djangogirls.org/) (Tutorial)
* [ ] Quality assurance & Test automation
* [ ] Game development
* [ ] Data mining & analytics
* [ ] System/Server administration (DevOps)
* [ ] AI & machine Learning
* [ ] Hacking
* [ ] ...

## Editor (IDE) recommendation
 - for PART I: https://repl.it/languages/python3 (no installation require)
 - for PART II: PyCharm CE / IntelliJ CE / VisualStudio 2015+
 - for PART III: one of PART II + some specialized tools or frameworks




MY! GIT configuration
=================
What do I need to do to configure git properly for Github?

NOTE: Assuming cmder, git and git-lfs is already installed (e.g. with chocolatey)

NOTE: Assuming Github is configured to keep your email private

1. `git config --global user.name "tset-noitamotua"`
2. `git config --global user.email "tset-noitamotua@users.noreply.github.com"`
3. `git config --global credential.helper wincred`
    
    NOTE: first time you use e.g. `git push` you will be prompt for credentials though

GIT tricks
==========

### **HOW TO** create a new repository on the command line
> ... and connect it to your repo on Github 

```bash
echo "# Name of Project" >> README.md
git init
git add README.md
git commit -m "initial commit"
git remote add origin https://github.com/Tset-Noitamotua/repository_name.git
git push -u origin master
```


### **HOW TO** push an existing repository from the command line

```bash
git remote add origin https://github.com/Tset-Noitamotua/repository_name.git
git push -u origin master
```


### **HOW TO** setup your fork repo so that it is connected with original repo on Github. 
> That allows you to easily merge changes from original repo into your fork
> and thus keeps you synced:

```bash
1. git clone https://github.com/Tset-Noitamotua/robotframework    # my fork url
2. git remote add upstream https://github.com/robotframework/robotframework.git    # upstream repo url
3. git checkout master    # if not already on master branch
4. git pull upstream master    # or any other branch 
5. git push origin master    # to update your remote branch
```

For more details read original Github documentation:

[Sync a fork of a repository to keep it up-to-date with the upstream repository (syncing a fork)](https://help.github.com/articles/syncing-a-fork/)


### **HOW TO** reset url of cloned repo so that it points to your (later created) fork
> You might need this in case you cloned a repo directly (without forking it in the first place) but later decide to fork it.

```bash
git remote set-url origin https://github.com/Tset-Noitamotua/awesome-test-automation   # my fork url
```

### **HOW TO** undo an initial commit
> NOTE: can't use `reset`here becauser there is only one commit in that case
```bash
git update-ref -d HEAD
```
It will delete the named reference HEAD, so it will reset (softly, you will not lose your work) all your commits of your current branch.
([more details][] on stackoverflow.com)
To get an working git repo after that you will have to init it again
```bash
git init
git add .
git commit -am "initial commit"
git push -f
```

[more details]: http://stackoverflow.com/a/32765827/4445175


