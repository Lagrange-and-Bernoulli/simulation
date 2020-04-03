import matplotlib.pyplot as plt
import numpy as np

MAX_STEP = 50
all_mode = ['fifo', 'filo', 'mode3']
mode = all_mode[0]

list = [(0, 0)]
cnt = 0
max_x, max_y = (0,0)

def print_crr_state(list):
    x = [a for (a, b) in list]
    y = [b for (a, b) in list]
    plt.scatter(x, y, s=100)
    plt.plot([0, 2], [2, 0], color='r')

    plt.grid(True)  # 增加网格，也可以改变网格的线形，颜色
    plt.grid(axis='both')
    plt.grid(color='b')
    plt.grid(linewidth='1')

    plt.axis([0, max(max_x, max_y) +1 , 0, max(max_x, max_y) + 1])
    plt.xticks(np.arange(0, max(max_x, max_y) + 1, 1))
    plt.yticks(np.arange(0, max(max_x, max_y) + 1, 1))

    plt.title(mode+'-%d steps' % cnt)
    plt.show()
    plt.savefig(mode+'-%d.png' % cnt)

# class scheduler():
#     def __init__(self):
#         pass
#     def get_candidate(self):
#         pass
#     def add_point(self):
#         pass

def get_candidate(list):
    if mode == 'fifo':
        candidate = list[0]
        list.pop(0)
    elif mode == 'filo':
        candidate = list[-1]
        list.pop(-1)
    elif mode == 'mode3':
        if (-1)**cnt == -1:
            candidate = list[0]
            list.pop(0)
        else:
            candidate = list[-1]
            list.pop(-1)
    return candidate


while cnt < MAX_STEP and {(0,0), (0,1), (0,2), (1,0), (1,1), (2,0)}.intersection(set(list)) != set([]):
    cnt += 1
    (x,y) = get_candidate(list)
    if ((x+1, y) not in list) and ((x, y+1) not in list):
        list.append((x+1, y))
        list.append((x, y+1))
        max_x = max(max_x, x+1)
        max_y = max(max_y, y+1)
        print('move (%d, %d)' % (x,y))
    else:
        list.append((x,y))
    # print(list)
    # print_crr_state(list)

print(cnt)
print_crr_state(list)
