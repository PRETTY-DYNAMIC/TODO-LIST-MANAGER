
                                                 PROJECT DESCRIPTION
This project is a terminal based To-Do List Manager written in Python. It allows users to manage their tasks by adding, viewing, updating 
g and deleting tasks.Tasks are stored in a file so that they are saved even after the program closes.
 
                                             MEMBER 1 RESPONSIBILITIES
Member 1 implemented the core tasks creation anf file storage features of the application.

                                              FUNCTIONS IMPLEMENTED
1. LOAD TASKS
   This function loads tasks from the file when the program starts. It reads each file from the file and stores the tasks in a list of dictionaries.

2. SAVE_TASKS
   This function stores tasks in the task.txt file. Whenever the file is added and updated, this function writes the updated tasks back to the file.

3. ADD_TASK
   This function allows users to add a new task. When the user enters the task title, the program automatically assigns an ID and sets the task status to pending.

4.  VIEW_TASKS
   The function displays all the tasks in the program. Each tasks is shown with it's ID, status and title.

                                                 TECHNOLOGIES USED
. Python
. File Handling
. Lists and Dictionaries
. Loops and Functions

                                                 FILES USED IN PROJECT
. todo.py - contains main python program.
. tasks.txt - it stores tasks.
. README.md - project description.

                                                EXAMPLE OF TASK FORMAT
1 | Groceries | Pending

Each line contains:
. Task ID
. Task Title
. Task Status

                              
                                     To-Do List Manager – Member 2 Contribution


                                                Project Description
This project is a terminal-based To-Do List Manager written in Python.  
It allows users to manage their daily tasks by adding, viewing, completing, deleting, and filtering tasks.  
Tasks are saved in a file (`tasks.txt`) so they persist even after the program closes.


                                             Member 2 Responsibilities
Member 2 implemented the **task management and user interaction features** of the application.


                                             Functions Implemented

1. mark_done(tasks) 
Allows the user to mark a task as completed. Updates the task’s status to `done`.

2. delete_task(tasks)  
Allows the user to delete a task by its ID. Renumbers the remaining tasks automatically.

3. filter_tasks(tasks)  
Allows the user to filter tasks by status (`pending` or `done`) to view specific tasks.

4. main() 
The main menu system of the program.  
- Provides a terminal menu with all options: Add, View, Mark Done, Delete, Filter, Exit  
- Handles user input and calls the appropriate functions  
- Saves tasks to `tasks.txt` when exiting the program


                                       Importing Member 1 Functions
Member 2’s code uses Member 1’s functions from `member1_todo.py`:
-from member1_todo import load_tasks, save_tasks, add_task, view_tasks
