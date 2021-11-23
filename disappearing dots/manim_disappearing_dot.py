from manim import *
from colour import Color


class DotsDissapear(Scene):
    def construct(self):

        def dataframe_swap_scale_opacity(x, y, color_name, opacity_is):
            rect = Rectangle(
                width=x,
                height=y,
            )
            rect.set_stroke(color=YELLOW_D)
            rect.set_fill(color=color_name, opacity=opacity_is)
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

        color_name = BLUE_E


        line1 = Line(0.2 * DOWN + ORIGIN, 0.2 * UP + ORIGIN, color=color_name)
        line2 = Line(ORIGIN + 0.2 * LEFT, ORIGIN + 0.2 * RIGHT, color=color_name)
        line_g1 = VGroup(line1,line2)
        # self.play(Create(line_g1))


        line3 = Line(0.4 * UP + ORIGIN, 0.8 * UP + ORIGIN, color=color_name)
        line4 = Line(0.6 * UP + 0.2 * LEFT, 0.6 * UP + 0.2 * RIGHT, color=color_name)
        line_g2 = VGroup(line3,line4)
        # self.play(Create(line_g2))


        line5 = Line(0.4 * DOWN + ORIGIN, 0.8 * DOWN + ORIGIN, color=color_name)
        line6 = Line(0.6 * DOWN + 0.2 * LEFT, 0.6 * DOWN + 0.2 * RIGHT, color=color_name)
        line_g3 = VGroup(line5, line6)
        # self.play(Create(line_g3))


        line7 = Line( 0.2 * DOWN + 0.6 * LEFT, 0.2 * UP + 0.6 * LEFT, color=color_name)
        line8 = Line(ORIGIN + 0.4 * LEFT, ORIGIN + 0.8 * LEFT, color=color_name)
        line_g4 = VGroup(line7, line8)
        # self.play(Create(line_g4))


        line9 = Line(0.2 * DOWN + 0.6 * RIGHT, 0.2 * UP + 0.6 * RIGHT, color=color_name)
        line10 = Line(ORIGIN + 0.4 * RIGHT, ORIGIN + 0.8 * RIGHT, color=color_name)
        line_g5 = VGroup(line9, line10)
        # self.play(Create(line_g5))



        #   next set of tempatetion

        line11 = Line(1 * UP + ORIGIN, 1.4 * UP + ORIGIN, color=color_name)
        line12 = Line(1.2 * UP + 0.2 * LEFT, 1.2 * UP + 0.2 * RIGHT, color=color_name)
        line_g6 = VGroup(line11,line12)
        # self.play(Create(line_g6))


        line13 = Line(1 * DOWN + ORIGIN, 1.4 * DOWN + ORIGIN, color=color_name)
        line14 = Line(1.2 * DOWN + 0.2 * LEFT, 1.2 * DOWN + 0.2 * RIGHT, color=color_name)
        line_g7 = VGroup(line13, line14)
        # self.play(Create(line_g3))


        line15 = Line( 0.2 * DOWN + 1.2 * LEFT, 0.2 * UP + 1.2 * LEFT, color=color_name)
        line16 = Line(ORIGIN + 1 * LEFT, ORIGIN + 1.4 * LEFT, color=color_name)
        line_g8 = VGroup(line15, line16)
        # self.play(Create(line_g4))


        line17 = Line(0.2 * DOWN + 1.2 * RIGHT, 0.2 * UP + 1.2* RIGHT, color=color_name)
        line18 = Line(ORIGIN + 1 * RIGHT, ORIGIN + 1.4 * RIGHT, color=color_name)
        line_g9 = VGroup(line17, line18)
        # self.play(Create(line_g5))

        # third line of cross--------------------------------------------------------------

        line19 = Line(1.6 * UP + ORIGIN, 2 * UP + ORIGIN, color=color_name)
        line20 = Line(1.8 * UP + 0.2 * LEFT, 1.8 * UP + 0.2 * RIGHT, color=color_name)
        line_g10 = VGroup(line19,line20)
        # self.play(Create(line_g6))


        line21 = Line(1.6 * DOWN + ORIGIN, 2 * DOWN + ORIGIN, color=color_name)
        line22 = Line(1.8 * DOWN + 0.2 * LEFT, 1.8 * DOWN + 0.2 * RIGHT, color=color_name)
        line_g11 = VGroup(line21, line22)
        # self.play(Create(line_g3))


        line23 = Line( 0.2 * DOWN + 1.8 * LEFT, 0.2 * UP + 1.8 * LEFT, color=color_name)
        line24 = Line(ORIGIN + 1.6 * LEFT, ORIGIN + 2 * LEFT, color=color_name)
        line_g12 = VGroup(line23, line24)
        # self.play(Create(line_g4))


        line25 = Line(0.2 * DOWN + 1.8 * RIGHT, 0.2 * UP + 1.8* RIGHT, color=color_name)
        line26 = Line(ORIGIN + 1.6 * RIGHT, ORIGIN + 2 * RIGHT, color=color_name)
        line_g13 = VGroup(line25, line26)
        # self.play(Create(line_g5))

        # -------------- next set of cross ing -------------------------------

        line27 = Line(0.4 * UP + 0.6 * RIGHT, 0.8 * UP + 0.6 * RIGHT, color=color_name)
        line28 = Line(0.6 * UP + 0.4 * RIGHT, 0.6 * UP + 0.8 * RIGHT, color=color_name)
        line_g14 = VGroup(line27,line28)
        # self.play(Create(line_g2))


        line29 = Line(0.4 * DOWN + 0.6 * RIGHT, 0.8 * DOWN + 0.6 * RIGHT, color=color_name)
        line30 = Line(0.6 * DOWN + 0.4 * RIGHT, 0.6 * DOWN + 0.8 * RIGHT, color=color_name)
        line_g15 = VGroup(line29, line30)
        # self.play(Create(line_g3))

        line31 = Line(0.4 * UP + 0.6 * LEFT, 0.8 * UP + 0.6 * LEFT, color=color_name)
        line32 = Line(0.6 * UP + 0.4 * LEFT, 0.6 * UP + 0.8 * LEFT, color=color_name)
        line_g16 = VGroup(line31,line32)
        # self.play(Create(line_g2))


        line33 = Line(0.4 * DOWN + 0.6 * LEFT, 0.8 * DOWN + 0.6 * LEFT, color=color_name)
        line34 = Line(0.6 * DOWN + 0.4 * LEFT, 0.6 * DOWN + 0.8 * LEFT, color=color_name)
        line_g17 = VGroup(line33, line34)
        # self.play(Create(line_g3))

        #  --- left 2nd group line --------------
        line35 = Line(0.4 * UP + 1.2 * RIGHT, 0.8 * UP + 1.2 * RIGHT, color=color_name)
        line36 = Line(0.6 * UP + 1 * RIGHT, 0.6 * UP + 1.4 * RIGHT, color=color_name)
        line_g18 = VGroup(line35, line36)

        line37 = Line(0.4 * UP + 1.8 * RIGHT, 0.8 * UP + 1.8 * RIGHT, color=color_name)
        line38 = Line(0.6 * UP + 1.6 * RIGHT, 0.6 * UP + 2 * RIGHT, color=color_name)
        line_g19 = VGroup(line37, line38)

        line39 = Line(0.4 * UP + 1.2 * LEFT, 0.8 * UP + 1.2 * LEFT, color=color_name)
        line40 = Line(0.6 * UP + 1 * LEFT, 0.6 * UP + 1.4 * LEFT, color=color_name)
        line_g20 = VGroup(line39, line40)

        line41 = Line(0.4 * UP + 1.8 * LEFT, 0.8 * UP + 1.8 * LEFT, color=color_name)
        line42 = Line(0.6 * UP + 1.6 * LEFT, 0.6 * UP + 2 * LEFT, color=color_name)
        line_g21 = VGroup(line41, line42)

        #  down town lets see the result ---------------------------------

        line43 = Line(0.4 * DOWN + 1.2 * RIGHT, 0.8 * DOWN + 1.2 * RIGHT, color=color_name)
        line44 = Line(0.6 * DOWN + 1 * RIGHT, 0.6 * DOWN + 1.4 * RIGHT, color=color_name)
        line_g22 = VGroup(line43, line44)

        line45 = Line(0.4 * DOWN + 1.8 * RIGHT, 0.8 * DOWN + 1.8 * RIGHT, color=color_name)
        line46 = Line(0.6 * DOWN + 1.6 * RIGHT, 0.6 * DOWN + 2 * RIGHT, color=color_name)
        line_g23 = VGroup(line45, line46)

        line47 = Line(0.4 * DOWN + 1.2 * LEFT, 0.8 * DOWN + 1.2 * LEFT, color=color_name)
        line48 = Line(0.6 * DOWN + 1 * LEFT, 0.6 * DOWN + 1.4 * LEFT, color=color_name)
        line_g24 = VGroup(line47, line48)

        line49 = Line(0.4 * DOWN + 1.8 * LEFT, 0.8 * DOWN + 1.8 * LEFT, color=color_name)
        line50 = Line(0.6 * DOWN + 1.6 * LEFT, 0.6 * DOWN + 2 * LEFT, color=color_name)
        line_g25 = VGroup(line49, line50)


        # ------------ 3rd left to up to down to right ----------------------------------------------

        line51 = Line(1 * UP + 1.2 * RIGHT, 1.4 * UP + 1.2 * RIGHT, color=color_name)
        line52 = Line(1.2 * UP + 1 * RIGHT, 1.2 * UP + 1.4 * RIGHT, color=color_name)
        line_g26 = VGroup(line51, line52)

        line53 = Line(1 * UP + 1.8 * RIGHT, 1.4 * UP + 1.8 * RIGHT, color=color_name)
        line54 = Line(1.2 * UP + 1.6 * RIGHT, 1.2 * UP + 2 * RIGHT, color=color_name)
        line_g27 = VGroup(line53, line54)

        line55 = Line(1 * UP + 1.2 * LEFT, 1.4 * UP + 1.2 * LEFT, color=color_name)
        line56 = Line(1.2 * UP + 1 * LEFT, 1.2 * UP + 1.4 * LEFT, color=color_name)
        line_g28 = VGroup(line55, line56)

        line57 = Line(1 * UP + 1.8 * LEFT, 1.4 * UP + 1.8 * LEFT, color=color_name)
        line58 = Line(1.2 * UP + 1.6 * LEFT, 1.2 * UP + 2 * LEFT, color=color_name)
        line_g29 = VGroup(line57, line58)

        #  down town lets see the result ---------------------------------

        line59 = Line(1 * DOWN + 1.2 * RIGHT, 1.4 * DOWN + 1.2 * RIGHT, color=color_name)
        line60 = Line(1.2 * DOWN + 1 * RIGHT, 1.2 * DOWN + 1.4 * RIGHT, color=color_name)
        line_g30 = VGroup(line59, line60)

        line61 = Line(1 * DOWN + 1.8 * RIGHT, 1.4 * DOWN + 1.8 * RIGHT, color=color_name)
        line62 = Line(1.2 * DOWN + 1.6 * RIGHT, 1.2 * DOWN + 2 * RIGHT, color=color_name)
        line_g31 = VGroup(line61, line62)

        line63 = Line(1 * DOWN + 1.2 * LEFT, 1.4 * DOWN + 1.2 * LEFT, color=color_name)
        line64 = Line(1.2 * DOWN + 1 * LEFT, 1.2 * DOWN + 1.4 * LEFT, color=color_name)
        line_g32 = VGroup(line63, line64)

        line65 = Line(1 * DOWN + 1.8 * LEFT, 1.4 * DOWN + 1.8 * LEFT, color=color_name)
        line66 = Line(1.2 * DOWN + 1.6 * LEFT, 1.2 * DOWN + 2 * LEFT, color=color_name)
        line_g33 = VGroup(line65, line66)

        # ---------------- 4th updown left right --------------------------

        line67 = Line(1.6 * UP + 1.2 * RIGHT, 2 * UP + 1.2 * RIGHT, color=color_name)
        line68 = Line(1.8 * UP + 1 * RIGHT, 1.8 * UP + 1.4 * RIGHT, color=color_name)
        line_g34 = VGroup(line67, line68)

        line69 = Line(1.6 * UP + 1.8 * RIGHT, 2 * UP + 1.8 * RIGHT, color=color_name)
        line70 = Line(1.8 * UP + 1.6 * RIGHT, 1.8 * UP + 2 * RIGHT, color=color_name)
        line_g35 = VGroup(line69, line70)

        line71 = Line(1.6 * UP + 1.2 * LEFT, 2 * UP + 1.2 * LEFT, color=color_name)
        line72 = Line(1.8 * UP + 1 * LEFT, 1.8 * UP + 1.4 * LEFT, color=color_name)
        line_g36 = VGroup(line71, line72)

        line73 = Line(1.6 * UP + 1.8 * LEFT, 2 * UP + 1.8 * LEFT, color=color_name)
        line74 = Line(1.8 * UP + 1.6 * LEFT, 1.8 * UP + 2 * LEFT, color=color_name)
        line_g37 = VGroup(line73, line74)

        #  down town lets see the result ---------------------------------

        line75 = Line(1.6 * DOWN + 1.2 * RIGHT, 2 * DOWN + 1.2 * RIGHT, color=color_name)
        line76 = Line(1.8 * DOWN + 1 * RIGHT, 1.8 * DOWN + 1.4 * RIGHT, color=color_name)
        line_g38 = VGroup(line75, line76)

        line77 = Line(1.6 * DOWN + 1.8 * RIGHT, 2 * DOWN + 1.8 * RIGHT, color=color_name)
        line78 = Line(1.8 * DOWN + 1.6 * RIGHT, 1.8 * DOWN + 2 * RIGHT, color=color_name)
        line_g39 = VGroup(line77, line78)

        line79 = Line(1.6 * DOWN + 1.2 * LEFT, 2 * DOWN + 1.2 * LEFT, color=color_name)
        line80 = Line(1.8 * DOWN + 1 * LEFT, 1.8 * DOWN + 1.4 * LEFT, color=color_name)
        line_g40 = VGroup(line79, line80)

        line81 = Line(1.6 * DOWN + 1.8 * LEFT, 2 * DOWN + 1.8 * LEFT, color=color_name)
        line82 = Line(1.8 * DOWN + 1.6 * LEFT, 1.8 * DOWN + 2 * LEFT, color=color_name)
        line_g41 = VGroup(line81, line82)


        # -----------------last defence system -----------------------------------------

        line83 = Line(1 * UP + 0.6 * RIGHT, 1.4 * UP + 0.6 * RIGHT, color=color_name)
        line84 = Line(1.2 * UP + 0.4 * RIGHT, 1.2 * UP + 0.8 * RIGHT, color=color_name)
        line_g42 = VGroup(line83,line84)
        # self.play(Create(line_g2))


        line85 = Line(1 * DOWN + 0.6 * RIGHT, 1.4 * DOWN + 0.6 * RIGHT, color=color_name)
        line86 = Line(1.2 * DOWN + 0.4 * RIGHT, 1.2 * DOWN + 0.8 * RIGHT, color=color_name)
        line_g43 = VGroup(line85, line86)
        # self.play(Create(line_g3))

        line87 = Line(1 * UP + 0.6 * LEFT, 1.4 * UP + 0.6 * LEFT, color=color_name)
        line88 = Line(1.2 * UP + 0.4 * LEFT, 1.2 * UP + 0.8 * LEFT, color=color_name)
        line_g44 = VGroup(line87,line88)
        # self.play(Create(line_g2))


        line89 = Line(1 * DOWN + 0.6 * LEFT, 1.4 * DOWN + 0.6 * LEFT, color=color_name)
        line90 = Line(1.2 * DOWN + 0.4 * LEFT, 1.2 * DOWN + 0.8 * LEFT, color=color_name)
        line_g45 = VGroup(line89, line90)
        # self.play(Create(line_g3))


        #  -- ehat is this

        line91 = Line(1.6 * UP + 0.6 * RIGHT, 2 * UP + 0.6 * RIGHT, color=color_name)
        line92 = Line(1.8 * UP + 0.4 * RIGHT, 1.8 * UP + 0.8 * RIGHT, color=color_name)
        line_g46 = VGroup(line91,line92)
        # self.play(Create(line_g2))


        line93 = Line(1.6 * DOWN + 0.6 * RIGHT, 2 * DOWN + 0.6 * RIGHT, color=color_name)
        line94 = Line(1.8 * DOWN + 0.4 * RIGHT, 1.8 * DOWN + 0.8 * RIGHT, color=color_name)
        line_g47 = VGroup(line93, line94)
        # self.play(Create(line_g3))

        line95 = Line(1.6 * UP + 0.6 * LEFT, 2 * UP + 0.6 * LEFT, color=color_name)
        line96 = Line(1.8 * UP + 0.4 * LEFT, 1.8 * UP + 0.8 * LEFT, color=color_name)
        line_g48 = VGroup(line95,line96)
        # self.play(Create(line_g2))


        line97 = Line(1.6 * DOWN + 0.6 * LEFT, 2 * DOWN + 0.6 * LEFT, color=color_name)
        line98 = Line(1.8 * DOWN + 0.4 * LEFT, 1.8 * DOWN + 0.8 * LEFT, color=color_name)
        line_g49 = VGroup(line97, line98)
        # self.play(Create(line_g3))



        self.play(Create(line_g1), Create(line_g2), Create(line_g3), Create(line_g4), Create(line_g5), Create(line_g6),
                  Create(line_g7),Create(line_g8),Create(line_g9), Create(line_g10), Create(line_g11),Create(line_g12),Create(line_g13),
                  Create(line_g14),Create(line_g15),Create(line_g16),Create(line_g17),Create(line_g18),Create(line_g19),Create(line_g20),
                  Create(line_g21), Create(line_g22), Create(line_g23), Create(line_g24),Create(line_g25),Create(line_g26),Create(line_g27)
                  ,Create(line_g28),Create(line_g29),Create(line_g30),Create(line_g31),Create(line_g32),Create(line_g33),Create(line_g34)
                  ,Create(line_g35),Create(line_g36),Create(line_g37),Create(line_g38),Create(line_g39),Create(line_g40),Create(line_g41)
                  ,Create(line_g42),Create(line_g43),Create(line_g44),Create(line_g45),Create(line_g46),Create(line_g47),Create(line_g48)
                  ,Create(line_g49))

        dot1 = Dot(color=YELLOW).scale(0.5)
        dot2 = Dot(1.1 * UP + 1.1 * LEFT, color=YELLOW).scale(0.5)
        dot3 = Dot(1.1 * UP + 1.1 * RIGHT, color=YELLOW).scale(0.5)
        dot4 = Dot(1.1 * DOWN + ORIGIN, color=YELLOW).scale(0.5)

        self.play(Create(dot1), Create(dot2), Create(dot3), Create(dot4))


        object_box = dataframe_swap_scale(10, 0.8, DARKER_GRAY)
        object_box.shift(3.6* UP + 0.01 * LEFT)
        self.play(Create(object_box))
        object_frame_text = """While fixating on the flashing dot, the stationary dots may disappear due to the brain prioritizing motion information."""       
        object_frame_text_style = MarkupText(f'<span font_family="monospace"><b>{object_frame_text}</b></span>').scale(0.3)
        object_frame_text_style.shift(3.6 * UP + 0.01 * LEFT)
        self.play(Write(object_frame_text_style), run_time=2)



        angle_rotation = 30
        running_time = 1


        for i in range(60): # time of rotation 30 * 0.7(running_time) = 21 seconds    
            # self.play(FadeOut(dot1), run_time=0.5)
            if i%2 ==0 :
                dot_dis = FadeOut(dot1, run_time=0.5)
            else:
                dot_dis = FadeIn(dot1, run_time=0.5)        
            self.play(dot_dis,
                Rotating(line_g1, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g2, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g3, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g4, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g5, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g6, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g7, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g8, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g9, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g10, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g11, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g12, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g13, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g14, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g15, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g16, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g17, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g18, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g19, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g20, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g21, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g22, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g23, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g24, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g25, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g26, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g27, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g28, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g29, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g30, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g31, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g32, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g33, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g34, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g35, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g36, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g37, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g38, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g39, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g40, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g41, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g42, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g43, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g44, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g45, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g46, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g47, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g48, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                      Rotating(line_g49, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                    #   Rotating(line_g50, radians=angle_rotation*DEGREES,about_point = line_g1.get_center(),run_time=running_time, rate_func=linear),
                    )

        
