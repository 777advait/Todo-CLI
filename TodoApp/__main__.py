"""
The strange syntax in console.print statements is being used to print colored text
Prerequisites => {
	PyInquirer==1.0.3 : for command-line interface(CLI),
	rich==10.11.0 : for colored text,
	click==8.0.1 : for command-line utilty
}
"""

from . import database # databse.py
from PyInquirer import prompt # for for command-line interface(CLI)
from rich.console import Console # for colored text
import click # for command-line utilty

console = Console()
db = database.Database()
exit = False

@click.group()
def main():
	'''A basic Todo application that works on CRUD operations. Fueled by PyInquirer, rich and click for CLI.'''
	pass

@main.command()
@click.option(
	'--name', '-n',
	prompt="Enter the name of your list(Avoid using spaces)",
	help="Name of your list"
)
def create(name): # creates a list entitled --name to add tasks to it!
	'''creates a list entitled --name to add tasks to it!'''

	while True:
		questions = [
			{
				'type':'input',
				'name':'task',
				'message':'Add your first task to the newly created list: '
			}
		]

		answer = prompt(questions)

		try:
			db.create(name)
		except Exception as e:
			console.print(e, style="bold red")
			continue
		else:
			break

	db.add(name, answer["task"])
	console.print(f"List [bold magenta]{name}[/] created!\n")

@main.command()
def add(): # adds tasks to selected list
	'''adds tasks to selected list'''

	questions = [
		{
			'type':'list',
			'name':'l_name',
			'message':'To which list would you like to add your task?',
			'choices':database.get_tables()
		},
		{
			'type':'input',
			'name':'task',
			'message':'Your task:'
		}
	]

	answer = prompt(questions)

	db.add(answer["l_name"], answer["task"])

	console.print(
		f"Task [bold green]{answer['task']}[/] added to [bold magenta]{answer['l_name']}[/]!\n"
	)

@main.command()
def ls(): # shows tasks from selected list
	'''shows tasks from selected list'''

	questions = [
		{
			'type':'list',
			'name':'l_name',
			'message':'From which of the following list would you like to view your task',
			'choices':database.get_tables()
		}
	]

	answer = prompt(questions)

	console.print(f"Showing tasks from [bold magenta]{answer['l_name']}[/]...")
	db.show(answer["l_name"])

@main.command()
def update(): # updates tasks from selected list
	'''updates tasks from selected list'''

	status = {
		"0":False,
		"1":True
	}

	list_name = [
		{
			"type":"list",
			"name":"l_name",
			"message":"Update tasks from which list?",
			"choices":database.get_tables()
		}
	]

	ans_list_name = prompt(list_name)

	questions = [
		{
			"type":"checkbox",
			"name":"updated_tasks",
			"message":"Update your completed tasks",
			"choices":[
				{
					"name":task, "checked":status[str(completed)]
				} for task, completed in database.get_rows(ans_list_name["l_name"])
			]
		}
	]

	answer = prompt(questions)
	db.update(ans_list_name["l_name"], answer["updated_tasks"])

	console.print(f'Task [bold green]{answer["updated_tasks"]}[/] marked as completed!\n')

@main.command()
def delete(): # deletes the selected list
	'''deletes the selected list'''

	questions = [
		{
			'type':'list',
			'name':'l_name',
			'message':'Which list would you like to delete?',
			'choices':database.get_tables()
		}
	]

	answer = prompt(questions)

	db.delete(answer["l_name"])

	console.print(f"List [bold magenta]{answer['l_name']}[/] successfully deleted!\n")

if __name__ == "__main__":
	main()