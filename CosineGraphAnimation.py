from manim.mobject.coordinate_systems import Axes
import numpy as np
import manim as m
from manim import *
from numpy.core.records import array

'''
This scene intends to show how to build a simple cosine-like function of a given period, oscillating between given bounds.

As a classical cosine function (f(x) = cos(x), x in R) oscillates between -1 and 1, the idea is to stretch it to [0, 1]
and then multiply by some values to extend it to [a, b] for any given a and b. In details :

#1. Adjust period
~ cos(x)                                [-1, 1], period 2pi
~ cos(2*pi*x)                           [-1, 1], period 1
~ cos(2*pi*x / p)                       [-1, 1], period p

#2. Adjust interval
~ cos(2*pi*x / p) + 1                   [0, 2], period p
~ .5(cos(2*pi*x / p) + 1)               [0, 1], period p
~ .5(cos(2*pi*x / p) + 1)(b-a)          [0, b-a], period p
~ .5(cos(2*pi*x / p) + 1)(b-a) + a      [a, b], period p

The scene goes through these steps sequencially and plot matching graph.
'''

# Aim function declaration
f = lambda a, b: lambda p: lambda x: 0.5 * (np.cos(2*np.pi*x/p) + 1) * (b-a) + a

# Argument values list (used for animation)
p_list = [5, 1, 2, 0.7]
a_list = [-2, -4, 1, 0]
b_list = [1, 8, 4.5, 7]

class CosineGraphAnimation1(m.Scene):
    def construct(self):
        #region =========== SCENE SETTINGS ===========
        # Background color
        self.camera.background_color = GREY_A
        config.frame_rate = 30
        #endregion

        #region =========== SCENE OBJECTS ===========

        # Graph 
        axes = Axes(
            x_range=np.array([-16, 16, 2]),
            y_range=np.array([-10, 10, 2]),
            x_length=13,
            y_length=7,
            axis_config={
                'color' : BLACK,
                'stroke_width' : 4,
                'include_numbers' : True,
                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'include_sign' : False,
                    'color' : BLACK
                }
            },
        )

        

        # function parameters (period, bounds)
        a = DecimalNumber(-1, num_decimal_places=1, color=GREEN_E)
        b = DecimalNumber(2, num_decimal_places=1, color=PURPLE)
        p = DecimalNumber(8, num_decimal_places=1, color=RED)

        # Value trackers for a, b and p
        a_tracker = ValueTracker(-1)
        b_tracker = ValueTracker(1)
        p_tracker = ValueTracker(4)

        # curve
        curve = axes.get_graph(f(a.get_value(), b.get_value())(p.get_value()), color=BLUE)

        # text
        empty_label = Tex('$y = 0.5\left(cos\left(\dfrac{2\\pi x}{}\\right)+1\\right)(\qquad - \qquad )\ +$', color=BLACK)
        p.move_to(np.array([-0.9, -0.3, 0]))
        b.move_to(np.array([1.9, 0, 0]))
        a.move_to(np.array([3.3, 0, 0]))
        a2 = a.copy()
        a2.move_to(np.array([5.1, 0, 0]))

        # end label with dynamic parameters (show examples for a, b and p values)
        dynamic_label = Group(empty_label, p, b, a, a2)
        dynamic_label.scale(0.6)
        dynamic_label.to_corner(UL)

        # label for explanation (follow header steps)

        # header
        header_label_func = Tex('Function', color=BLACK)
        header_label_interval = Tex('$y$ Interval', color=BLACK)
        header_label_period = Tex('Period', color=BLACK)
        header_label_func.move_to(np.array([-4, 0, 0]))
        header_label_period.move_to(np.array([4, 0, 0]))
        header_label = Group(header_label_func, header_label_interval, header_label_period)
        header_label.to_edge(UP)

        # function labels
        func_label_0 = Tex('$cos(x)$', color=BLACK)
        func_label_1 = Tex('$cos(2\\pi x)$', color=BLACK)
        func_label_2 = Tex('$cos(\\frac{2\\pi x}p)$', color=BLACK)
        func_label_3 = Tex('$cos(\\frac{2\\pi x}p) + 1$', color=BLACK)
        func_label_4 = Tex('$\\frac12 \\left(cos(\\frac{2\\pi x}p) + 1\\right)$', color=BLACK)
        func_label_5 = Tex('$\\frac12 \\left(cos(\\frac{2\\pi x}p) + 1\\right)(b-a)$', color=BLACK)
        func_label_5.scale(0.7)
        func_label_6 = Tex('$\\frac12 \\left(cos(\\frac{2\\pi x}p) + 1\\right)(b-a)+a$', color=BLACK)
        func_label_6.scale(0.7)
        func_group = Group(func_label_0, func_label_1, func_label_2, func_label_3, func_label_4, func_label_5, func_label_6)

        # interval labels
        interval_label_0 = Tex('$[-1,\ 1]$', color=BLACK)
        interval_label_1 = Tex('$[0,\ 2]$', color=BLACK)
        interval_label_2 = Tex('$[0,\ 1]$', color=BLACK)
        interval_label_3 = Tex('$[0,\ b-a]$', color=BLACK)
        interval_label_4 = Tex('$[a,\ b]$', color=BLACK)
        interval_group = Group(interval_label_0, interval_label_1, interval_label_2, interval_label_3, interval_label_4)

        # period labels
        period_label_0 = Tex('$2\\pi$', color=BLACK)
        period_label_1 = Tex('$1$', color=BLACK)
        period_label_2 = Tex('$p$', color=BLACK)
        period_group = Group(period_label_0, period_label_1, period_label_2)

        # adjusting labels positions
        func_group.move_to(np.array([-4, 0, 0]))
        period_group.move_to(np.array([4, 0, 0]))
        label_0 = Group(func_label_0, interval_label_0, period_label_0)
        
        # Updaters
        p.add_updater(lambda m : m.set_value(p_tracker.get_value()))
        a.add_updater(lambda m : m.set_value(a_tracker.get_value()))
        a2.add_updater(lambda m : m.set_value(a_tracker.get_value()))
        b.add_updater(lambda m : m.set_value(b_tracker.get_value()))

        curve.add_updater(
            lambda c : c.become(
                axes.get_graph(
                    f(a.get_value(), b.get_value())(p.get_value()), color=BLUE)
                )
            )
        
        #endregion

        #region =========== VIDEO (step-by-step) ===========
        
        #1. Header steps
        self.add((header_label))
        self.wait(1)
        self.play(FadeIn(label_0))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_1), Transform(period_label_0, period_label_1))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_2), Transform(period_label_0, period_label_2))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_3), Transform(interval_label_0, interval_label_1))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_4), Transform(interval_label_0, interval_label_2))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_5), Transform(interval_label_0, interval_label_3))
        self.wait(2)
        self.play(Transform(func_label_0, func_label_6), Transform(interval_label_0, interval_label_4))
        self.wait(2)
        self.remove(header_label, interval_label_0, period_label_0)
        self.play(func_label_0.animate.scale(1/0.7).center())
        self.wait(2)

        #2. Reducing formula to corner and adding matching curve
        self.play(
            Transform(func_label_0, empty_label), 
            Create(axes), 
            Create(curve), 
            Create(a), 
            Create(a2), 
            Create(b), 
            Create(p)
        )

        self.wait(2)

        for i, j, k in zip(p_list, a_list, b_list):
            self.play(p_tracker.animate.set_value(i))
            self.play(a_tracker.animate.set_value(j))
            self.play(b_tracker.animate.set_value(k))
            self.wait(2)
        #endregion