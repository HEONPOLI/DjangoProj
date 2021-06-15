from datetime import date
import gantt
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Change font default

gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")
#https://towardsdatascience.com/visualize-your-teams-projects-using-python-gantt-chart-5a1c1c98ea35
# Create 2 employees
# Ben = gantt.Resource("Ben")
# Alex = gantt.Resource("Alex")

task1_project1 = gantt.Task(name='task1', start=date(2021, 1, 27), duration=13,  color="#a3ddcb")
task2_project1 = gantt.Task(name='task2', start=date(2021, 2, 10), duration=8,  color="#a3ddcb")
task3_project1 = gantt.Task(name='task3', start=date(2021, 2, 19), duration=10,  color="#a3ddcb")
task4_project1 = gantt.Task(name='task4', start=date(2021, 3, 1), duration=12, color="#a3ddcb")

# Createa a project
project_1 = gantt.Project(name='Project 1')

# Add tasks to that project
for task in [task1_project1, task2_project1, task3_project1, task4_project1]:
    project_1.add_task(task)

gantt.add_vacations(start_date=date(2021, 3, 15), end_date= date(2021,3,20))


project_1.make_svg_for_tasks(
                      filename='./todolist/Project_1.svg', 
                      today=date(2021, 1, 27), 
                      start=date(2021,1, 20),
                      end=date(2021, 4, 1)
                     )
drawing = svg2rlg('./todolist/Project_1.svg')
renderPM.drawToFile(drawing,'./todolist/Project_1.png',fmt='PNG')