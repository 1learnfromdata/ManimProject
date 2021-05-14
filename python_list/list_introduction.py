from manim import *

class ListIntroduction(Scene):
    def construct(self):

        spacy_model = TextMobject(r"""List is a most versatile and useful data types in Python.""")
        # spacy_model.to_corner(4 * UP - 10 * RIGHT)
        self.play(Write(spacy_model))
        self.play(FadeOut(spacy_model))
        self.wait(1)

        list_one = Text(r"""List can hold Arbitary Objects""")
        self.play(Write(list_one))
        self.play(ApplyMethod(list_one.scale, 0.5))
        list_one.move_to(3.5 * UP + ORIGIN)
        self.wait(1)

        list_one = Text(r"""list_a = [ 'one', 'two', 'three', 'four']""")
        self.play(Write(list_one))
        self.play(ApplyMethod(list_one.scale, 0.5))
        list_one.move_to(2 * UP + 3.5 * LEFT)
        self.wait(1)

        # First rectangle ------------------

        def create_rectange(x, y, z):

            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                                        width=EXPLAIN_WIDTH,
                                        height=EXPLAIN_HEIGHT,
                                        stroke_width=1,
                                        fill_color=DARK_GRAY
                                    )
            explain_filled_rect.to_edge(z,buff=0)
            # explain_filled_rect = explain_rect.copy()
            explain_filled_rect.set_fill(DARK_GRAY,0.5)
            # Use stretch=True to preserve the dimension that is not modified
            # explain_filled_rect.set_height(1)
            # compress the definitions of your objects, this will make it easier to read them.
            explain_line_left, explain_line_bottom = [
                Line(
                        explain_filled_rect.get_corner(start),
                        explain_filled_rect.get_corner(end),
                        color=RED_A
                    )
                for start,end in [(DL,UL),(DL,DR)] 
            ]

            self.play(FadeIn(explain_filled_rect))
            self.play(
                    GrowFromEdge(explain_line_left, DOWN),
                    GrowFromEdge(explain_line_bottom, LEFT)
            )

        # end first rectangle
        create_rectange(7,5,LEFT)

        self.wait(1)
        list_two = Text(r"""list_b = [ 1, 2, 3, 4]""")
        self.play(Write(list_two))
        self.play(ApplyMethod(list_two.scale, 0.5))
        list_two.shift( UP + 3 * LEFT)
        list_two.align_to(list_one, LEFT)
        self.wait(1)

        list_three = Text(r"""list_c = [ 10.3, 20.3, 40.5, 50.6]""")
        self.play(Write(list_three))
        self.play(ApplyMethod(list_three.scale, 0.5))
        list_three.shift(ORIGIN + 3 *LEFT)
        list_three.align_to(list_one, LEFT)
        self.wait(1)

        list_four = Text(r"""list_d = [ 'one', 20.367, 6, False]""")
        list_four.shift( DOWN + LEFT)
        self.play(Write(list_four))
        self.play(ApplyMethod(list_four.scale, 0.5))
        list_four.align_to(list_one, LEFT)
        self.wait(1)


        list_five = Text(r"""list_e = [ math, test_func, float, sorted]""")
        list_five.shift( 2 * DOWN + LEFT)
        self.play(Write(list_five))
        self.play(ApplyMethod(list_five.scale, 0.47))
        list_five.align_to(list_one, LEFT)
        create_rectange(7,5, RIGHT)
        self.wait(2)

        paragraph = Paragraph(">>> type(False)", "<class 'bool'>",
                      '>>> def test_func():', '...     pass','...', '>>> test_func', '<function test_func at 0x7f270c77f3a0>',
                      '>>> import math', '>>> math', "<module 'math' (built-in)>",
                      '>>> float', "<class 'float'>", 
                      '>>> sorted', '<built-in function sorted>')

        paragraph.shift( ORIGIN + 4 * RIGHT)
        self.play(ApplyMethod(paragraph.scale, 0.5))
        self.play(Write(paragraph))
        self.wait(1)

        first_arrow = Arrow(0.7 * DOWN + 1.4 * LEFT, 2 * UP + 0.5 * RIGHT , buff=0)
        self.play(ShowCreation(first_arrow))
        self.wait(2)

        second_arrow = Arrow(1.8 * DOWN +   4.2 * LEFT, 0.2 * DOWN + 0.5 * RIGHT , buff=0)
        self.play(ShowCreation(second_arrow))
        self.play(FadeOut(first_arrow))
        self.wait(2)

        third_arrow = Arrow(1.8 * DOWN +   3.2 * LEFT, 1.4 * UP + 0.5 * RIGHT , buff=0)
        self.play(ShowCreation(third_arrow))
        self.play(FadeOut(second_arrow))
        self.wait(2)

        fourth_arrow = Arrow(1.8 * DOWN +   1.7 * LEFT, 1.2 * DOWN + 0.5 * RIGHT , buff=0)
        self.play(ShowCreation(fourth_arrow))
        self.play(FadeOut(third_arrow))
        self.wait(2)

        fifth_arrow = CurvedArrow(2.1 * DOWN +   0.8 * LEFT, 1.9 * DOWN + 0.5 * RIGHT )
        self.play(ShowCreation(fifth_arrow))
        self.play(FadeOut(fourth_arrow))
        

        

        # self.add(explain_filled_rect)
        # This generates a copy of the element in an 
        # attribute called "target" to which we 
        # can indicate when we want.
        # explain_filled_rect.generate_target()


        self.wait(4)


class ListElementAccess(Scene):
    def construct(self):

        list_one = Text(r"""How to access List elements""")
        self.play(Write(list_one))
        self.play(ApplyMethod(list_one.scale, 0.5))
        list_one.move_to(3.5 * UP + ORIGIN)
        self.wait(1)

        def create_rectange(x, y, z):

            EXPLAIN_WIDTH = x
            EXPLAIN_HEIGHT = y
            explain_filled_rect = Rectangle(
                                        width=EXPLAIN_WIDTH,
                                        height=EXPLAIN_HEIGHT,
                                        stroke_width=1,
                                        fill_color=DARK_GRAY
                                    )
            explain_filled_rect.shift(z)
            # self.play(Write(explain_filled_rect))
            # explain_filled_rect = explain_rect.copy()
            explain_filled_rect.set_fill(DARK_GRAY,0.5)
            self.play(GrowFromCenter(explain_filled_rect,run_time=1))
            # Use stretch=True to preserve the dimension that is not modified
            # explain_filled_rect.set_height(1)
            # compress the definitions of your objects, this will make it easier to read them.
            explain_line_left, explain_line_bottom = [
                Line(
                        explain_filled_rect.get_corner(start),
                        explain_filled_rect.get_corner(end),
                        color=RED_A
                    )
                for start,end in [(DL,UL),(DL,DR)] 
            ]

            # self.play(FadeIn(explain_filled_rect))
            self.play(
                    GrowFromEdge(explain_line_left, DOWN),
                    GrowFromEdge(explain_line_bottom, LEFT)
            )

        # end first rectangle
        create_rectange(12,2, 2 * UP +  LEFT)

        text = MathTex(
            "listE = ",
            "[ ",
            " 'one' " ,
             " , ",    
             " 20.3 " , " , "," 6 " , " , ", " False  " , " ]"
        )

        self.play(Write(text))
        self.play(ApplyMethod(text.scale, 1.4))
        text.shift( 2 * UP + LEFT)
        self.wait(2)

        def indexPosition(name, position):

            index_text = Text(name)
            index_text.shift(position)
            self.play(ApplyMethod(index_text.scale, 0.5))
            
            # self.play(Write(index_text))


        indexPosition("0", 1.3 * UP + 1.7 * LEFT)
        indexPosition("1", 1.3 * UP + 0.2 * LEFT)
        indexPosition("2", 1.3 * UP + 0.9 * RIGHT)
        indexPosition("3", 1.3 * UP + 2.2 * RIGHT)
        self.wait(1)

        create_rectange(6,4, 1.2 * DOWN + 4 * LEFT )
        self.wait(1)

        def text_position(name, position):
            text_name = TextMobject(name)
            text_name.shift(position)
            self.play(Write(text_name))
            return text_name

        text_1 = text_position('>>> listE[1]', 0.5 * DOWN + 5 * LEFT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[4], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.2 * LEFT,  1 * DOWN + 4.6 * LEFT, angle=-1.23)
        self.play(ShowCreation(first_arrow))
        text_2 = text_position("20.3", 1 * DOWN + 5.5 * LEFT)
        self.wait(1)

        text_3 = text_position('>>> listE[3]', 1.8 * DOWN + 5 * LEFT)
        self.wait(1)
        framebox2 = SurroundingRectangle(text[8], buff = .1)
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait(1)
        second_arrow = CurvedArrow(1.6 * UP + 2.2 * RIGHT,  2.3 * DOWN + 4.6 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))
        text_4 = text_position("False", 2.3 * DOWN + 5.5 * LEFT)

        self.play(FadeOut(first_arrow), FadeOut(second_arrow), FadeOut(framebox2))

        
        indexPosition("-1", 2.8 * UP + 2.2 * RIGHT)
        indexPosition("-2", 2.8 * UP + 0.9 * RIGHT)
        indexPosition("-3", 2.8 * UP + 0.2 * LEFT)
        indexPosition("-4", 2.8 * UP + 1.7 * LEFT)

        self.wait(1)

        create_rectange(6,4, 1.2 * DOWN + 4 * RIGHT )
        self.wait(1)

        text_5 = text_position('>>> listE[-2]', 0.5 * DOWN + 2.5 * RIGHT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[6], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.9 * RIGHT,  1 * DOWN + 1.5 * RIGHT, angle=2.23)
        self.play(ShowCreation(first_arrow))
        text_6 = text_position("6", 1 * DOWN + 2 * RIGHT)
        self.wait(1)

        text_7 = text_position('>>> listE[-4]', 1.8 * DOWN + 2.5 * RIGHT)
        self.wait(1)
        framebox2 = SurroundingRectangle(text[2], buff = .1)
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait(1)
        second_arrow = CurvedArrow(1.6 * UP + 1.7 * LEFT,  2.3 * DOWN + 1.5 * RIGHT, angle=2.23)
        self.play(ShowCreation(second_arrow))
        text_8 = text_position("'one'", 2.3 * DOWN + 2 * RIGHT)

        self.play(FadeOut(first_arrow), FadeOut(second_arrow), FadeOut(framebox2),
            FadeOut(text_1),FadeOut(text_2),FadeOut(text_3), FadeOut(text_4))

        # this is a[2:3] and type
        self.wait(1)

        text_9 = text_position('>>> listE[1:3]', 0.5 * DOWN + 5 * LEFT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[4:7], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.2 * LEFT,  1 * DOWN + 4.6 * LEFT, angle=-1.23)
        self.play(ShowCreation(first_arrow))
        text_10 =text_position("[20.3, 6]", 1 * DOWN + 5.5 * LEFT)

        self.wait(2)

        text_11 = text_position('>>> type(listE[1:3])', 1.8 * DOWN + 4.5 * LEFT)
        self.wait(1)
        text_12 = text_position("- <class 'list'>", 2.3 * DOWN + 4.5 * LEFT)

        self.play(FadeOut(framebox1),FadeOut(text_7),FadeOut(text_5),
            FadeOut(text_6), FadeOut(text_8), FadeOut(first_arrow))


        text_13 = text_position('>>> listE[-3:-1]', 0.5 * DOWN + 3 * RIGHT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[4:7], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.9 * RIGHT,  1 * DOWN + 1.5 * RIGHT, angle=2.23)
        self.play(ShowCreation(first_arrow))
        text_14 = text_position("[20.3, 6]", 1 * DOWN + 2.5 * RIGHT)

        self.wait(1)

        text_15 = text_position('>>> listE[-3:-1] == listE[1:3]', 1.8 * DOWN + 3.5 * RIGHT)
        self.play(ApplyMethod(text_15.scale, 0.7))
        self.wait(1)
        text_16 = text_position("True", 2.3 * DOWN + 2 * RIGHT)

        self.play(FadeOut(framebox1),FadeOut(text_9),FadeOut(text_10),
            FadeOut(text_11), FadeOut(text_12),FadeOut(first_arrow))


        text_1 = text_position('>>> listE[0:3:2]', 0.5 * DOWN + 5 * LEFT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[2], buff = .1)
        framebox2 = SurroundingRectangle(text[6], buff = .1)
        self.play(
            ShowCreation(framebox1),ShowCreation(framebox2)
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.9 * RIGHT,  1 * DOWN + 4.6 * LEFT, angle=-2.23)
        second_arrow = CurvedArrow(1.6 * UP + 1.7 * LEFT,  1 * DOWN + 4.6 * LEFT, angle=-2.23)

        self.play(ShowCreation(first_arrow), 
            ShowCreation(second_arrow))

        self.wait(1)

        text_2 = text_position("['one', 6]", 1 * DOWN + 5.5 * LEFT)

        self.play(FadeOut(first_arrow), FadeOut(second_arrow), FadeOut(framebox2), FadeOut(framebox1))



        text_3 = text_position('>>> listE[3:0:-2]', 1.8 * DOWN + 5 * LEFT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[4], buff = .1)
        framebox2 = SurroundingRectangle(text[8], buff = .1)
        self.play(
            ShowCreation(framebox1),ShowCreation(framebox2)
        )
        self.wait(1)

        first_arrow = CurvedArrow(1.6 * UP + 0.2 * LEFT,  2.3 * DOWN + 4 * LEFT, angle=-1.23)
        second_arrow = CurvedArrow(1.6 * UP + 2.2 * RIGHT,  2.3 * DOWN + 4 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow), ShowCreation(first_arrow))
        text_4 = text_position("[False, 20.3]", 2.3 * DOWN + 5.5 * LEFT)

        self.play(FadeOut(first_arrow), FadeOut(second_arrow), FadeOut(framebox2), FadeOut(framebox1),
            FadeOut(text_15), FadeOut(text_13), FadeOut(text_16), FadeOut(text_14))

        text_13 = text_position('>>> listE[::-1]', 0.5 * DOWN + 3 * RIGHT)
        self.wait(1)
        framebox1 = SurroundingRectangle(text[2:9], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = CurvedArrow(1.6 * UP + 0.9 * RIGHT,  1 * DOWN + 1.5 * RIGHT, angle=2.23)
        self.play(ShowCreation(first_arrow))
        self.wait(1)
        text_14 = text_position("[False, 6, 20.3, 'one']", 1 * DOWN + 4 * RIGHT)

        self.wait(4)
