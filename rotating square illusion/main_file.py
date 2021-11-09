# import the python libraries
from manim import *
from colour import Color


class RotatingSquares(Scene):
    def construct(self):


        def dataframe_swap_scale(x, y, color_name):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=DARK_GRAY)
            rect.set_fill(color=color_name, opacity=1)
            return rect

        rect_0 = RoundedRectangle(corner_radius=1, height=5, width=5, stroke_width=20, fill_color=WHITE).shift(0.5 * DOWN)
        rect_1 = RoundedRectangle(corner_radius=0.7, height=4, width=4, stroke_width=20,fill_color=BLACK).shift(0.5 * DOWN)
        rect_2 = RoundedRectangle(corner_radius=0.5, height=3, width=3, stroke_width=20,fill_color=BLACK).shift(0.5 * DOWN)
        rect_3 = RoundedRectangle(corner_radius=0.5, height=2, width=2, stroke_width=20,fill_color=BLACK).shift(0.5 * DOWN)
        rect_4 = RoundedRectangle(corner_radius=0.2, height=1, width=1, stroke_width=20,fill_color=BLACK).shift(0.5 * DOWN)
        rect_5 = RoundedRectangle(corner_radius=0.1, height=0.4, width=0.4, stroke_width=1,fill_color=WHITE).shift(0.5 * DOWN)
        rect_5.set_fill(WHITE, 1)

        angle_rotation = 60   # displacement per loop
        running_time = 0.7     # speed of the rotation in second(S)


        for i in range(30): # time of rotation 30 * 0.7(running_time) = 21 seconds
            self.play(Rotating(rect_0, radians=angle_rotation*DEGREES,about_point = rect_0.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_1, radians=angle_rotation*DEGREES,about_point = rect_1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_2, radians=angle_rotation*DEGREES,about_point = rect_2.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_3, radians=angle_rotation*DEGREES,about_point = rect_3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_4, radians=angle_rotation*DEGREES,about_point = rect_4.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_5, radians=angle_rotation*DEGREES,about_point = rect_5.get_center(),run_time=running_time, rate_func=linear),)

        

        global_frame = dataframe_swap_scale(12, 1, DARKER_GREY) # create square box
        global_frame.shift(0.01 * UP + 0.05 * LEFT)
        self.play(Create(global_frame))

        heading_one1 = """When the concentric square borders with rounded edges are rotated slowly, the entire pattern appears to pulsate radially."""       
        heading_one_style1 = MarkupText(f'<span font_family="monospace"><b>{heading_one1}</b></span>').scale(0.4)
        heading_one_style1.shift(0.01 * UP + 0.05 * LEFT)
        self.play(Write(heading_one_style1), run_time=2.5)

        global_frame.shift(3.5 * UP)
        heading_one_style1.shift(3.5 * UP)

        for i in range(30):
            self.play(Rotating(rect_0, radians=-angle_rotation*DEGREES,about_point = rect_0.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_1, radians=-angle_rotation*DEGREES,about_point = rect_1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_2, radians=-angle_rotation*DEGREES,about_point = rect_2.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_3, radians=-angle_rotation*DEGREES,about_point = rect_3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_4, radians=-angle_rotation*DEGREES,about_point = rect_4.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(rect_5, radians=-angle_rotation*DEGREES,about_point = rect_5.get_center(),run_time=running_time, rate_func=linear),)

        

        nrect_0 = Rectangle(height=5, width=5, stroke_width=20, fill_color=WHITE)
        nrect_1 = Rectangle(height=4, width=4, stroke_width=20,fill_color=BLACK)
        nrect_2 = Rectangle(height=3, width=3, stroke_width=20,fill_color=BLACK)
        nrect_3 = Rectangle(height=2, width=2, stroke_width=20,fill_color=BLACK)
        nrect_4 = Rectangle(height=1, width=1, stroke_width=20,fill_color=BLACK)
        nrect_5 = Rectangle(height=0.4, width=0.4, stroke_width=1,fill_color=WHITE)
        nrect_5.set_fill(WHITE, 1)

        global_frame11 = dataframe_swap_scale(12, 1, DARKER_GREY)
        global_frame11.shift(0.01 * UP + 0.05 * LEFT)
        self.play(Create(global_frame11))

        heading_one11 = """Pulsating illusion will dissapear, if we remove rounded edges of Squares. """       
        heading_one_style11 = MarkupText(f'<span font_family="monospace"><b>{heading_one11}</b></span>').scale(0.4)
        heading_one_style11.shift(0.01 * UP + 0.05 * LEFT)
        self.play(Write(heading_one_style11))

        self.play(ShrinkToCenter(rect_0), ShrinkToCenter(rect_1), ShrinkToCenter(rect_2), ShrinkToCenter(rect_3), ShrinkToCenter(rect_4), ShrinkToCenter(rect_5))
        self.play(ShrinkToCenter(global_frame), ShrinkToCenter(heading_one_style1))

        global_frame11.shift(3.5 * UP)
        heading_one_style11.shift(3.5 * UP)

        self.play(Create(nrect_0), Create(nrect_1), Create(nrect_2), Create(nrect_3), Create(nrect_4), Create(nrect_5))

        running_time = 1

        for i in range(20):
            self.play(Rotating(nrect_0, radians=-angle_rotation*DEGREES,about_point = nrect_0.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(nrect_1, radians=-angle_rotation*DEGREES,about_point = nrect_1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(nrect_2, radians=-angle_rotation*DEGREES,about_point = nrect_2.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(nrect_3, radians=-angle_rotation*DEGREES,about_point = nrect_3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(nrect_4, radians=-angle_rotation*DEGREES,about_point = nrect_4.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(nrect_5, radians=-angle_rotation*DEGREES,about_point = nrect_5.get_center(),run_time=running_time, rate_func=linear),)

        self.wait(1.5)

        self.play(
            *[ShrinkToCenter(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        self.wait(0.7)

        text_name = """Thanks for watching"""

        thanks = MarkupText(f'<span font_family="monospace"><b>{text_name}</b></span>').scale(0.8)

        self.play(Write(thanks), run_time=2)

        self.wait(1.5)

        self.play(FadeOut(thanks))

        def HSL(hue,saturation=1,lightness=0.5):
            return Color(hsl=(hue,saturation,lightness))

        def get_hsl_set_colors(color_range=360,saturation=1,lightness=0.5):
            return [*[HSL(i/360,saturation,lightness) for i in range(color_range)]]

        like_text = MarkupText(f'<span font_family="monospace"><b>LIKE</b></span>').scale(1.8)
        like_text.set_color(color=get_hsl_set_colors(color_range=360))
        self.play(Write(like_text),run_time=2)
        like_text.shift(2.5*UP + 0.5* RIGHT)

        share_text = MarkupText(f'<span font_family="monospace"><b>SHARE</b></span>').scale(1.8)
        share_text.set_color(color=get_hsl_set_colors(color_range=120))
        self.play(Write(share_text), run_time=2)
        share_text.shift(ORIGIN + 0.5* RIGHT)
        

        sub_text = MarkupText(f'<span font_family="monospace"><b>SUBSCRIBE</b></span>').scale(1.8)
        sub_text.set_color(color=get_hsl_set_colors(color_range=240))
        sub_text.shift(2.5*DOWN + 0.5* RIGHT)
        self.play(Write(sub_text), run_time=2)



        self.wait(5)
