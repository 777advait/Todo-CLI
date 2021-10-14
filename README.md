# ``--About--``

A basic Todo application that works on CRUD operations. Fueled by *PyInquirer*, *rich* and *click* for CLI.

> Made by Advait Jadhav

  

# ``--Depends On--``

- click==8.0.1

- setuptools==56.0.0

- PyInquirer==1.0.3

- rich==10.12.0

  

# ``--Installation--``

1. Download or clone this repository.

2. Open command-line window in the directory containing this repository.

3. Run the command below on command-line.

> pip install -r requirements.txt

4. Once the dependencies are installed run the command below.

> python setup.py install

5. Voila! you are good to go!

  

# ``--How to use--``

Once you have installed the program following the steps above you must be able to run the todo command on your command line...

![todo --help](https://user-images.githubusercontent.com/76993204/137257090-22533ec0-15a7-4d25-a3eb-be3eccd8b5b9.png)

### Creating a list

Assume a list as a container which will hold all your tasks together. You can have unlimited lists at a time and you can easily play around with these lists using CRUD operations. You will be already provided with a **welcome_list** at the start, make sure to check out the tasks in it!

![todo create](https://user-images.githubusercontent.com/76993204/137257151-10bb5bd1-5c76-420a-9ac0-a77ca71c6bf9.png)  

To create a list simply run `todo create` command on your command line and it shall ask you to **enter a list name(try something funky and remember not use spaces).** You can also pass in **--name** flag in order to pre-define your list name.  

### Adding tasks to the list

Whenever you create a list you will be prompted to add your first task to it! But you can still add more tasks to it by using `todo add` command.

![todo add](https://user-images.githubusercontent.com/76993204/137257224-b5be5256-f9a8-44b9-a791-6d467566dd90.png)
![todo add](https://user-images.githubusercontent.com/76993204/137257219-b54aa804-764c-42af-acb0-93567d86d39d.png)


### Viewing tasks

Well, now that you have added tasks to your lists you might want to view the added tasks, `todo ls` will make it easier as it also shows tasks pending and tasks completed.

![todo ls](https://user-images.githubusercontent.com/76993204/137257344-56642367-c9e6-4f45-b393-e694743a1619.png)
![todo ls](https://user-images.githubusercontent.com/76993204/137257341-1fef117f-3d28-4ea7-875e-9ad21bd61b1e.png)

### Updating tasks

Adding tasks isn't enough, you need to complete them as well and if you have already completed them, don't waste a single minute, just fire up the command-line and run `todo update` command.

![todo update (1)](https://user-images.githubusercontent.com/76993204/137257467-a9d7260f-15f8-4dec-b9ab-c7327126cb3b.png)
![todo update (2)](https://user-images.githubusercontent.com/76993204/137257469-fe4bf58f-4bb9-4f0e-aa7a-0ecc8138201a.png)

### Deleting tasks

While creating a list you might encounter typos because of the super-high typing speed or eventually you might have completed all the tasks from a list. In such scenarios, you would no longer need the list and must be willing to delete it. In order to do so, use `todo delete` command this will load up an interactive menu of all your lists(choose wisely because changes can't be reverted!).

![todo delete](https://user-images.githubusercontent.com/76993204/137257568-9c17460a-94eb-47d2-8d41-d8c0a251a0ea.png)

# `--Bugs--`

I'm not sure but the program might be having some bugs or issues. If you stumble around them make sure to create a new [issues](https://github.com/advaitjadhav/Todo-CLI/issues) and I'll try to fix it as soon as possible!
