tasks = []
nextID = 1

def addTask(name):
    global nextID

    task = {
        "id": nextID,
        "name": name,
        "status": "pending"
    }

    tasks.append(task)
    nextID += 1

    print("Task added successfuly.")

def showTask():
    if not tasks:
        print("There is no task here")
        return

    for x in tasks:
        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Status: {x['status']}")
        print("-" *30)

def findTask(id):
    for x in tasks:
        if x['id'] == id:
            return x

    return None

def deleteTask(id):
    if not tasks:
        print("There is no task here")
        return

    for x in tasks:
        if x['id'] == id:
            tasks.remove(x)
            print(f"This task deleted = {x['id']}")
            return
        
        else:
            print("id not correct")

def updateTask(id, name, status):
    if not tasks:
        print("There is no task here")
        return

    statuss = ['Pending', 'Complated']
    try:
        for x in tasks:
            if x['id'] == id:
                newName = str(input("Enter new name; ")).strip()
                if newName.lower() != name.lower():
                    x['name'] = newName
                elif newName.lower() == name.lower():
                    print("New name same with current name.")
                    return
                
                print("""
                
                Avaible status pick one
                
                1. Pending
                2. Complated
                
                """)

                newStatus = str(input("Enter new status; ")).strip()

                if newStatus.lower() != status.lower() and newStatus in statuss:
                    x['status'] = status
                elif newStatus.lower() == status.lower():
                    print("New stats same with current status.")
                    return
                
    except Exception as e:
        print("Error found; ", e)
            


    

        