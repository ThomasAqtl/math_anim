from manim.mobject.coordinate_systems import Axes
import numpy as np
import manim as m
from manim import *
from numpy.core.records import array

f1 = lambda x: np.cos(x)

f2 = lambda p: lambda x: np.cos(2*np.pi*x/p)

f3 = lambda a, b: lambda p: lambda x: 0.5 * (np.cos(2*np.pi*x/p) + 1) * (b-a) + a

class scene(m.Scene):
    def construct(self):
        #=========== SCENE SETTINGS ===========

        # Background color
        self.camera.background_color = GREY_A

        #=========== SCENE OBJECTS ===========

        # Graph 
        graph = Axes(
            x_range=np.array([-8, 8, 1]),
            y_range=np.array([-4, 4, 1]),
            x_length=13,
            y_length=7,
            axis_config={
                'color' : BLACK,
                'stroke_width' : 4,
                'include_numbers' : False,
                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'include_sign' : True,
                    'color' : BLACK
                }
            },
        )

        # function parameters (period, bounds)
        a = DecimalNumber(-1, num_decimal_places=2)
        a_tracker = ValueTracker(-1)
        b = DecimalNumber(2, num_decimal_places=2)
        b_tracker = ValueTracker(1)
        p = DecimalNumber(8, num_decimal_places=2, show_ellipsis=True)
        p_tracker = ValueTracker(4)

        # axis labels
        axes_label = graph.get_axis_labels(Tex('$x$', color=BLACK), Tex('$y$', color=BLACK))

        # curves
        curve_0  = graph.get_graph(lambda x: f1(x), color=GREEN_B)

        curve_1 = graph.get_graph(f2(p.get_value()), color=BLUE)
        curve_1.add_updater(
            lambda period: period.become(
                graph.get_graph(
                    f2(p.get_value()),
                    color=BLUE
                )
            )
        )

        curve_2 = graph.get_graph(f3(a.get_value(), b.get_value())(p.get_value()), color=RED)

        # update functions
        p.add_updater(lambda period : period.set_value(p_tracker.get_value()))
        a.add_updater(lambda lower_bound : lower_bound.set_value(a_tracker.get_value()))
        b.add_updater(lambda upper_bound : upper_bound.set_value(b_tracker.get_value()))

        # curves labels
        curve1_label = graph.get_graph_label(curve_1, label=Tex('$2\\pi x/$',f'{p.get_value():.2f}'), x_val=8, direction=UP)
        curve1_label.add_updater(
            lambda m: m.become(
                graph.get_graph_label(curve_1, label=Tex('$2\\pi x/$',f'{p.get_value():.2f}'), x_val=8, direction=UP)
            )
        )

        
        
        #=========== SCENE PLAY (step-by-step) ===========
        # 1. Create graph, curves, labels
        self.add(p.set_opacity(0))
        self.play(Create(graph), run_time=1.5)
        #self.play(Create(curve_0), Create(curve_1), Create(curve_2), run_time=1.5)
        self.play(Create(curve_1), run_time=1)
        self.play(FadeIn(axes_label), Create(curve1_label)) 
        self.wait(1)
        self.play(p_tracker.animate.set_value(5))
        self.wait(1)
        self.play(p_tracker.animate.set_value(1))
        self.wait(2)

        # 2. 

