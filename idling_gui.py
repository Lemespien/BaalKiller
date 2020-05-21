import time
import tkinter as tk
import baalKiller as bk
import idling_to_rule_the_gods as idle
import coordinates as c


# def store_cords():
#     cord_text.set(bk.get_cords())


LABELS = {}


# def create_label(parent, text):
#     label_text_var = tk.StringVar()
#     label_var = tk.Label(MASTER, height=1, width=30, textvariable=label_text_var)
#     label_text_var.set(text)
#     label_var.pack()
#     LABELS[parent] = label_text_var


def infinite_loop(apps, root):
    for app in apps:
        if isinstance(app, Demo1):
            for action in app.actions:
                app.labels[action.name].set("{}: {:.0f} seconds".format(action.name, action.timer.time_remaining()))
    root.after(1000, infinite_loop, apps, root)


class Demo1:
    def __init__(self, master, actions=-1):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labels = {}
        self.actions = actions
        if actions == -1:
            self.actions = idle.create_default_actions(c.DungeonCords(), c.CampaignCords())
        self.create_dungeons()
        self.frame.pack()

    def update_timers(self):
        for action in self.actions:
            self.labels[action.name].set("{}: {:.0f} seconds".format(action.name, action.timer.time_remaining()))

    def create_dungeons(self):
        for ia in self.actions:
            self.create_label(ia.name, "{}: {:.0f} seconds".format(ia.name, ia.timer.time_remaining()))

    def create_label(self, parent, text):
        label_text_var = tk.StringVar()
        label_var = tk.Label(self.frame, height=1, width=30, textvariable=label_text_var)
        label_text_var.set(text)
        label_var.pack()
        self.labels[parent] = label_text_var


class Demo2:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.frame = tk.Frame(self.master)
        self.button = tk.Button(self.frame, text="My First Button", width=25, command=self.store_cords)
        self.button.pack()
        self.cord_text_var = tk.StringVar()
        self.cord_label = tk.Label(self.frame, height=1, width=30, textvariable=self.cord_text_var)
        self.cord_text_var.set("HELLO WORLD")
        self.cord_label.pack()
        self.frame.pack()

    def store_cords(self):
        self.cord_text_var.set(bk.get_cords())


def main():
    root = tk.Tk()
    # app = Demo1(root)
    app_2 = Demo2(root)
    apps = [app_2]
    root.after(1000, infinite_loop, apps, root)
    root.mainloop()


if __name__ == '__main__':
    main()
