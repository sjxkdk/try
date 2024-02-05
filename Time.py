# 导入time库和tkinter库
import time
import tkinter as tk

# 创建窗口对象
window = tk.Tk()
window.title("专注时钟")

# 创建标签对象，用于显示时间
label = tk.Label(window, font=("Helvetica", 48), fg="black")
label.pack(pady=20)

# 创建按钮对象，用于开始和停止计时
start_button = tk.Button(window, text="开始", command=lambda: start_timer(25, 5))
start_button.pack(side=tk.LEFT, padx=10)
stop_button = tk.Button(window, text="停止", command=lambda: stop_timer())
stop_button.pack(side=tk.RIGHT, padx=10)

# 定义全局变量，用于控制计时器的状态
running = False
work_time = 0
break_time = 0

# 定义开始计时的函数，接受工作时间和休息时间作为参数
def start_timer(work, break_):
    global running, work_time, break_time
    # 如果计时器已经在运行，不做任何操作
    if running:
        return
    # 否则，设置计时器为运行状态，记录工作时间和休息时间
    running = True
    work_time = work * 60
    break_time = break_ * 60
    # 调用更新时间的函数
    update_time()

# 定义停止计时的函数
def stop_timer():
    global running
    # 如果计时器已经停止，不做任何操作
    if not running:
        return
    # 否则，设置计时器为停止状态，清空标签的文本
    running = False
    label.config(text="")

# 定义更新时间的函数
def update_time():
    global running, work_time, break_time
    # 如果计时器已经停止，不做任何操作
    if not running:
        return
    # 如果工作时间大于0，显示工作时间，并每秒减一
    if work_time > 0:
        mins, secs = divmod(work_time, 60)
        timer = "工作 {:02d}:{:02d}".format(mins, secs)
        label.config(text=timer, fg="black")
        work_time -= 1
        window.after(1000, update_time)
    # 如果工作时间等于0，且休息时间大于0，显示休息时间，并每秒减一
    elif break_time > 0:
        mins, secs = divmod(break_time, 60)
        timer = "休息 {:02d}:{:02d}".format(mins, secs)
        label.config(text=timer, fg="green")
        break_time -= 1
        window.after(1000, update_time)
    # 如果工作时间和休息时间都等于0，显示时间到，并停止计时
    else:
        label.config(text="时间到！", fg="red")
        running = False

# 进入消息循环
window.mainloop()
