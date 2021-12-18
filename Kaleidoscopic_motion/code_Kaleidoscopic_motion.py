from manim import *
from colour import Color


class PolygonRotation(Scene):
    def construct(self):

        def create_rectange(x, y, z, color_fill):
            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                width=EXPLAIN_WIDTH,
                height=EXPLAIN_HEIGHT,
                stroke_width=1,
                fill_color=color_fill
            )
            explain_filled_rect.shift(z)
            explain_filled_rect.set_fill(color_fill, 0.9)
            self.play(GrowFromCenter(explain_filled_rect, run_time=0.2))
            explain_line_left, explain_line_bottom = [
                Line(
                    explain_filled_rect.get_corner(start),
                    explain_filled_rect.get_corner(end),
                    color=DARKER_GRAY
                )
                for start, end in [(DL, UL), (DL, DR)]
            ]

            self.play(
                GrowFromEdge(explain_line_left, DOWN),
                GrowFromEdge(explain_line_bottom, LEFT), run_time=0.2
            )

            return [explain_filled_rect, explain_line_bottom, explain_line_left]

        def currentTextPositionMarkup(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text

        def currentTextPositionText(name, size_of_text, color_text, position):
            index_text = Text(name,color=color_text).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text),run_time=0.1)
            return index_text

        def currentTextPositionMarkupWithout(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text).scale(size_of_text)
            index_text.shift(position)
            return index_text

        

        def square_text_box(number, square_color, text_color):
            square = Square(side_length=0.7)
            square.set_stroke(color=square_color)
            text = MarkupText(number, color=text_color)
            text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text

        def dataframe_swap(x, y, color_name):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=DARKER_GRAY, width=10)
            rect.set_fill(color=color_name, opacity=2)
            return rect

        def dataframe_swap_scale_opacity(x, y, color_name, opacity_is):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=YELLOW_D)
            rect.set_fill(color=color_name, opacity=opacity_is)
            return rect

        def dataframe_swap_scale(x, y, color_name):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=DARK_GRAY)
            rect.set_fill(color=color_name, opacity=1)
            return rect

        def dataframe_rectange(x, y, content):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=GOLD_C, opacity=1)
            rect.scale(0.6)
            text = MarkupText(content)
            text.scale(0.4)
            squ_text = VGroup()
            squ_text.add(rect, text)
            return squ_text

        # poly_1 = RegularPolygon(n=6)
        # poly_2 = RegularPolygon(n=26, start_angle=2*DEGREES, color=GREEN)
        # poly_3 = RegularPolygon(n=10, color=RED)

        # poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        # self.add(poly_group)

        # self.play(FadeIn(poly_group))
        # self.wait(2)
        # self.play(FadeOut(poly_group))

        pentagram = RegularPolygram(13, radius=3, color=PURPLE_E)
        pentagram.set_fill(color=PURPLE_E, opacity=1)
        pentagram.shift(3 * LEFT)
        self.play(Create(pentagram))

        self.wait(2)

        pentagram1 = RegularPolygram(13, radius=2.5, color=WHITE)
        pentagram1.set_fill(color=WHITE, opacity=1)
        pentagram1.shift(3 * LEFT)
        self.play(Create(pentagram1))

        self.wait(2)

        pentagram3 = RegularPolygram(13, radius=2.5, color=RED_D)
        pentagram3.set_fill(color=RED_D, opacity=1)
        pentagram3.shift(3 * LEFT)
        self.play(Create(pentagram3))

        self.wait(2)

        pentagram4 = RegularPolygram(13, radius=2, color=WHITE)
        pentagram4.set_fill(color=WHITE, opacity=1)
        pentagram4.shift(3 * LEFT)
        self.play(Create(pentagram4))

        self.wait(2)

        pentagram5 = RegularPolygram(13, radius=2, color=PURPLE_E)
        pentagram5.set_fill(color=PURPLE_E, opacity=1)
        pentagram5.shift(3 * LEFT)
        self.play(Create(pentagram5))

        self.wait(2)

        object_frame_text = """The smoothly rotating cogwheel may pulsate, jolt, or accelerate, and the inner stationary cogwheel may wiggle."""       
        object_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{object_frame_text}</b></span>').scale(0.5)
        object_frame_text_style.shift(3.6 * UP + 0.01 * LEFT)

        angle_rotation = -10
        running_time = 0.5

        for i in range(10):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                  Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                #   Write(object_frame_text_style, run_time=running_time)
                  )

        for i in range(2):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                  Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                  Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                  Write(object_frame_text_style, run_time=running_time)
                  )

        for i in range(25):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                  Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))

        text_print_box = dataframe_swap_scale_opacity(7, 1, DARKER_GRAY, 0.4)
        text_print_box.shift(2.5 * UP + 3.5 * RIGHT)
        think_frame_text = """Animation Created Using Python Manim Library\n>>> pip install manim"""       
        think_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{think_frame_text}</b></span>').scale(0.35)
        think_frame_text_style.shift(2.5 * UP + 3.5 * RIGHT)

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(text_print_box, run_time=running_time)
                  )

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Write(think_frame_text_style, run_time=running_time)
                  )
        
        for i in range(15):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))


        object_box = dataframe_swap_scale(6, 4, DARKER_GRAY)
        object_box.shift(1 * DOWN + 4 * RIGHT)
        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(object_box, run_time=running_time)
            )
        
        object_frame_text = """from manim import *

class PolygonRotation(Scene):
    def construct(self):
        pentagram = RegularPolygram(13, radius=3, 
                                   color=PURPLE_E)
        pentagram.set_fill(color=PURPLE_E, 
                           opacity=1)
        pentagram.shift(3 * LEFT)
        self.play(Create(pentagram))
        
        self.play(Rotating(pentagram3, 
                  radians=angle_rotation*DEGREES,
                  about_point = pentagram3.get_center(),
                  run_time=running_time, 
                  rate_func=linear))"""       
        object_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{object_frame_text}</b></span>').scale(0.25)
        object_frame_text_style.shift(1 * DOWN + 4 * RIGHT)

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Write(object_frame_text_style[:63], run_time=running_time)
                  )

        brace1 = BraceBetweenPoints(0.3 * DOWN + 1.9 * RIGHT, 1.4 * DOWN + 1.9 * RIGHT, buff=0)
        brace2 = BraceBetweenPoints(1.65 * DOWN + 1.9 * RIGHT, 2.6 * DOWN + 1.9 * RIGHT, buff=0)
        curve_arrow_1 = CurvedArrow(2.1 * DOWN + 2.3 * LEFT, brace2.get_center(), color=RED_D, angle=1.23)

        for i in range(5):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))

        arrow_1 = Arrow(0.9 * DOWN + 0.6 * LEFT, brace1.get_center(), color=RED_D, buff=0.1)
        # self.play(Create(arrow_1))

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(arrow_1, run_time=running_time)
            )

        
        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(brace1, run_time=running_time)
            )

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Write(object_frame_text_style[63:211], run_time=running_time)
            )

        for i in range(5):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))


        
        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(curve_arrow_1, run_time=running_time)
            )
        
        
        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Create(brace2, run_time=running_time)
            )

        for i in range(1):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear),
                      Write(object_frame_text_style[211:], run_time=running_time)
            )

        for i in range(25):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))

        for i in range(15):
            self.play(Rotating(pentagram3, radians=angle_rotation*DEGREES,about_point = pentagram3.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(pentagram4, radians=angle_rotation*DEGREES,about_point = pentagram4.get_center(),run_time=running_time, rate_func=linear))

        self.play(
            *[ShrinkToCenter(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        self.play(
            *[FadeOut(mob)for mob in self.mobjects], run_time=0.1
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

        





        self.wait(2)
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        circle = Circle(color=RED, radius=0.3)
        circle.set_stroke(color=RED, opacity=0.3)
        self.play(Write(circle,run_time=0.1))

        self.wait(5)
