import tkinter as tk
class DiwaliLights:

    def _init_(self):
        #window
        self.window = tk.Tk()
        #canvas
        self.canvas = tk.Canvas(master=self.window, width = 600, height = 300 )
        #button
        self.bttn_lights = tk.Button(master=self.window, text = 'On', command = self.lights, bg = 'red')

        #bulbs
        bulb_width = 50
        bulb_height = 50
        bulb_x = 125
        bulb_y = 125
        self.bulbs = []
        for i in range(7):
            self.bulbs.append(self.canvas.create_oval(bulb_x, bulb_y, bulb_x+bulb_width, bulb_y + bulb_height, outline = 'black'))
            bulb_x = bulb_x + bulb_width

        #pack the widgets into the window
        self.bttn_lights.pack(side = tk.BOTTOM)
        self.canvas.pack(fill = tk.BOTH, expand = True)

        #render the window, keep it alive until closed (destroyed)
        self.current_color =0
        self.blink_count = 3
        self.power = 'Off'
        self.blink_bulbs = False
        self.window.after(1000, self.blink)
        self.window.mainloop()

    def blink(self):
        if self.power == 'On':
            if self.blink_bulbs:
                rainbow = ['#FF0000', '#FF7700', '#FFDD00', '#00FF00', '#0000FF', '#8A2BE2', '#C77DF3']
                i = 0
                if self.current_color >= 0 and self.current_color < len(self.bulbs):
                    for bulb in self.bulbs:
                        self.canvas.itemconfig(bulb, fill=rainbow[self.current_color])
                        i += 1
                elif self.current_color == len(self.bulbs):
                    for bulb in self.bulbs:
                        self.canvas.itemconfig(bulb, fill=rainbow[i])
                        i += 1
                self.blink_bulbs = False
                self.blink_count -=1
                if self.blink_count == 0:
                    self.current_color = self.current_color + 1
                    if self.current_color == len(self.bulbs)+1:
                        self.current_color = 0
                    self.blink_count = 3
            else:
                for bulb in self.bulbs:
                    self.canvas.itemconfig(bulb, fill= self.canvas['bg'])
                self.blink_bulbs = True

        self.window.after(1000, self.blink)

    def lights(self):

        caption = self.bttn_lights['text']
        if caption == 'On':
            self.bttn_lights['text'] = 'Off'
            self.bttn_lights['bg'] = 'green'
            self.power = 'On'
            self.blink_bulbs = True
        else:
            self.bttn_lights['text'] = 'On'
            self.power = 'Off'
            self.bttn_lights['bg'] = 'red'
            self.blink_bulbs = False
            #ensure bulbs are off
            for bulb in self.bulbs:
                self.canvas.itemconfig(bulb, fill=self.canvas['bg'])
            self.current_color = 0 #forget old state
DiwaliLights()
DiwaliLights()
