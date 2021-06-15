from datetime import date
import gantt
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM

def mk_gantt(gantt_tasks):
    a = gantt.Task(name=gantt_tasks, start=date(2021, 1, 27), duration=7,  color="#a3ddcb")
    return a
    # # Createa a project
    # return task_project
    # project_1 = gantt.Project(name='Project 1')
    # # Add tasks to that project
    # for task in task_project:
    #     project_1.add_task(task)
    # return project_1
def create_gantt(task_project):
    gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")
    mod_not_worked_days=[] #쉬는 날 없게끔 설정해주었다.
    gantt.define_not_worked_days(mod_not_worked_days)
    project_1 = gantt.Project(name='Project 1')
    # Add tasks to that project
    for task in task_project:
        project_1.add_task(task)
    project_1.make_svg_for_tasks(
                        filename='./static/Project_gantt.svg', 
                        today=date(2021, 1, 27), 
                        start=date(2021,1, 20),
                        end=date(2021, 4, 1)
                        )
    # drawing = svg2rlg('./static/Project_gantt.svg')
    # renderPM.drawToFile(drawing,'./static/Project_gantt.png',fmt='PNG')