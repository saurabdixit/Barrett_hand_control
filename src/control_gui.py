#!/usr/bin/env python
from Tkinter import *
import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np

def run():
   root = Tk()
   app = Application(master=root)
   #app.mainloop()
   root.destroy()


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.pub = rospy.Publisher('control_slider_values', Float32MultiArray, queue_size = 1)
        rospy.init_node('Publish_values', anonymous=True)
        self.grid(row=0,column=0,sticky=N+S+E+W)
        Grid.rowconfigure(master,0,weight=1)
        Grid.columnconfigure(master,0,weight=1)
        self.CreateWidgets()
        self.flag = 0
        self.Publish_values()

    def CreateWidgets(self):
        for rows in xrange(28):
            Grid.rowconfigure(self, rows, weight=1)
        for columns in xrange(1):
            Grid.columnconfigure(self, columns, weight=1)
        self.master.title("barrett hand control")
        self.master.slider_1 = Scale(self, from_=-2.6, to=2.6, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_1.grid(row = 0, column = 0,sticky=N+S+E+W)
        self.master.label_1 = Label(self, text = "Base yaw Joint")       
        self.master.label_1.grid(row=1, column = 0, sticky=N+S+E+W)
        self.master.slider_2 = Scale(self, from_=-1.985, to=1.985, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_2.grid(row = 2, column = 0,sticky=N+S+E+W)
        self.master.label_2 = Label(self, text = "Shoulder pitch joint")       
        self.master.label_2.grid(row=3, column = 0, sticky=N+S+E+W)
        self.master.slider_3 = Scale(self, from_=-2.8, to=2.8, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_3.grid(row = 4, column = 0,sticky=N+S+E+W)
        self.master.label_3 = Label(self, text = "Shoulder yaw joint")
        self.master.label_3.grid(row=5, column = 0, sticky=N+S+E+W)
        self.master.slider_4 = Scale(self, from_=-0.9, to=3.1416, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_4.grid(row = 6, column = 0,sticky=N+S+E+W)
        self.master.label_4 = Label(self, text = "Elbow pitch joint")
        self.master.label_4.grid(row=7, column = 0, sticky=N+S+E+W)
        self.master.slider_5 = Scale(self, from_=-4.55, to=1.25, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_5.grid(row = 8, column = 0,sticky=N+S+E+W)
        self.master.label_5 = Label(self, text = "Wrist yaw joint")
        self.master.label_5.grid(row=9, column = 0, sticky=N+S+E+W)
        self.master.slider_6 = Scale(self, from_=-1.5707, to=1.5707, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_6.grid(row = 10, column = 0,sticky=N+S+E+W)
        self.master.label_6 = Label(self, text = "Wrist pitch joint")
        self.master.label_6.grid(row=11, column = 0, sticky=N+S+E+W)
        self.master.slider_7 = Scale(self, from_=-3, to=3, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_7.grid(row = 12, column = 0,sticky=N+S+E+W)
        self.master.label_7 = Label(self, text = "Palm yaw joint")
        self.master.label_7.grid(row=13, column = 0, sticky=N+S+E+W)
        self.master.slider_8 = Scale(self, from_=0, to=3.1416, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_9 = Scale(self, from_=0, to=3.1416, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_10 = Scale(self, from_=0, to=3.1416, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_10.grid(row = 14, column = 0,sticky=N+S+E+W)
        self.master.label_10 = Label(self, text = "Fingers spread")
        self.master.label_10.grid(row=15, column = 0, sticky=N+S+E+W)
        self.master.slider_11 = Scale(self, from_=0, to=2.4434, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_11.grid(row = 16, column = 0,sticky=N+S+E+W)
        self.master.label_11 = Label(self, text = "Finger 1: Medial joint")
        self.master.label_11.grid(row=17, column = 0, sticky=N+S+E+W)
        self.master.slider_12 = Scale(self, from_=0, to=0.837, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_12.grid(row = 18, column = 0,sticky=N+S+E+W)
        self.master.label_12 = Label(self, text = "Finger 1: Distal Joint")
        self.master.label_12.grid(row=19, column = 0, sticky=N+S+E+W)
        self.master.slider_14 = Scale(self, from_=0, to=2.4434, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_14.grid(row = 20, column = 0,sticky=N+S+E+W)
        self.master.label_14 = Label(self, text = "Finger 2: Medial joint")
        self.master.label_14.grid(row=21, column = 0, sticky=N+S+E+W)
        self.master.slider_15 = Scale(self, from_=0, to=0.837, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_15.grid(row = 22, column = 0,sticky=N+S+E+W)
        self.master.label_15 = Label(self, text = "Finger 2: Distal joint")
        self.master.label_15.grid(row=23, column = 0, sticky=N+S+E+W)
        self.master.slider_16 = Scale(self, from_=0, to=2.4434, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_16.grid(row = 24, column = 0,sticky=N+S+E+W)
        self.master.label_16 = Label(self, text = "Finger 3: Medial joint")
        self.master.label_16.grid(row=25, column = 0, sticky=N+S+E+W)
        self.master.slider_17 = Scale(self, from_=0, to=0.837, resolution=0.001,orient = HORIZONTAL) 
        self.master.slider_17.grid(row = 26, column = 0,sticky=N+S+E+W)
        self.master.label_17 = Label(self, text = "Finger 3: Distal joint")
        self.master.label_17.grid(row=27, column = 0, sticky=N+S+E+W)
        self.master.button = Button(self, text="click to move spare hand with arm other wise double click to lock hand at single position", command = self.toggle_bit)
        self.master.button.grid(row = 28, column = 0,sticky = N+S+E+W)
# Note: Slider 8, 9 and 13 are removed from grid deliberately because 8 and 9 doesn't have any effect on the wam and 13 is for finger spread so we have combined the spread of each finger as robot doesn't allow you to do that
    def toggle_bit(self):
        if self.flag==0:
            self.flag = 1
        else:
            self.flag = 0
    def Publish_values(self):
        try:
            while not rospy.is_shutdown():
                vector = [self.master.slider_1.get(),self.master.slider_2.get(),self.master.slider_3.get(),self.master.slider_4.get(),self.master.slider_5.get(),self.master.slider_6.get(),self.master.slider_7.get(),self.master.slider_8.get(),self.master.slider_9.get(),self.master.slider_10.get(),self.master.slider_11.get(),self.master.slider_12.get(),self.master.slider_10.get(),self.master.slider_14.get(),self.master.slider_15.get(),self.master.slider_16.get(),self.master.slider_17.get(),self.flag]
                self.master.pub.publish(data=vector)
                self.update()

        except KeyboardInterrupt, e:
            print e

if __name__== '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass


