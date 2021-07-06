from manim import *


class PythonOneLinerCodes(GraphScene,Scene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"Accuracy(score)",
            x_axis_label="Models",
            y_max = 1,
            y_min = -1,
            x_max= 5,
            x_min= 0,
            # y_tick_frequency= 3,
            # x_tick_frequency= 3,
            y_axis_config =  {"tick_frequency": 0.5},
            x_axis_config = {"tick_frequency": 0.5},
            axes_color= BLUE,
            **kwargs
        )

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
            explain_filled_rect.set_fill(color_fill, 0.5)
            self.play(GrowFromCenter(explain_filled_rect, run_time=1))
            explain_line_left, explain_line_bottom = [
                Line(
                    explain_filled_rect.get_corner(start),
                    explain_filled_rect.get_corner(end),
                    color=RED_A
                )
                for start, end in [(DL, UL), (DL, DR)]
            ]

            self.play(
                GrowFromEdge(explain_line_left, DOWN),
                GrowFromEdge(explain_line_bottom, LEFT)
            )

        def currentTextPositionMarkup(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text

        def currentTextPositionText(name, size_of_text, color_text, position):
            index_text = Text(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text),run_time=0.1)
            return index_text

        def currentTextPositionMarkupWithout(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            return index_text

        create_rectange(13.9, 0.8, 2.25 * UP + 0.1 * LEFT, BLACK)
        create_rectange(6, 5, 1.2 * DOWN + 4  * LEFT, DARK_GRAY)
        create_rectange(6, 0.6, 0.8 * UP + 3.5 * RIGHT, BLACK)

        top_disapper_text = currentTextPositionMarkup(f'<span font_family="monospace"><b>Python One Liner: </b></span>',
                      0.5, TEAL_A, 3.5 * UP + 2.6 * LEFT)

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Single if-else condition</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        


        fixed_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>One Liner Python Code</b></span>',
                      0.4, TEAL_D, 2.9 * UP + 5.3 * LEFT)


        
        fixed_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>Python Code</b></span>',
                      0.4, TEAL_D, 1.5 * UP + 5.5 * LEFT)

        
        fixed_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>Output</b></span>',
                      0.4, TEAL_D, 1.35 * UP + 1.15 * RIGHT)

        thinking_letter = SVGMobject("/home/manmohan/python_projects/manim_projects/regex_visual/last_thinking_cloud")
        thinking_letter.set_height(1)
        thinking_letter.set_width(5)
        thinking_letter.set_color(GREEN)
        thinking_letter.shift(2.2 * DOWN + 4.8 * RIGHT)

        owl_image = ImageMobject("/home/manmohan/python_projects/manim_projects/regex_visual/new_owl.png")
        owl_image.set_height(1)
        owl_image.shift(3.6 * DOWN + 6.6 * RIGHT)

        self.play(Write(top_text_replace), Write(fixed_text1), Write(fixed_text2), Write(fixed_text3),
                  FadeIn(thinking_letter), FadeIn(owl_image))

        if_else_code = """>>> if 96 > 100:\n...    print('Pass')\n... else:\n...    print("Fail")"""
        
        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 0.5 * UP + 5 * LEFT)
        code_text1[0:3].set_color(RED_D)
        code_text1[3:5].set_color(ORANGE)
        code_text1[12:15].set_color(RED_D)
        code_text1[15:20].set_color(BLUE_C)
        code_text1[21:27].set_color(GREEN_E)
        code_text1[28:31].set_color(RED_D)
        code_text1[31:35].set_color(ORANGE)
        code_text1[36:39].set_color(RED_D)
        code_text1[39:44].set_color(BLUE_C)
        code_text1[45:51].set_color(GREEN_E)
        self.play(Write(code_text1), run_time=2)
        self.wait(1)

        frametext1 = SurroundingRectangle(code_text1[15:28], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text1[3:11], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text1[31:35], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text1[39:52], fill_opacity=0.2, buff=0.05)
        


        if_else_code_one = """>>> print('Pass') if 96 > 100 else print("Fail")"""
        
        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.6, GREY_A, 2.25 * UP + 0.6 * LEFT)
        code_text2[0:3].set_color(RED_D)
        code_text2[3:8].set_color(BLUE_C)
        code_text2[9:15].set_color(GREEN_E)
        code_text2[16:18].set_color(ORANGE)
        code_text2[24:28].set_color(ORANGE)
        code_text2[28:33].set_color(BLUE_C)
        code_text2[34:40].set_color(GREEN_E)

        self.add(code_text2[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text1[15:28], code_text2[3:16]), run_time=2)
        self.play(TransformFromCopy(frametext1, frametext2))
        self.play(TransformFromCopy(code_text1[3:11], code_text2[16:24]), run_time=2)
        self.play(TransformFromCopy(frametext2, frametext3))
        self.play(TransformFromCopy(code_text1[31:35], code_text2[24:28]), run_time=2)
        self.play(TransformFromCopy(frametext3, frametext4))
        self.play(TransformFromCopy(code_text1[39:52], code_text2[28:41]), run_time=2)

        self.play(FadeOut(frametext1),FadeOut(frametext2),FadeOut(frametext3),FadeOut(frametext4))
        topics_names = """Topics"""
        
        topics_names_fix = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{topics_names}</b></span>',
                      0.37, BLACK, 0.6 * DOWN + 4.8 * RIGHT)
        self.play(Write(topics_names_fix), run_time=0.5)

        first_menu = """* Single if-else condition\n* Multiple if-else condition\n\nList comprehension\n* For loop with If condition\n* Double For loop with If condition\n\nDifference in if and if-else\n     one-liner"""
        
        first_menu_vary = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{first_menu}</b></span>',
                      0.3, BLACK, 2 * DOWN + 4.8 * RIGHT)
        self.play(Write(first_menu_vary), run_time=3)


        frametext_o1 = SurroundingRectangle(code_text2[16:24], fill_opacity=0.2, buff=0.05)
        self.play(FadeIn(frametext2), FadeIn(frametext_o1))
        self.wait(1)
        frametext_o2 = SurroundingRectangle(code_text2[24:28], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext2,frametext3), Transform(frametext_o1,frametext_o2))
        self.wait(1)
        frametext_o3 = SurroundingRectangle(code_text2[28:41], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3,frametext4), Transform(frametext_o2,frametext_o3), 
                  FadeOut(frametext2), FadeOut(frametext_o1))
        self.wait(1)

        curved_arrow1 = CurvedArrow(0.1 * DOWN + 4.1 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        curved_arrow2 = CurvedArrow(2 * UP + 4.1 * RIGHT,  0.8 * UP + 1.5 * RIGHT, angle=-1.5)
        self.play(ShowCreation(curved_arrow2))

        inside_output = currentTextPositionMarkup(r'<span font_family="monospace"><b>Fail</b></span>',
                      0.4, TEAL_D, 0.8 * UP + 1.15 * RIGHT)
        self.wait(8)

        self.play(FadeOut(curved_arrow1), FadeOut(curved_arrow2), FadeOut(inside_output), FadeOut(frametext_o2),
                  FadeOut(frametext_o3), FadeOut(frametext4), FadeOut(frametext3), FadeOut(code_text2), 
                  FadeOut(top_text_replace))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Multiple if-else condition</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))


        if_else_code = """>>> x = 96\n>>> if x > 100:\n...     print("no")\n... elif x == 100:\n...     print("yes")\n... else:\n...     print("maybe")"""
        
        code_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.15 * DOWN + 4.8 * LEFT)
        code_text4[0:3].set_color(RED_D)
        code_text4[7:10].set_color(RED_D)
        code_text4[10:12].set_color(ORANGE)
        code_text4[18:21].set_color(RED_D)
        code_text4[21:26].set_color(BLUE_C)
        code_text4[27:31].set_color(GREEN_E)
        code_text4[32:35].set_color(RED_D)
        code_text4[35:39].set_color(ORANGE)
        code_text4[46:49].set_color(RED_D)
        code_text4[49:54].set_color(BLUE_C)
        code_text4[55:60].set_color(GREEN_E)
        code_text4[61:64].set_color(RED_D)
        code_text4[64:68].set_color(ORANGE)
        code_text4[69:72].set_color(RED_D)
        code_text4[72:77].set_color(BLUE_C)
        code_text4[78:85].set_color(GREEN_E)
        self.play(Write(code_text4), run_time=2)

        frametext1 = SurroundingRectangle(code_text4[10:17], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text4[21:32], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text4[35:39], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text4[39:45], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text4[49:61], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text4[64:68], fill_opacity=0.2, buff=0.05)
        frametext7 = SurroundingRectangle(code_text4[72:86], fill_opacity=0.2, buff=0.05)
        


        if_else_code_one = """>>> print("no") if x > 100 else print("yes") if x == 100 else""" # 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[3:8].set_color(BLUE_C)
        code_text5[9:13].set_color(GREEN_E)
        code_text5[14:16].set_color(ORANGE)
        code_text5[21:25].set_color(ORANGE)
        code_text5[25:30].set_color(BLUE_C)
        code_text5[31:36].set_color(GREEN_E)
        code_text5[37:39].set_color(ORANGE)
        code_text5[45:49].set_color(ORANGE)

        if_else_code_one1 = """print("maybe")"""
        code_text6 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one1}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 5 * RIGHT)
        
        code_text6[0:5].set_color(BLUE_C)
        code_text6[6:13].set_color(GREEN_E)

        self.add(code_text5[0:3])
        self.play(Create(frametext2))
        
        self.play(TransformFromCopy(code_text4[21:32], code_text5[3:14]), run_time=2) 
        self.play(TransformFromCopy(frametext2, frametext1))
        self.play(TransformFromCopy(code_text4[10:17], code_text5[14:21]), run_time=2)
        self.play(TransformFromCopy(frametext1, frametext3))
        self.play(TransformFromCopy(code_text4[35:39], code_text5[21:25]), 
                  TransformFromCopy(code_text4[35:39], code_text5[37:39]), run_time=2)
        self.play(TransformFromCopy(frametext3, frametext5))
        self.play(TransformFromCopy(code_text4[49:61], code_text5[25:37]), run_time=2)
        self.play(TransformFromCopy(frametext5, frametext4))
        self.play(TransformFromCopy(code_text4[39:45], code_text5[39:45]), run_time=2)
        self.play(TransformFromCopy(frametext4, frametext6))
        self.play(TransformFromCopy(code_text4[64:68], code_text5[45:49]), run_time=2)
        self.play(TransformFromCopy(frametext6, frametext7))
        self.play(TransformFromCopy(code_text4[72:86], code_text6), run_time=2)

        self.wait(0.5)

        self.play(FadeOut(frametext1),FadeOut(frametext2),FadeOut(frametext3),FadeOut(frametext4),
                  FadeOut(frametext5),FadeOut(frametext6),FadeOut(frametext7))
        frametext_o1 = SurroundingRectangle(code_text5[14:21], fill_opacity=0.2, buff=0.05)
        self.play(FadeIn(frametext1), FadeIn(frametext_o1))
        self.wait(1)
        frametext_o2 = SurroundingRectangle(code_text5[37:45], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext1,frametext3), Transform(frametext1,frametext4), 
                  Transform(frametext_o1,frametext_o2))
        self.wait(1)

        frametext_o3 = SurroundingRectangle(code_text5[45:49], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3,frametext6), Transform(frametext4,frametext6), 
                  Transform(frametext_o2,frametext_o3), 
                  FadeOut(frametext1), FadeOut(frametext_o1))
        self.wait(1)
        frametext_o4 = SurroundingRectangle(code_text6, fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext6,frametext7), Transform(frametext4,frametext6), 
                  Transform(frametext_o3,frametext_o4), 
                  FadeOut(frametext3), FadeOut(frametext4), FadeOut(frametext_o2))

        self.wait(0.5)


        curved_arrow1 = CurvedArrow(2.2 * DOWN + 4.1 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        curved_arrow2 = CurvedArrow(2.1 * UP + 4.1 * RIGHT,  0.8 * UP + 1.7 * RIGHT, angle=-1.5)
        self.play(ShowCreation(curved_arrow2))

        inside_output = currentTextPositionMarkup(r'<span font_family="monospace"><b>maybe</b></span>',
                      0.4, TEAL_D, 0.8 * UP + 1.15 * RIGHT)

        self.wait(8)

        # ------------------- for loop - and - list comprehension ----------------------

        self.play(FadeOut(curved_arrow1), FadeOut(curved_arrow2), FadeOut(inside_output),
                  FadeOut(frametext_o3), FadeOut(frametext6), FadeOut(frametext7), FadeOut(code_text5), 
                  FadeOut(top_text_replace), FadeOut(code_text6), FadeOut(code_text1), FadeOut(code_text4))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>List Comprehension</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> numbers = []\n>>> for i in range(10):\n...     numbers.append(i)\n>>> print(numbers)"""
        
        code_text7 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 0.5 * UP + 5 * LEFT)
        code_text7[0:3].set_color(RED_D)
        code_text7[13:16].set_color(RED_D)
        code_text7[16:19].set_color(ORANGE)
        code_text7[20:22].set_color(ORANGE)
        code_text7[22:27].set_color(BLUE_C)
        code_text7[32:35].set_color(RED_D)
        code_text7[52:55].set_color(RED_D)
        code_text7[55:60].set_color(BLUE_C)
        self.play(Write(code_text7), run_time=2)

        frametext1 = SurroundingRectangle(code_text7[16:31], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text7[55:69], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text7[50:51], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text7[3:13], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text7[35:52], fill_opacity=0.2, buff=0.05)

        if_else_code_one = """>>> numbers = [i for i in range(10)]""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[13:16].set_color(ORANGE)
        code_text5[17:19].set_color(ORANGE)
        code_text5[19:24].set_color(BLUE_C)
        # self.play(Write(code_text5))

        self.add(code_text5[0:3])
        self.play(Create(frametext4))
        self.play(TransformFromCopy(code_text7[3:13], code_text5[3:12]), 
                  TransformFromCopy(code_text7[3:13], code_text5[-1:]), run_time=2)
        self.play(TransformFromCopy(frametext4, frametext3))
        self.play(TransformFromCopy(code_text7[50:51], code_text5[12:13]), run_time=2)

        self.play(TransformFromCopy(frametext3, frametext1))
        self.play(TransformFromCopy(code_text7[16:31], code_text5[13:-1]), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(frametext1),FadeOut(frametext3),FadeOut(frametext4))

        frametext_o1 = SurroundingRectangle(code_text5[13:-1], fill_opacity=0.2, buff=0.05)
        self.play(FadeIn(frametext1), FadeIn(frametext_o1))
        self.wait(1)
        frametext_o2 = SurroundingRectangle(code_text5[12:13], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext1,frametext5), 
                  Transform(frametext_o1,frametext_o2))
        self.wait(1)

        self.play(Transform(frametext5,frametext2), Transform(frametext_o2,frametext2),
                  FadeOut(frametext1), FadeOut(frametext_o1))
        self.wait(1)

        curved_arrow1 = CurvedArrow(0.2 * UP + 4.2 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r'<span font_family="monospace"><b>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</b></span>',
                      0.4, TEAL_D, 0.8 * UP + 3.15 * RIGHT)

        self.play(FadeOut(first_menu_vary))
        suggest = """We can't use for loop \nin one line without \nstoring the result in \nlist or dictionary."""
        
        suggest_not_fixed = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{suggest}</b></span>',
                      0.4, BLACK, 2 * DOWN + 4.8 * RIGHT)
        self.play(Write(suggest_not_fixed), run_time=3)

        self.wait(8)

        # ------------------- for loop with if - and - list comprehension ----------------------

        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o2), FadeOut(frametext2), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5))

        pros_cons = """Pros\n-Reduced runtime\n-Reduced memory usage\n\nCons\n-Readability\n-maintainability"""
        
        pros_cons_fixed = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{pros_cons}</b></span>',
                      0.37, GREY_A, 2 * DOWN + 0.8 * RIGHT)
        self.play(Write(pros_cons_fixed[:19]), run_time=1)

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>For loop with If condition</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> squares = []\n>>> for i in range(10):\n...     if i%2==0:\n...         squares.append(i**2)\n>>> print(squares)"""
        
        code_text8 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.1 * DOWN + 4.5 * LEFT)
        code_text8[0:3].set_color(RED_D)
        code_text8[13:16].set_color(RED_D)
        code_text8[16:19].set_color(ORANGE)
        code_text8[20:22].set_color(ORANGE)
        code_text8[22:27].set_color(BLUE_C)
        code_text8[32:35].set_color(RED_D)
        code_text8[35:37].set_color(ORANGE)
        code_text8[44:47].set_color(RED_D)
        code_text8[67:70].set_color(RED_D)
        code_text8[70:75].set_color(BLUE_C)
        self.play(Write(code_text8), run_time=2)

        frametext1 = SurroundingRectangle(code_text8[3:13], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text8[16:31], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text8[35:43], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text8[62:66], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text8[-14:], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text8[47:67], fill_opacity=0.2, buff=0.05)

        if_else_code_one = """>>> squares = [i**2 for i in range(10) if i%2==0]""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[16:19].set_color(ORANGE)
        code_text5[20:22].set_color(ORANGE)
        code_text5[22:27].set_color(BLUE_C)
        code_text5[31:33].set_color(ORANGE)
        # self.play(Write(code_text5))

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text8[3:13], code_text5[3:12]), 
                  TransformFromCopy(code_text8[3:13], code_text5[-1:]), run_time=2)
        self.play(TransformFromCopy(frametext1, frametext4))
        self.play(TransformFromCopy(code_text8[62:66], code_text5[12:16]), run_time=2)

        self.play(TransformFromCopy(frametext4, frametext2))
        self.play(TransformFromCopy(code_text8[16:31], code_text5[16:31]), run_time=2)

        self.play(TransformFromCopy(frametext2, frametext3))
        self.play(TransformFromCopy(code_text8[35:43], code_text5[-9:-1]), run_time=2)

        self.play(FadeOut(frametext2),FadeOut(frametext3),FadeOut(frametext1), FadeOut(frametext4))
        self.wait(0.5)

        frametext_o1 = SurroundingRectangle(code_text5[16:31], fill_opacity=0.2, buff=0.05)
        self.play(FadeIn(frametext2), FadeIn(frametext_o1))
        self.wait(1)
        frametext_o2 = SurroundingRectangle(code_text5[31:-1], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext2,frametext3), 
                  Transform(frametext_o1,frametext_o2))
        self.wait(1)

        frametext_o3 = SurroundingRectangle(code_text5[12:16], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3,frametext6), Transform(frametext_o2,frametext_o3),
                  FadeOut(frametext2), FadeOut(frametext_o1))
        self.wait(1)

        self.play(Transform(frametext6,frametext5), Transform(frametext_o3,frametext5),
                  FadeOut(frametext3), FadeOut(frametext_o2))
        self.wait(1)

        curved_arrow1 = CurvedArrow(1.7 * DOWN + 4.2 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r'<span font_family="monospace"><b>[0, 4, 16, 36, 64]</b></span>',
                      0.4, TEAL_D, 0.8 * UP + 2 * RIGHT)
        self.play(FadeOut(suggest_not_fixed))
        self.play(FadeIn(first_menu_vary))
        self.wait(8)

        # ------------------- Double for loop with if - and - list comprehension ----------------------

        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o3), FadeOut(frametext6), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Double For loop with If condition</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> combs = []\n>>> for x in [1,2,3]:\n...     for y in [3,1,2]:\n...         if x != y:\n...             combs.append((x, y))\n>>> print(combs)"""
        
        code_text9 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 2.8 * DOWN + 4.18 * LEFT)
        code_text9[0:3].set_color(RED_D)
        code_text9[11:14].set_color(RED_D)
        code_text9[14:17].set_color(ORANGE)
        code_text9[18:20].set_color(ORANGE)
        code_text9[28:31].set_color(RED_D)
        code_text9[31:34].set_color(ORANGE)
        code_text9[35:37].set_color(ORANGE)
        code_text9[45:48].set_color(RED_D)
        code_text9[48:50].set_color(ORANGE)
        code_text9[55:58].set_color(RED_D)
        code_text9[77:80].set_color(RED_D)
        code_text9[80:85].set_color(BLUE_C)
        self.play(Write(code_text9), run_time=2)

        frametext1 = SurroundingRectangle(code_text9[3:11], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text9[14:27], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text9[31:44], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text9[48:54], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text9[58:77], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text9[80:], fill_opacity=0.2, buff=0.05)
        frametext7 = SurroundingRectangle(code_text9[71:76], fill_opacity=0.2, buff=0.05)


        if_else_code_one = """>>> combs = [(x, y) for x in [1,2,3] for y in [3,1,2] if x != y]""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[15:18].set_color(ORANGE)
        code_text5[19:21].set_color(ORANGE)
        code_text5[28:31].set_color(ORANGE)
        code_text5[32:34].set_color(ORANGE)
        code_text5[41:43].set_color(ORANGE)

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text9[3:11], code_text5[3:10]), 
                  TransformFromCopy(code_text9[3:11], code_text5[-1:]), run_time=2)

        self.play(TransformFromCopy(frametext1, frametext7))
        self.play(TransformFromCopy(code_text9[71:76], code_text5[10:15]), run_time=2)

        self.play(TransformFromCopy(frametext7, frametext2))
        self.play(TransformFromCopy(code_text9[14:27], code_text5[15:28]), run_time=2)

        self.play(TransformFromCopy(frametext2, frametext3))
        self.play(TransformFromCopy(code_text9[31:44], code_text5[28:41]), run_time=2)

        self.play(TransformFromCopy(frametext3, frametext4))
        self.play(TransformFromCopy(code_text9[48:54], code_text5[41:47]), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(frametext2),FadeOut(frametext3),FadeOut(frametext1), FadeOut(frametext4),
                  FadeOut(frametext7))

        frametext_o1 = SurroundingRectangle(code_text5[15:28], fill_opacity=0.2, buff=0.05)
        self.play(FadeIn(frametext2), FadeIn(frametext_o1))
        self.wait(1)

        frametext_o2 = SurroundingRectangle(code_text5[28:41], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext2,frametext3), 
                  Transform(frametext_o1,frametext_o2))
        self.wait(1)

        frametext_o3 = SurroundingRectangle(code_text5[41:47], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3,frametext4), Transform(frametext_o2,frametext_o3),
                  FadeOut(frametext2), FadeOut(frametext_o1))
        self.wait(1)

        frametext_o4 = SurroundingRectangle(code_text5[10:15], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext4,frametext5), Transform(frametext_o3,frametext_o4),
                  FadeOut(frametext3), FadeOut(frametext_o2))
        self.wait(1)


        self.play(Transform(frametext5,frametext6), Transform(frametext_o4,frametext6),
                  FadeOut(frametext4), FadeOut(frametext_o3))
        self.wait(1)

        curved_arrow1 = CurvedArrow(3.5 * DOWN + 4.5 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r'<span font_family="monospace"><b>[(1, 3), (1, 2), (2, 3), (2, 1), (3, 1), (3, 2)]</b></span>',
                      0.3, TEAL_D, 0.8 * UP + 3.5 * RIGHT)
        self.wait(8)

        # ------------------- difference list comprehension ----------------------

        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o4), FadeOut(frametext6), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5), FadeOut(code_text7), 
                  FadeOut(code_text8), FadeOut(code_text9), FadeOut(first_menu_vary))

        second_menu = """Dictionary Comprehension\n* For Loop\n* For loop With if-condition\n\n* Swapping two variables\n* Multiple Variables Assignment\n* Global Variable\n\nLambda function\n* Fibonacci Series With lambda"""
        
        second_menu_vary = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{second_menu}</b></span>',
                      0.3, BLACK, 2 * DOWN + 4.8 * RIGHT)
        self.play(Write(second_menu_vary), run_time=3)


        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Difference in if and if-else</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> squares = []\n>>> for i in range(1, 6):\n...     if i%2==0:\n...         squares.append(i**2)\n>>> print(squares)"""
        
        code_text8 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 2.1 * DOWN + 4.5 * LEFT)
        code_text8[0:3].set_color(RED_D)
        code_text8[13:16].set_color(RED_D)
        code_text8[16:19].set_color(ORANGE)
        code_text8[20:22].set_color(ORANGE)
        code_text8[22:27].set_color(BLUE_C)
        code_text8[33:36].set_color(RED_D)
        code_text8[36:38].set_color(ORANGE)
        code_text8[45:48].set_color(RED_D)
        code_text8[68:71].set_color(RED_D)
        code_text8[71:76].set_color(BLUE_C)
        self.play(Write(code_text8), run_time=2)

        frametext1 = SurroundingRectangle(code_text8[3:13], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text8[16:32], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text8[36:44], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text8[63:67], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text8[-14:], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text8[48:68], fill_opacity=0.2, buff=0.05)

        if_else_code = """>>> square_cube = []\n>>> for i in range(1, 6):\n...     if i%2 == 0:\n...         square_cube.append(i**2)\n...     else:\n...          square_cube.append(i**3)\n>>> print(square_cube)"""
        
        code_text7 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, ORIGIN + 4.15 * LEFT)
        code_text7[0:3].set_color(RED_D)
        code_text7[17:20].set_color(RED_D)
        code_text7[20:23].set_color(ORANGE)
        code_text7[24:26].set_color(ORANGE)
        code_text7[26:31].set_color(BLUE_C)
        code_text7[37:40].set_color(RED_D)
        code_text7[40:42].set_color(ORANGE)
        code_text7[49:52].set_color(RED_D)
        code_text7[76:79].set_color(RED_D)
        code_text7[79:83].set_color(ORANGE)
        code_text7[84:87].set_color(RED_D)
        code_text7[111:114].set_color(RED_D)
        code_text7[114:119].set_color(BLUE_C)
        self.play(Write(code_text7), run_time=2)

        frametext11 = SurroundingRectangle(code_text7[3:17], fill_opacity=0.2, buff=0.05)
        frametext12 = SurroundingRectangle(code_text7[20:36], fill_opacity=0.2, buff=0.05)
        frametext13 = SurroundingRectangle(code_text7[40:48], fill_opacity=0.2, buff=0.05)
        frametext14 = SurroundingRectangle(code_text7[71:75], fill_opacity=0.2, buff=0.05)
        frametext15 = SurroundingRectangle(code_text7[79:83], fill_opacity=0.2, buff=0.05)
        frametext16 = SurroundingRectangle(code_text7[106:110], fill_opacity=0.2, buff=0.05)# num
        frametext17 = SurroundingRectangle(code_text7[114:], fill_opacity=0.2, buff=0.05) # ** 


        if_else_code_one = """>>> square_cube = [i**2 if i%2==0 else i**3 for i in range(1, 6)]""" 
        code_text10 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.35, GREY_A, 2.45 * UP + 1.2 * LEFT)

        code_text10[0:3].set_color(RED_D)
        code_text10[20:22].set_color(ORANGE)
        code_text10[28:32].set_color(ORANGE)
        code_text10[36:39].set_color(ORANGE)
        code_text10[40:42].set_color(ORANGE)
        code_text10[42:47].set_color(BLUE_C)
        # self.play(Write(code_text10))

        if_else_code_one = """>>> squares = [i**2 for i in range(1, 6) if i%2==0]""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.35, GREY_A, 2.05 * UP + 1.52 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[16:19].set_color(ORANGE)
        code_text5[20:22].set_color(ORANGE)
        code_text5[22:27].set_color(BLUE_C)
        code_text5[32:34].set_color(ORANGE)
        # self.play(Write(code_text5))

        # square

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text8[3:13], code_text5[3:12]), 
                  TransformFromCopy(code_text8[3:13], code_text5[-1:]), run_time=2)

        self.add(code_text10[0:3])
        self.play(Create(frametext11))
        self.play(TransformFromCopy(code_text7[3:17], code_text10[3:16]), 
                  TransformFromCopy(code_text7[3:17], code_text10[-1:]), run_time=2)

        # i**2


        self.play(TransformFromCopy(frametext1, frametext4))
        self.play(TransformFromCopy(code_text8[62:66], code_text5[12:16]), run_time=2)

        self.play(TransformFromCopy(frametext11, frametext14))  
        self.play(TransformFromCopy(code_text7[71:75], code_text10[16:20]), run_time=2)
        self.play(FadeOut(second_menu_vary))
        suggest = """Closely observe the 'IF' \ncondition placement in one \nliner square_cube and \nsquares list variables."""
        
        suggest_not_fixed = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{suggest}</b></span>',
                      0.4, BLACK, 2 * DOWN + 4.8 * RIGHT)
        self.play(Write(suggest_not_fixed), run_time=3)

        # if
        self.play(TransformFromCopy(frametext4, frametext3))
        self.play(TransformFromCopy(code_text8[35:43], code_text5[-9:-1]), run_time=2)

        self.play(TransformFromCopy(frametext14, frametext13))
        self.play(TransformFromCopy(code_text7[40:48], code_text10[20:28]), run_time=2)

        self.wait(2) # drop cloud text here---------important

        # # for

        self.play(TransformFromCopy(frametext3, frametext2))
        self.play(TransformFromCopy(code_text8[16:32], code_text5[16:32]), run_time=2)

        self.play(TransformFromCopy(frametext13, frametext12))
        self.play(TransformFromCopy(code_text7[20:36], code_text10[-17:-1]), run_time=2)

        # else

        self.play(TransformFromCopy(frametext12, frametext15))
        self.play(TransformFromCopy(code_text7[79:83], code_text10[28:32]), run_time=2)

        # i**3

        self.play(TransformFromCopy(frametext15, frametext16))
        self.play(TransformFromCopy(code_text7[106:110], code_text10[32:36]), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(frametext4),FadeOut(frametext3),FadeOut(frametext1),FadeOut(frametext2),
                  FadeOut(frametext14),FadeOut(frametext13),FadeOut(frametext11),FadeOut(frametext12),
                  FadeOut(frametext15), FadeOut(frametext16))

        frametext_o1 = SurroundingRectangle(code_text10[20:28], fill_opacity=0.2, buff=0.05)

        frametext_o2 = SurroundingRectangle(code_text5[-9:-1], fill_opacity=0.2, buff=0.05)

        self.play(FadeIn(frametext_o2), FadeIn(frametext_o1))

        self.wait(2)

        self.play(Create(frametext5),Create(frametext17))

        create_rectange(6, 0.6, 0.01 * UP + 3.5 * RIGHT, BLACK)


        curved_arrow2 = CurvedArrow(0.68 * DOWN + 4.1 * LEFT,  1 * UP + 1.4 * RIGHT, angle=-1.5)
        curved_arrow1 = CurvedArrow(2.8 * DOWN + 4.5 * LEFT,  0.15 * DOWN + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow2), ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkupWithout(r"<span font_family='monospace'><b>[1, 4, 27, 16, 125]</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 2.2 * RIGHT)

        inside_output1 = currentTextPositionMarkupWithout(r"<span font_family='monospace'><b>[4, 16]</b></span>",
                      0.4, TEAL_D, 0.01 * UP + 1.2 * RIGHT)

        self.play(Write(inside_output1), Write(inside_output))
        self.wait(8)


        # ------------------- for loop - or - Dictionary comprehension ----------------------
        self.play(FadeOut(curved_arrow1),FadeOut(curved_arrow2), FadeOut(inside_output), FadeOut(inside_output1),
                  FadeOut(frametext_o2), FadeOut(frametext_o1),  FadeOut(frametext17), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5), FadeOut(code_text7), 
                  FadeOut(code_text8), FadeOut(code_text10))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Dictionary Comprehension</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> nums = [1, 2, 3]\n>>> alphs = ['A', 'B', 'C']\n>>> new_dict = {}\n>>> for i, j in zip(nums, alphs):\n...     new_dict[i] = j\n>>> print(new_dict)"""
        
        code_text9 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 0.25 * UP + 4.5 * LEFT)
        code_text9[0:3].set_color(RED_D)
        code_text9[15:18].set_color(RED_D)
        code_text9[25:36].set_color(GREEN_D)
        code_text9[37:40].set_color(RED_D)
        code_text9[51:54].set_color(RED_D)
        code_text9[54:57].set_color(ORANGE)
        code_text9[60:62].set_color(ORANGE)
        code_text9[62:65].set_color(BLUE_C)
        code_text9[78:81].set_color(RED_D)
        code_text9[94:97].set_color(RED_D)
        code_text9[97:102].set_color(BLUE_C)
        self.play(Write(code_text9), run_time=2)

        frametext1 = SurroundingRectangle(code_text9[3:15], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text9[18:37], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text9[40:51], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text9[54:77], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text9[81:94], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text9[97:], fill_opacity=0.2, buff=0.05)
        frametext7 = SurroundingRectangle(code_text9[90:91], fill_opacity=0.2, buff=0.05) # i
        frametext8 = SurroundingRectangle(code_text9[93:94], fill_opacity=0.2, buff=0.05) # j

        if_else_code_one = """>>> new_dict = {i: j for i, j in zip(nums, alphs)}""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[16:19].set_color(ORANGE)
        code_text5[22:24].set_color(ORANGE)
        code_text5[24:27].set_color(BLUE_C)

        self.add(code_text5[0:3])
        self.play(Create(frametext3))
        self.play(TransformFromCopy(code_text9[40:51], code_text5[3:13]), 
                  TransformFromCopy(code_text9[40:51], code_text5[-1:]), run_time=2)

        self.play(TransformFromCopy(frametext3, frametext7), TransformFromCopy(frametext3, frametext8))
        self.play(TransformFromCopy(code_text9[90:91], code_text5[13:15]), 
                  TransformFromCopy(code_text9[93:94], code_text5[15:16]), run_time=2)

        self.play(TransformFromCopy(frametext7, frametext4))
        self.play(TransformFromCopy(frametext8, frametext4))
        self.play(TransformFromCopy(code_text9[54:77], code_text5[16:-1]), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(suggest_not_fixed))

        suggest = """we have used zip to \navoid extra 'for' loops."""
        
        suggest_not_fixed = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{suggest}</b></span>',
                      0.4, BLACK, 2 * DOWN + 4.8 * RIGHT)
        self.play(Write(suggest_not_fixed), run_time=1.5)

        self.play(FadeOut(frametext8),FadeOut(frametext3),FadeOut(frametext4),
                  FadeOut(frametext7))

        self.play(FadeIn(frametext1))
        self.wait(0.5)
        self.play(Transform(frametext1, frametext2))
        self.wait(0.5)
        self.play(Transform(frametext2, frametext3), FadeOut(frametext1))
        self.wait(0.5)


        frametext_o1 = SurroundingRectangle(code_text5[16:-1], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3, frametext4), FadeIn(frametext_o1), FadeOut(frametext2))
        self.wait(1)

        frametext_o2 = SurroundingRectangle(code_text5[13:16], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext4,frametext5), 
                  Transform(frametext_o1,frametext_o2), FadeOut(frametext3))
        self.wait(1)

        self.play(Transform(frametext5,frametext6), Transform(frametext_o2,frametext6),
                  FadeOut(frametext4), FadeOut(frametext_o1))
        self.wait(1)

        curved_arrow1 = CurvedArrow(0.6 * DOWN + 4.5 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>{1: 'A', 2: 'B', 3: 'C'}</b></span>",
                      0.3, TEAL_D, 0.8 * UP + 2.1 * RIGHT)

        self.wait(8)

        # ------------------- for loop - if-else condition - or - Dictionary comprehension ----------------------
        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o2), FadeOut(frametext6), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>For loop With if-condition</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> even_squares = {}\n>>> for num in range(10):\n...     if num % 2 == 0:\n...         even_squares[num] = num**2\n>>> print(even_squares)"""
        
        code_text7 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.45 * DOWN + 4.1 * LEFT)
        code_text7[0:3].set_color(RED_D)
        code_text7[18:21].set_color(RED_D)
        code_text7[21:24].set_color(ORANGE)
        code_text7[27:29].set_color(ORANGE)
        code_text7[29:34].set_color(BLUE_C)
        code_text7[39:42].set_color(RED_D)
        code_text7[42:44].set_color(ORANGE)
        code_text7[53:56].set_color(RED_D)
        code_text7[80:83].set_color(RED_D)
        code_text7[83:88].set_color(BLUE_C)
        self.play(Write(code_text7), run_time=2)

        frametext1 = SurroundingRectangle(code_text7[3:18], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text7[21:38], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text7[42:52], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text7[56:80], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text7[83:], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text7[69:72], fill_opacity=0.2, buff=0.05)# num
        frametext7 = SurroundingRectangle(code_text7[74:80], fill_opacity=0.2, buff=0.05) # ** 2


        if_else_code_one = """>>> even_squares = {num: num**2 for num in range(10) if num % 2 == 0}""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[27:30].set_color(ORANGE)
        code_text5[33:35].set_color(ORANGE)
        code_text5[35:40].set_color(BLUE_C)
        code_text5[44:46].set_color(ORANGE)

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text7[3:18], code_text5[3:17]), 
                  TransformFromCopy(code_text7[3:18], code_text5[-1:]), run_time=2)

        self.play(TransformFromCopy(frametext1, frametext6), TransformFromCopy(frametext1, frametext7))
        self.play(TransformFromCopy(code_text7[69:72], code_text5[17:21]), 
                  TransformFromCopy(code_text7[74:80], code_text5[21:27]), run_time=2)

        self.play(TransformFromCopy(frametext6, frametext2))
        self.play(TransformFromCopy(frametext7, frametext2))
        self.play(TransformFromCopy(code_text7[21:38], code_text5[27:44]), run_time=2)

        self.play(TransformFromCopy(frametext2, frametext3))
        self.play(TransformFromCopy(code_text7[42:52], code_text5[44:-1]), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(frametext6),FadeOut(frametext3),FadeOut(frametext1),FadeOut(frametext2),
                  FadeOut(frametext7), FadeOut(suggest_not_fixed))

        self.play(FadeIn(frametext1), FadeIn(second_menu_vary))


        frametext_o1 = SurroundingRectangle(code_text5[27:44], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext1, frametext2), FadeIn(frametext_o1))
        self.wait(1)

        frametext_o2 = SurroundingRectangle(code_text5[44:-1], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext2,frametext3), 
                  Transform(frametext_o1,frametext_o2), FadeOut(frametext1))
        self.wait(1)

        frametext_o3 = SurroundingRectangle(code_text5[17:27], fill_opacity=0.2, buff=0.05)
        self.play(Transform(frametext3,frametext4), Transform(frametext_o2,frametext_o3),
                  FadeOut(frametext2), FadeOut(frametext_o1))
        self.wait(1)

        self.play(Transform(frametext4,frametext5), Transform(frametext_o3,frametext5),
                  FadeOut(frametext3), FadeOut(frametext_o2))
        self.wait(1)

        curved_arrow1 = CurvedArrow(2.21 * DOWN + 4.5 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}</b></span>",
                      0.3, TEAL_D, 0.8 * UP + 2.7 * RIGHT)
        self.wait(8)

        # ------------------- swap variable  ----------------------
        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o3), FadeOut(frametext4), FadeOut(frametext5), 
                  FadeOut(top_text_replace), FadeOut(code_text5),FadeOut(code_text7),FadeOut(code_text9))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Swapping two variables</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> first_var = 8\n>>> second_var = 'nine'\n>>> temp = first_var\n>>> first_var = second_var\n>>> second_var = temp\n>>> print(first_var, second_var)"""
        
        code_text17 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 0.25 * UP + 4.55 * LEFT)
        code_text17[0:3].set_color(RED_D)
        code_text17[14:17].set_color(RED_D)
        code_text17[28:34].set_color(GREEN_D)
        code_text17[34:37].set_color(RED_D)
        code_text17[51:54].set_color(RED_D)
        code_text17[74:77].set_color(RED_D)
        code_text17[92:95].set_color(RED_D)
        code_text17[95:100].set_color(BLUE_C)
        self.play(Write(code_text17), run_time=2)

        frametext1 = SurroundingRectangle(code_text17[3:12], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text17[17:27], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text17[-28:], fill_opacity=0.2, buff=0.05)


        if_else_code_one = """>>> first_var, second_var = second_var, first_var""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text17[3:12], code_text5[3:12]), 
                  TransformFromCopy(code_text17[3:12], code_text5[-9:]), run_time=2)

        self.play(Create(frametext2))
        self.play(TransformFromCopy(code_text17[17:27], code_text5[13:23]), 
                  TransformFromCopy(code_text17[17:27], code_text5[24:35]), 
                  FadeIn(code_text5[12:13]), FadeIn(code_text5[23:24]),run_time=2)
        self.wait(0.5)

        self.play(FadeOut(frametext1), Transform(frametext2, frametext3))

        curved_arrow1 = CurvedArrow(0.68 * DOWN + 4.5 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>nine 8</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 1.2 * RIGHT)

        self.play(Write(pros_cons_fixed[19:38]))

        # ------------------- swap variable  ----------------------
        self.play(FadeOut(curved_arrow1), FadeOut(inside_output), 
                  FadeOut(frametext2), FadeOut(frametext3), 
                  FadeOut(top_text_replace), FadeOut(code_text5))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Multiple Variables Assignment</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> var1 = {2:"a", 3:"b"}\n>>> var2 = [1,2,4]\n>>> var3 = (12,34,56)"""
        
        code_text7 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.2 * DOWN + 5.03 * LEFT)
        code_text7[0:3].set_color(RED_D)
        code_text7[11:14].set_color(GREEN_D)
        code_text7[17:20].set_color(GREEN_D)
        code_text7[21:24].set_color(RED_D)
        code_text7[36:39].set_color(RED_D)
        self.play(Write(code_text7), run_time=2)

        frametext1 = SurroundingRectangle(code_text7[3:7], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text7[8:21], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text7[24:28], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text7[29:36], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text7[39:43], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text7[44:], fill_opacity=0.2, buff=0.05)# num


        if_else_code_one = """>>> var1, var2, var3 = {2:"a", 3:"b"}, [1,2,4], (12,34,56)""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[21:24].set_color(GREEN_D)
        code_text5[27:30].set_color(GREEN_D)

        self.add(code_text5[0:3])
        self.play(Create(frametext1), Create(frametext2))
        self.play(TransformFromCopy(code_text7[3:7], code_text5[3:8]), 
                  TransformFromCopy(code_text7[8:21], code_text5[17:32]), run_time=2)

        self.play(TransformFromCopy(frametext1, frametext3), TransformFromCopy(frametext2, frametext4))
        self.play(TransformFromCopy(code_text7[24:28], code_text5[8:13]), 
                  TransformFromCopy(code_text7[29:36], code_text5[32:40]), run_time=2)

        self.play(TransformFromCopy(frametext3, frametext5), TransformFromCopy(frametext4, frametext6))
        self.play(TransformFromCopy(code_text7[39:43], code_text5[13:17]), 
                  TransformFromCopy(code_text7[44:], code_text5[40:]), run_time=2)

        # --------------------------- new variable assignment -------------------------------

        self.play(FadeOut(code_text5))


        if_else_code_one = """>>> a,b,*c = ["this", 'is', 'a', 'great', 'day']""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[11:-1].set_color(GREEN_D)
        self.play(FadeOut(frametext1), FadeOut(frametext2), FadeOut(frametext3),
                  FadeOut(frametext4),FadeOut(frametext5),FadeOut(frametext6))
        self.play(Write(code_text5))

        frametext_o2 = SurroundingRectangle(code_text5[3:9], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext_o2))


        if_else_code = """>>> print(a, b, c)"""

        code_text8 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.8 * DOWN + 5.58 * LEFT)
        code_text8[0:3].set_color(RED_D)
        code_text8[3:8].set_color(GREEN_D)

        self.play(TransformFromCopy(code_text5[3:9], code_text8[9:-1]))
        self.play(Write(code_text8[0:9]), Write(code_text8[-1]), run_time=1)
        self.wait(0.5)


        frametext12 = SurroundingRectangle(code_text8[3:], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext12))
        curved_arrow1 = CurvedArrow(2 * DOWN + 4.5 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>this is ['a', 'great', 'day']</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 2.9 * RIGHT)

        self.wait(8)

        self.play(FadeOut(code_text5), FadeOut(frametext_o2), FadeOut(frametext12), FadeOut(curved_arrow1), 
                  FadeOut(inside_output), FadeOut(top_text_replace))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Global Variables</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> num = 20\n>>> def update():\n...     global num\n...     num = 40\n>>> update()\n>>> print(num)"""

        code_text9 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 2.8 * DOWN + 5.54 * LEFT)
        code_text9[0:3].set_color(RED_D)
        code_text9[9:12].set_color(RED_D)
        code_text9[12:15].set_color(ORANGE)
        code_text9[15:21].set_color(YELLOW_C)
        code_text9[24:27].set_color(RED_D)
        code_text9[27:33].set_color(ORANGE)
        code_text9[36:39].set_color(RED_D)
        code_text9[45:48].set_color(RED_D)
        code_text9[56:59].set_color(RED_D)
        code_text9[59:64].set_color(BLUE_C)

        self.play(Write(code_text9), run_time=1)
        frametext1 = SurroundingRectangle(code_text9[27:36], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text9[39:45], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text9[48:56], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text9[59:], fill_opacity=0.2, buff=0.05)


        if_else_code_one = """>>> def update():\n...     globals()['num'] = 40""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[3:6].set_color(ORANGE)
        code_text5[6:12].set_color(YELLOW_C)
        code_text5[15:18].set_color(RED_D)
        code_text5[18:25].set_color(BLUE_C)
        self.play(Write(code_text5[0:18]))


        self.play(Create(frametext1), Create(frametext2))
        self.play(TransformFromCopy(code_text9[27:36], code_text5[18:]), 
                  run_time=2)

        frametext_o1 = SurroundingRectangle(code_text5[18:44], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext_o1))

        self.play(Transform(frametext1, frametext3), FadeOut(frametext2), Transform(frametext_o1,frametext3))
        self.wait(1)
        self.play(Transform(frametext3, frametext4), FadeOut(frametext1), FadeOut(frametext_o1))
        self.wait(1)

        curved_arrow1 = CurvedArrow(3.4 * DOWN + 4.8 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>40</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 0.9 * RIGHT)

        self.wait(1)

        if_else_code_one = """>>> def update():\n...     globals().update(num=40)""" 
        code_text25 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text25[0:3].set_color(RED_D)
        code_text25[3:6].set_color(ORANGE)
        code_text25[6:12].set_color(YELLOW_C)
        code_text25[15:18].set_color(RED_D)
        code_text25[18:25].set_color(BLUE_C)
        self.add(code_text25[0:18])

        self.play(FadeOut(code_text5))
        frametext1 = SurroundingRectangle(code_text9[27:36], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text9[39:45], fill_opacity=0.2, buff=0.05)

        self.play(Create(frametext1), Create(frametext2))
        self.play(TransformFromCopy(code_text9[27:36], code_text25[18:]), 
                  run_time=2)

        frametext_o1 = SurroundingRectangle(code_text25[18:], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext_o1))
        self.wait(8)

        # ------------------- lambda function  ----------------------
        self.play(FadeOut(curved_arrow1), FadeOut(inside_output),
                  FadeOut(frametext_o1), FadeOut(frametext1), FadeOut(frametext2),FadeOut(frametext3), FadeOut(frametext4), 
                  FadeOut(top_text_replace), FadeOut(code_text25) , FadeOut(code_text7), FadeOut(code_text8),
                  FadeOut(code_text9), FadeOut(code_text17))

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Lambda function</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> list_add = [3,4,5,6,7]\n>>> def list_sum(list_var):\n...     return sum(list_var)\n>>> total = list_sum(list_add)\n>>> print(total)"""
        
        code_text7 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 0.4 * UP + 4.7 * LEFT)
        code_text7[0:3].set_color(RED_D)
        code_text7[23:26].set_color(RED_D)
        code_text7[26:29].set_color(ORANGE)
        code_text7[29:37].set_color(YELLOW_C)
        code_text7[48:51].set_color(RED_D)

        code_text7[51:57].set_color(ORANGE)
        code_text7[57:60].set_color(BLUE_C)
        code_text7[70:73].set_color(RED_D)
        code_text7[97:100].set_color(RED_D)
        code_text7[100:105].set_color(BLUE_C)
        self.play(Write(code_text7), run_time=2)

        frametext1 = SurroundingRectangle(code_text7[29:47], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text7[57:70], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text7[73:97], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text7[100:], fill_opacity=0.2, buff=0.05)


        if_else_code_one = """>>> list_sum = lambda list_var: sum(list_var)""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[12:18].set_color(GREEN_D)
        code_text5[27:30].set_color(BLUE_C)

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text7[29:47], code_text5[3:27]), run_time=2)

        self.play(TransformFromCopy(frametext1, frametext2))
        self.play(TransformFromCopy(code_text7[57:70], code_text5[27:]), run_time=2)
        self.wait(1)

        frametext_o1 = SurroundingRectangle(code_text5[3:11], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext_o1))

        self.play(Transform(frametext2, frametext3), FadeOut(frametext1), Transform(frametext_o1,frametext3))
        self.wait(1)
        self.play(Transform(frametext3, frametext4), FadeOut(frametext2), FadeOut(frametext_o1))
        self.wait(0.5)

        curved_arrow1 = CurvedArrow(0.35 * DOWN + 4.8 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>25</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 0.9 * RIGHT)

        self.wait(8)
        self.play(Write(pros_cons_fixed[38:]))
        self.play(FadeOut(curved_arrow1), FadeOut(inside_output), FadeOut(frametext4), FadeOut(frametext3), 
                  FadeOut(top_text_replace), FadeOut(code_text5))


        # -------------- lambda Fibonacci Series -----------

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>Fibonacci Series With lambda</b></span>',
                      0.5, TEAL_A, 3.5 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        if_else_code = """>>> def fib(n):\n...     if n in [0, 1]:\n...         return 1\n...     else:\n...         return fib(n-1) + fib(n-2)\n>>> print(fib(10))"""

        code_text9 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.37, GREY_A, 1.28 * DOWN + 4.11 * LEFT)
        code_text9[0:3].set_color(RED_D)
        code_text9[3:6].set_color(ORANGE)
        code_text9[6:9].set_color(YELLOW_C)
        code_text9[13:16].set_color(RED_D)
        code_text9[16:18].set_color(ORANGE)
        code_text9[19:21].set_color(ORANGE)
        code_text9[27:30].set_color(RED_D)
        code_text9[30:36].set_color(ORANGE)
        code_text9[37:40].set_color(RED_D)
        code_text9[40:44].set_color(ORANGE)
        code_text9[45:48].set_color(RED_D)
        code_text9[48:54].set_color(ORANGE)
        code_text9[71:74].set_color(RED_D)
        code_text9[74:79].set_color(BLUE_C)
        self.play(Write(code_text9), run_time=2)

        frametext1 = SurroundingRectangle(code_text9[6:12], fill_opacity=0.2, buff=0.05)
        frametext2 = SurroundingRectangle(code_text9[16:26], fill_opacity=0.2, buff=0.05)
        frametext3 = SurroundingRectangle(code_text9[36:37], fill_opacity=0.2, buff=0.05)
        frametext4 = SurroundingRectangle(code_text9[40:44], fill_opacity=0.2, buff=0.05)
        frametext5 = SurroundingRectangle(code_text9[54:71], fill_opacity=0.2, buff=0.05)
        frametext6 = SurroundingRectangle(code_text9[74:], fill_opacity=0.2, buff=0.05)


        if_else_code_one = """>>> fib = lambda n: 1 if n in [0, 1] else fib(n-1) + fib(n-2)""" 
        code_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code_one}</b></span>',
                      0.4, GREY_A, 2.25 * UP + 1.2 * LEFT)

        code_text5[0:3].set_color(RED_D)
        code_text5[7:13].set_color(ORANGE)
        code_text5[16:18].set_color(ORANGE)
        code_text5[19:21].set_color(ORANGE)
        code_text5[26:30].set_color(ORANGE)

        self.add(code_text5[0:3])
        self.play(Create(frametext1))
        self.play(TransformFromCopy(code_text9[6:12], code_text5[3:15]), 
                  run_time=2)

        self.play(TransformFromCopy(frametext1, frametext3))
        self.play(TransformFromCopy(code_text9[36:37], code_text5[15:16]), 
                  run_time=2)

        self.play(TransformFromCopy(frametext3, frametext2))
        self.play(TransformFromCopy(code_text9[16:26], code_text5[16:26]), 
                  run_time=2)

        self.play(TransformFromCopy(frametext2, frametext4))
        self.play(TransformFromCopy(code_text9[40:44], code_text5[26:30]), 
                  run_time=2)

        self.play(TransformFromCopy(frametext4, frametext5))
        self.play(TransformFromCopy(code_text9[54:71], code_text5[30:]), 
                  run_time=2)

        frametext_o1 = SurroundingRectangle(code_text5[3:6], fill_opacity=0.2, buff=0.05)
        self.play(Create(frametext_o1))

        self.play(Transform(frametext5, frametext6), Transform(frametext_o1,frametext6))
        self.play(FadeOut(frametext1), FadeOut(frametext2), FadeOut(frametext3), FadeOut(frametext4))
        self.wait(1)

        curved_arrow1 = CurvedArrow(2.2 * DOWN + 4.8 * LEFT,  0.6 * UP + 0.9 * RIGHT, angle=1.5)
        self.play(ShowCreation(curved_arrow1))

        inside_output = currentTextPositionMarkup(r"<span font_family='monospace'><b>89</b></span>",
                      0.4, TEAL_D, 0.8 * UP + 0.9 * RIGHT)

        self.wait(4)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
