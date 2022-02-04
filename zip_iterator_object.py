from manim import *
from colour import Color


class ListTricks(Scene):
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
            self.play(GrowFromCenter(explain_filled_rect, run_time=0.3))
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
                GrowFromEdge(explain_line_bottom, LEFT), run_time=0.3
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


        text_print_box = dataframe_swap_scale(12, 3, DARKER_GRAY)
        text_print_box.shift(0.01 * UP + 0.2 * RIGHT)
        self.play(Create(text_print_box), run_time=0.2)
        think_frame_text = """      Question to explain:\n\nWhy can't zip function object iterate\ntwice over the same data?"""       
        think_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{think_frame_text}</b></span>').scale(0.7)
        think_frame_text_style.shift(0.01 * UP + 0.2 * RIGHT)
        self.play(Write(think_frame_text_style), run_time=3)
        self.wait(2)

        self.play(ShrinkToCenter(text_print_box), ShrinkToCenter(think_frame_text_style), run_time=0.3)

        fixed_left_code_box = create_rectange(12, 7, 0.1 * DOWN + 0.001 * RIGHT, DARKER_GRAY)
        heading_one = """Interactive shell"""       
        heading_one_style = MarkupText(f'<span font_family="monospace"><b>{heading_one}</b></span>').scale(0.3)
        heading_one_style.shift(3.54 * UP + 5 * LEFT)
        self.play(Write(heading_one_style), run_time=0.2)
        

        left_side_code = """>>> num_list = ['one', 'two', 'three', 'four']
>>> fruits_list = ['apple', 'grapes', 'cherry', 'orange']
>>> zip_fruits_num = zip(num_list, fruits_list)
>>> for i in zip_fruits_num:
...     print(i)
... 
('one', 'apple')
('two', 'grapes')
('three', 'cherry')
('four', 'orange')
>>> for i in zip_fruits_num:
...     print(i)
... 
>>>
"""       
        left_side_style = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code}</b></span>',
                      0.35, GREY_A, 1.35 * UP + 2.05 * LEFT)
        left_side_style[0:3].set_color(RED_D)
        left_side_style[13:18].set_color(GREEN_E) # one
        left_side_style[19:24].set_color(GREEN_E) #  two
        left_side_style[25:32].set_color(GREEN_E) #  three
        left_side_style[33:39].set_color(GREEN_E) #
        left_side_style[40:43].set_color(RED_D) # 
        left_side_style[56:63].set_color(GREEN_E) # apple
        left_side_style[64:72].set_color(GREEN_E) # grapes
        left_side_style[73:81].set_color(GREEN_E) # cherry
        left_side_style[82:90].set_color(GREEN_E) # orange
        left_side_style[91:94].set_color(RED_D) #
        left_side_style[109:112].set_color(BLUE_D) # zip
        left_side_style[134:137].set_color(RED_D) #
        left_side_style[137:140].set_color(ORANGE) #for
        left_side_style[141:143].set_color(ORANGE) #in
        left_side_style[158:161].set_color(RED_D) #
        left_side_style[161:166].set_color(BLUE_D) #print
        left_side_style[169:172].set_color(RED_D) #
        left_side_style[238:241].set_color(RED_D) #
        left_side_style[241:244].set_color(ORANGE) #for
        left_side_style[245:247].set_color(ORANGE) #i
        left_side_style[262:265].set_color(RED_D) #
        left_side_style[265:270].set_color(BLUE_D) #print
        left_side_style[273:276].set_color(RED_D) #
        left_side_style[276:].set_color(RED_D) #



        self.play(Write(left_side_style[:91]), run_time=2)

        heading_one1 = """num_list"""       
        heading_one_style1 = MarkupText(f'<span font_family="monospace"><b>{heading_one1}</b></span>').scale(0.3)
        heading_one_style1.shift(0.45* UP + 0.5 * RIGHT)
        self.play(FocusOn(heading_one_style1))
        self.play(Write(heading_one_style1),run_time=0.3)


        heading_one2 = """fruits_list"""       
        heading_one_style2 = MarkupText(f'<span font_family="monospace"><b>{heading_one2}</b></span>').scale(0.3)
        heading_one_style2.shift(0.45 * UP + 2 * RIGHT)
        


        object_box_left = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left.shift(0.01 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left))
        object_frame_text_left = """'one'"""       
        object_frame_text_style_left = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left}</b></span>').scale(0.25)
        object_frame_text_style_left.shift(0.01 * DOWN + 0.5 * RIGHT)

        object_box_right = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_right.shift(0.01 * DOWN + 2 * RIGHT)
        # self.play()
        object_frame_text_right = """'apple'"""       
        object_frame_text_style_right = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_right}</b></span>').scale(0.25)
        object_frame_text_style_right.shift(0.01 * DOWN + 2 * RIGHT)


        object_box_left1 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left1.shift(0.75 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left1))
        object_frame_text_left1 = """'two'"""       
        object_frame_text_style_left1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left1}</b></span>').scale(0.25)
        object_frame_text_style_left1.shift(0.75 * DOWN + 0.5 * RIGHT)

        object_box_right1 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_right1.shift(0.75 * DOWN + 2 * RIGHT)
        # self.play(Create(object_box_right1))
        object_frame_text_right1 = """'grapes'"""       
        object_frame_text_style_right1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_right1}</b></span>').scale(0.25)
        object_frame_text_style_right1.shift(0.75 * DOWN + 2 * RIGHT)



        object_box_left2 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left2.shift(1.5 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left2))
        object_frame_text_left2 = """'three'"""       
        object_frame_text_style_left2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left2}</b></span>').scale(0.25)
        object_frame_text_style_left2.shift(1.5 * DOWN + 0.5 * RIGHT)

        object_box_right2 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_right2.shift(1.5 * DOWN + 2 * RIGHT)
        # self.play(Create(object_box_right2))
        object_frame_text_right2 = """'cherry'"""       
        object_frame_text_style_right2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_right2}</b></span>').scale(0.25)
        object_frame_text_style_right2.shift(1.5 * DOWN + 2 * RIGHT)


        object_box_left3 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left3.shift(2.2 * DOWN + 0.5 * RIGHT)
        # self.play(FocusOn(object_box_left))
        self.play(Create(object_box_left3), Create(object_box_left2), Create(object_box_left1), Create(object_box_left))
        object_frame_text_left3 = """'four'"""       
        object_frame_text_style_left3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left3}</b></span>').scale(0.25)
        object_frame_text_style_left3.shift(2.2 * DOWN + 0.5 * RIGHT)
        self.play(FocusOn(left_side_style[13:18]))
        self.play(TransformFromCopy(left_side_style[33:39], object_frame_text_style_left3),
                  TransformFromCopy(left_side_style[13:18], object_frame_text_style_left),
                  TransformFromCopy(left_side_style[19:24], object_frame_text_style_left1),
                  TransformFromCopy(left_side_style[25:32], object_frame_text_style_left2), run_time=1)

        # self.play(FocusOn(heading_one_style2))
        self.play(Write(heading_one_style2), run_time=0.3)

        object_box_right3 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_right3.shift(2.2 * DOWN + 2 * RIGHT)
        # self.play(FocusOn(object_box_right))
        self.play(Create(object_box_right3), Create(object_box_right), Create(object_box_right1), Create(object_box_right2))
        object_frame_text_right3 = """'orange'"""       
        object_frame_text_style_right3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_right3}</b></span>').scale(0.25)
        object_frame_text_style_right3.shift(2.2 * DOWN + 2 * RIGHT)
        self.play(FocusOn(left_side_style[56:63]))
        self.play(TransformFromCopy(left_side_style[82:90], object_frame_text_style_right3),
                  TransformFromCopy(left_side_style[73:81], object_frame_text_style_right2),
                  TransformFromCopy(left_side_style[64:72], object_frame_text_style_right1),
                  TransformFromCopy(left_side_style[56:63], object_frame_text_style_right), run_time=1)


        heading_one3 = """Index"""       
        heading_one_style3 = MarkupText(f'<span font_family="monospace"><b>{heading_one3}</b></span>').scale(0.2)
        heading_one_style3.shift(0.25 * UP + 0.2 * LEFT)
        self.play(FocusOn(heading_one_style3))
        self.play(Write(heading_one_style3), run_time=0.3)

        heading_one4 = """1"""       
        heading_one_style4 = MarkupText(f'<span font_family="monospace"><b>{heading_one4}</b></span>').scale(0.3)
        heading_one_style4.shift(0.01 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style4), run_time=0.1)

        heading_one5 = """2"""       
        heading_one_style5 = MarkupText(f'<span font_family="monospace"><b>{heading_one5}</b></span>').scale(0.3)
        heading_one_style5.shift(0.75 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style5), run_time=0.1)

        heading_one6 = """3"""       
        heading_one_style6 = MarkupText(f'<span font_family="monospace"><b>{heading_one6}</b></span>').scale(0.3)
        heading_one_style6.shift(1.5 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style6), run_time=0.1)

        heading_one7 = """4"""       
        heading_one_style7 = MarkupText(f'<span font_family="monospace"><b>{heading_one7}</b></span>').scale(0.3)
        heading_one_style7.shift(2.2 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style7), run_time=0.1)

        self.play(FocusOn(left_side_style[91]))
        self.play(Write(left_side_style[91:134]), run_time=2)


        heading_one8 = """zip_fruits_num"""       
        heading_one_style8 = MarkupText(f'<span font_family="monospace"><b>{heading_one8}</b></span>').scale(0.3)
        heading_one_style8.shift(0.45 * UP + 5.5 * RIGHT)
        self.play(FocusOn(heading_one_style8))
        self.play(Write(heading_one_style8), run_time=0.3)



        object_box_extremer = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer), run_time=0.1)
        object_frame_text_extremer = """('one', 'apple')"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)



        object_box_extremer1 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer1), run_time=0.1)
        object_frame_text_extremer1 = """('two', 'grapes')"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)


        object_box_extremer2 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer2), run_time=0.1)
        object_frame_text_extremer2 = """('three', 'cherry')"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)


        object_box_extremer3 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer3), run_time=0.1)
        object_frame_text_extremer3 = """('four', 'orange')"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)

        object_default = """zip(num_list, fruits_list)"""       
        object_default1 = MarkupText(f'<span font_family="monospace"><b>{object_default}</b></span>').scale(0.2)
        object_default1.shift(1.1 * DOWN + 3.3 * RIGHT)
        arrow_default = Arrow(1.3 * DOWN + 2.6 * RIGHT, 1.3 * DOWN + 4.2 * RIGHT, color=BLUE_D, buff=0)
        self.play(Write(object_default1), Create(arrow_default), run_time=0.7)

        self.play(Write(object_frame_text_style_extremer), run_time=0.7)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.6)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.5)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.4)

        self.play(FocusOn(left_side_style[134]))
        self.play(Write(left_side_style[134:172]), run_time=2)

        fixed_left_code_box1 = create_rectange(6, 3, 0.5 * UP + 0.001 * LEFT, DARKER_GRAY)

        left_side_code3 = """>>> next(zip_fruits_num)
>>> next(zip_fruits_num)
>>> next(zip_fruits_num)
>>> next(zip_fruits_num)
>>> next(zip_fruits_num)
Traceback (most recent call last):
  File "&lt;stdin>", line 1, in &lt;module>
StopIteration
"""       
        left_side_style3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code3}</b></span>',
                      0.35, GREY_A, 0.5 * UP + 0.4 * LEFT)
        left_side_style3[0:3].set_color(RED_D)
        left_side_style3[3:7].set_color(BLUE_D) # next
        left_side_style3[23:26].set_color(RED_D) #  
        left_side_style3[26:30].set_color(BLUE_D) #  next
        left_side_style3[46:49].set_color(RED_D) #
        left_side_style3[49:53].set_color(BLUE_D) # next
        left_side_style3[69:72].set_color(RED_D) # 
        left_side_style3[72:76].set_color(BLUE_D) # next
        left_side_style3[92:95].set_color(RED_D) # 
        left_side_style3[95:103].set_color(BLUE_D) # next


        

        frame_itr1 = SurroundingRectangle(object_frame_text_style_extremer, buff=0.1)
        frame_itr1.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr1), run_time=0.5)
        arrow_to_1 = Arrow(frame_itr1.get_left(), SurroundingRectangle(left_side_style[172:187], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_1), run_time=0.5)
        self.play(Write(left_side_style3[:23]), run_time=0.4)
        self.play(Write(left_side_style[172:187]), Unwrite(object_frame_text_style_extremer), run_time=0.3)

        self.play(FadeOut(arrow_to_1), FadeOut(frame_itr1), run_time=0.2)


        frame_itr2 = SurroundingRectangle(object_frame_text_style_extremer1, buff=0.1)
        frame_itr2.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr2), run_time=0.5)
        arrow_to_2 = Arrow(frame_itr2.get_left(), SurroundingRectangle(left_side_style[187:203], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_2), run_time=0.5)
        self.play(Write(left_side_style3[23:46]), run_time=0.4)
        self.play(Write(left_side_style[187:203]), Unwrite(object_frame_text_style_extremer1), run_time=0.3)

        self.play(FadeOut(arrow_to_2), FadeOut(frame_itr2), run_time=0.2)


        frame_itr3 = SurroundingRectangle(object_frame_text_style_extremer2, buff=0.1)
        frame_itr3.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr3), run_time=0.5)
        arrow_to_3 = Arrow(frame_itr3.get_left(), SurroundingRectangle(left_side_style[203:221], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_3), run_time=0.5)
        self.play(Write(left_side_style3[46:69]), run_time=0.4)
        self.play(Write(left_side_style[203:221]), Unwrite(object_frame_text_style_extremer2), run_time=0.3)
        

        self.play(FadeOut(arrow_to_3), FadeOut(frame_itr3), run_time=0.2)


        frame_itr4 = SurroundingRectangle(object_frame_text_style_extremer3, buff=0.1)
        frame_itr4.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr4), run_time=0.5)
        arrow_to_4 = Arrow(frame_itr4.get_left(), SurroundingRectangle(left_side_style[221:238], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_4), run_time=0.5)
        self.play(Write(left_side_style3[69:92]), run_time=0.4)
        self.play(Write(left_side_style[221:238]), Unwrite(object_frame_text_style_extremer3), run_time=0.3)
        self.play(FadeOut(arrow_to_4), FadeOut(frame_itr4), run_time=0.2)


        object_box_right121 = dataframe_swap_scale(8, 0.8, BLACK)
        object_box_right121.shift(2 * DOWN + 3 * LEFT)

        stop_itr = """StopIteration"""       
        stop_itr_st = MarkupText(f'<span font_family="monospace"><b>{stop_itr}</b></span>').scale(0.3)
        stop_itr_st.shift(2.8 * DOWN + 5.5 * RIGHT)
        self.play(Write(stop_itr_st), run_time=0.2)

        frame_itr8 = SurroundingRectangle(stop_itr_st, buff=0.1)
        frame_itr8.set_fill(color=BLUE_D, opacity=0.2)
        arrow_to_8 = Arrow(frame_itr8.get_left(), object_box_right121.get_right(), color=BLUE_D, buff=0)

        self.play(Write(left_side_style3[92:]), run_time=0.4)
        frame_itr9 = SurroundingRectangle(left_side_style3[92:], buff=0.1)
        frame_itr9.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr9),Create(frame_itr8), run_time=0.5)
        arrow_to_9 = Arrow(frame_itr9.get_bottom(), object_box_right121.get_top(), color=BLUE_D, buff=0)
        self.play(Create(arrow_to_9),Create(arrow_to_8), run_time=0.5)
        self.play(Create(object_box_right121), run_time=0.2)

        stop_itr1 = """For loop will end the loop and next() function will raise\nStopIteration error when the iterator has been consumed."""       
        stop_itr_st1 = MarkupText(f'<span font_family="monospace"><b>{stop_itr1}</b></span>').scale(0.3)
        stop_itr_st1.shift(2 * DOWN + 3 * LEFT)
        self.play(Write(stop_itr_st1), run_time=2)
        self.wait(2)

        self.play(ShrinkToCenter(frame_itr8), ShrinkToCenter(frame_itr9), FadeOut(arrow_to_8), 
                  FadeOut(arrow_to_9), run_time=0.4)
        self.play(ShrinkToCenter(fixed_left_code_box1[0]), ShrinkToCenter(fixed_left_code_box1[1]), 
                  ShrinkToCenter(fixed_left_code_box1[2]), ShrinkToCenter(left_side_style3), run_time=0.3)
        self.play(ShrinkToCenter(object_box_right121), ShrinkToCenter(stop_itr_st1), run_time=0.3)

        self.play(FocusOn(left_side_style[238]))
        self.play(Write(left_side_style[238:]))

        object_box_right122 = dataframe_swap_scale(8, 1, BLACK)
        object_box_right122.shift(1.5 * UP + 3 * RIGHT)
        self.play(Create(object_box_right122), run_time=0.3)
        stop_itr2 = """If we try to iterate over zip_fruits_num again, we'll get the StopIteration exception, because the iterator has already been consumed."""       
        stop_itr_st2 = MarkupText(f'<span font_family="monospace"><b>{stop_itr2}</b></span>').scale(0.3)
        stop_itr_st2.shift(1.5 * UP + 3 * RIGHT)
        frame_itr8 = SurroundingRectangle(stop_itr_st, buff=0.1)
        frame_itr8.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Write(stop_itr_st2), Wiggle(stop_itr_st), Create(frame_itr8), run_time=3)
        self.wait(2)



        # --------------------- bring back after sometime time has come

        left_side_code1 = """>>> print(list(zip_fruits_num))
[('one', 'apple'), ('two', 'grapes'), 
('three', 'cherry'), ('four', 'orange')]
>>> print(list(zip_fruits_num))
[]
>>> zip_fruits_num = zip(num_list, fruits_list)
>>> fruits_num_list = list(zip_fruits_num)
>>> fruits_num_list
[('one', 'apple'), ('two', 'grapes'), 
('three', 'cherry'), ('four', 'orange')]
>>> fruits_num_list
[('one', 'apple'), ('two', 'grapes'), 
('three', 'cherry'), ('four', 'orange')]"""       
        left_side_style1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code1}</b></span>',
                      0.35, GREY_A, 0.3 * DOWN + 2.75 * LEFT)
        left_side_style1[0:3].set_color(RED_D)
        left_side_style1[3:8].set_color(BLUE_D) # print
        left_side_style1[9:13].set_color(BLUE_D) #  list
        left_side_style1[101:104].set_color(RED) #  
        left_side_style1[104:109].set_color(BLUE_D) # print
        left_side_style1[110:114].set_color(BLUE_D) # list
        left_side_style1[133:136].set_color(RED_D) # 
        left_side_style1[151:154].set_color(BLUE_D) # zip
        left_side_style1[176:179].set_color(RED_D) # 

        left_side_style1[195:199].set_color(BLUE_D) # list
        left_side_style1[215:218].set_color(RED) # 
        left_side_style1[304:307].set_color(RED_D) #

        object_box_right123 = dataframe_swap_scale(8, 0.8, BLACK)
        object_box_right123.shift(0.5 * UP + 3 * RIGHT)
        self.play(Create(object_box_right123), run_time=0.3)
        stop_itr3 = """StopIteration exception also will be raised, if you use other ways to iterate, like List."""       
        stop_itr_st3 = MarkupText(f'<span font_family="monospace"><b>{stop_itr3}</b></span>').scale(0.3)
        stop_itr_st3.shift(0.5 * UP + 3 * RIGHT)
        self.play(Write(stop_itr_st3), run_time=2)
        self.wait(2)

        left_side_style1.shift(1.3 * DOWN)
        self.play(FocusOn(left_side_style1[101]))
        self.play(Write(left_side_style1[101:133]), run_time=2)
        self.wait(1)

        text_print_box = dataframe_swap_scale_opacity(12, 1.2, DARKER_GRAY, 1)
        text_print_box.shift(0.01 * UP + 0.2 * RIGHT)
        self.play(Create(text_print_box), run_time=0.5)
        think_frame_text = """Question: What if we do need to traverse the iterator\nmore than once?"""       
        think_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{think_frame_text}</b></span>').scale(0.5)
        think_frame_text_style.shift(0.01 * UP + 0.2 * RIGHT)
        self.play(Write(think_frame_text_style), run_time=2)
        self.wait(1)

        text_print_box1 = dataframe_swap_scale_opacity(12, 1.2, DARKER_GRAY, 1)
        text_print_box1.shift(2 * DOWN + 0.2 * RIGHT)
        self.play(Create(text_print_box1), run_time=0.5)
        think_frame_text1 = """Solution: Create a list with the elements, and\nwe can traverse it as many times as needed."""       
        think_frame_text_style1 = MarkupText(f'<span font_family="monospace"><b>{think_frame_text1}</b></span>').scale(0.5)
        think_frame_text_style1.shift(2 * DOWN + 0.2 * RIGHT)
        self.play(Write(think_frame_text_style1), run_time=2)
        self.wait(1)

        left_side_style.set_color(DARK_GRAY)
        left_side_style1[:133].set_color(DARK_GRAY)

        self.play(ShrinkToCenter(object_box_right122), ShrinkToCenter(stop_itr_st2), FadeOut(frame_itr8), run_time=0.4)
        self.play(ShrinkToCenter(object_box_right123), ShrinkToCenter(stop_itr_st3), run_time=0.3)
        self.play(ShrinkToCenter(text_print_box), ShrinkToCenter(think_frame_text_style), run_time=0.3)
        self.play(ShrinkToCenter(text_print_box1), ShrinkToCenter(think_frame_text_style1), run_time=0.3)

        self.play(FocusOn(left_side_style1[133]))
        self.play(Write(left_side_style1[133:215]), run_time=2.5)
        self.wait(0.5)

        self.play(FadeOut(heading_one_style8), run_time=0.3)
        heading_one8 = """fruits_num_list"""       
        heading_one_style8 = MarkupText(f'<span font_family="monospace"><b>{heading_one8}</b></span>').scale(0.3)
        heading_one_style8.shift(0.45 * UP + 5.5 * RIGHT)
        self.play(FocusOn(heading_one_style8))
        self.play(Write(heading_one_style8), run_time=0.3)


        object_frame_text_extremer = """('one', 'apple')"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)

        object_frame_text_extremer1 = """('two', 'grapes')"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)

        object_frame_text_extremer2 = """('three', 'cherry')"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)

        object_frame_text_extremer3 = """('four', 'orange')"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)

        self.play(Write(object_frame_text_style_extremer), run_time=0.6)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.5)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.4)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.3)

        self.play(FocusOn(left_side_style1[215]))
        self.play(Write(left_side_style1[215:]), run_time=2)
        self.wait(1)

        self.play(
            *[ShrinkToCenter(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        self.play(
            *[FadeOut(mob)for mob in self.mobjects], run_time=0.1
            # All mobjects in the screen are saved in self.mobjects
        )

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
        self.wait(1)
