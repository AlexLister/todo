import web

TASKS = ["Learn to create templates", "Learn to populate them"]



def render_tasklist():

    render = web.template.render('templates/')
    return render.tasklist(TASKS)



if __name__ == "__main__":

    file = open("tasklist.html", "w")
    file.write(str(render_tasklist()))
    file.close()

