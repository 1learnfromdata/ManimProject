from manim import *


class DataframeFilters(Scene):
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
            rect.set_stroke(color=color_name, opacity=1)
            rect.set_fill(color=color_name, opacity=0.5)
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

        # for x in range(-7, 8):
        #     for y in range(-4, 5):
        #         self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
        # circle = Circle(color=RED, radius=0.3)
        # circle.set_stroke(color=RED, opacity=0.3)
        # self.play(Write(circle,run_time=0.1))

        top_disapper_text = currentTextPositionMarkup(f'<span font_family="monospace"><b>Filter Pandas DataFrame: </b></span>',
                      0.5, TEAL_A, 3.7 * UP + 1.6 * LEFT)

        top_text_replace = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>.loc and .iloc</b></span>',
                      0.5, TEAL_A, 3.7 * UP + 0.6 * LEFT)
        top_text_replace.next_to(top_disapper_text)
        self.play(Write(top_text_replace))

        create_rectange(13.9, 0.6, 3.1 * UP + 0.1 * LEFT, DARK_GREY)
        red_arrow_fixed1 = currentTextPositionMarkupWithout(r'<span font_family="monospace">>>> </span>',
                      0.45, WHITE, 3.1 * UP + 6.65 * LEFT)
        red_arrow_fixed1.set_color(RED_D)
        self.play(Write(red_arrow_fixed1))

        box_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace">  student_df</span>',
                      0.45, WHITE, 3.1 * UP + 5.6 * LEFT)
        box_disapper_text1.next_to(red_arrow_fixed1)
        self.play(Write(box_disapper_text1))



        #     ROLLNO NAME                      BRANCH                    TOTAL   Age  | Hobby 

        width_r = 3
        height_r = 0.6 

        # ----------- row 0 -----------

        table_00 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>INDEX</b></span>')
        table_00.shift(2.4 * UP + 5.3 * LEFT)
        # table_00.set_stroke(color=GOLD_C, opacity=0)

        # print(self.get_edges(table_00))

        table_01 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>ROLLNO</b></span>')
        table_01.next_to(table_00, buff=0)

        table_02 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>NAME</b></span>')
        table_02.next_to(table_01, buff=0)

        table_03 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>BRANCH</b></span>')
        table_03.next_to(table_02, buff=0)

        table_04 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>TOTAL</b></span>')
        table_04.next_to(table_03, buff=0)

        table_05 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>AGE</b></span>')
        table_05.next_to(table_04, buff=0)

        table_06 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>HOBBY</b></span>')
        table_06.next_to(table_05, buff=0)

        self.play(GrowFromCenter(table_05), GrowFromCenter(table_04), GrowFromCenter(table_03), GrowFromCenter(table_02),
                  GrowFromCenter(table_01), GrowFromCenter(table_06),GrowFromCenter(table_00))

        row_zero_group = VGroup()
        row_zero_group.add(table_00, table_01, table_02, table_03, table_04, table_05,table_06)

        # -----------row 1 -------------------


        table_10 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>0</b></span>')
        table_10.shift(2.05 * UP + 5.3 * LEFT)
        # table_10.set_stroke(color=GOLD_C, opacity=0)

        table_11 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>101</b></span>')
        table_11.next_to(table_10, buff=0)

        table_12 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>ANUJ</b></span>')
        table_12.next_to(table_11, buff=0)

        table_13 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>COMMERCE</b></span>')
        table_13.next_to(table_12, buff=0)

        table_14 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>200</b></span>')
        table_14.next_to(table_13, buff=0)

        table_15 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>23</b></span>')
        table_15.next_to(table_14, buff=0)

        table_16 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>BASKETBALL</b></span>')
        table_16.next_to(table_15, buff=0)

        self.play(GrowFromCenter(table_15), GrowFromCenter(table_14), GrowFromCenter(table_13), GrowFromCenter(table_12),
                  GrowFromCenter(table_11), GrowFromCenter(table_16),GrowFromCenter(table_10))

        row_one_group = VGroup()
        row_one_group.add(table_10, table_11, table_12, table_13, table_14, table_15,table_16)

        # ---------- row 2 ---------------------

        table_20 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>1</b></span>')
        table_20.shift(1.7 * UP + 5.3 * LEFT)
        # table_20.set_stroke(color=GOLD_C, opacity=0)

        table_21 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>102</b></span>')
        table_21.next_to(table_20, buff=0)

        table_22 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>BALE</b></span>')
        table_22.next_to(table_21, buff=0)

        table_23 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>SCIENCE</b></span>')
        table_23.next_to(table_22, buff=0)

        table_24 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>150</b></span>')
        table_24.next_to(table_23, buff=0)

        table_25 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>21</b></span>')
        table_25.next_to(table_24, buff=0)

        table_26 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>CHESS</b></span>')
        table_26.next_to(table_25, buff=0)

        self.play(GrowFromCenter(table_25), GrowFromCenter(table_24), GrowFromCenter(table_23), GrowFromCenter(table_21),
                  GrowFromCenter(table_22), GrowFromCenter(table_26),GrowFromCenter(table_20))

        row_two_group = VGroup()
        row_two_group.add(table_20, table_21, table_22, table_23, table_24, table_25,table_26)

        #   -------- row 4 ---------------
        table_30 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>2</b></span>')
        table_30.shift(1.35 * UP + 5.3 * LEFT)
        # table_30.set_stroke(color=GOLD_C, opacity=0)

        table_31 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>103</b></span>')
        table_31.next_to(table_30, buff=0)

        table_32 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>GEORGE</b></span>')
        table_32.next_to(table_31, buff=0)

        table_33 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>HUMANITIES</b></span>')
        table_33.next_to(table_32, buff=0)

        table_34 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>400</b></span>')
        table_34.next_to(table_33, buff=0)

        table_35 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>22</b></span>')
        table_35.next_to(table_34, buff=0)

        table_36 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>PAINTING</b></span>')
        table_36.next_to(table_35, buff=0)

        self.play(GrowFromCenter(table_35), GrowFromCenter(table_34), GrowFromCenter(table_33), GrowFromCenter(table_32),
                  GrowFromCenter(table_31), GrowFromCenter(table_36),GrowFromCenter(table_30))

        row_three_group = VGroup()
        row_three_group.add(table_30, table_31, table_32, table_33, table_34, table_35,table_36)


        # ------------- ROW 5  ------------------

        table_40 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>3</b></span>')
        table_40.shift(1 * UP + 5.3 * LEFT)
        # table_40.set_stroke(color=GOLD_C, opacity=0)

        table_41 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>104</b></span>')
        table_41.next_to(table_40, buff=0)

        table_42 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>JIBIN</b></span>')
        table_42.next_to(table_41, buff=0)

        table_43 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>COMMERCE</b></span>')
        table_43.next_to(table_42, buff=0)

        table_44 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>300</b></span>')
        table_44.next_to(table_43, buff=0)

        table_45 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>23</b></span>')
        table_45.next_to(table_44, buff=0)

        table_46 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>BASKETBALL</b></span>')
        table_46.next_to(table_45, buff=0)

        self.play(GrowFromCenter(table_45), GrowFromCenter(table_44), GrowFromCenter(table_43), GrowFromCenter(table_42),
                  GrowFromCenter(table_41), GrowFromCenter(table_46),GrowFromCenter(table_40))
        row_four_group = VGroup()
        row_four_group.add(table_40, table_41, table_42, table_43, table_44, table_45,table_46)

        # --------------ROW 6 ---------------

        table_50 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>4</b></span>')
        table_50.shift(0.65 * UP + 5.3 * LEFT)
        # table_50.set_stroke(color=GOLD_C, opacity=0)

        table_51 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>105</b></span>')
        table_51.next_to(table_50, buff=0)

        table_52 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>JOHN</b></span>')
        table_52.next_to(table_51, buff=0)

        table_53 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>SCIENCE</b></span>')
        table_53.next_to(table_52, buff=0)

        table_54 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>150</b></span>')
        table_54.next_to(table_53, buff=0)

        table_55 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>18</b></span>')
        table_55.next_to(table_54, buff=0)

        table_56 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>SWIMMING</b></span>')
        table_56.next_to(table_55, buff=0)

        self.play(GrowFromCenter(table_55), GrowFromCenter(table_54), GrowFromCenter(table_53), GrowFromCenter(table_52),
                  GrowFromCenter(table_51), GrowFromCenter(table_56),GrowFromCenter(table_50))

        row_five_group = VGroup()
        row_five_group.add(table_50, table_51, table_52, table_53, table_54, table_55,table_56)

        #  --------------- ROW 7---------------

        table_60 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>5</b></span>')
        table_60.shift(0.3 * UP + 5.3 * LEFT)
        # table_60.set_stroke(color=GOLD_C, opacity=0)

        table_61 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>106</b></span>')
        table_61.next_to(table_60, buff=0)

        table_62 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>SOMAN</b></span>')
        table_62.next_to(table_61, buff=0)

        table_63 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>HUMANITIES</b></span>')
        table_63.next_to(table_62, buff=0)

        table_64 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>430</b></span>')
        table_64.next_to(table_63, buff=0)

        table_65 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>22</b></span>')
        table_65.next_to(table_64, buff=0)

        table_66 = dataframe_rectange(width_r, height_r, r'<span font_family="monospace"><b>CRICKET</b></span>')
        table_66.next_to(table_65, buff=0)

        self.play(GrowFromCenter(table_65), GrowFromCenter(table_64), GrowFromCenter(table_63), GrowFromCenter(table_62),
                  GrowFromCenter(table_61), GrowFromCenter(table_66),GrowFromCenter(table_60))

        row_six_group = VGroup()
        row_six_group.add(table_60, table_61, table_62, table_63, table_64, table_65,table_66)

        self.wait(0.5)

        create_rectange(6, 0.6, 0.8 * DOWN + 4  * LEFT, DARK_GREY)
        create_rectange(6, 0.6, 0.8 * DOWN + 3.5 * RIGHT, DARK_GREY)
        self.wait(5)

        red_arrow_fixed2 = currentTextPositionMarkupWithout(r'<span font_family="monospace">>>> </span>',
                      0.45, WHITE, 0.8 * DOWN + 6.65  * LEFT)
        red_arrow_fixed2.set_color(RED_D)
        self.play(Write(red_arrow_fixed2))

        box_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace">student_df.loc[3]</span>',
                      0.45, WHITE, 0.8 * DOWN + 5  * LEFT)
        box_disapper_text2.next_to(red_arrow_fixed2)
        self.play(Write(box_disapper_text2))
        self.wait(5)


        self.wait(1)    



        loc_result = """ROLLNO           104\nNAME           JIBIN\nBRANCH      COMMERCE\nTOTAL            300\nAGE               23\nHOBBY     basketball\nName: 3, dtype: object"""
        
        loc_result_vary = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{loc_result}</b></span>',
                      0.37, GREY_A, 2.3 * DOWN + 5  * LEFT)

        highlight_row = dataframe_swap(12.6, 0.4, BLUE_D)
        highlight_row.shift(1 * UP + 0.11 * RIGHT)
        self.play(Create(highlight_row),run_time=2)

        self.play(TransformFromCopy(row_four_group, loc_result_vary), run_time=2)

        self.wait(0.5)
        self.wait(5)

        red_arrow_fixed3 = currentTextPositionMarkupWithout(r'<span font_family="monospace">>>> </span>',
                      0.45, WHITE, 0.8 * DOWN + 0.9 * RIGHT)
        red_arrow_fixed3.set_color(RED_D)
        self.play(Write(red_arrow_fixed3))

        box_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace">student_df.iloc[3]</span>',
                      0.45, WHITE, 0.8 * DOWN + 2.5 * RIGHT)
        box_disapper_text3.next_to(red_arrow_fixed3)
        self.play(Write(box_disapper_text3))

        iloc_result = """ROLLNO           104\nNAME           JIBIN\nBRANCH      COMMERCE\nTOTAL            300\nAGE               23\nHOBBY     basketball\nName: 3, dtype: object"""
        
        iloc_result_vary = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{iloc_result}</b></span>',
                      0.37, GREY_A, 2.3 * DOWN + 3  * RIGHT)
        self.wait(0.5)


        self.play(TransformFromCopy(row_four_group, iloc_result_vary), run_time=2)

        self.wait(4)

        self.play(FadeOut(highlight_row), FadeOut(loc_result_vary), FadeOut(iloc_result_vary), 
                  FadeOut(box_disapper_text2), FadeOut(box_disapper_text3))
        self.wait(5)

        box_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace">student_df.loc[0:3]</span>',
                      0.45, WHITE, 0.8 * DOWN + 5  * LEFT)
        box_disapper_text2.next_to(red_arrow_fixed2)
        self.play(Write(box_disapper_text2))

        self.wait(1)
        self.wait(5)

        highlight_row = dataframe_swap(12.6, 1.4, BLUE_D)
        highlight_row.shift(1.55 * UP + 0.11 * RIGHT)
        self.play(Create(highlight_row),run_time=2)  
        self.wait(5)

        def dataframe_rectange_s(x, y, content):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=GOLD_C, opacity=1)
            rect.scale(0.6)
            text = MarkupText(content)
            text.scale(0.23)
            squ_text = VGroup()
            squ_text.add(rect, text)
            return squ_text

        width_s = 1.5
        height_s = 0.6

        # -------------------- left side results -----------------------------------------

        # ----------- row 0 -----------

        left_tab_00 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>INDEX</b></span>')
        left_tab_00.shift(1.6 * DOWN + 6.5 * LEFT)
        left_tab_00.set_stroke(color=GOLD_C, opacity=0)


        left_tab_01 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>ROLLNO</b></span>')
        left_tab_01.next_to(left_tab_00, buff=0)

        left_tab_02 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>NAME</b></span>')
        left_tab_02.next_to(left_tab_01, buff=0)

        left_tab_03 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BRANCH</b></span>')
        left_tab_03.next_to(left_tab_02, buff=0)

        left_tab_04 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>TOTAL</b></span>')
        left_tab_04.next_to(left_tab_03, buff=0)

        left_tab_05 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>AGE</b></span>')
        left_tab_05.next_to(left_tab_04, buff=0)

        left_tab_06 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>HOBBY</b></span>')
        left_tab_06.next_to(left_tab_05, buff=0)


        left_zero_group = VGroup()
        left_zero_group.add(left_tab_06, left_tab_05, left_tab_04, left_tab_03, left_tab_02, left_tab_01,left_tab_00)

        self.play(TransformFromCopy(row_zero_group, left_zero_group), run_time=2)
        self.play(FadeOut(left_tab_00))

        # -----------row 1 -------------------


        left_tab_10 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>0</b></span>')
        left_tab_10.shift(1.95 * DOWN + 6.5 * LEFT)
        # left_tab_10.set_stroke(color=GOLD_C, opacity=0)

        left_tab_11 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>101</b></span>')
        left_tab_11.next_to(left_tab_10, buff=0)

        left_tab_12 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>ANUJ</b></span>')
        left_tab_12.next_to(left_tab_11, buff=0)

        left_tab_13 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>COMMERCE</b></span>')
        left_tab_13.next_to(left_tab_12, buff=0)

        left_tab_14 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>200</b></span>')
        left_tab_14.next_to(left_tab_13, buff=0)

        left_tab_15 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>23</b></span>')
        left_tab_15.next_to(left_tab_14, buff=0)

        left_tab_16 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BASKETBALL</b></span>')
        left_tab_16.next_to(left_tab_15, buff=0)

        left_one_group = VGroup()
        left_one_group.add(left_tab_16, left_tab_15, left_tab_14, left_tab_13, left_tab_12, left_tab_11,left_tab_10)

        self.play(TransformFromCopy(row_one_group, left_one_group), run_time=2)

        # ---------- row 2 ---------------------

        left_tab_20 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>1</b></span>')
        left_tab_20.shift(2.3 * DOWN + 6.5 * LEFT)
        # left_tab_20.set_stroke(color=GOLD_C, opacity=0)

        left_tab_21 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>102</b></span>')
        left_tab_21.next_to(left_tab_20, buff=0)

        left_tab_22 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BALE</b></span>')
        left_tab_22.next_to(left_tab_21, buff=0)

        left_tab_23 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>SCIENCE</b></span>')
        left_tab_23.next_to(left_tab_22, buff=0)

        left_tab_24 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>150</b></span>')
        left_tab_24.next_to(left_tab_23, buff=0)

        left_tab_25 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>21</b></span>')
        left_tab_25.next_to(left_tab_24, buff=0)

        left_tab_26 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>CHESS</b></span>')
        left_tab_26.next_to(left_tab_25, buff=0)

        left_two_group = VGroup()
        left_two_group.add(left_tab_26, left_tab_25, left_tab_24, left_tab_23, left_tab_22, left_tab_21,left_tab_20)

        self.play(TransformFromCopy(row_two_group, left_two_group), run_time=1)

        #   -------- row 4 ---------------
        left_tab_30 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>2</b></span>')
        left_tab_30.shift(2.65 * DOWN + 6.5 * LEFT)
        # left_tab_30.set_stroke(color=GOLD_C, opacity=0)

        left_tab_31 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>103</b></span>')
        left_tab_31.next_to(left_tab_30, buff=0)

        left_tab_32 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>GEORGE</b></span>')
        left_tab_32.next_to(left_tab_31, buff=0)

        left_tab_33 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>HUMANITIES</b></span>')
        left_tab_33.next_to(left_tab_32, buff=0)

        left_tab_34 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>400</b></span>')
        left_tab_34.next_to(left_tab_33, buff=0)

        left_tab_35 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>22</b></span>')
        left_tab_35.next_to(left_tab_34, buff=0)

        left_tab_36 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>PAINTING</b></span>')
        left_tab_36.next_to(left_tab_35, buff=0)

        left_three_group = VGroup()
        left_three_group.add(left_tab_36, left_tab_35, left_tab_34, left_tab_33, left_tab_32, left_tab_31,left_tab_30)

        self.play(TransformFromCopy(row_three_group, left_three_group), run_time=1)


        # ------------- ROW 5  ------------------

        left_tab_40 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>3</b></span>')
        left_tab_40.shift(3 * DOWN + 6.5 * LEFT)
        # left_tab_40.set_stroke(color=GOLD_C, opacity=0)

        left_tab_41 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>104</b></span>')
        left_tab_41.next_to(left_tab_40, buff=0)

        left_tab_42 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>JIBIN</b></span>')
        left_tab_42.next_to(left_tab_41, buff=0)

        left_tab_43 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>COMMERCE</b></span>')
        left_tab_43.next_to(left_tab_42, buff=0)

        left_tab_44 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>300</b></span>')
        left_tab_44.next_to(left_tab_43, buff=0)

        left_tab_45 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>23</b></span>')
        left_tab_45.next_to(left_tab_44, buff=0)

        left_tab_46 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BASKETBALL</b></span>')
        left_tab_46.next_to(left_tab_45, buff=0)

        left_four_group = VGroup()
        left_four_group.add(left_tab_46, left_tab_45, left_tab_44, left_tab_43, left_tab_42, left_tab_41,left_tab_40)
        self.play(TransformFromCopy(row_four_group, left_four_group), run_time=2)

        self.wait(1)
        self.play(FadeOut(highlight_row))

        self.wait(5)

        box_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace">student_df.iloc[0:3]</span>',
                      0.45, WHITE, 0.8 * DOWN + 2.5 * RIGHT)
        box_disapper_text3.next_to(red_arrow_fixed3)
        self.play(Write(box_disapper_text3))

        self.wait(1)
        self.wait(5)

        highlight_row = dataframe_swap(12.6, 1.09, BLUE_D)
        highlight_row.shift(1.7 * UP + 0.11 * RIGHT)
        self.play(Create(highlight_row),run_time=2)  

        self.wait(1)
        self.wait(5)


        right_tab_00 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>INDEX</b></span>')
        right_tab_00.shift(1.6 * DOWN + 0.8 * RIGHT)
        right_tab_00.set_stroke(color=GOLD_C, opacity=0)

        right_tab_01 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>ROLLNO</b></span>')
        right_tab_01.next_to(right_tab_00, buff=0)

        right_tab_02 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>NAME</b></span>')
        right_tab_02.next_to(right_tab_01, buff=0)

        right_tab_03 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BRANCH</b></span>')
        right_tab_03.next_to(right_tab_02, buff=0)

        right_tab_04 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>TOTAL</b></span>')
        right_tab_04.next_to(right_tab_03, buff=0)

        right_tab_05 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>AGE</b></span>')
        right_tab_05.next_to(right_tab_04, buff=0)

        right_tab_06 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>HOBBY</b></span>')
        right_tab_06.next_to(right_tab_05, buff=0)


        right_zero_group = VGroup()
        right_zero_group.add(right_tab_06, right_tab_05, right_tab_04, right_tab_03, right_tab_02, 
                             right_tab_01,right_tab_00)

        self.play(TransformFromCopy(row_zero_group, right_zero_group), run_time=2)
        self.play(FadeOut(right_tab_00))

        # -----------row 1 -------------------


        right_tab_10 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>0</b></span>')
        right_tab_10.shift(1.95 * DOWN + 0.8 * RIGHT)

        right_tab_11 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>101</b></span>')
        right_tab_11.next_to(right_tab_10, buff=0)

        right_tab_12 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>ANUJ</b></span>')
        right_tab_12.next_to(right_tab_11, buff=0)

        right_tab_13 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>COMMERCE</b></span>')
        right_tab_13.next_to(right_tab_12, buff=0)

        right_tab_14 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>200</b></span>')
        right_tab_14.next_to(right_tab_13, buff=0)

        right_tab_15 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>23</b></span>')
        right_tab_15.next_to(right_tab_14, buff=0)

        right_tab_16 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BASKETBALL</b></span>')
        right_tab_16.next_to(right_tab_15, buff=0)

        right_one_group = VGroup()
        right_one_group.add(right_tab_16, right_tab_15, right_tab_14, right_tab_13, 
                            right_tab_12, right_tab_11,right_tab_10)

        self.play(TransformFromCopy(row_one_group, right_one_group), run_time=2)

        # ---------- row 2 ---------------------

        right_tab_20 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>1</b></span>')
        right_tab_20.shift(2.3 * DOWN + 0.8 * RIGHT)

        right_tab_21 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>102</b></span>')
        right_tab_21.next_to(right_tab_20, buff=0)

        right_tab_22 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>BALE</b></span>')
        right_tab_22.next_to(right_tab_21, buff=0)

        right_tab_23 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>SCIENCE</b></span>')
        right_tab_23.next_to(right_tab_22, buff=0)

        right_tab_24 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>150</b></span>')
        right_tab_24.next_to(right_tab_23, buff=0)

        right_tab_25 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>21</b></span>')
        right_tab_25.next_to(right_tab_24, buff=0)

        right_tab_26 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>CHESS</b></span>')
        right_tab_26.next_to(right_tab_25, buff=0)

        right_two_group = VGroup()
        right_two_group.add(right_tab_26, right_tab_25, right_tab_24, right_tab_23, right_tab_22, 
                            right_tab_21,right_tab_20)

        self.play(TransformFromCopy(row_two_group, right_two_group), run_time=2)

        #   -------- row 4 ---------------
        right_tab_30 = dataframe_rectange_s(width_s,height_s,r'<span font_family="monospace"><b>2</b></span>')
        right_tab_30.shift(2.65 * DOWN + 0.8 * RIGHT)
        # right_tab_30.set_stroke(color=GOLD_C, opacity=0)

        right_tab_31 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>103</b></span>')
        right_tab_31.next_to(right_tab_30, buff=0)

        right_tab_32 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>GEORGE</b></span>')
        right_tab_32.next_to(right_tab_31, buff=0)

        right_tab_33 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>HUMANITIES</b></span>')
        right_tab_33.next_to(right_tab_32, buff=0)

        right_tab_34 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>400</b></span>')
        right_tab_34.next_to(right_tab_33, buff=0)

        right_tab_35 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>22</b></span>')
        right_tab_35.next_to(right_tab_34, buff=0)

        right_tab_36 = dataframe_rectange_s(width_s, height_s, r'<span font_family="monospace"><b>PAINTING</b></span>')
        right_tab_36.next_to(right_tab_35, buff=0)

        right_three_group = VGroup()
        right_three_group.add(right_tab_36, right_tab_35, right_tab_34, right_tab_33, 
                              right_tab_32, right_tab_31,right_tab_30)

        self.play(TransformFromCopy(row_three_group, right_three_group), run_time=2)

        self.wait(4)
        self.wait(5)

        self.play(FadeOut(box_disapper_text1), FadeOut(highlight_row))

        box_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace">student_df.index = student_df["NAME"]</span>',
                      0.45, WHITE, 3.1 * UP + 5.6 * LEFT)
        box_disapper_text1.next_to(red_arrow_fixed1)
        self.play(Write(box_disapper_text1))
        self.wait(5)

        table_101 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>ANUJ</b></span>')
        table_101.shift(2.05 * UP + 5.3 * LEFT)

        self.play(Transform(table_10, table_101), run_time=0.5)

        # ---------- row 2 ---------------------

        table_202 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>BALE</b></span>')
        table_202.shift(1.7 * UP + 5.3 * LEFT)

        self.play(Transform(table_20, table_202), run_time=0.5)
        

        #   -------- row 4 ---------------
        table_303 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>GEORGE</b></span>')
        table_303.shift(1.35 * UP + 5.3 * LEFT)

        self.play(Transform(table_30, table_303), run_time=0.5)
        

        # ------------- ROW 5  ------------------

        table_404 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>JIBIN</b></span>')
        table_404.shift(1 * UP + 5.3 * LEFT)

        self.play(Transform(table_40, table_404), run_time=0.5)
        

        # --------------ROW 6 ---------------

        table_505 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>JOHN</b></span>')
        table_505.shift(0.65 * UP + 5.3 * LEFT)

        self.play(Transform(table_50, table_505), run_time=0.5)

        #  --------------- ROW 7---------------

        table_606 = dataframe_rectange(width_r,height_r,r'<span font_family="monospace"><b>SOMAN</b></span>')
        table_606.shift(0.3 * UP + 5.3 * LEFT)
        self.play(Transform(table_60, table_606), run_time=0.5)

        self.wait(1)
        self.wait(5)
        self.play(FadeOut(box_disapper_text1))

        box_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"> student_df</span>',
                      0.45, WHITE, 3.1 * UP + 5.6 * LEFT)
        box_disapper_text1.next_to(red_arrow_fixed1)
        self.play(Write(box_disapper_text1))
        self.wait(5)

        if_else_code = """0\n1\n2\n3\n4\n5"""
        
        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{if_else_code}</b></span>',
                      0.45, GREY_A, 1.2 * UP + 6.5 * LEFT)
        self.play(Write(code_text1), run_time=0.5)
        

        
        self.wait(5)
