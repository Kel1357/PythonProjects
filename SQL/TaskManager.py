import pymysql
import matplotlib.pyplot as plt
from datetime import datetime
def add_data():
    id=int(input("Enter the Task ID:"))
    description=input("Enter the Task Description:")
    category=input("Enter the Category (College, Work, Personal,etc.):")
    priority=input("Enter the Priority (1=Lowest to 5=Highest):")
    deadline=input("Enter the Deadline (DD-MM-YYYY):")
    try:
        cur=cn.cursor()
        sql="insert into taskmanager values("+str(id)+",'"+description+"','"+category+"',"+str(priority)+",'"+deadline+"','Pending')"
        cur.execute(sql)
        n=cur.rowcount
        if n>0:
            print("Data Saved Successfully")
            task_history("Added", id, f"Description: {description}, Deadline: {deadline}")
        else:
            print("Data Not Saved")
    except pymysql.err.IntegrityError:
        print(id,"Task Id Number Already Exists")
def show_data():
    sql="select * from taskmanager"
    cur=cn.cursor()
    cur.execute(sql)
    n=cur.rowcount
    print("Selected Record Count:",n)
    if n>0:
        data=cur.fetchall()
        print("Id\t Description\t\t Category\t  Priority\t Deadline\t\t Status")
        for d in data:
            print(d[0],"\t",d[1],"\t",d[2],"\t\t",d[3],"\t\t",d[4],"\t",d[5])
    else:
        print("No Records Found")
def next_task():
    sql="select * from taskmanager where status='Pending' order by priority desc, deadline asc limit 1"
    cur=cn.cursor()
    cur.execute(sql)
    d=cur.fetchone()
    if d:
        print("Next Recommended Task:", d[1], "| Category:", d[2], "| Priority:", d[3], "| Deadline:", d[4])
    else:
        print("No Pending Tasks Found")
def sort_by_deadline():
    sql="select * from taskmanager order by deadline asc"
    cur=cn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    for d in data:
        print(d)
def filter_tasks():
    try:
        print("\n--- FILTER TASKS ---")
        print("1. Filter by Category")
        print("2. Filter by Status (Pending/Completed)")
        choice=input("Enter your choice: ")
        cur=cn.cursor()
        if choice=="1":
            cat=input("Enter Category: ")
            sql="select * from taskmanager where category='" + cat + "'"
        elif choice=="2":
            status=input("Enter Status (Pending/Completed): ")
            sql="select * from taskmanager where status='" + status + "'"
        else:
            print("Invalid choice")
            return
        cur.execute(sql)
        data=cur.fetchall()
        if data:
            print("\n--- Filtered Tasks ---")
            for d in data:
                print(d)
        else:
            print("No tasks found for given filter.")
    except Exception as e:
        print("Error occurred:", e)
def dashboard():
    try:
        cur=cn.cursor()
        cur.execute("select count(*) from taskmanager")
        total=cur.fetchone()[0]
        cur.execute("select count(*) from taskmanager where status='Completed'")
        completed=cur.fetchone()[0]
        pending=total-completed
        cur.execute("select count(*) from taskmanager where status='Pending' and priority>=4")
        high_priority=cur.fetchone()[0]
        rate=(completed/total*100) if total>0 else 0
        print("---PRODUCTIVITY DASHBOARD---")
        print("Total Tasks:",total)
        print("Completed:",completed)
        print("Pending:",pending)
        print("High Priority Pending:",high_priority)
        print("Completion Rate:",round(rate, 1),"%")
        labels=['Completed','Pending','High Priority Pending']
        values=[completed,pending,high_priority]
        plt.figure()
        plt.bar(labels,values,color=['green','blue','red'])
        plt.title("Task Productivity Overview")
        plt.xlabel("Task Status")
        plt.ylabel("Number of Tasks")
        plt.show()
    except Exception as e:
        print("Error occurred:", e)
def status_completed():
    show_data()
    try:
        task_id=input("Enter Task ID to mark completed:")
        sql="update taskmanager set status='Completed' where id=" +task_id
        cur=cn.cursor()
        cur.execute(sql)
        if cur.rowcount>0:
            print("Task marked as Completed")
            task_history("Completed",task_id,"Marked as done")
        else:
            print("Task ID not found")
    except ValueError:
        print("Invalid input, Please enter a valid Task ID")
    except Exception as e:
        print("Error occurred:", e)
def edit_task():
    show_data()
    try:
        task_id=input("Enter Task ID to edit:")
        print("1. Edit Description\n2. Edit Category\n3. Edit Priority\n4. Edit Deadline")
        choice=int(input("Enter choice:"))
        cur=cn.cursor()
        if choice==1:
            new_description=input("Enter new description:")
            sql="update taskmanager set description='" +new_description+ "' where id=" +task_id
            details=f"New Description: {new_description}"
        elif choice==2:
            new_category=input("Enter new category:")
            sql="update taskmanager set category='" +new_category+ "' where id=" +task_id
            details=f"New Category: {new_category}"
        elif choice==3:
            new_priority=input("Enter new priority (1-5):")
            sql="update taskmanager set priority=" +new_priority+ " where id=" +task_id
            details=f"New Priority: {new_priority}"
        elif choice==4:
            new_deadline=input("Enter new deadline (DD-MM-YYYY):")
            sql="update taskmanager set deadline='" +new_deadline+ "' where id=" +task_id
            details=f"New Deadline: {new_deadline}"
        else:
            print("Invalid choice")
            return
        cur.execute(sql)
        if cur.rowcount>0:
            print("Task updated successfully")
            task_history("Edited",task_id,details)
        else:
            print("Task ID not found")
    except ValueError:
        print("Invalid input, Please enter numbers where required")
    except Exception as e:
        print("Error occurred:",e)
def delete_task():
    show_data()
    try:
        task_id=input("Enter Task ID to delete:")
        sql="delete from taskmanager where id=" +task_id
        cur=cn.cursor()
        cur.execute(sql)
        if cur.rowcount>0:
            print("Task deleted successfully")
            task_history("Deleted",task_id,"Removed from taskmanager")
        else:
            print("Task ID not found")
    except ValueError:
        print("Invalid input, Please enter a valid Task ID")
    except Exception as e:
        print("Error occurred:", e)
def search_task():
    key=input("Enter keyword:")
    sql="select * from taskmanager where description like '%" +key+ "%'"
    cur=cn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    for d in data:
        print(d)
def check_system():
    try:
        cur=cn.cursor()
        cur.execute("select id,description,deadline,status from taskmanager where status='Pending'")
        tasks=cur.fetchall()
        today=datetime.today().date()
        print("\n--- REMINDER SYSTEM (Next 7 Days) ---")
        found=False
        for t in tasks:
            try:
                deadline=datetime.strptime(t[2],"%d-%m-%Y").date()
                differ=(deadline.year-today.year)*365+(deadline.month-today.month)*30+(deadline.day-today.day)
                if 0<=differ<=7:
                    print("Task ID:",t[0],"|",t[1],"| Deadline:",t[2],"| Status:",t[3])
                    found=True
            except ValueError:
                continue
        if not found:
            print("No tasks due in the next 7 days.")
    except Exception as e:
        print("Error in reminder system:", e)
def task_history(action=None,task_id=None,details=""):
    if "history" not in task_history.__dict__:
        task_history.history=[]
    if action and task_id:
        ts=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry=f"Task ID: {task_id} | Action: {action} | Time: {ts} | Details: {details}"
        task_history.history.append(entry)
    print("\n--- TASK HISTORY LOG ---")
    if task_history.history:
        for h in task_history.history:
            print(h)
    else:
        print("No history available.")
if __name__=='__main__':
    cn=pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        db="task",
        passwd="12345678",
        autocommit=True
    )
    while True:
        print("\n---TASK MANAGER---")
        print("1. Add a New Task")
        print("2. Show all Tasks")
        print("3. What Should I do next (Heap Selection)?")
        print("4. View Tasks Sorted By Deadline")
        print("5. Filter Tasks")
        print("6. View Productivity Dashboard (Analytics)")
        print("7. Mark Task as Completed")
        print("8. Edit an Existing Task")
        print("9. Delete an Existing Task")
        print("10. Search Task by Name / Keyword")
        print("11. Check Incompleted Tasks This Week")
        print("12. Task History Log")
        print("0. Exit")
        try:
            n=int(input("Enter your choice:="))
            if n==1:
                add_data()
            elif n==2:
                show_data()
            elif n==3:
                next_task()
            elif n==4:
                sort_by_deadline()
            elif n==5:
                filter_tasks()
            elif n==6:
                dashboard()
            elif n==7:
                status_completed()
            elif n==8:
                edit_task()
            elif n==9:
                delete_task()
            elif n==10:
                search_task()
            elif n==11:
                check_system()
            elif n==12:
                task_history()
            elif n==0:
                print("Program Exited Successfully")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Value, Please Try Again")
