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

        object_frame_text_heading1 = """zip(*iterables)"""       
        object_frame_text_style_heading1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading1}</b></span>').scale(0.5)
        object_frame_text_style_heading1.shift(0.05 * UP + 0.03 * RIGHT)
        self.play(Write(object_frame_text_style_heading1), run_time=1)

        object_frame_text_heading101 = """This video will explain"""       
        object_frame_text_style_heading101 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading101}</b></span>').scale(0.5)
        object_frame_text_style_heading101.shift(3.2 * UP + 4.5 * RIGHT)
        self.play(Write(object_frame_text_style_heading101), run_time=0.5)
        self.wait(0.5)

        object_box_headingx= dataframe_swap_scale(3, 0.4, BLACK)
        object_box_headingx.shift(0.05 * UP + 5.5 * LEFT)
        object_frame_text_headingx = """Introduction"""       
        object_frame_text_style_headingx = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_headingx}</b></span>').scale(0.35)
        object_frame_text_style_headingx.shift(0.05 * UP + 5.5 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading1, buff=0.1).get_left(), 
                      SurroundingRectangle(object_frame_text_style_headingx, buff=0).get_right(),color=BLUE_D)
        self.play(Create(line11), run_time=0.1)
        self.play(Create(object_box_headingx), run_time=0.001)
        self.play(Write(object_frame_text_style_headingx), run_time=0.2)


        object_box_heading= dataframe_swap_scale(6.2, 0.4, BLACK)
        object_box_heading.shift(1 * DOWN + 0.03 * RIGHT)
        
        object_frame_text_heading = """Pass different Data types in zip() function"""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.35)
        object_frame_text_style_heading.shift(1 * DOWN + 0.01 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading1, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_frame_text_style_heading, buff=0).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)
        self.play(Create(object_box_heading), run_time=0.01)
        self.play(Write(object_frame_text_style_heading), run_time=0.1)

        object_box_heading2= dataframe_swap_scale(5, 0.4, BLACK)
        object_box_heading2.shift(1 * UP + 0.03 * RIGHT)
        
        object_frame_text_heading2 = """Iterate over zip() object"""       
        object_frame_text_style_heading2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading2}</b></span>').scale(0.35)
        object_frame_text_style_heading2.shift(1 * UP + 0.03 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading1, buff=0.1).get_top(), 
                      SurroundingRectangle(object_frame_text_style_heading2, buff=0).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)   
        self.play(Create(object_box_heading2), run_time=0.01)     
        self.play(Write(object_frame_text_style_heading2), run_time=0.1)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 0.03 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Tuple"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 0.03 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 0.03 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Tuple"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 0.03 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)


        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 2 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Dict"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 2 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 2 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Dict"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 2 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)


        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 2 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Set"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 2 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 2 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Set"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 2 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)



        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 4 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """List"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 4 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 4 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """List"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 4 * RIGHT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)


        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 4 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Str"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 4 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 4 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Str"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 4 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)


        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 6 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Int"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 6 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_top(), 
                      SurroundingRectangle(object_box_heading, buff=0.1).get_bottom(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)         
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        object_box_heading3= dataframe_swap_scale(1, 0.4, BLACK)
        object_box_heading3.shift(2.5 * UP + 6 * LEFT)
        self.play(Create(object_box_heading3), run_time=0.01)
        object_frame_text_heading3 = """Int"""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.35)
        object_frame_text_style_heading3.shift(2.5 * UP + 6 * LEFT)
        line11 = Line(SurroundingRectangle(object_frame_text_style_heading3, buff=0.1).get_bottom(), 
                      SurroundingRectangle(object_box_heading2, buff=0.1).get_top(),color=BLUE_D)
        self.play(Create(line11), run_time=0.01)  
        self.play(Write(object_frame_text_style_heading3), run_time=0.01)

        self.wait(3)
        heading_one = """Interactive shell"""
        heading_one_style = MarkupText(f'<span font_family="monospace"><b>{heading_one}</b></span>').scale(0.3)
        heading_one_style.shift(3.54 * UP + 5 * LEFT)
        self.play(
            *[ShrinkToCenter(mob)for mob in self.mobjects], Write(heading_one_style), run_time=0.5
            # All mobjects in the screen are saved in self.mobjects
        )
        
        fixed_left_code_box = create_rectange(12, 7, 0.1 * DOWN + 0.001 * RIGHT, DARKER_GRAY)
          

        left_side_code = """>>> num_list = ['one', 'two', 'three', 'four']
>>> fruits_list = ['apple', 'grapes', 'cherry', 'orange']
>>> zip(num_list, fruits_list) 
  &lt;zip object at 0x7fa8e7b3a600>
>>> list(zip(num_list, fruits_list))
  [('one', 'apple'), ('two', 'grapes'), 
  ('three', 'cherry'), ('four', 'orange')]"""       
        left_side_style = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code}</b></span>',
                      0.35, GREY_A, 2.1 * UP + 2.05 * LEFT)
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
        left_side_style[94:97].set_color(BLUE_D) # zip
        left_side_style[146:149].set_color(RED_D) #
        left_side_style[149:153].set_color(BLUE_D) #
        left_side_style[154:157].set_color(BLUE_D) #

        self.play(Write(left_side_style[:91]), run_time=2)

        heading_one1 = """num_list"""       
        heading_one_style1 = MarkupText(f'<span font_family="monospace"><b>{heading_one1}</b></span>').scale(0.3)
        heading_one_style1.shift(0.45* UP + 0.5 * RIGHT)
        self.play(FocusOn(heading_one_style1))
        self.play(Write(heading_one_style1),run_time=0.5)


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
                  TransformFromCopy(left_side_style[25:32], object_frame_text_style_left2), run_time=2)

        # self.play(FocusOn(heading_one_style2))
        self.play(Write(heading_one_style2), run_time=0.5)

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
                  TransformFromCopy(left_side_style[56:63], object_frame_text_style_right), run_time=2)


        heading_one3 = """Index"""       
        heading_one_style3 = MarkupText(f'<span font_family="monospace"><b>{heading_one3}</b></span>').scale(0.2)
        heading_one_style3.shift(0.25 * UP + 0.2 * LEFT)
        self.play(FocusOn(heading_one_style3))
        self.play(Write(heading_one_style3), run_time=0.5)

        heading_one4 = """1"""       
        heading_one_style4 = MarkupText(f'<span font_family="monospace"><b>{heading_one4}</b></span>').scale(0.3)
        heading_one_style4.shift(0.01 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style4), run_time=0.2)

        heading_one5 = """2"""       
        heading_one_style5 = MarkupText(f'<span font_family="monospace"><b>{heading_one5}</b></span>').scale(0.3)
        heading_one_style5.shift(0.75 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style5), run_time=0.2)

        heading_one6 = """3"""       
        heading_one_style6 = MarkupText(f'<span font_family="monospace"><b>{heading_one6}</b></span>').scale(0.3)
        heading_one_style6.shift(1.5 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style6), run_time=0.2)

        heading_one7 = """4"""       
        heading_one_style7 = MarkupText(f'<span font_family="monospace"><b>{heading_one7}</b></span>').scale(0.3)
        heading_one_style7.shift(2.2 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style7), run_time=0.2)

        self.play(FocusOn(left_side_style[91]))
        self.play(Write(left_side_style[91:146]), run_time=2)

        object_box_heading3xx= dataframe_swap_scale(7, 0.8, BLACK)
        object_box_heading3xx.shift(3 * UP + 3 * RIGHT)
        object_frame_text_heading3xx = """The zip() function takes in one or more \niterables as arguments."""       
        object_frame_text_style_heading3xx = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3xx}</b></span>').scale(0.35)
        object_frame_text_style_heading3xx.shift(3 * UP + 3 * RIGHT)
        cur_arrow_str = CurvedArrow(SurroundingRectangle(left_side_style[91:119], buff=0).get_right(), 
                                    object_box_heading3xx.get_bottom(), color=RED_D, angle=1)
        
        self.play(Create(object_box_heading3xx), Create(cur_arrow_str), run_time=0.3)
        self.play(Write(object_frame_text_style_heading3xx), run_time=2)
        self.wait(1)
        self.play(ShrinkToCenter(cur_arrow_str), ShrinkToCenter(object_box_heading3xx), 
                  ShrinkToCenter(object_frame_text_style_heading3xx), run_time=0.3)



        heading_one8 = """Iterator of Tuples"""       
        heading_one_style8 = MarkupText(f'<span font_family="monospace"><b>{heading_one8}</b></span>').scale(0.3)
        heading_one_style8.shift(0.45 * UP + 5.5 * RIGHT)
        self.play(FocusOn(heading_one_style8))
        self.play(Write(heading_one_style8), run_time=0.5)



        object_box_extremer = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer), run_time=0.3)
        arrow_z = Arrow(object_box_right.get_right(), object_box_extremer.get_left(), color=BLUE_D, buff=0)
        object_zip = """zip('one','apple')"""       
        object_zip = MarkupText(f'<span font_family="monospace"><b>{object_zip}</b></span>').scale(0.2)
        object_zip.shift(0.1 * UP + 3.3 * RIGHT)
        object_frame_text_extremer = """('one', 'apple')"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)



        object_box_extremer1 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer1), run_time=0.3)
        arrow_z1 = Arrow(object_box_right1.get_right(), object_box_extremer1.get_left(), color=BLUE_D, buff=0)
        object_zip1 = """zip('two', 'grapes')"""       
        object_zip1 = MarkupText(f'<span font_family="monospace"><b>{object_zip1}</b></span>').scale(0.2)
        object_zip1.shift(0.65 * DOWN + 3.3 * RIGHT)
        object_frame_text_extremer1 = """('two', 'grapes')"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)


        object_box_extremer2 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer2), run_time=0.3)
        arrow_z2 = Arrow(object_box_right2.get_right(), object_box_extremer2.get_left(), color=BLUE_D, buff=0)
        object_zip2 = """zip('three', 'cherry')"""       
        object_zip2 = MarkupText(f'<span font_family="monospace"><b>{object_zip2}</b></span>').scale(0.2)
        object_zip2.shift(1.35 * DOWN + 3.3 * RIGHT)
        object_frame_text_extremer2 = """('three', 'cherry')"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)


        object_box_extremer3 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)
        self.play(Create(object_box_extremer3), run_time=0.3)
        arrow_z3 = Arrow(object_box_right3.get_right(), object_box_extremer3.get_left(), color=BLUE_D, buff=0)
        object_zip3 = """zip('four', 'orange')"""       
        object_zip3 = MarkupText(f'<span font_family="monospace"><b>{object_zip3}</b></span>').scale(0.2)
        object_zip3.shift(2.05 * DOWN + 3.3 * RIGHT)
        object_frame_text_extremer3 = """('four', 'orange')"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)

        self.play(Create(arrow_z), Create(arrow_z1), Create(arrow_z2), Create(arrow_z3))
        self.play(Write(object_zip), run_time=0.8)
        self.play(Write(object_zip1), run_time=0.7)
        self.play(Write(object_zip2), run_time=0.6)
        self.play(Write(object_zip3), run_time=0.5)

        self.play(Write(object_frame_text_style_extremer), run_time=0.8)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.7)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.6)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.5)

        self.play(FocusOn(left_side_style[146:180]))
        self.play(Write(left_side_style[146:180]), run_time=0.7)
        self.play(FadeOut(arrow_z), FadeOut(object_zip), run_time=0.4)
        self.play(FadeOut(arrow_z1), FadeOut(object_zip1), run_time=0.4)
        self.play(FadeOut(arrow_z2), FadeOut(object_zip2), run_time=0.4)
        self.play(FadeOut(arrow_z3), FadeOut(object_zip3), run_time=0.4)
        self.wait(0.7)
        
        object_default = """zip(num_list, fruits_list)"""       
        object_default1 = MarkupText(f'<span font_family="monospace"><b>{object_default}</b></span>').scale(0.2)
        object_default1.shift(1.1 * DOWN + 3.3 * RIGHT)
        arrow_default = Arrow(1.3 * DOWN + 2.6 * RIGHT, 1.3 * DOWN + 4.2 * RIGHT, color=BLUE_D, buff=0)
        self.play(Write(object_default1), Create(arrow_default))

        frame_itr1 = SurroundingRectangle(object_frame_text_style_extremer, buff=0.1)
        frame_itr1.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr1), run_time=0.5)
        arrow_to_1 = Arrow(frame_itr1.get_left(), SurroundingRectangle(left_side_style[181:196], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_1), run_time=0.5)
        self.play(Write(left_side_style[181:196]), Write(left_side_style[180]), Write(left_side_style[196]), run_time=0.3)

        self.play(FadeOut(arrow_to_1), FadeOut(frame_itr1), run_time=0.3)


        frame_itr2 = SurroundingRectangle(object_frame_text_style_extremer1, buff=0.1)
        frame_itr2.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr2), run_time=0.5)
        arrow_to_2 = Arrow(frame_itr2.get_left(), SurroundingRectangle(left_side_style[197:213], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_2), run_time=0.5)
        self.play(Write(left_side_style[197:213]), Write(left_side_style[213]), run_time=0.3)

        self.play(FadeOut(arrow_to_2), FadeOut(frame_itr2), run_time=0.3)


        frame_itr3 = SurroundingRectangle(object_frame_text_style_extremer2, buff=0.1)
        frame_itr3.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr3), run_time=0.5)
        arrow_to_3 = Arrow(frame_itr3.get_left(), SurroundingRectangle(left_side_style[214:232], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_3), run_time=0.5)
        self.play(Write(left_side_style[214:232]), Write(left_side_style[232]), run_time=0.3)

        self.play(FadeOut(arrow_to_3), FadeOut(frame_itr3), run_time=0.3)


        frame_itr4 = SurroundingRectangle(object_frame_text_style_extremer3, buff=0.1)
        frame_itr4.set_fill(color=BLUE_D, opacity=0.2)
        self.play(Create(frame_itr4), run_time=0.5)
        arrow_to_4 = Arrow(frame_itr4.get_left(), SurroundingRectangle(left_side_style[233:250], buff=0).get_right(), color=RED_D, buff=0)
        self.play(Create(arrow_to_4), run_time=0.5)
        self.play(Write(left_side_style[233:250]), Write(left_side_style[250:]), run_time=0.3)

        self.play(FadeOut(arrow_to_4), FadeOut(frame_itr4), run_time=0.5)


        object_box_heading= dataframe_swap_scale(10, 1, BLACK)
        object_box_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Create(object_box_heading), run_time=0.2)
        object_frame_text_heading = """Iterables with Different Lengths"""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.6)
        object_frame_text_style_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Write(object_frame_text_style_heading))
        self.wait(1)
        self.play(ShrinkToCenter(object_frame_text_style_heading), ShrinkToCenter(object_box_heading), run_time=0.4)



        left_side_code1 = """>>> num_list = ['one', 'two', 'three', 'four', 'five']
>>> fruits_list = ['apple', 'grapes', 'cherry', 'orange']
>>> list(zip(num_list, fruits_list))
  [('one', 'apple'), ('two', 'grapes'), 
  ('three', 'cherry'), ('four', 'orange')]"""       
        left_side_style1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code1}</b></span>',
                      0.35, GREY_A, 0.5 * UP + 2.05 * LEFT)
        left_side_style1[0:3].set_color(RED_D)
        left_side_style1[13:18].set_color(GREEN_E) # one
        left_side_style1[19:24].set_color(GREEN_E) #  two
        left_side_style1[25:32].set_color(GREEN_E) #  three
        left_side_style1[33:39].set_color(GREEN_E) # four
        left_side_style1[40:46].set_color(GREEN_E) # five
        left_side_style1[47:50].set_color(RED_D) # 
        left_side_style1[63:70].set_color(GREEN_E) # apple
        left_side_style1[71:79].set_color(GREEN_E) # grapes
        left_side_style1[80:88].set_color(GREEN_E) # cherry
        left_side_style1[89:97].set_color(GREEN_E) # orange
        left_side_style1[98:101].set_color(RED_D) #
        left_side_style1[101:105].set_color(BLUE_D) # list
        left_side_style1[106:109].set_color(BLUE_D) #

        left_side_style.set_color(DARK_GRAY)
        self.play(Write(left_side_style1[:98]), run_time=2)

        object_box_left4 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left4.shift(3 * DOWN + 0.5 * RIGHT)
        self.play(Create(object_box_left4))
        object_frame_text_left4 = """'five'"""       
        object_frame_text_style_left4 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left4}</b></span>').scale(0.25)
        object_frame_text_style_left4.shift(3 * DOWN + 0.5 * RIGHT)
        self.play(FocusOn(left_side_style1[40:46]))
        self.play(TransformFromCopy(left_side_style1[40:46], object_frame_text_style_left4), run_time=0.5)

        heading_one8 = """5"""       
        heading_one_style8 = MarkupText(f'<span font_family="monospace"><b>{heading_one8}</b></span>').scale(0.3)
        heading_one_style8.shift(3 * DOWN + 0.2 * LEFT)
        self.play(Write(heading_one_style8), run_time=0.2)

        self.play(FocusOn(left_side_style1[98:103]))
        self.play(Write(left_side_style1[98:132]))


        object_box_extremer4 = dataframe_swap_scale(2.5, 0.5, BLACK)
        object_box_extremer4.shift(3 * DOWN + 5.5 * RIGHT)
        self.play(FocusOn(object_box_extremer4))
        self.play(Create(object_box_extremer4), run_time=0.3)
        arrow_z4 = Arrow(object_box_left4.get_right(), object_box_extremer4.get_left(), color=BLUE_D, buff=0)
        self.play(Create(arrow_z4))

        wrong_image = ImageMobject("wrong_sign.png")
        wrong_image.scale(0.1)
        wrong_image.shift(3.1 * DOWN + 2.5 * RIGHT)
        self.play(FadeIn(wrong_image))

        object_box_heading1 = dataframe_swap_scale(10, 1, BLACK)
        object_box_heading1.shift(2.5 * UP + 0.01 * RIGHT)
        self.play(Create(object_box_heading1), run_time=0.2)
        object_frame_text_heading = """The iterator stops when the shortest input iterable is exhausted. The shortest input iterable is fruits_list."""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.4)
        object_frame_text_style_heading.shift(2.5 * UP + 0.01 * RIGHT)
        self.play(Write(object_frame_text_style_heading), run_time=2.5)
        self.wait(1)

        self.play(FocusOn(left_side_style1[132]))
        self.play(Write(left_side_style1[132:]))
        self.wait(0.7)

        self.play(ShrinkToCenter(object_box_heading1), ShrinkToCenter(object_frame_text_style_heading), run_time=0.3)
        self.play(FadeOut(wrong_image), FadeOut(arrow_z4), run_time=0.3)


        object_box_heading= dataframe_swap_scale(10, 1.8, BLACK)
        object_box_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Create(object_box_heading), run_time=0.2)
        object_frame_text_heading = """When You Pass in One or No Iterable\nto the zip() Function"""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.6)
        object_frame_text_style_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Write(object_frame_text_style_heading), run_time=2)
        self.wait(1)
        self.play(ShrinkToCenter(object_frame_text_style_heading), ShrinkToCenter(object_box_heading), run_time=0.4)

        self.play(ShrinkToCenter(left_side_style))
        left_side_style1.shift(1.9 * UP)

        left_side_code = """>>> fruits_list = ['apple', 'grapes', 'cherry', 'orange']
>>> list(zip(fruits_list))
  [('apple',), ('grapes',), ('cherry',), ('orange',)]
>>> list(zip())
  []
"""       
        left_side_style = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code}</b></span>',
                      0.35, GREY_A, 0.95 * UP + 2.05 * LEFT)
        left_side_style[0:3].set_color(RED_D)
        left_side_style[16:23].set_color(GREEN_E) # apple
        left_side_style[24:32].set_color(GREEN_E) #  grapes
        left_side_style[33:41].set_color(GREEN_E) #  cherry
        left_side_style[42:50].set_color(GREEN_E) #orange
        left_side_style[51:54].set_color(RED_D) # 
        left_side_style[54:58].set_color(BLUE_D) # 
        left_side_style[59:62].set_color(BLUE_D) # 
        left_side_style[124:127].set_color(RED_D)
        left_side_style[127:131].set_color(BLUE_D)
        left_side_style[132:135].set_color(BLUE_D)

        left_side_style1.set_color(DARK_GRAY)        
        self.play(Write(left_side_style[:76]), run_time=2)


        self.play(ShrinkToCenter(object_box_left3),
                  ShrinkToCenter(object_box_left2), ShrinkToCenter(object_box_left1), ShrinkToCenter(object_box_left4),
                  ShrinkToCenter(object_box_left), run_time=0.3)
        self.play(ShrinkToCenter(object_frame_text_style_left3),
                  ShrinkToCenter(object_frame_text_style_left),
                  ShrinkToCenter(object_frame_text_style_left1),
                  ShrinkToCenter(object_frame_text_style_left2),ShrinkToCenter(object_frame_text_style_left4), 
                  FadeOut(object_default1), FadeOut(arrow_default),
                  FadeOut(heading_one_style8),ShrinkToCenter(heading_one_style1), run_time=0.3)

        self.play(ShrinkToCenter(object_frame_text_style_extremer),ShrinkToCenter(object_frame_text_style_extremer1),
                  ShrinkToCenter(object_frame_text_style_extremer2),ShrinkToCenter(object_frame_text_style_extremer3),
                  ShrinkToCenter(object_box_extremer4), run_time=0.3)

        heading_one_style3.shift(1.32 * RIGHT)
        heading_one_style4.shift(1.5 * RIGHT)
        heading_one_style5.shift(1.5 * RIGHT)
        heading_one_style6.shift(1.5 * RIGHT)
        heading_one_style7.shift(1.5 * RIGHT)


        object_default = """zip(fruits_list)"""       
        object_default1 = MarkupText(f'<span font_family="monospace"><b>{object_default}</b></span>').scale(0.2)
        object_default1.shift(1.1 * DOWN + 3.3 * RIGHT)
        self.play(Write(object_default1), FadeIn(arrow_default))

        object_frame_text_extremer = """('apple',)"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer), run_time=0.8)

        object_frame_text_extremer1 = """('grapes',)"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.7)

        object_frame_text_extremer2 = """('cherry',)"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.6)

        object_frame_text_extremer3 = """('orange',)"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.5)

        self.play(Write(left_side_style[76]), Write(left_side_style[123]), 
                  Write(left_side_style[87]),Write(left_side_style[99]),Write(left_side_style[111]),
                  TransformFromCopy(object_frame_text_style_extremer, left_side_style[77:87]),
                  TransformFromCopy(object_frame_text_style_extremer1, left_side_style[88:99]),
                  TransformFromCopy(object_frame_text_style_extremer2, left_side_style[100:111]),
                  TransformFromCopy(object_frame_text_style_extremer3, left_side_style[112:123]), run_time=2)

        self.wait(1)

        self.play(Write(left_side_style[124:-2]))

        object_box_heading1 = dataframe_swap_scale(10, 1, BLACK)
        object_box_heading1.shift(2.5 * UP + 0.01 * RIGHT)
        self.play(Create(object_box_heading1), run_time=0.2)
        object_frame_text_heading = """zip() function with no arguments, return an empty list"""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.4)
        object_frame_text_style_heading.shift(2.5 * UP + 0.01 * RIGHT)
        self.play(Write(object_frame_text_style_heading))
        self.wait(1)

        self.play(FocusOn(left_side_style[-2:]))
        self.play(Write(left_side_style[-2:]))

        self.wait(1)

        self.play(ShrinkToCenter(object_box_heading1), ShrinkToCenter(object_frame_text_style_heading), run_time=0.4)
        self.play(ShrinkToCenter(left_side_style1[:47]), ShrinkToCenter(left_side_style1[98:]), ShrinkToCenter(left_side_style1), run_time=0.3)

        # ----------------------new weight ******************************************8

        object_box_heading= dataframe_swap_scale(11, 1, BLACK)
        object_box_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Create(object_box_heading), run_time=0.2)
        object_frame_text_heading = """Pass different Data types in zip() function"""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.55)
        object_frame_text_style_heading.shift(0.01 * DOWN + 0.01 * RIGHT)
        self.play(Write(object_frame_text_style_heading))
        self.wait(1)
        self.play(ShrinkToCenter(object_frame_text_style_heading), ShrinkToCenter(object_box_heading),ShrinkToCenter(left_side_style), run_time=0.4)

        left_side_code1 = """>>> num_list = ['one', 'two', 'three', 'four', 'five']
>>> fruits_list = ['apple', 'grapes', 'cherry', 'orange']
>>> list(zip(num_list, fruits_list))
  [('one', 'apple'), ('two', 'grapes'), 
  ('three', 'cherry'), ('four', 'orange')]"""       
        left_side_style1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code1}</b></span>',
                      0.35, GREY_A, 0.5 * UP + 2.05 * LEFT)
        left_side_style1[0:3].set_color(RED_D)
        left_side_style1[13:18].set_color(GREEN_E) # one
        left_side_style1[19:24].set_color(GREEN_E) #  two
        left_side_style1[25:32].set_color(GREEN_E) #  three
        left_side_style1[33:39].set_color(GREEN_E) # four
        left_side_style1[40:46].set_color(GREEN_E) # five
        left_side_style1[47:50].set_color(RED_D) # 
        left_side_style1[63:70].set_color(GREEN_E) # apple
        left_side_style1[71:79].set_color(GREEN_E) # grapes
        left_side_style1[80:88].set_color(GREEN_E) # cherry
        left_side_style1[89:97].set_color(GREEN_E) # orange
        left_side_style1[98:101].set_color(RED_D) #
        left_side_style1[101:105].set_color(BLUE_D) # list
        left_side_style1[106:109].set_color(BLUE_D) #

        left_side_style1.shift(1.9 * UP)
        self.play(Write(left_side_style1[47:98]), run_time=1)
        

        left_side_code = """>>> alpha_str = 'abcd'
>>> list(zip(alpha_str, fruits_list))
  [('a', 'apple'), ('b', 'grapes'), 
  ('c', 'cherry'), ('d', 'orange')]
"""       
        left_side_style = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code}</b></span>',
                      0.35, GREY_A, 1.95 * UP + 3.48 * LEFT)
        left_side_style[0:3].set_color(RED_D)
        left_side_style[13:19].set_color(GREEN_E) # 'abcd'
        left_side_style[19:22].set_color(RED_D) #  
        left_side_style[22:26].set_color(BLUE_D) #  
        left_side_style[27:30].set_color(BLUE_D) #

        self.play(Write(left_side_style[:54]), run_time=2)


        object_box_heading= dataframe_swap_scale(6.5, 1, BLACK)
        object_box_heading.shift(1.5 * UP + 3 * RIGHT)
        self.play(Create(object_box_heading), run_time=0.2)
        object_frame_text_heading = """String and List data types has __iter__\ninbuilt function which makes them valid\ninput for zip() function."""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.3)
        object_frame_text_style_heading.shift(1.5 * UP + 3 * RIGHT)
        cur_arrow_str = CurvedArrow(SurroundingRectangle(left_side_style1[47:98], buff=0).get_right(), 
                                    object_box_heading.get_top(), color=RED_D, angle=-1.23)
        cur_arrow_list = CurvedArrow(SurroundingRectangle(left_side_style[13:19], buff=0).get_bottom(), 
                                    object_box_heading.get_left(), color=RED_D, angle=1.23)
        self.play(Create(cur_arrow_str), Create(cur_arrow_list), run_time=0.5)
        self.play(Write(object_frame_text_style_heading), run_time=2)
        self.wait(1)

        self.play(ShrinkToCenter(object_frame_text_style_extremer),ShrinkToCenter(object_frame_text_style_extremer1),
                  ShrinkToCenter(object_frame_text_style_extremer2),ShrinkToCenter(object_frame_text_style_extremer3), run_time=0.3)

        self.play(FadeOut(object_default1), FadeOut(arrow_default), run_time=0.3)


        heading_one_style3.shift(1.32 * LEFT)
        heading_one_style4.shift(1.5 * LEFT)
        heading_one_style5.shift(1.5 * LEFT)
        heading_one_style6.shift(1.5 * LEFT)
        heading_one_style7.shift(1.5 * LEFT)

        heading_one1 = """alpha_str"""       
        heading_one_style1 = MarkupText(f'<span font_family="monospace"><b>{heading_one1}</b></span>').scale(0.3)
        heading_one_style1.shift(0.45* UP + 0.5 * RIGHT)
        self.play(FocusOn(heading_one_style1))
        self.play(Write(heading_one_style1),run_time=0.5)

        object_box_left = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left.shift(0.01 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left))
        object_frame_text_left = """'a'"""       
        object_frame_text_style_left = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left}</b></span>').scale(0.25)
        object_frame_text_style_left.shift(0.01 * DOWN + 0.5 * RIGHT)

        object_box_left1 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left1.shift(0.75 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left1))
        object_frame_text_left1 = """'b'"""       
        object_frame_text_style_left1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left1}</b></span>').scale(0.25)
        object_frame_text_style_left1.shift(0.75 * DOWN + 0.5 * RIGHT)

        object_box_left2 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left2.shift(1.5 * DOWN + 0.5 * RIGHT)
        # self.play(Create(object_box_left2))
        object_frame_text_left2 = """'c'"""       
        object_frame_text_style_left2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left2}</b></span>').scale(0.25)
        object_frame_text_style_left2.shift(1.5 * DOWN + 0.5 * RIGHT)

        object_box_left3 = dataframe_swap_scale(1, 0.5, BLACK)
        object_box_left3.shift(2.2 * DOWN + 0.5 * RIGHT)
        # self.play(FocusOn(object_box_left))
        self.play(Create(object_box_left3), Create(object_box_left2), Create(object_box_left1), Create(object_box_left))
        object_frame_text_left3 = """'d'"""       
        object_frame_text_style_left3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left3}</b></span>').scale(0.25)
        object_frame_text_style_left3.shift(2.2 * DOWN + 0.5 * RIGHT)
        self.play(FocusOn(left_side_style[13:16]))
        self.play(TransformFromCopy(left_side_style[17], object_frame_text_style_left3),
                  TransformFromCopy(left_side_style[14], object_frame_text_style_left),
                  TransformFromCopy(left_side_style[15], object_frame_text_style_left1),
                  TransformFromCopy(left_side_style[16], object_frame_text_style_left2), run_time=2)

        object_default = """zip(alpha_str, fruits_list)"""       
        object_default1 = MarkupText(f'<span font_family="monospace"><b>{object_default}</b></span>').scale(0.2)
        object_default1.shift(1.1 * DOWN + 3.3 * RIGHT)
        arrow_default = Arrow(1.3 * DOWN + 2.6 * RIGHT, 1.3 * DOWN + 4.2 * RIGHT, color=BLUE_D, buff=0)
        self.play(FocusOn(arrow_default))
        self.play(Write(object_default1), FadeIn(arrow_default))


        object_frame_text_extremer = """('a', 'apple')"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer), run_time=0.8)

        object_frame_text_extremer1 = """('b', 'grapes')"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.7)

        object_frame_text_extremer2 = """('c', 'cherry')"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.6)

        object_frame_text_extremer3 = """('d', 'orange')"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.5)


        self.play(Write(left_side_style[54]), Write(left_side_style[68]), 
                  Write(left_side_style[83]),Write(left_side_style[98]),Write(left_side_style[113]),
                  TransformFromCopy(object_frame_text_style_extremer, left_side_style[55:68]),
                  TransformFromCopy(object_frame_text_style_extremer1, left_side_style[69:83]),
                  TransformFromCopy(object_frame_text_style_extremer2, left_side_style[84:98]),
                  TransformFromCopy(object_frame_text_style_extremer3, left_side_style[99:113]), run_time=2)

        self.wait(1)

        self.play(ShrinkToCenter(object_frame_text_style_heading), ShrinkToCenter(object_box_heading), run_time=0.4)
        self.play(FadeOut(cur_arrow_str), FadeOut(cur_arrow_list), run_time=0.3)
        self.play(FadeOut(left_side_style[19:]),run_time=0.3)


        left_side_code2 = """>>> mix_dict = {6:'apple', 7:'ball', 8:'cat', 9:'dog'}
>>> list(zip(mix_dict, fruits_list))
  [(6, 'apple'), (7, 'grapes'), (8 'cherry'), (9, 'orange')]
>>> list(zip(mix_dict.values(), fruits_list))
  [('apple', 'apple'), ('ball', 'grapes'), 
   ('cat', 'cherry'), ('dog', 'orange')]
"""       
        left_side_style2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code2}</b></span>',
                      0.35, GREY_A, 1.35 * UP + 1.87 * LEFT)
        left_side_style2[0:3].set_color(RED_D)
        left_side_style2[15:22].set_color(GREEN_E) # 'apple'
        left_side_style2[25:31].set_color(GREEN_E) #  'ball'
        left_side_style2[34:39].set_color(GREEN_E) #  'cat'
        left_side_style2[42:47].set_color(GREEN_E) # 'dog'
        left_side_style2[48:51].set_color(RED_D) # 
        left_side_style2[51:55].set_color(BLUE_D) # list
        left_side_style2[56:59].set_color(BLUE_D) # zip
        left_side_style2[133:136].set_color(RED_D) # 
        left_side_style2[136:140].set_color(BLUE_D) # list
        left_side_style2[141:144].set_color(BLUE_D) # zip

        self.play(Write(left_side_style2[:82]), run_time=2)

        self.play(ShrinkToCenter(object_frame_text_style_left3),
                  ShrinkToCenter(object_frame_text_style_left),
                  ShrinkToCenter(object_frame_text_style_left1),
                  ShrinkToCenter(object_frame_text_style_left2), ShrinkToCenter(heading_one_style1),  run_time=0.3)

        self.play(FadeOut(object_default1), FadeOut(arrow_default), run_time=0.3)
        self.play(ShrinkToCenter(object_frame_text_style_extremer),ShrinkToCenter(object_frame_text_style_extremer1),
                  ShrinkToCenter(object_frame_text_style_extremer2),ShrinkToCenter(object_frame_text_style_extremer3), run_time=0.3)

        heading_one1 = """mix_dict\n (keys)"""       
        heading_one_style1 = MarkupText(f'<span font_family="monospace"><b>{heading_one1}</b></span>').scale(0.3)
        heading_one_style1.shift(0.55* UP + 0.5 * RIGHT)
        self.play(FocusOn(heading_one_style1))
        self.play(Write(heading_one_style1),run_time=0.5)

        object_frame_text_left = """6"""       
        object_frame_text_style_left = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left}</b></span>').scale(0.25)
        object_frame_text_style_left.shift(0.01 * DOWN + 0.5 * RIGHT)

        object_frame_text_left1 = """7"""       
        object_frame_text_style_left1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left1}</b></span>').scale(0.25)
        object_frame_text_style_left1.shift(0.75 * DOWN + 0.5 * RIGHT)

        object_frame_text_left2 = """8"""       
        object_frame_text_style_left2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left2}</b></span>').scale(0.25)
        object_frame_text_style_left2.shift(1.5 * DOWN + 0.5 * RIGHT)

        object_frame_text_left3 = """9"""       
        object_frame_text_style_left3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_left3}</b></span>').scale(0.25)
        object_frame_text_style_left3.shift(2.2 * DOWN + 0.5 * RIGHT)
        self.play(FocusOn(left_side_style2[13]))
        self.play(TransformFromCopy(left_side_style2[40], object_frame_text_style_left3),
                  TransformFromCopy(left_side_style2[13], object_frame_text_style_left),
                  TransformFromCopy(left_side_style2[23], object_frame_text_style_left1),
                  TransformFromCopy(left_side_style2[32], object_frame_text_style_left2), run_time=2)


        object_default = """zip(mix_dict, fruits_list)"""       
        object_default1 = MarkupText(f'<span font_family="monospace"><b>{object_default}</b></span>').scale(0.2)
        object_default1.shift(1.1 * DOWN + 3.3 * RIGHT)
        arrow_default = Arrow(1.3 * DOWN + 2.6 * RIGHT, 1.3 * DOWN + 4.2 * RIGHT, color=BLUE_D, buff=0)
        self.play(FocusOn(arrow_default))
        self.play(Write(object_default1), FadeIn(arrow_default))


        object_frame_text_extremer = """(6, 'apple')"""       
        object_frame_text_style_extremer = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer}</b></span>').scale(0.3)
        object_frame_text_style_extremer.shift(0.01 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer), run_time=0.8)

        object_frame_text_extremer1 = """(7, 'grapes')"""       
        object_frame_text_style_extremer1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer1}</b></span>').scale(0.3)
        object_frame_text_style_extremer1.shift(0.75 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer1), run_time=0.7)

        object_frame_text_extremer2 = """(8, 'cherry')"""       
        object_frame_text_style_extremer2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer2}</b></span>').scale(0.3)
        object_frame_text_style_extremer2.shift(1.5 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer2), run_time=0.6)

        object_frame_text_extremer3 = """(9, 'orange')"""       
        object_frame_text_style_extremer3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_extremer3}</b></span>').scale(0.3)
        object_frame_text_style_extremer3.shift(2.2 * DOWN + 5.5 * RIGHT)
        self.play(Write(object_frame_text_style_extremer3), run_time=0.5)


        self.play(Write(left_side_style2[82]), Write(left_side_style2[94]), 
                  Write(left_side_style2[107]),Write(left_side_style2[119]),Write(left_side_style2[132]),
                  TransformFromCopy(object_frame_text_style_extremer, left_side_style2[83:94]),
                  TransformFromCopy(object_frame_text_style_extremer1, left_side_style2[95:107]),
                  TransformFromCopy(object_frame_text_style_extremer2, left_side_style2[108:119]),
                  TransformFromCopy(object_frame_text_style_extremer3, left_side_style2[120:132]), run_time=2)

        self.wait(1)

        object_box_heading= dataframe_swap_scale(8, 0.6, BLACK)
        object_box_heading.shift(3.2 * UP + 2 * RIGHT)
        self.play(Create(object_box_heading), run_time=0.2)
        object_frame_text_heading = """By default, dictionary uses keys in zip function."""       
        object_frame_text_style_heading = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading}</b></span>').scale(0.3)
        object_frame_text_style_heading.shift(3.2 * UP + 2 * RIGHT)
        cur_arrow_str = CurvedArrow(SurroundingRectangle(left_side_style2[48:82], buff=0).get_right(), 
                                    object_box_heading.get_bottom(), color=RED_D, angle=1.23)
        self.play(Create(cur_arrow_str), run_time=0.5)
        self.play(Write(object_frame_text_style_heading), run_time=1)
        self.wait(1)

        left_side_style2[48:133].set_color(DARK_GRAY)
        self.play(FocusOn(left_side_style2[136]))
        self.play(Write(left_side_style2[133:176]))

        object_box_heading1= dataframe_swap_scale(6, 0.8, BLACK)
        object_box_heading1.shift(0.5 * UP + 3 * RIGHT)
        self.play(Create(object_box_heading1), run_time=0.2)
        object_frame_text_heading1 = """To use Dictionary values in zip function \ntry .values() method on mix_dict variable"""       
        object_frame_text_style_heading1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading1}</b></span>').scale(0.3)
        object_frame_text_style_heading1.shift(0.5 * UP + 3 * RIGHT)
        cur_arrow_str1 = CurvedArrow(SurroundingRectangle(left_side_style2[133:161], buff=0).get_right(), 
                                    object_box_heading1.get_top(), color=RED_D, angle=-1.23)
        self.play(Create(cur_arrow_str1), run_time=0.5)
        self.play(Write(object_frame_text_style_heading1), run_time=2)
        self.wait(1)

        self.play(FocusOn(left_side_style2[177]))
        self.play(Write(left_side_style2[176:]))
        self.wait(1)


        left_side_code3 = """>>> tuple_num = (11, 12, 13, 14)
>>> list(zip(alpha_str, tuple_num))
  [('a', 11), ('b', 12), 
  ('c', 13), ('d', 14)]
>>> set_num = {100, 101, 102, 103}
>>> list(zip(alpha_str, set_num))
  [('a', 100), ('b', 101), 
  ('c', 102), ('d', 103)]
>>> num_zip = 12345
>>> list(zip(alpha_str, num_zip))
  Traceback (most recent call last):
    File "&lt;stdin>", line 1, in &lt;module>
  TypeError: 'int' object is not iterable
"""       
        left_side_style3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code3}</b></span>',
                      0.35, GREY_A, 1.25 * DOWN + 3.15 * LEFT)
        left_side_style3[0:3].set_color(RED_D)
        left_side_style3[26:29].set_color(RED_D) # 
        left_side_style3[29:33].set_color(BLUE_D) #  list
        left_side_style3[34:37].set_color(BLUE_D) #  zip
        left_side_style3[96:99].set_color(RED_D) # 
        left_side_style3[124:127].set_color(RED_D) # 
        left_side_style3[127:131].set_color(BLUE_D) # list
        left_side_style3[132:135].set_color(BLUE_D) # zip
        left_side_style3[196:199].set_color(RED_D) # 
        left_side_style3[212:215].set_color(RED_D) # 
        left_side_style3[215:219].set_color(BLUE_D) # list
        left_side_style3[220:223].set_color(BLUE_D) # zip

        left_side_style2[133:].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[:196]), run_time=2)
        self.wait(1.5)

        object_box_heading2= dataframe_swap_scale(6, 1, BLACK)
        object_box_heading2.shift(1 * DOWN + 3 * RIGHT)
        self.play(Create(object_box_heading2), run_time=0.2)
        object_frame_text_heading2 = """Tuple and Set have __iter__ inbuilt function.\nA valid input for zip() function."""       
        object_frame_text_style_heading2 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading2}</b></span>').scale(0.3)
        object_frame_text_style_heading2.shift(1 * DOWN + 3 * RIGHT)
        cur_arrow_str2 = Arrow(SurroundingRectangle(left_side_style3[26:59], buff=0).get_right(), 
                                    object_box_heading2.get_left(), color=RED_D, buff=0)

        cur_arrow_list2 = Arrow(SurroundingRectangle(left_side_style3[124:155], buff=0).get_right(), 
                                    object_box_heading2.get_left(), color=RED_D, buff=0)

        self.play(Create(cur_arrow_str2), Create(cur_arrow_list2), run_time=0.5)
        self.play(Write(object_frame_text_style_heading2), run_time=2)
        self.wait(2)

        left_side_style3[:196].set_color(DARK_GRAY)
        self.play(FocusOn(left_side_style3[197]))
        self.play(Write(left_side_style3[196:]), run_time=2)
        self.wait(1)


        object_box_heading3= dataframe_swap_scale(6, 1, BLACK)
        object_box_heading3.shift(2.5 * DOWN + 3 * RIGHT)
        self.play(Create(object_box_heading3), run_time=0.2)
        object_frame_text_heading3 = """Integer don't have __iter__ inbuilt function.\nIt will raise TypeError."""       
        object_frame_text_style_heading3 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading3}</b></span>').scale(0.3)
        object_frame_text_style_heading3.shift(2.5 * DOWN + 3 * RIGHT)
        cur_arrow_str3 = Arrow(SurroundingRectangle(left_side_style3[212:243], buff=0).get_right(), 
                                    object_box_heading3.get_left(), color=RED_D, buff=0)

        self.play(Create(cur_arrow_str3), run_time=0.5)
        self.play(Write(object_frame_text_style_heading3), run_time=2)
        self.wait(2)

        self.play(
            *[ShrinkToCenter(mob)for mob in self.mobjects], run_time=0.5
            # All mobjects in the screen are saved in self.mobjects
        )

        self.play(
            *[FadeOut(mob)for mob in self.mobjects], run_time=0.5
            # All mobjects in the screen are saved in self.mobjects
        )

        fixed_left_code_box = create_rectange(12, 7, 0.1 * DOWN + 0.001 * RIGHT, DARKER_GRAY)
        heading_one = """Interactive shell"""       
        heading_one_style = MarkupText(f'<span font_family="monospace"><b>{heading_one}</b></span>').scale(0.3)
        heading_one_style.shift(3.54 * UP + 5 * LEFT)
        self.play(Write(heading_one_style), run_time=0.2)


        object_box_heading1= dataframe_swap_scale(6, 0.8, BLACK)
        object_box_heading1.shift(0.05 * UP + 0.03 * RIGHT)
        self.play(Create(object_box_heading1), run_time=0.2)
        object_frame_text_heading1 = """Iterate over zip() object"""       
        object_frame_text_style_heading1 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading1}</b></span>').scale(0.5)
        object_frame_text_style_heading1.shift(0.05 * UP + 0.03 * RIGHT)
        self.play(Write(object_frame_text_style_heading1), run_time=1)
        self.wait(1)
        
        self.play(ShrinkToCenter(object_box_heading1), ShrinkToCenter(object_frame_text_style_heading1), run_time=0.3)
        
        left_side_code3 = """>>> tuple_num = (11, 12, 13, 14)
>>> num_list = ['one', 'two', 'three', 'four']
>>> alpha_str = 'abcd'
>>> list(zip(tuple_num, num_list, alpha_str))
  [(11, 'one', 'a'), (12, 'two', 'b'), 
  (13, 'three', 'c'), (14, 'four', 'd')]
>>> dict(zip(tuple_num, num_list, alpha_str))
>>> dict(zip(tuple_num, num_list))
  {11: 'one', 12: 'two', 13: 'three', 14: 'four'}
>>> tuple(zip(tuple_num, num_list, alpha_str))
  ((11, 'one', 'a'), (12, 'two', 'b'), 
  (13, 'three', 'c'), (14, 'four', 'd'))
>>> set(zip(tuple_num, num_list, alpha_str))
  {(12, 'two', 'b'), (14, 'four', 'd'), 
  (13, 'three', 'c'), (11, 'one', 'a')}
>>> int(zip(tuple_num, num_list, alpha_str))
Traceback (most recent call last):
  File "&lt;stdin>", line 1, in &lt;module>
TypeError: int() argument must be a string, 
a bytes-like object or a number, not 'zip'
>>> str(zip(tuple_num, num_list, alpha_str))
  '&lt;zip object at 0x7f1c69efd8c0>'
"""       
        left_side_style3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{left_side_code3}</b></span>',
                      0.35, GREY_A, 0.15 * DOWN + 2.6 * LEFT)
        left_side_style3[0:3].set_color(RED_D)
        left_side_style3[26:29].set_color(RED_D) # 
        left_side_style3[39:44].set_color(GREEN_E) #  one
        left_side_style3[45:50].set_color(GREEN_E) #  two
        left_side_style3[51:58].set_color(GREEN_E) # three
        left_side_style3[59:65].set_color(GREEN_E) # four
        left_side_style3[66:69].set_color(RED_D) # 
        left_side_style3[79:85].set_color(GREEN_E) # 'abcd'
        left_side_style3[85:88].set_color(RED_D) # 
        left_side_style3[88:92].set_color(BLUE_D) # list
        left_side_style3[93:96].set_color(BLUE_D) # zip
        left_side_style3[191:194].set_color(RED_D) #
        left_side_style3[194:198].set_color(BLUE_D) # dict
        left_side_style3[199:202].set_color(BLUE_D) #zip
        left_side_style3[233:236].set_color(RED_D) #
        left_side_style3[236:240].set_color(BLUE_D) # dict
        left_side_style3[241:244].set_color(BLUE_D) #zip
        left_side_style3[305:308].set_color(RED_D) #
        left_side_style3[308:313].set_color(BLUE_D) # tuple
        left_side_style3[314:317].set_color(BLUE_D) # zip
        left_side_style3[412:415].set_color(RED_D) #
        left_side_style3[415:418].set_color(BLUE_D) # set
        left_side_style3[419:422].set_color(BLUE_D) # zip
        left_side_style3[517:520].set_color(RED_D) #
        left_side_style3[520:523].set_color(BLUE_D) # int
        left_side_style3[524:527].set_color(BLUE_D) # zip
        left_side_style3[690:693].set_color(RED_D) #
        left_side_style3[693:696].set_color(BLUE_D) # str
        left_side_style3[697:700].set_color(BLUE_D) # zip

        self.play(Write(left_side_style3[:191]), run_time=2)


        object_box_heading21= dataframe_swap_scale(5, 0.5, BLACK)
        object_box_heading21.shift(3 * UP + 4 * RIGHT)
        self.play(Create(object_box_heading21), run_time=0.2)
        object_frame_text_heading21 = """Iterate zip() function object by List"""       
        object_frame_text_style_heading21 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading21}</b></span>').scale(0.3)
        object_frame_text_style_heading21.shift(3 * UP + 4 * RIGHT)
        cur_arrow_str21 = CurvedArrow(SurroundingRectangle(left_side_style3[85:127], buff=0).get_right(), 
                                    object_box_heading21.get_bottom(), color=RED_D, angle=1)
        self.play(Create(cur_arrow_str21), run_time=0.5)
        self.play(Write(object_frame_text_style_heading21), run_time=1)
        self.wait(1)

        left_side_style3[85:191].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[191:233]), run_time=1)

        object_box_heading22= dataframe_swap_scale(8.5, 1.8, BLACK)
        object_box_heading22.shift(1.5 * DOWN + 2 * RIGHT)
        self.play(Create(object_box_heading22), run_time=0.2)
        object_frame_text_heading22 = """More than 2 inputs in zip function while iterating using dict will Raise Error.\nTraceback (most recent call last):
  File "&lt;stdin>", line 1, in &lt;module>
ValueError: dictionary update sequence element #0 has length 3; 2 is required"""       
        object_frame_text_style_heading22 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading22}</b></span>').scale(0.3)
        object_frame_text_style_heading22.shift(1.5 * DOWN + 2 * RIGHT)
        cur_arrow_str22 = CurvedArrow(SurroundingRectangle(left_side_style3[191:233], buff=0).get_right(), 
                                    object_box_heading22.get_top(), color=RED_D, angle=-1.23)
        self.play(Create(cur_arrow_str22), run_time=0.5)
        self.play(Write(object_frame_text_style_heading22), run_time=2)
        self.wait(2)

        line1 = Line(SurroundingRectangle(left_side_style3[191:233], buff=0).get_left(), 
                     SurroundingRectangle(left_side_style3[191:233], buff=0).get_right())
        self.play(Create(line1), run_time=0.7)

        self.play(ShrinkToCenter(object_frame_text_style_heading22), ShrinkToCenter(object_box_heading22), FadeOut(cur_arrow_str22), run_time=0.3)
        self.play(Write(left_side_style3[233:305]))

        object_box_heading22= dataframe_swap_scale(7, 0.5, BLACK)
        object_box_heading22.shift(2 * UP + 3.5 * RIGHT)
        self.play(Create(object_box_heading22), run_time=0.2)
        object_frame_text_heading22 = """Iterate zip() function(Only 2 inputs) object by Dict"""       
        object_frame_text_style_heading22 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading22}</b></span>').scale(0.3)
        object_frame_text_style_heading22.shift(2  * UP + 3.5 * RIGHT)
        cur_arrow_str22 = CurvedArrow(SurroundingRectangle(left_side_style3[233:265], buff=0).get_right(), 
                                    object_box_heading22.get_bottom(), color=RED_D, angle=1)
        self.play(Create(cur_arrow_str22), run_time=0.5)
        self.play(Write(object_frame_text_style_heading22), run_time=1)
        self.wait(1)

        left_side_style3[233:305].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[305:412]))

        object_box_heading23= dataframe_swap_scale(5, 0.5, BLACK)
        object_box_heading23.shift(1 * UP + 4 * RIGHT)
        self.play(Create(object_box_heading23), run_time=0.2)
        object_frame_text_heading23 = """Iterate zip() function object by tuple"""       
        object_frame_text_style_heading23 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading23}</b></span>').scale(0.3)
        object_frame_text_style_heading23.shift(1  * UP + 4 * RIGHT)
        cur_arrow_str23 = CurvedArrow(SurroundingRectangle(left_side_style3[305:348], buff=0).get_right(), 
                                    object_box_heading23.get_bottom(), color=RED_D, angle=1)
        self.play(Create(cur_arrow_str23), run_time=0.5)
        self.play(Write(object_frame_text_style_heading23), run_time=1)
        self.wait(1)

        left_side_style3[305:412].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[412:517]))

        object_box_heading24= dataframe_swap_scale(5, 0.5, BLACK)
        object_box_heading24.shift(0.01 * UP + 4 * RIGHT)
        self.play(Create(object_box_heading24), run_time=0.2)
        object_frame_text_heading24 = """Iterate zip() function object by set"""       
        object_frame_text_style_heading24 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading24}</b></span>').scale(0.3)
        object_frame_text_style_heading24.shift(0.01  * UP + 4 * RIGHT)
        cur_arrow_str24 = CurvedArrow(SurroundingRectangle(left_side_style3[412:453], buff=0).get_right(), 
                                    object_box_heading24.get_bottom(), color=RED_D, angle=1)
        self.play(Create(cur_arrow_str24), run_time=0.5)
        self.play(Write(object_frame_text_style_heading24), run_time=1)
        self.wait(1)

        left_side_style3[412:517].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[517:690]))
        object_box_heading25= dataframe_swap_scale(5.5, 0.5, BLACK)
        object_box_heading25.shift(1 * DOWN + 4 * RIGHT)
        self.play(Create(object_box_heading25), run_time=0.2)
        object_frame_text_heading25 = """Can't Iterate zip() function object by int"""       
        object_frame_text_style_heading25 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading25}</b></span>').scale(0.3)
        object_frame_text_style_heading25.shift(1  * DOWN + 4 * RIGHT)
        cur_arrow_str25 = Arrow(SurroundingRectangle(left_side_style3[517:558], buff=0).get_right(), 
                                    object_box_heading25.get_left(), color=RED_D, buff=0)
        self.play(Create(cur_arrow_str25), run_time=0.5)
        self.play(Write(object_frame_text_style_heading25), run_time=1)
        self.wait(1)

        left_side_style3[517:690].set_color(DARK_GRAY)
        self.play(Write(left_side_style3[690:]))
        object_box_heading26= dataframe_swap_scale(5.5, 0.5, BLACK)
        object_box_heading26.shift(2 * DOWN + 4 * RIGHT)
        self.play(Create(object_box_heading26), run_time=0.2)
        object_frame_text_heading26 = """str convert zip object into string"""       
        object_frame_text_style_heading26 = MarkupText(f'<span font_family="monospace"><b>{object_frame_text_heading26}</b></span>').scale(0.3)
        object_frame_text_style_heading26.shift(2  * DOWN + 4 * RIGHT)
        cur_arrow_str26 = CurvedArrow(SurroundingRectangle(left_side_style3[690:731], buff=0).get_right(), 
                                    object_box_heading26.get_bottom(), color=RED_D, angle=1)
        self.play(Create(cur_arrow_str26), run_time=0.5)
        self.play(Write(object_frame_text_style_heading26), run_time=1)
        self.wait(2)

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



    
