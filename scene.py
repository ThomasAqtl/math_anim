from manim.mobject.coordinate_systems import Axes
import numpy as np
import manim as m
from manim import *
from numpy.core.records import array

f1 = lambda x: np.cos(x)

f2 = lambda x: lambda p: f1(2*np.pi*x/p)

f3 = lambda x: lambda p: lambda a: lambda b: 0.5 * f2(x,p)*(b-a) + a

class scene(m.Scene):
    def construct(self):
        #=========== SCENE SETTINGS ===========

        # Background color
        self.camera.background_color = GREY_A

        #=========== SCENE OBJECTS ===========

        # Graph 
        graph = Axes(
            x_range=np.array([-8, 8, 2]),
            y_range=np.array([-4, 4, 2]),
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
        b = DecimalNumber(1, num_decimal_places=2)
        p = DecimalNumber(np.pi, num_decimal_places=2)

        # axis labels
        axes_label = graph.get_axis_labels(Tex('x', color=BLACK), Tex('y', color=BLACK))

        # curves
        curve_1 = graph.get_graph(f1, color=BLUE)
        curve_2 = graph.get_graph(lambda x: np.sin(x), color=GREEN)

        # curves labels
        curve1_label = graph.get_graph_label(curve_1, label=Tex('$\dfrac{2\pi x}{p}$'), x_val=6.5, direction=UP)
        curve2_label = graph.get_graph_label(curve_2,label=Tex('sin(x)'), x_val=-8, direction=DOWN)

        
        
        #=========== SCENE PLAY (step-by-step) ===========
        # 1. Create graph, curves, labels
        self.play(Create(graph), run_time=1.5)
        self.play(Create(curve_1), Create(curve_2), run_time=1.5)
        self.play(FadeIn(axes_label), FadeIn(curve1_label), FadeIn(curve2_label))
        self.wait(2)

        # 2. 

