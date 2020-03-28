import tkinter as tk
from tkinter import ttk
import numpy as np
import random
from threading import Thread
import os
from cefpython3 import cefpython as cef
from pddl import PDDL_Parser
from planner import Planner
import datetime
import plotly.figure_factory as ff
from plotly.offline import plot
from tkinter import *
from PIL import ImageTk, Image
from action_ur5_trans import *

resources = ['Robot', 'Human']


class App(object):
    def __init__(self, master, path):
        self.nodes = dict()
        frame = tk.Frame(master, width=250, height=450)
        frame.grid_propagate(False)
        self.tree = ttk.Treeview(frame, selectmode="extended")
        ysb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Project tree', anchor='w')

        self.tree.grid()
        ysb.grid(row=0, column=1, sticky='ns')
        xsb.grid(row=1, column=0, sticky='ew')
        frame.grid()

        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))


def Validation(S):
    if S in ['1', '2', '3', '4', '5', '6']:
        return True
    root.bell()     # .bell() plays that ding sound telling you there was invalid input
    return False

plan_act = []
def mainCallBack(block_n, domain_c):
    global plan_act
    start_time = time.time()
    outputtext.delete(1.0, tk.END)  # clear the output text text widget
    print(block_n, domain_c)
    if domain_c == 'Blocks-world':
        domain = 'plan_files/domain_bw.pddl'
        if block_n == '2':
            problem = 'plan_files/p2_bw.pddl'
        elif block_n == '3':
            problem = 'plan_files/p3_bw.pddl'
        elif block_n == '4':
            problem = 'plan_files/p4_1_bw.pddl'
        elif block_n == '5':
            problem = 'plan_files/p5_2_bw.pddl'
        elif block_n == '6':
            problem = 'plan_files/p6_bw.pddl'    # 2 minutes
            outputtext.insert(tk.END, 'This one might take some time...' + '\n')
        else:
            entNumRo.configure(state='normal')
            cbDomain.configure(state='readonly')
            outputtext.delete(1.0, tk.END)  # clear the output text text widget
            outputtext.insert(tk.END, 'Please insert a number of blocks!' + '\n')
            raise Exception
    elif domain_c == 'BoxBall-world':
        domain = 'plan_files/domain_gripper.pddl'
        if block_n == '2':
            problem = 'plan_files/p2_gripper.pddl'
        elif block_n == '3':
            problem = 'plan_files/p3_gripper.pddl'
        elif block_n == '4':
            problem = 'plan_files/p4_gripper.pddl'
        elif block_n == '5':
            problem = 'plan_files/p5_gripper.pddl'  # 459 sec - 8min
            outputtext.insert(tk.END, 'This one might take some time...' + '\n')
        else:
            entNumRo.configure(state='normal')
            cbDomain.configure(state='readonly')
            outputtext.delete(1.0, tk.END)  # clear the output text text widget
            outputtext.insert(tk.END, 'Please insert a number of blocks!' + '\n')
            raise Exception
    elif domain_c == 'Tower-world':
        domain = 'plan_files/domain_hanoi.pddl'
        if block_n == '2':
            problem = 'plan_files/p2_hanoi.pddl'
        elif block_n == '3':
            problem = 'plan_files/p3_hanoi.pddl'
        elif block_n == '4':
            problem = 'plan_files/p4_hanoi.pddl'
        elif block_n == '5':
            problem = 'plan_files/p5_hanoi.pddl'        # 3 seconds
        elif block_n == '6':
            problem = 'plan_files/p6_hanoi.pddl'        # 1 minute
            outputtext.insert(tk.END, 'This one might take some time...' + '\n')
        else:
            entNumRo.configure(state='normal')
            cbDomain.configure(state='readonly')
            outputtext.delete(1.0, tk.END)  # clear the output text text widget
            outputtext.insert(tk.END, 'Please insert a number of blocks!' + '\n')
            raise Exception
    else:
        entNumRo.configure(state='normal')
        cbDomain.configure(state='readonly')
        outputtext.delete(1.0, tk.END)  # clear the output text text widget
        outputtext.insert(tk.END, 'Please insert the domain!' + '\n')
        raise Exception
    plan_act = []
    planner = Planner()
    outputtext.insert(tk.END, 'Getting the solution!' + '\n')
    plan = planner.solve(domain, problem)

    print('Time taken: ' + str(time.time() - start_time) + 's')
    if plan:
        df = []
        start_act = [datetime.datetime(2020, 1, 28, 12, 45, 00)]
        a = []
        for act in plan:
            a.append(((str(act).split('\n'))[0]).split()[1])
            a.append(((str(act).split('\n'))[1]).split(':')[1])
        print('Length of plan:', len(a))
        aa= []
        for k in range(int(len(a)/2)):
            ai = a[k*2]+a[(k*2)+1]
            aa.append(ai)
        if aa[0][0] == 'p':
            time_act = (np.random.normal(1.044, 0.317))
        elif aa[0][0] == 'd':
            time_act = (np.random.normal(1.042, 0.502))
        elif aa[0][0] == 'm':
            time_act = (np.random.normal(2.036, 0.548))
        elif aa[0][0] == 'u':
            time_act =  (np.random.normal(0.504, 0.048))
        elif aa[0][0] == 's':
            time_act = 0.802
        else:
            time_act = 2
        end_act = [start_act[0] + datetime.timedelta(seconds=(time_act*60))]
        test = random.randrange(len(aa))
        for i in range(len(aa)):
            name_act = (aa[i])
            if name_act[0] == 'p':
                time_act2 = (np.random.normal(1.044, 0.317))
            elif name_act[0] == 'd':
                time_act2 = (np.random.normal(1.042, 0.502))
            elif name_act[0] == 'm':
                time_act2 = (np.random.normal(2.036, 0.548))
            elif name_act[0] == 'u':
                time_act2 = (np.random.normal(0.504, 0.048))
            elif name_act[0] == 's':
                time_act2 = 0.802
            else:
                time_act2 = 2
            start_act.append(end_act[i])
            end_act.append(start_act[i + 1] + datetime.timedelta(seconds=(time_act2*60)))
            count=0
            if i == test or i == int(test/2) or i == int(test*2):
                count = count+1
                end_act[i] = end_act[i] + datetime.timedelta(seconds=0.336)
                df.append(dict(Task=name_act, Start=str(start_act[i]), Finish=str(end_act[i]), Resource=resources[1]))
            else:
                if count == 1:
                    start_act[i]=start_act[i]+datetime.timedelta(seconds=0.336)
                    df.append(
                        dict(Task=name_act, Start=str(start_act[i]), Finish=str(end_act[i]), Resource=resources[0]))
                else:
                    df.append(dict(Task=name_act, Start=str(start_act[i]), Finish=str(end_act[i]), Resource=resources[0]))
            plan_act.append(name_act)
        r = lambda: random.randint(0, 255)
        colors = ['#%02X%02X%02X' % (r(), r(), r())]
        for i in range(1, len(aa) + 1):
            colors.append('#%02X%02X%02X' % (r(), r(), r()))
        fig = ff.create_gantt(df, index_col='Resource', colors=colors, title='Daily Schedule',
                              show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
        plot(fig, filename='other/%s%s.html' % (domain_c, block_n), auto_open=False)
        outputtext.delete(1.0, tk.END)  # clear the output text text widget
        for x in plan_act:
            outputtext.insert(tk.END, x + '\n')
        outputtext.insert(tk.END, 'Total Task Time: ' + str(end_act[len(aa)]-start_act[0]) + '\n')
        entNumRo.configure(state='normal')
        cbDomain.configure(state='readonly')
    else:
        print('No plan was found')
        entNumRo.configure(state='normal')
        cbDomain.configure(state='readonly')


def butCallBack(block_n, domain_c):
    Thread(target=mainCallBack, args=(block_n, domain_c, )).start()


def okCallBack():
    global block_n
    block_n2 = entNumRo.get()
    block_n = block_n2
    entNumRo.configure(state='disabled')


def domCallBack(event):
    global domain_c
    domain_c = cbDomain.get()
    cbDomain.configure(state='disabled')


def open_link(block_n, domain_c):
    print(block_n, domain_c)
    root.destroy()
    url = 'file:///C:/Users/Liliana/PycharmProjects/mams/other/%s%s.html' % (domain_c, block_n)
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url=url,
                          window_title=url)
    cef.MessageLoop()
    main()

def link_sim(plan):
    c = Path_planner()
    traj = c.generate_traj(plan)
    count = 0
    if block_n == 0 or domain_c == 0:
        outputtext.delete(1.0, tk.END)  # clear the output text text widget
        outputtext.insert(tk.END, 'Please generate a Task plan first!' + '\n')
    else:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((c.host, c.port))
            time.sleep(0.5)
        except socket.error:
            outputtext.delete(1.0, tk.END)  # clear the output text text widget
            outputtext.insert(tk.END,
                              'Could not connect to simulator! Please initiate the URSim simulator and enable the robot' + '\n')
            count = count + 1
        if count == 0:
            path_length = len(traj)
            outputtext.insert(tk.END,"Initiating generated plan" + '\n')
            for i in range(path_length):
                s.send(traj[i].encode())
                (print('sent 1'))
                time.sleep(3)

block_n = 0
domain_c = 0
def main():
    global block_n, domain_c
    global root, cbDomain, entNumRo, outputtext
    root = tk.Tk()
    root.title("GUI")
    vcmd = (root.register(Validation), '%S')
    cbDomain = ttk.Combobox(root, state='readonly', values=["Blocks-world", "BoxBall-world", "Tower-world"])
    labTask = ttk.Label(root, text='Task Domain:')
    cbPolicy = ttk.Combobox(root, state='readonly', values=["Max Production", "Min Costs"])
    labPolicy = ttk.Label(root, text='Policy to apply:')
    labNumRo = ttk.Label(root, text='Nº of blocks (2 to 6):')
    entNumRo = tk.Entry(root, validate='key', vcmd=vcmd)
    okBut = tk.Button(root, text='ok', command=okCallBack)
    runBut = tk.Button(root, text='Get Solution!', font='Helvetica 12 bold',
                       command=lambda: butCallBack(block_n, domain_c,))
    outputtext = tk.Text(root, width=40, height=15)
    newBut = tk.Button(root, text="Show Gantt chart for Solution!", command=lambda: open_link(block_n, domain_c,))
    simBut = tk.Button(root, text="Generate UR5 trajectory", command=lambda: link_sim(plan_act,))
    img = ImageTk.PhotoImage(Image.open("bwp.png"))
    panel = Label(root, image=img)
    panel.grid(row=0, rowspan=9, column=5)
    cbDomain.grid(row=1, column=2)
    cbDomain.bind("<<ComboboxSelected>>", domCallBack)
    labTask.grid(row=1, column=1, padx=20, pady=5)
    labPolicy.grid(row=2, column=1, padx=20, pady=5)
    cbPolicy.grid(row=2, column=2)
    labNumRo.grid(row=3, column=1, padx=10)
    okBut.grid(row=3, column=3, ipadx=10)
    entNumRo.grid(row=3, column=2, ipadx=10, ipady=2)
    runBut.grid(row=4, column=1, columnspan=3, pady=8, padx=8)
    outputtext.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    newBut.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
    simBut.grid(row=6, column=1, columnspan=3, padx=10, pady=10)
    root.mainloop()
    cef.Shutdown()
    root.quit()


main()
