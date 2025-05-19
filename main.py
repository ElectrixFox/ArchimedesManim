from manim import *
from math import ceil

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

class FractionalNumber():
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.val = p / q
        self.tex = CreateTexFrac(p, q)
        self.str = self.tex.get_tex_string()

class NumberLineScene(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range = [0, 10, 1],
            length = 10,
            color = BLUE,
            include_numbers = True,
            label_direction = UP,
        )
        self.add(l0)

        a, b = FractionalNumber(29, 7), FractionalNumber(26, 3)
        at = Tex('$a =$ ' + a.str, font_size=40)
        bt = Tex('$b =$ ' + b.str, font_size=40)

        at.set_color(RED)
        bt.set_color(BLUE)

        vg = VGroup(at, bt).arrange(UP, buff=0.5)
        vg.to_corner(UP + LEFT)


        num1, dot1, num2, dot2 = self.select_two_points(a.val, b.val, l0)    # creates the points
        self.wait(2)
        self.play(
            Write(at),
            Write(bt)
        )
        self.play(FadeIn(dot1), Write(num1))
        self.play(FadeIn(dot2), Write(num2))

        nnum, ndot = Tex('nb'), Dot(color=GREEN)
        ndot.z_index = -1
        n = ceil(a.val / b.val)
        self.place_nb(n, b, l0, nnum, ndot)

        self.wait(1)

        # change the values of a and b
        # self.update_labels([dot1, dot2], [num1, num2], at, bt, FractionalNumber(17, 5), FractionalNumber(17, 3), l0)    # creates the points
        # self.wait(1)
        a, b = FractionalNumber(71, 11), FractionalNumber(7, 2)
        self.update_labels([dot1, dot2], [num1, num2], at, bt, a, b, l0)    # creates the points
        n = ceil(a.val / b.val) # updating to the new value of n
        self.place_nb(n, b, l0, nnum, ndot)
        self.wait(1)
    
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
    
    def update_labels(self, dts, nms, at, bt, a, b, nl):
        at0 = Tex('$a =$ ' + a.str, font_size=40)
        bt0 = Tex('$b =$ ' + b.str, font_size=40)

        at0.set_color(RED)
        bt0.set_color(BLUE)

        at0.move_to(at)
        bt0.move_to(bt)

        self.play(Transform(at, at0), Transform(bt, bt0))

        num1a, dot1a, num2a, dot2a = self.select_two_points(a.val, b.val, nl)    # creates the points

        self.play(Transform(nms[0], num1a), Transform(dts[0], dot1a))
        self.play(Transform(nms[1], num2a), Transform(dts[1], dot2a))
    
    def place_nb(self, n, b, nl, num0, dot0):
        num = Tex('nb')
        num.move_to(nl.n2p(n * b.val) + UP)
        num.set_color(GREEN)
        dot = Dot(color=GREEN)
        dot.z_index = -1
        dot.move_to(nl.n2p(n * b.val))
        self.play(Transform(num0, num), Transform(dot0, dot))