from manim import *


class SentimentAnalysisSingle(GraphScene,Scene):
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
            self.play(Write(index_text))
            return index_text

        def currentTextPositionMarkupWithout(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            return index_text


        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Positive Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        create_rectange(13.9, 0.6, 3.1 * UP + 0.1 * LEFT, BLACK)
        box_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace">str1 = "Even the most beautiful days eventually have their sunsets."</span>',
                      0.45, WHITE, 3.1 * UP + 0.6 * LEFT)


        create_rectange(7.1, 0.8, 2.3 * UP + 3.5 * LEFT, DARK_GRAY)
        transformer_code_fixed = """>>> transformer_sentiment( str1 )"""

        transformer_code_text_fixed = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_fixed}</b></span>',
                      0.3, GREY_A, 2.5 * UP + 5 * LEFT)
        transformer_code_text_fixed[0:3].set_color(RED_D)

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'POSITIVE', 'score': 0.9987558126449585}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)


        self.play(Write(transformer_code_text_fixed), Write(transformer_output_text))


        create_rectange(7.1, 0.8, 1.4 * UP + 3.5 * LEFT, DARK_GRAY)
        flair_code_fixed = """>>> flair_sentiment( str1 )"""

        flair_code_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_code_fixed}</b></span>',
                      0.32, GREY_A, 1.6 * UP + 5.3 * LEFT)
        flair_code_text[0:3].set_color(RED_D)


        flair_output = """Sentiment of above sentence is: [POSITIVE (0.999)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play(Write(flair_code_text), Write(flair_output_text))


        create_rectange(7.1, 0.8, 0.5 * UP + 3.5 * LEFT, DARK_GRAY)
        textblob_code_fixed = """>>> textblob_sentiment( str1 )"""

        textblob_code_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_code_fixed}</b></span>',
                      0.32, GREY_A, 0.75 * UP + 5.08  * LEFT)
        textblob_code_text[0:3].set_color(RED_D)

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=0.675, subjectivity=0.75)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 3.9 * LEFT)
        self.play(Write(textblob_code_text), Write(textblob_output_text))


        create_rectange(7.1, 0.8, 0.4 * DOWN + 3.5 * LEFT, DARK_GRAY)
        vader_code_fixed = """>>> vader_sentiment( str1 )"""

        vadar_code_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_code_fixed}</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 5.5 * LEFT)
        vadar_code_text[0:3].set_color(RED_D)


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.0, 'neu': 0.6, 'pos': 0.3, 'compound': 0.63}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.75 * LEFT)
        self.play(Write(vadar_code_text), Write(vadar_output_text))



        thinking_letter = SVGMobject("/home/manmohan/python_projects/manim_projects/regex_visual/last_thinking_cloud")
        thinking_letter.set_height(1)
        thinking_letter.set_width(5.4)
        thinking_letter.set_color(GREEN)
        thinking_letter.shift(0.8 * UP + 3 * RIGHT)

        owl_image = ImageMobject("/home/manmohan/python_projects/manim_projects/regex_visual/new_owl.png")
        owl_image.set_height(1)
        owl_image.shift(0.9 * DOWN + 5.5 * RIGHT)

        self.play(FadeIn(thinking_letter), FadeIn(owl_image))

        cloud_text1 = """Transformer and flair have high \nconfidence scores.They are best suited to \ndetect positive sentiment sentences."""


        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 1.93 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1), run_time=3)

        sentiment_time_bar_p = BarChart([1.5,1.2,41.82,59.29],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_p.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(ShowCreation(sentiment_time_bar_p),run_time=2)

        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>59.29</b></span>',
                      0.3, GREY_A, 1.35 * DOWN + 5.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>41.82</b></span>',
                      0.3, GREY_A, 2 * DOWN + 4.3 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.2</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.5</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))


        y_axis_label_name = currentTextPositionMarkup(r'<span font_family="monospace"><b>Time(milliseconds)</b></span>',
                      0.3, BLUE_D, 0.9 * DOWN + 1.1 * RIGHT)

        cloud_text3 = """Execution Speed of 4 models are in order \n     TB > VADER > Flair > TF"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.6 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))

        # ---------- graph of positive sentences ------------

        data = [0.64,  0.68,  0.99,  0.99]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], 0.64))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>0.64(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], 0.68))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>0.68(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.99))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.99))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis, self.x_axis_labels)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        cloud_text2 = """Accuracy score of 4 models are in order :\n   Flair = TF > TB > VADER"""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.2 * UP + 2.95 * RIGHT)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]))
        self.play(ShowCreation(dot_collection[1]), Write(cloud_disapper_text2), run_time = 3)
        self.play(ShowCreation(dot_collection[2]))

        cloud_text4 = """Transformer and Flair have high \nexecution time hence, they are not \nsuitable for projects with speed-sensitive."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 0.19 * DOWN + 3 * RIGHT)


        self.play(ShowCreation(dot_collection[3]), Write(cloud_disapper_text4), run_time=4)


        #  ------------------ negative sentence -----------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(transformer_output_text), 
                  FadeOut(flair_output_text), FadeOut(textblob_output_text), FadeOut(vadar_output_text))

        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text4),
                  FadeOut(cloud_disapper_text1))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Negative Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        box_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace">str2 = "She hates playing tennis with her classmates."</span>',
                      0.45, WHITE, 3.1 * UP + 0.6 * LEFT)
        self.play(Transform(box_disapper_text, box_disapper_text1))

        transformer_str_replace2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str2</b></span>',
                      0.3, GREY_A, 2.5 * UP + 3.47 * LEFT)
        self.play(Transform(transformer_code_text_fixed[25:29], transformer_str_replace2))

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'NEGATIVE', 'score': 0.9989798126449585}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)


        self.play( Write(transformer_output_text))


        flair_str_replace2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str2</b></span>',
                      0.32, GREY_A, 1.6 * UP + 4.05 * LEFT)
        self.play(Transform(flair_code_text[19:23], flair_str_replace2))


        flair_output = """Sentiment of above sentence is: [NEGATIVE (0.998)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play( Write(flair_output_text))


        textblob_str_replace2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str2</b></span>',
                      0.32, GREY_A, 0.75 * UP + 3.67 * LEFT)
        self.play(Transform(textblob_code_text[22:26], textblob_str_replace2))

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=-0.799, subjectivity=1.0)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 3.9 * LEFT)
        self.play(Write(textblob_output_text))


        vadar_str_replace2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str2</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 4.45 * LEFT)
        self.play(Transform(vadar_code_text[19:23], vadar_str_replace2))


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.5, 'neu': 0.4, 'pos': 0.1, 'compound': -0.67}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.69 * LEFT)
        self.play( Write(vadar_output_text))

        cloud_text1 = """Confidence score level - \nFlair = TF > TB > VADER"""


        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 1.93 * UP + 2.6 * RIGHT)
        self.play(Write(cloud_disapper_text1), run_time=2)


        cloud_text2 = """Transformer and flair do not have \nnegative value to represent negative \nsentiment sentences."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.2 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)


        sentiment_time_bar_n = BarChart([1.2,1.019,31.52,34.97],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_n.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(Transform(sentiment_time_bar_p, sentiment_time_bar_n),run_time=2)

        self.play(FadeOut(bar_disapper_text1) ,FadeOut(bar_disapper_text2), 
                  FadeOut(bar_disapper_text3),FadeOut(bar_disapper_text4), FadeOut(dot_collection),)

        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>34.97</b></span>',
                      0.3, GREY_A, 2.2 * DOWN + 5.46 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>31.52</b></span>',
                      0.3, GREY_A, 2.35 * DOWN + 4.3 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.02</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.2</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))

        cloud_text3 = """Text "He is my enemy" is a negative \nsentiment text. But, only Transformer \nand VADER predict it as negative sentiment \ntext. TextBlob and flair predict it as \nneutral and positive text."""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.01 * UP + 3.05 * RIGHT)
        self.play(Write(cloud_disapper_text3), run_time=5)

        data = [-0.67,  -0.79,  0.99,  0.99]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], -0.67))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>-0.67(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], -0.79))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>-0.79(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.99))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.99(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.99))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.99(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis, self.x_axis_labels)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        self.play(FadeOut(cloud_disapper_text1), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text3))

        cloud_text4 = """For negative sentiment sentence \nprediction, Transformer and VADER \noutperform the other models."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 1.2 * UP + 2.8 * RIGHT)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]))
        self.play(ShowCreation(dot_collection[1]), Write(cloud_disapper_text4))
        self.play(ShowCreation(dot_collection[2]))
        self.play(ShowCreation(dot_collection[3]))


        #  ------------------ Neutral sentence -----------------------------


        self.play(FadeOut(top_disapper_text), FadeOut(transformer_output_text), 
                  FadeOut(flair_output_text), FadeOut(textblob_output_text), FadeOut(vadar_output_text))
        self.play(FadeOut(cloud_disapper_text4))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Neutral Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        
        box_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace">str3 = "Childhood is the time to play."</span>',
                      0.45, WHITE, 3.1 * UP + 0.6 * LEFT)
        self.play(Transform(box_disapper_text1, box_disapper_text2), FadeOut(box_disapper_text))


        transformer_str_replace3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str3</b></span>',
                      0.3, GREY_A, 2.5 * UP + 3.47 * LEFT)
        self.play(Transform( transformer_str_replace2, transformer_str_replace3), FadeOut(transformer_code_text_fixed[25:29]))

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'POSITIVE', 'score': 0.9988179206848145}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)
        self.play( Write(transformer_output_text))


        flair_str_replace3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str3</b></span>',
                      0.32, GREY_A, 1.6 * UP + 4.05 * LEFT)
        self.play(Transform( flair_str_replace2, flair_str_replace3), FadeOut(flair_code_text[19:23]))


        flair_output = """Sentiment of above sentence is: [POSITIVE (0.999)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play( Write(flair_output_text))


        textblob_str_replace3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str3</b></span>',
                      0.32, GREY_A, 0.75 * UP + 3.67 * LEFT)
        self.play(Transform(textblob_str_replace2, textblob_str_replace3), FadeOut(textblob_code_text[22:26]))

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=0.0, subjectivity=0.0)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 4.12 * LEFT)
        self.play(Write(textblob_output_text))

        vadar_str_replace3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str3</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 4.45 * LEFT)
        self.play(Transform(vadar_str_replace2, vadar_str_replace3), FadeOut(vadar_code_text[19:23]))


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.0, 'neu': 0.7, 'pos': 0.3, 'compound': 0.34}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.74 * LEFT)
        self.play( Write(vadar_output_text))

        cloud_text1 = """Only TextBlob has categorized the \nstr3 in neutral."""


        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 2.1 * UP + 2.6 * RIGHT)
        self.play(Write(cloud_disapper_text1), run_time=2)


        cloud_text2 = """For the text "study is going on as usual",\nonly VADER has categorized it in neutral."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.2 * UP + 2.9 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)


        sentiment_time_bar_nu = BarChart([1.2,1.3,41.25,65.62],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_nu.shift(2.47 * DOWN + 3.5 * RIGHT)

        self.play(Transform(sentiment_time_bar_n, sentiment_time_bar_nu), FadeOut(sentiment_time_bar_p),run_time=2)

        self.play(FadeOut(bar_disapper_text1) ,FadeOut(bar_disapper_text2), 
                  FadeOut(bar_disapper_text3),FadeOut(bar_disapper_text4), FadeOut(dot_collection),)


        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>65.62</b></span>',
                      0.3, GREY_A, 1.15 * DOWN + 5.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>41.25</b></span>',
                      0.3, GREY_A, 1.95 * DOWN + 4.35 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.3</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.2</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))

        cloud_text3 = """There is a blurred line between\npositive sentiment and neutral sentiment\nwhich makes the model's job hard."""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.01 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text3), run_time=3)

        # ---------- graph of positive sentences ------------

        data = [0.34,  0.0,  0.99,  0.99]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], 0.34))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>0.34(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], 0.0))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>0.0(±)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.99))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.99))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        self.play(FadeOut(cloud_disapper_text1), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text3))

        cloud_text4 = """Transformer and flair do not have \na neutral category. Generally, \nconfidence score of text below, 0.50, \ncan be categorized as neutral."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 1.8 * UP + 2.8 * RIGHT)

        cloud_text5 = """TextBlob and VADER are the best \noptions for detecting neutral \nsentiment sentences. """
        cloud_disapper_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text5}</b></span>',
                      0.3, BLACK, 0.21 * UP + 2.8 * RIGHT)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]), Write(cloud_disapper_text4), run_time=5)
        self.play(ShowCreation(dot_collection[1]))
        self.play(ShowCreation(dot_collection[2]), Write(cloud_disapper_text5), run_time=2)
        self.play(ShowCreation(dot_collection[3]))


        #  ------------------ Racism type sentence -----------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(transformer_output_text), 
                  FadeOut(flair_output_text), FadeOut(textblob_output_text), FadeOut(vadar_output_text))
        self.play(FadeOut(cloud_disapper_text4), FadeOut(cloud_disapper_text5))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Racism Type Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        
        box_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace">str4 = "Every second and third face is Asian and their slitted almond eyes bore straight through you."</span>',
                      0.41, WHITE, 3.1 * UP + 0.6 * LEFT)
        self.play(Transform(box_disapper_text2, box_disapper_text3), FadeOut(box_disapper_text1))


        transformer_str_replace4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str4</b></span>',
                      0.3, GREY_A, 2.5 * UP + 3.47 * LEFT)
        self.play(Transform( transformer_str_replace3, transformer_str_replace4), FadeOut(transformer_str_replace2))

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'POSITIVE', 'score': 0.7424587607383728}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)
        self.play(Write(transformer_output_text))

        


        flair_str_replace4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str4</b></span>',
                      0.32, GREY_A, 1.6 * UP + 4.05 * LEFT)
        self.play(Transform( flair_str_replace3, flair_str_replace4), FadeOut(flair_str_replace2))


        flair_output = """Sentiment of above sentence is: [NEGATIVE (0.997)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play( Write(flair_output_text))


        textblob_str_replace4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str4</b></span>',
                      0.32, GREY_A, 0.75 * UP + 3.67 * LEFT)
        self.play(Transform(textblob_str_replace3, textblob_str_replace4), FadeOut(textblob_str_replace2))

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=0.05, subjectivity=0.1)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 4.12 * LEFT)
        self.play(Write(textblob_output_text))


        vadar_str_replace4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str4</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 4.45 * LEFT)
        self.play(Transform(vadar_str_replace3, vadar_str_replace4), FadeOut(vadar_str_replace2))


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.1, 'neu': 0.8, 'pos': 0.1, 'compound': -0.03}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.74 * LEFT)
        self.play( Write(vadar_output_text))

        cloud_text1 = """only Flair consider this text \nas negative.Because, it's trained on \nsocial media data."""

        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 1.9 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1))

        cloud_text2 = """Other sentences will have similar results.\nIt's because racism-type sample \ntext data are not abundantly available."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 0.85 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)



        sentiment_time_bar_ra = BarChart([2.1,1.3,39.67,68.42],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_ra.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(Transform(sentiment_time_bar_nu, sentiment_time_bar_ra), FadeOut(sentiment_time_bar_n),run_time=2)

        self.play(FadeOut(bar_disapper_text1) ,FadeOut(bar_disapper_text2), 
                  FadeOut(bar_disapper_text3),FadeOut(bar_disapper_text4), FadeOut(dot_collection),)


        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>68.42</b></span>',
                      0.3, GREY_A, 1.05 * DOWN + 5.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>39.67</b></span>',
                      0.3, GREY_A, 2 * DOWN + 4.35 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.3</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>2.1</b></span>',
                      0.3, GREY_A, 3.3 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))

        cloud_text3 = """Flair will be the best choice to\ndetect Racism type text data."""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.01 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))


        data = [-0.03,  0.05,  0.99,  0.74]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], -0.03))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>-0.3(±)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], 0.05))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>0.05(±)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.99))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.99(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.74))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.74(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis, self.x_axis_labels)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]))
        self.play(ShowCreation(dot_collection[1]))
        self.play(ShowCreation(dot_collection[2]))
        self.play(ShowCreation(dot_collection[3]))


        #  ------------------ Racism type sentence -----------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(transformer_output_text), 
                  FadeOut(flair_output_text), FadeOut(textblob_output_text), FadeOut(vadar_output_text))
        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text1))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Gender Bias Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        
        box_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace">str5 = "Boys are better than girls in sports."</span>',
                      0.45, WHITE, 3.1 * UP + 0.6 * LEFT)
        self.play(Transform(box_disapper_text3, box_disapper_text4), FadeOut(box_disapper_text2))


        transformer_str_replace5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str5</b></span>',
                      0.3, GREY_A, 2.5 * UP + 3.47 * LEFT)
        self.play(Transform( transformer_str_replace4, transformer_str_replace5), FadeOut(transformer_str_replace3))

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'POSITIVE', 'score': 0.997786760302002}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)
        self.play( Write(transformer_output_text))


        flair_str_replace5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str5</b></span>',
                      0.32, GREY_A, 1.6 * UP + 4.05 * LEFT)
        self.play(Transform( flair_str_replace4, flair_str_replace5), FadeOut(flair_str_replace3))


        flair_output = """Sentiment of above sentence is: [POSITIVE (0.968)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play( Write(flair_output_text))




        textblob_str_replace5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str5</b></span>',
                      0.32, GREY_A, 0.75 * UP + 3.67 * LEFT)
        self.play(Transform(textblob_str_replace4, textblob_str_replace5), FadeOut(textblob_str_replace3))

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=0.5, subjectivity=0.5)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 4.12 * LEFT)
        self.play(Write(textblob_output_text))


        vadar_str_replace5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str5</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 4.45 * LEFT)
        self.play(Transform(vadar_str_replace4, vadar_str_replace5), FadeOut(vadar_str_replace3))


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.0, 'neu': 0.7, 'pos': 0.3, 'compound': 0.44}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.74 * LEFT)
        self.play( Write(vadar_output_text))

        cloud_text1 = """In the case of a string, \n"girls are better than boys in sports.", \nthe output of 4 models will be same."""

        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 1.9 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1), run_time=2)

        cloud_text2 = """These models are not affected by \ngender bias sentiments."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 0.85 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=1)


        sentiment_time_bar_ge = BarChart([1.3,0.9,36.13,66.52],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_ge.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(Transform(sentiment_time_bar_ra, sentiment_time_bar_ge), FadeOut(sentiment_time_bar_nu),run_time=2)
        self.play(FadeOut(bar_disapper_text1) ,FadeOut(bar_disapper_text2), 
                  FadeOut(bar_disapper_text3),FadeOut(bar_disapper_text4), FadeOut(dot_collection),)


        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>66.52</b></span>',
                      0.3, GREY_A, 1.15 * DOWN + 5.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>36.13</b></span>',
                      0.3, GREY_A, 2.15 * DOWN + 4.35 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>0.9</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.3</b></span>',
                      0.3, GREY_A, 3.3 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))

        cloud_text3 = """All models consider these type of \nsentences as positive sentiment only."""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.01 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))


        # ---------- graph of positive sentences ------------

        data = [0.44,  0.5,  0.96,  0.99]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], 0.44))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>0.44(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], 0.5))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>0.5(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.96))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.96(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.99))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis, self.x_axis_labels)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]))
        self.play(ShowCreation(dot_collection[1]))
        self.play(ShowCreation(dot_collection[2]))
        self.play(ShowCreation(dot_collection[3]))


        #  ---------------------- Negative and positive sentiment in one sentence -----------------

        self.play(FadeOut(top_disapper_text), FadeOut(transformer_output_text), 
                  FadeOut(flair_output_text), FadeOut(textblob_output_text), FadeOut(vadar_output_text))
        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text1))


        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Positive and Negative sentiment in one Sentence</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        
        box_disapper_text5 = currentTextPositionMarkupWithout(r'<span font_family="monospace">str6 = "I love this car. This view is horrible. I don not like this car. This view is amazing."</span>',
                      0.42, WHITE, 3.1 * UP + 0.6 * LEFT)
        
        self.play(Transform(box_disapper_text4, box_disapper_text5), FadeOut(box_disapper_text3))


        transformer_str_replace6 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str6</b></span>',
                      0.3, GREY_A, 2.5 * UP + 3.47 * LEFT)
        self.play(Transform( transformer_str_replace5, transformer_str_replace6), FadeOut(transformer_str_replace4))

        transformer_code_output = """Sentiment of above sentence is:\n[{'label': 'POSITIVE', 'score': 0.9995825886726379}]"""

        transformer_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code_output}</b></span>',
                      0.3, GREY_A, 2.15 * UP + 3.65 * LEFT)

        self.play( Write(transformer_output_text))


        flair_str_replace6 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str6</b></span>',
                      0.32, GREY_A, 1.6 * UP + 4.05 * LEFT)
        self.play(Transform( flair_str_replace5, flair_str_replace6), FadeOut(flair_str_replace4))


        flair_output = """Sentiment of above sentence is: [NEGATIVE (0.999)]"""

        flair_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_output}</b></span>',
                      0.32, GREY_A, 1.3 * UP + 3.55 * LEFT)

        self.play( Write(flair_output_text))


        textblob_str_replace6 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str6</b></span>',
                      0.32, GREY_A, 0.75 * UP + 3.67 * LEFT)
        self.play(Transform(textblob_str_replace5, textblob_str_replace6), FadeOut(textblob_str_replace4))

        textblob_output = """Sentiment of above sentence is:\nSentiment(polarity=0.55, subjectivity=0.75)"""

        textblob_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_output}</b></span>',
                      0.32, GREY_A, 0.35 * UP + 4.12 * LEFT)
        self.play(Write(textblob_output_text))


        vadar_str_replace6 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>str6</b></span>',
                      0.28, GREY_A, 0.15 * DOWN + 4.45 * LEFT)
        self.play(Transform(vadar_str_replace5, vadar_str_replace6), FadeOut(vadar_str_replace4))


        vader_output = """Sentiment of above sentence is:\n{'neg': 0.1, 'neu': 0.6, 'pos': 0.3, 'compound': 0.78}"""

        vadar_output_text = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_output}</b></span>',
                      0.28, GREY_A, 0.5 * DOWN + 3.74 * LEFT)
        self.play( Write(vadar_output_text))

        cloud_text1 = """It depends on whether the overall\nsentiment is positive or negative."""
        cloud_disapper_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text1}</b></span>',
                      0.3, BLACK, 2.1 * UP + 2.9 * RIGHT)
        self.play(Write(cloud_disapper_text1), run_time=2)


        cloud_text2 = """The confidence score of different\nmodels varies a lot for different mixed\nsentiment types of sentences."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.2 * UP + 2.9 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=3)



        sentiment_time_bar_np = BarChart([1.4,0.9,32.35,29.92],bar_names=['vader', 'textblob', 'flair', 'Transformers'],
                         width=9, n_ticks=7,max_value=70,
                         stroke_width=15,bar_colors=['#AD59B4', '#C0ED3C', '#978CCC', '#7AEAB6'],
                         fill_opacity=1).scale(.6)
        sentiment_time_bar_np.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(Transform(sentiment_time_bar_ge, sentiment_time_bar_np), FadeOut(sentiment_time_bar_ra),run_time=2)
        self.play(FadeOut(bar_disapper_text1) ,FadeOut(bar_disapper_text2), 
                  FadeOut(bar_disapper_text3),FadeOut(bar_disapper_text4), FadeOut(dot_collection),)


        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>29.92</b></span>',
                      0.3, GREY_A, 2.35 * DOWN + 5.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>32.35</b></span>',
                      0.3, GREY_A, 2.25 * DOWN + 4.35 * RIGHT)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>0.9</b></span>',
                      0.3, GREY_A, 3.4 * DOWN + 3.1 * RIGHT)
        bar_disapper_text4 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.4</b></span>',
                      0.3, GREY_A, 3.3 * DOWN + 1.9 * RIGHT)

        self.play(Write(bar_disapper_text1), Write(bar_disapper_text2),Write(bar_disapper_text3),Write(bar_disapper_text4))

        cloud_text3 = """In such texts it's hard to rely\non only a single prediction model."""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.01 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text3), run_time=3)


        data = [0.78,  0.5,  0.99,  0.99]
        x = [1,     2,   3,  4]
        self.setup_axes()

        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))

        values_x = [
        (1, "VADAR"),  # (position 3.5, label "3.5")
        (2, "TEXTBLOB"),
        (3, "FLAIR"),
        (4, "TF"),  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        label_nums_color = WHITE
        x_label_font_size =  0.6,
        for x_val, x_tex in values_x:
            tex = MarkupText(f'<span font_family="monospace"><b>{x_tex}</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
            # tex = TexMobject(x_tex)  # Convert string to tex
            tex.set_color(label_nums_color)
            tex.scale(x_label_font_size)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph

        
        dot_collection = VGroup()
        # for time, val in enumerate(data):

        dot1_group = VGroup()
        dot1 = Dot().move_to(self.coords_to_point(x[0], 0.78))
        # self.add(dot1)
        dot1_name = MarkupText(r'<span font_family="monospace"><b>0.78(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot1_name.next_to(dot1)
        dot1_group.add(dot1,dot1_name)
        dot_collection.add(dot1_group)


        dot2_group = VGroup()
        dot2 = Dot().move_to(self.coords_to_point(x[1], 0.55))
        # self.add(dot2)
        dot2_name = MarkupText(r'<span font_family="monospace"><b>0.55(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot2_name.next_to(dot2)
        dot2_group.add(dot2,dot2_name)
        dot_collection.add(dot2_group)



        dot3_group = VGroup()
        dot3 = Dot().move_to(self.coords_to_point(x[2], 0.99))
        # self.add(dot3)
        dot3_name = MarkupText(r'<span font_family="monospace"><b>0.99(-)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot3_name.next_to(dot3)
        dot3_group.add(dot3,dot3_name)
        dot_collection.add(dot3_group)



        dot4_group = VGroup()
        dot4 = Dot().move_to(self.coords_to_point(x[3], 0.99))
        # self.add(dot4)
        dot4_name = MarkupText(r'<span font_family="monospace"><b>0.99(+)</b></span>',
                               color=TEAL_D,opacity=1).scale(0.7)
        dot4_name.next_to(dot4)
        dot4_group.add(dot4,dot4_name)
        dot_collection.add(dot4_group)
        
        group2 = VGroup(dot_collection, self.x_axis, self.y_axis, self.x_axis_labels)
        group2.scale(0.45)
        group2.shift(0.1 * DOWN + 4.5 * LEFT)
        group2.remove(dot_collection)

        self.play(FadeOut(cloud_disapper_text1), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text3))

        cloud_text4 = """All models will predict either positive\nsentiment or negative sentiment."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 1.8 * UP + 2.95 * RIGHT)

        cloud_text5 = """This model doesn't categorize\nthis type of text as neutral sentiment."""
        cloud_disapper_text5 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text5}</b></span>',
                      0.3, BLACK, 1 * UP + 2.8 * RIGHT)

        self.play(ShowIncreasingSubsets(group2))
        self.play(ShowCreation(dot_collection[0]), Write(cloud_disapper_text4), run_time=3)
        self.play(ShowCreation(dot_collection[1]))
        self.play(ShowCreation(dot_collection[2]), Write(cloud_disapper_text5), run_time=2)
        self.play(ShowCreation(dot_collection[3]))

        self.wait(4)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(4)
