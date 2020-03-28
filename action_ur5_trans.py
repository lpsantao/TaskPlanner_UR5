# Echo client program
import socket
import time
import sys

positions_htower = {"d1": [0.10, 0.20, 0.6, 2.22, -2.22, 0.00], "d2": [0.10, 0.20, 0.5, 2.22, -2.22, 0.00],
                    "d3": [0.10, 0.20, 0.4, 2.22, -2.22, 0.00], "d4": [0.10, 0.20, 0.3, 2.22, -2.22, 0.00],
                    "d5": [0.10, 0.20, 0.2, 2.22, -2.22, 0.00], "drop": [0.10, 0.1, 0.2, 2.22, -2.22, 0.00],        # all disks in peg1
                    "peg1": [0.10, 0.20, 0.2, 2.22, -2.22, 0.00], "peg2": [0.10, 0.40, 0.2, 2.22, -2.22, 0.00],
                    "peg3": [0.10, 0.60, 0.2, 2.22, -2.22, 0.00]}
positions_blocks = {"a": [0.00, 0.3, 0.2, 2.22, -2.22, 0.00], "b": [0.50, 0.30, 0.2, 2.22, -2.22, 0.00],
                    "c": [0.2, 0.2, 0.2, 2.22, -2.22, 0.00], "d": [0.4, 0.2, 0.2, 2.22, -2.22, 0.00],
                    "e": [0.4, 0.5, 0.2, 2.22, -2.22, 0.00], "drop": [0.10, 0.1, 0.2, 2.22, -2.22, 0.00]}
positions_gripper = {"a": [0.20, 0.3, 0.2, 2.22, -2.22, 0.00], "b": [0.40, 0.3, 0.2, 2.22, -2.22, 0.00],
                     "c": [0.10, 0.3, 0.2, 2.22, -2.22, 0.00], "d": [0.30, 0.4, 0.2, 2.22, -2.22, 0.00],
                     "e": [0.00, 0.5, 0.2, 2.22, -2.22, 0.00],
                     "boxa": [0.00, 0.3, 0.2, 2.22, -2.22, 0.00], "boxb": [0.20, 0.60, 0.2, 2.22, -2.22, 0.00]}

class Path_planner:
    def __init__(self):
        self.host = "192.168.238.129"  # The remote host
        self.port = 30003  # The same port as used by the server

    def get_positions(self, block_n, domain_c):
        if domain_c == 'Blocks_world':
            if block_n == 2:
                positions = {"a": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "b": [0.50, 0.30, 0.4, 2.22, -2.22, 0.00]}
            elif block_n == 3:
                positions = {"a": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "b": [0.50, 0.30, 0.4, 2.22, -2.22, 0.00],
                             "c": [0.50, 0.30, 0.6, 2.22, -2.22, 0.00]}
            elif block_n == 4:
                positions = {"a": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "b": [0.50, 0.30, 0.4, 2.22, -2.22, 0.00],
                             "c": [0.00, 0.50, 0.4, 2.22, -2.22, 0.00], "d": [0.20, 0.30, 0.4, 2.22, -2.22, 0.00]}
            elif block_n == 5:
                positions = {"a":  [0.20, 0.30, 0.6, 2.22, -2.22, 0.00], "b":  [0.20, 0.30, 0.7, 2.22, -2.22, 0.00],
                             "c": [0.00, 0.50, 0.4, 2.22, -2.22, 0.00], "d": [0.20, 0.30, 0.4, 2.22, -2.22, 0.00],
                             "e": [0.20, 0.50, 0.4, 2.22, -2.22, 0.00]}
        elif domain_c == 'Gripper-world':
            if block_n == 2:
                positions = {"ball1": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball2": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                             "boxa": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "boxb": [0.20, 0.60, 0.4, 2.22, -2.22, 0.00]}
            elif block_n == 3:
                positions = {"ball1": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball2": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "ball3": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "boxa": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "boxb": [0.20, 0.60, 0.4, 2.22, -2.22, 0.00]}
            elif block_n == 4:
                positions = {"ball1": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball2": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "ball3": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball4": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "boxa": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "boxb": [0.20, 0.60, 0.4, 2.22, -2.22, 0.00]}
            elif block_n == 5:
                positions = {"ball1": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball2": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "ball3": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "ball4": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "ball5": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00],
                            "boxa": [0.00, 0.3, 0.4, 2.22, -2.22, 0.00], "boxb": [0.20, 0.60, 0.4, 2.22, -2.22, 0.00]}
        elif domain_c == 'Tower-world':
            if block_n == 2:
                positions = {"d1": [0.10, 0.30, 0.3, 2.22, -2.22, 0.00], "d2": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00],
                             "peg1": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00], "peg2": [0.10, 0.40, 0.2, 2.22, -2.22, 0.00],
                             "peg3": [0.10, 0.60, 0.2, 2.22, -2.22, 0.00]}
            elif block_n == 3:
                positions = {"d1": [0.10, 0.30, 0.4, 2.22, -2.22, 0.00], "d2": [0.10, 0.30, 0.3, 2.22, -2.22, 0.00],
                             "d3": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00], "peg1": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00],
                             "peg2": [0.10, 0.40, 0.2, 2.22, -2.22, 0.00], "peg3": [0.10, 0.60, 0.2, 2.22, -2.22, 0.00]}
            elif block_n == 4:
                positions = {"d1": [0.10, 0.30, 0.5, 2.22, -2.22, 0.00], "d2": [0.10, 0.30, 0.4, 2.22, -2.22, 0.00],
                             "d3": [0.10, 0.30, 0.3, 2.22, -2.22, 0.00], "d4": [0.10, 0.3, 0.2, 2.22, -2.22, 0.00],
                             "peg1": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00],
                             "peg2": [0.10, 0.40, 0.2, 2.22, -2.22, 0.00], "peg3": [0.10, 0.60, 0.2, 2.22, -2.22, 0.00]}
            elif block_n == 5:
                positions = {"d1": [0.10, 0.30, 0.6, 2.22, -2.22, 0.00], "d2": [0.10, 0.30, 0.5, 2.22, -2.22, 0.00],
                             "d3": [0.10, 0.30, 0.4, 2.22, -2.22, 0.00], "d4": [0.10, 0.30, 0.3, 2.22, -2.22, 0.00],
                             "d5": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00], "peg1": [0.10, 0.30, 0.2, 2.22, -2.22, 0.00],
                             "peg2": [0.10, 0.40, 0.2, 2.22, -2.22, 0.00], "peg3": [0.10, 0.60, 0.2, 2.22, -2.22, 0.00]}

        return positions

    # plan = ["unstack ('c', 'b')", "drop ('c',)", "pick ('b',)", "stack ('b', 'c')", "pick ('a',)", "stack ('a', 'b')"]
    # plan2 = ["pick ('b', 'boxa', 'right')", "move ('boxa', 'boxb')", "drop ('b', 'boxb', 'right')", "move ('boxb', 'boxa')", "pick ('a', 'boxa', 'right')", "move ('boxa', 'boxb')", "drop ('a', 'boxb', 'right')"]

    def generate_traj(self, plan2):
        poses = []
        print(len(plan2))
        for k in range(len(plan2)):
            a = plan2[k].split()
            operation = a[0]
            if operation == 'pick':
                if len(a) <=2:
                    goal_pose = a[1][2]
                    coordinates = positions_blocks.get(goal_pose)
                else:
                    goal_pose = a[1][2]
                    coordinates = positions_gripper.get(goal_pose)
            elif operation == 'stack':
                goal_pose = a[2][1]
                initial_pose = a[1][2]
                coordinates = positions_blocks.get(goal_pose)
                updated_pose = {initial_pose: coordinates}
                positions_blocks.update(updated_pose)
            elif operation == 'unstack':
                goal_pose = a[1][2]
                coordinates = positions_blocks.get(goal_pose)
            elif operation == 'drop':
                if len(a) <= 2:
                    goal_pose = a[1][2]
                    coordinates = positions_blocks.get('drop')
                    updated_pose = {goal_pose: coordinates}
                    positions_blocks.update(updated_pose)
                else:
                    goal_pose = a[2][1:-2]
                    initial_pose = a[1][2]
                    coordinates = positions_gripper.get(goal_pose)
                    updated_pose = {initial_pose: coordinates}
                    positions_gripper.update(updated_pose)
            elif operation == 'move':
                if len(a) > 3:
                    goal_pose = a[3][1:-2]
                    initial_pose = a[1][2:-2]
                    coordinates = positions_htower.get(goal_pose)
                    updated_pose = {initial_pose: coordinates}
                    positions_htower.update(updated_pose)
            else:
                raise IndexError
            poses.append(coordinates)
        traj=[]
        for i in range(len(poses)):
            traj2 = ("movej(p%s, a=%s, v=%s)" % (poses[i], 3.0, 0.9) + "\n")
            traj.append(traj2)
            print(traj2)
        return traj

    def send_path(self, traj):
        count = 0
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            time.sleep(0.5)
        except socket.error:
            count = count + 1
        if count == 0:
            path_length = len(traj)
            print("Initiating generated plan" + '\n')
            for i in range(path_length):
                s.send(traj[i].encode())
                (print('sent 1'))
                time.sleep(3)

#plan3 = ["move ('d1', 'd2', 'peg3')", "move ('d2', 'd3', 'peg2')", "move ('d1', 'peg3', 'd2')", "move ('d3', 'peg1', 'peg3')", "move ('d1', 'd2', 'peg1')", "move ('d2', 'peg2', 'd3')", "move ('d1', 'peg1', 'd2')"]
#c = Path_planner()
#traj = c.generate_traj(plan3)
#print(traj)
#c.send_path(traj)
#posi = c.get_positions(5, 'Tower-world')
#traj = c.generate_traj(posi)
#c.send_path(traj)
