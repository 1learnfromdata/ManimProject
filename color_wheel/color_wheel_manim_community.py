from manim import *
from colour import Color


class MySector(Sector):
    """ Circular sector shape with a custom interpolation method. """

    def interpolate(self, mobject1, mobject2, alpha, path_func=straight_path):
        if not (isinstance(mobject1, MySector) and isinstance(mobject2, MySector)):
            return super().interpolate(mobject1, mobject2, alpha, path_func=path_func)

        for attr in (
            'start_angle', 'angle',
            'inner_radius', 'outer_radius',
        ):
            v1 = getattr(mobject1, attr)
            v2 = getattr(mobject2, attr)
            setattr(self, attr, path_func(v1, v2, alpha))

        self.arc_center = path_func(
            mobject1.get_arc_center(),
            mobject2.get_arc_center(),
            alpha
        )
        self.interpolate_color(mobject1, mobject2, alpha)
        self.clear_points()
        self.generate_points()
        return self


class TestSceneCircle(MovingCameraScene, Scene):

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        color_palette = [BLACK,BLUE_A,BLUE_B,BLUE_C,BLUE_D,BLUE_E,DARK_BLUE,DARK_BROWN,DARK_GREY,DARKER_GREY,GOLD_A,GOLD_B,
                         GOLD_C,GOLD_D,GOLD_E,GRAY,GREEN_A,GREEN_B,GREEN_C,GREEN_D,GREEN_E,GREEN_SCREEN,GREY_A,GREY_BROWN,
                         LIGHT_BROWN,LIGHT_GRAY,LIGHT_PINK,MAROON_A,MAROON_B,MAROON_C,MAROON_D,MAROON_E,ORANGE,PINK,PURPLE_A,
                         PURPLE_B,PURPLE_C,PURPLE_D,PURPLE_E,RED_A,RED_B,RED_C,RED_D,RED_E,TEAL_A,TEAL_B,TEAL_C,TEAL_D,TEAL_E,
                         WHITE,YELLOW_A,YELLOW_B,YELLOW_C,YELLOW_D,YELLOW_E]
        color_palette_str = ["BLACK","BLUE_A","BLUE_B","BLUE_C","BLUE_D","BLUE_E","DARK_BLUE","DARK_BROWN","DARK_GREY","DARKER_GREY","GOLD_A","GOLD_B",
 "GOLD_C","GOLD_D","GOLD_E","GRAY","GREEN_A","GREEN_B","GREEN_C","GREEN_D","GREEN_E","GREEN_SCREEN","GREY_A","GREY_BROWN",
 "LIGHT_BROWN","LIGHT_GRAY","LIGHT_PINK","MAROON_A","MAROON_B","MAROON_C","MAROON_D","MAROON_E","ORANGE","PINK","PURPLE_A",
 "PURPLE_B","PURPLE_C","PURPLE_D","PURPLE_E","RED_A","RED_B","RED_C","RED_D","RED_E","TEAL_A","TEAL_B","TEAL_C","TEAL_D",
 "TEAL_E","WHITE","YELLOW_A","YELLOW_B","YELLOW_C","YELLOW_D","YELLOW_E"]
 
 
        weights = np.array([1.0] * 55)
        weights /= weights.sum()

        angles = weights * TAU
        angles_offset = np.cumsum((0, *angles[:-1]))

        sectors2 = [
            MySector(start_angle=ao, angle=a,
                stroke_width=0,
                stroke_color=WHITE,
                fill_color=color_palette[i % len(color_palette)], fill_opacity=1)
            for i, (ao, a) in enumerate(zip(angles_offset, angles))
        ]

        def HSL(hue,saturation=1,lightness=0.5):
            return Color(hsl=(hue,saturation,lightness))

        def get_hsl_set_colors(color_range=360,saturation=1,lightness=0.5):
            return [*[HSL(i/360,saturation,lightness) for i in range(color_range)]]

        self.play(
            *(ShowCreation(a1, run_time=1) for a1 in sectors2)
        )


        circle_1 = Circle(radius=0.2, color=DARK_GRAY, fill_opacity=1)
        self.add(circle_1)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.3).move_to(sectors2[1]))
        arrow_1 = Arrow(1.5*RIGHT, 1 * RIGHT, buff=0)
        arrow_1.shift(0.03 * UP)
        self.play(Write(arrow_1))

        code_text = Text(r"Manim Color Code").scale(0.2)
        code_text.set_color(color=get_hsl_set_colors(color_range=360))
        code_text.shift(0.2 * UP + 2 * RIGHT)
        self.play(Write(code_text))




        for i in range(55):
            color_name = color_palette_str[i]
            temp_text = Text(f'{color_name}',).scale(0.2)
            if i == 0:
                temp_text.set_color(color=WHITE)
            else:
                temp_text.set_color(color=color_palette[i])
            # temp_text.set_color(color=color_palette[i])
            temp_text.next_to(arrow_1,buff=0.02)
            circle_1.set_color(color=color_palette[i])
            
            self.add(circle_1)


            self.play(
                FadeOut(temp_text,run_time=0.3),
                Rotating(sectors2[0], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[1], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[2], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[3], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[4], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[5], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[6], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[7], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[8], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[9], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[10], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[11], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[12], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[13], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[14], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[15], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[16], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[17], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[18], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[19], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[20], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[21], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[22], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[23], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[24], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[25], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[26], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[27], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[28], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[29], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[30], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[31], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[32], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[33], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[34], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[35], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[36], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[37], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[38], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[39], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[40], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[41], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[42], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[43], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[44], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[45], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[46], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[47], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[48], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[49], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[50], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[51], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[52], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[53], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Rotating(sectors2[54], radians=-6.5*DEGREES,about_point = circle_1.get_center(),run_time=2, rate_func=linear),
Write(temp_text,run_time=0.5)

)

        self.wait(4)
