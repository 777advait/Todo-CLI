import sqlite3 # for storage
from tempfile import gettempdir # to get temp dir path
from sys import platform # to identify os

# creates a db file in temp dir
if platform == 'win32': # os => windows
	conn = sqlite3.connect(gettempdir() + '\\Todo-CLI.db')
else: # os => darwin(OS X) or linux
	conn = sqlite3.connect(gettempdir() + '/Todo-CLI.db')

cur = conn.cursor()

class Database(): # database class
	def __init__(self):
		try:
			self.create('welcome_list')
			self.add('welcome_list', 'create your first list')
			self.add('welcome_list', 'add tasks to your list')
			self.add('welcome_list', 'complete your tasks and update them respectively!')
		except sqlite3.OperationalError:
			pass

	def create(self, l_name): # creates a table of l_name
		cur.execute(f"""
				CREATE TABLE {l_name} (
				tasks text,
				completed integer
			)
		""")

	def add(self, l_name, task): # inserts task into the table
		with conn:
			cur.execute(f"INSERT INTO {l_name} VALUES (:task, :completed)", {
				'task':task,
				'completed':0
			})

	def show(self, l_name): # shows tasks from selected table
		res = cur.execute(f"SELECT * FROM {l_name}").fetchall()

		for tasks in res:
			task, completed = tasks
			
			if completed == 0:
				print("[ ]" + task)
			else:
				print("[✔]" + task)

	def update(self, l_name, task): # updates selected tasks from the selected table
		res = cur.execute(f"SELECT * FROM {l_name} WHERE completed=:completed", {
			"completed":1
		}).fetchall()

		completed_tasks = set()
		selected_tasks = set()

		for t, c in res:
			completed_tasks.add(t)

		for t in task:
			selected_tasks.add(t)

		with conn:
			if len(selected_tasks) > len(completed_tasks): # new task selected
				new_task = selected_tasks.difference(completed_tasks)
				for tasks in new_task:
						cur.execute(f"UPDATE {l_name} SET completed = ? WHERE tasks = ?", (1, tasks))

			elif len(selected_tasks) < len(completed_tasks): # previous task deselected
				new_task = completed_tasks.difference(selected_tasks)
				for tasks in new_task:
						cur.execute(f"UPDATE {l_name} SET completed = ? WHERE tasks = ?", (0, tasks))

			elif len(selected_tasks) == len(completed_tasks): # new task selected and previous task deselected
				if selected_tasks.difference(completed_tasks) != set() and completed_tasks.difference(selected_tasks) != set():
					new_task = selected_tasks.difference(completed_tasks)
					for tasks in new_task:
						cur.execute(f"UPDATE {l_name} SET completed = ? WHERE tasks = ?", (1, tasks))

					new_task = completed_tasks.difference(selected_tasks)
					for tasks in new_task:
						cur.execute(f"UPDATE {l_name} SET completed = ? WHERE tasks = ?", (0, tasks))	

			else: # selecting tasks for first time
				for tasks in task:
					cur.execute(f"UPDATE {l_name} SET completed = ? WHERE tasks = ?", (1, tasks))

	def delete(self, l_name): # deletes the selected table
		with conn:
			cur.execute(f"DROP TABLE {l_name}"

def get_tables(): # returns a list of strings of tables in database
	result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
	table_names = sorted(list(zip(*result))[0])

	return table_names

def get_rows(l_name): # returns a list of strings of rows in database
	result = cur.execute(f"SELECT * FROM {l_name}").fetchall()
	lst = []

	for tasks in result:
		lst.append(tasks)

	return lst

if __name__ == "__main__":
	conn.commit()
	conn.close()
