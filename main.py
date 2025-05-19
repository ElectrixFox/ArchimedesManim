from operator import le
from tkinter import font
from manim import *

class Intro(Scene):
    def construct(self):
        # the starting scene
        title = Text("The theorem of Archimedes")
        self.play(
            Write(title)
        )
        self.wait()

        self.play(title.animate.to_edge(UP))

        # Use a single Tex object for the full statement
        tex1 = Tex('Let $a, b \\in \\mathbb{R}$ with $b > 0$')
        tex2 = Tex('Then there exists a natural number $n$ with $nb > a$.')

        # Animate up to 'with' first, then the rest
        # Find the index where 'with' starts
        VGroup(tex1, tex2).arrange(DOWN, buff=0.5)
        self.play(Write(tex1))
        self.wait(0.5)
        self.play(Write(tex2, run_time = 2))
        self.wait()

def CreateTexFrac(p, q):
    return Tex(f'$\\frac{{{p}}}{{{q}}}$')

class NumberLineScene(Scene):
    def construct(self):
        p1, q1 = 29, 7
        p2, q2 = 26, 3
        a, b = p1 / q1, p2 / q2
        at = Tex('$a =$ ' + CreateTexFrac(p1, q1).get_tex_string(), font_size=40)
        bt = Tex('$b =$ ' + CreateTexFrac(p2, q2).get_tex_string(), font_size=40)
        at.set_color(RED)
        bt.set_color(BLUE)

        vg = VGroup(at, bt).arrange(UP, buff=0.5)
        vg.to_corner(UP + LEFT)

        l0 = NumberLine(
            x_range = [0, 10, 1],
            length = 10,
            color = BLUE,
            include_numbers = True,
            label_direction = UP,
        )

        self.add(l0)

        num1, dot1, num2, dot2 = self.select_two_points(a, b, l0)    # creates the points
        self.wait(2)
        self.play(
            Write(at),
            Write(bt)
        )
        self.play(FadeIn(dot1), Write(num1))
        self.play(FadeIn(dot2), Write(num2))

        self.wait(2)
        p1, q1 = 17, 5
        p2, q2 = 17, 3

        # change the values of a and b
        at0 = Tex('$a =$ ' + CreateTexFrac(p1, q1).get_tex_string(), font_size=40)
        bt0 = Tex('$b =$ ' + CreateTexFrac(p2, q2).get_tex_string(), font_size=40)
        at0.set_color(RED)
        bt0.set_color(BLUE)
        at0.move_to(at)
        bt0.move_to(bt)
        self.play(Transform(at, at0), Transform(bt, bt0))

        num1a, dot1a, num2a, dot2a = self.select_two_points(p1 / q1, p2 / q2, l0)    # creates the points
        

        self.play(Transform(num1, num1a), Transform(dot1, dot1a))
        self.play(Transform(num2, num2a), Transform(dot2, dot2a))
        self.wait(2)
    
    def select_two_points(self, a, b, nl):
        num1, num2 = Tex('a'), Tex('b')
        num1.move_to(nl.n2p(a) + DOWN)
        num2.move_to(nl.n2p(b) + DOWN)
        num1.set_color(RED)
        num2.set_color(BLUE)
        dot1 = Dot(color=RED)
        dot2 = Dot(color=BLUE)
        dot1.move_to(nl.n2p(a))
        dot2.move_to(nl.n2p(b))
        return num1, dot1, num2, dot2
    
    def update_labels(self, at, bt, a, b):
        at.set_text('$a =$ ' + CreateTexFrac(a[0], a[1]).get_tex_string(), font_size=40)
        bt.set_text('$b =$ ' + CreateTexFrac(b[0], b[1]).get_tex_string(), font_size=40)
        at.set_color(RED)
        bt.set_color(BLUE)
