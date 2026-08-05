import customtkinter as ctk
import math


class AnimatedRing(ctk.CTkCanvas):

    def __init__(self, parent, size=270):

        super().__init__(
            parent,
            width=size,
            height=size,
            bg="#F6F4EC",
            highlightthickness=0
        )

        self.size = size
        self.radius = 110
        self.angle = 0

        self.animate()

    def animate(self):

        self.delete("all")

        cx = self.size / 2
        cy = self.size / 2

        dots = 36

        for i in range(dots):

            theta = math.radians(
                (360 / dots) * i + self.angle
            )

            x = cx + self.radius * math.cos(theta)
            y = cy + self.radius * math.sin(theta)

            brightness = (math.sin(theta + math.radians(self.angle)) + 1) / 2

            if brightness > 0.75:
                color = "#66C27A"
                r = 5

            elif brightness > 0.45:
                color = "#9AD8A8"
                r = 4

            else:
                color = "#D7EEDC"
                r = 3

            self.create_oval(
                x-r,
                y-r,
                x+r,
                y+r,
                fill=color,
                outline=color
            )

        self.angle += 4

        self.after(40, self.animate)