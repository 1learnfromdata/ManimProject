from manim import *


class SentimentAnalysisSingle(GraphScene,Scene):

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
            self.play(Write(index_text), run_time=0.1)
            return index_text

        def currentTextPositionMarkupWithout(name, size_of_text, color_text, position):
            index_text = MarkupText(name,color=color_text,opacity=1).scale(size_of_text)
            index_text.shift(position)
            return index_text


        # transformers ---------------------------------------------------------------------------------------


        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>HuggingFace Transformers Library</b></span>',
                      0.6, TEAL_A, 3.7 * UP + 0.6 * LEFT)

        create_rectange(13.9, 0.6, 3.1 * UP + 0.1 * LEFT, BLACK)
        create_rectange(7.1, 4.5, 0.4 * UP + 3.5 * LEFT, DARK_GRAY)

        thinking_letter = SVGMobject("/home/manmohan/python_projects/manim_projects/regex_visual/last_thinking_cloud")
        thinking_letter.set_height(1)
        thinking_letter.set_width(5.4)
        thinking_letter.set_color(GREEN)
        thinking_letter.shift(0.8 * UP + 3 * RIGHT)

        owl_image = ImageMobject("/home/manmohan/python_projects/manim_projects/regex_visual/new_owl.png")
        owl_image.set_height(1)
        owl_image.shift(0.9 * DOWN + 5.5 * RIGHT)

        self.play(FadeIn(thinking_letter), FadeIn(owl_image))

        box_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace">str1 = "Even the most beautiful days eventually have their sunsets."</span>',
                      0.45, WHITE, 3.1 * UP + 0.6 * LEFT)

        cloud_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>pip install transformers</b></span>',
                      0.35, BLACK, 2.2 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1))


        transformer_code = """from transformers import pipeline\nclassifier = pipeline('sentiment-analysis')\n\ndef transformer_sentiment(sentence):\n    sentence_sentiment = classifier(sentence)\n    print(f"Sentiment of above sentence is: "\n      f"{sentence_sentiment}")\n\ntransformer_sentiment(str1)"""
        
        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code}</b></span>',
                      0.37, GREY_A, 1 * UP + 3.5 * LEFT)
        code_text1[0:4].set_color(ORANGE)
        code_text1[16:22].set_color(ORANGE)
        code_text1[50:70].set_color(GREEN_E)
        code_text1[71:74].set_color(ORANGE)
        code_text1[74:95].set_color(YELLOW_C)
        code_text1[145:150].set_color(BLUE_C)
        code_text1[151:183].set_color(GREEN_E)
        code_text1[203:204].set_color(GREEN_E)
        self.play(Write(code_text1), run_time=3)

        cloud_text2 = """pipeline("sentiment-analysis") will use \ndefault model distilbert-base-uncased\n-finetuned-sst-2-english"""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.5 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)


        cloud_text3 = """To use model other then default \nVisit https://huggingface.co/models"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.55 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))

        fixed_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Output</b></span>',
                      0.4, TEAL_D, 2.14 * DOWN + 6.4 * LEFT)

        create_rectange(7.1, 1.5, 3.2 * DOWN + 3.5 * LEFT, DARK_GRAY)


        transformer_code1 = """Sentiment of above sentence is:\n [{'label': 'POSITIVE', 'score': 0.9987558126449585}]"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{transformer_code1}</b></span>',
                      0.32, GREY_A, 3 * DOWN + 3.6 * LEFT)
        self.play(Write(code_text2))

        cloud_text4 = """Classification - Positive and Negative\nSentiment Score scale - 0 to 1"""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 0.15 * DOWN + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text4))


        poly = BarChart([59.29],bar_names=["Transformers"],
                         width=9, n_ticks=8,max_value=80, 
                         stroke_width=15,bar_colors=['#7AEAB6'],
                         fill_opacity=1).scale(.6)
        poly.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(ShowCreation(poly),run_time=3)
        bar_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>59.29(ms)</b></span>',
                      0.4, GREY_A, 1.6 * DOWN + 3.7 * RIGHT)
        

        y_axis_label_name = currentTextPositionMarkup(r'<span font_family="monospace"><b>Time(milliseconds)</b></span>',
                      0.3, BLUE_D, 0.9 * DOWN + 1.1 * RIGHT)

        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text4))

        cloud_text4 = """Transformer will only process sentence \nwhose length is less than 512."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.3, BLACK, 1.1 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text4), run_time=2)


        # flair ---------------------------------------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(code_text1),FadeOut(code_text2))
        self.play(FadeOut(cloud_disapper_text4), FadeOut(cloud_disapper_text1))


        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Flair NLP Library</b></span>',
                      0.6, BLUE_D, 3.7 * UP + 0.6 * LEFT)

        cloud_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>pip install flair</b></span>',
                      0.35, BLACK, 2.2 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1))


        flair_code = """from flair.models import TextClassifier\nfrom flair.data import Sentence\n\nclassifier = TextClassifier.load('en-sentiment')\n\ndef flair_sentiment(sentence):\n    sentence_sentiment = Sentence(sentence)\n    classifier.predict(sentence_sentiment)\n    print(f'Sentiment of above sentence is: '\n          f'{sentence_sentiment.labels}')\n\nflair_sentiment(str1)"""

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_code}</b></span>',
                      0.37, GREY_A, 0.7 * UP + 3.5 * LEFT)
        code_text1[0:4].set_color(ORANGE)
        code_text1[16:22].set_color(ORANGE)
        code_text1[36:40].set_color(ORANGE)
        code_text1[50:56].set_color(ORANGE)
        code_text1[95:109].set_color(GREEN_E)
        code_text1[110:113].set_color(ORANGE)
        code_text1[113:128].set_color(YELLOW_C)
        code_text1[214:219].set_color(BLUE_C)
        code_text1[220:252].set_color(GREEN_E)
        code_text1[279:280].set_color(GREEN_E)
        self.play(Write(code_text1), run_time=3)

        cloud_text2 = """TextClassifier.load('en-sentiment') use \ndefault model which has trained on \nIMDB dataset."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.5 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)

        fixed_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Output</b></span>',
                      0.4, TEAL_D, 2.14 * DOWN + 6.4 * LEFT)


        flair_code1 = """Sentiment of above sentence is: [POSITIVE (0.999)]"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{flair_code1}</b></span>',
                      0.32, GREY_A, 3 * DOWN + 3.6 * LEFT)
        self.play(Write(code_text2))

        cloud_text3 = """Classification - Positive and Negative\nSentiment Score scale - 0 to 1"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.55 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))

        cloud_text4 = """There is no sentence length \nlimitation in flair."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.35, BLACK, 0.15 * DOWN + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text4))


        poly_flair = BarChart([41.82],bar_names=["Flair"],
                         width=9, n_ticks=8,max_value=80, 
                         stroke_width=15,bar_colors=['#978CCC'],
                         fill_opacity=1).scale(.6)
        poly_flair.shift(2.47 * DOWN + 3.5 * RIGHT)
        bar_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>41.82(ms)</b></span>',
                      0.4, GREY_A, 2.1 * DOWN + 3.7 * RIGHT)
        self.play(Transform(poly,poly_flair),FadeOut(bar_disapper_text), FadeIn(bar_disapper_text1) ,run_time=2)


        

        # # y_axis_label_name = currentTextPositionMarkup(r'<span font_family="monospace"><b>Time(milliseconds)</b></span>',
        # #               0.3, TEAL_D, 0.9 * DOWN + 1.1 * RIGHT)


        # # Textblob ---------------------------------------------------------------------------------------
        self.play(FadeOut(top_disapper_text), FadeOut(code_text1),FadeOut(code_text2))
        self.play(FadeOut(cloud_disapper_text1), FadeOut(cloud_disapper_text2), FadeOut(cloud_disapper_text3), 
                  FadeOut(cloud_disapper_text4))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>TextBlob NLP Library</b></span>',
                      0.6, GREEN_SCREEN, 3.7 * UP + 0.6 * LEFT)

        cloud_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>pip install textblob</b></span>',
                      0.35, BLACK, 2.2 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1))


        textblob_code = """from textblob import TextBlob\n\ndef textblob_sentiment(sentence):\n\n    sentence_sentiment = TextBlob(sentence)\n    print(f'Sentiment of above sentence is: '\n          f'{sentence_sentiment.sentiment}')\n\ntextblob_sentiment(str1)"""

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_code}</b></span>',
                      0.37, GREY_A, 0.7 * UP + 3.5 * LEFT)
        code_text1[0:4].set_color(ORANGE)
        code_text1[12:18].set_color(ORANGE)
        code_text1[26:29].set_color(ORANGE)
        code_text1[29:47].set_color(YELLOW_C)
        code_text1[95:100].set_color(BLUE_C)
        code_text1[101:133].set_color(GREEN_E)
        code_text1[163:164].set_color(ORANGE)
        self.play(Write(code_text1), run_time=2)

        cloud_text2 = """TextBlob is a python library which \nfollow Rule-based sentiment analysis \napproach to calculate text sentiments."""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.5 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=2)

        fixed_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Output</b></span>',
                      0.4, TEAL_D, 2.14 * DOWN + 6.4 * LEFT)


        textblob_code1 = """Sentiment of above sentence is:\nSentiment(polarity=0.675, subjectivity=0.75)"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{textblob_code1}</b></span>',
                      0.32, GREY_A, 3 * DOWN + 4 * LEFT)
        self.play(Write(code_text2))

        cloud_text3 = """Classification - Polarity and Subjectivity\n Polarity Sentiment scale - \nfrom -1 (Negative) to +1 ( Positive)\nSubjectivity scale - \nfrom 0 (opinion) to 1 (fact)"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.1 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text3), run_time = 3)


        poly_textblob = BarChart([1.2],bar_names=["TextBlob"],
                         width=9, n_ticks=8,max_value=80, 
                         stroke_width=15,bar_colors=['#C0ED3C'],
                         fill_opacity=1).scale(.6)
        poly_textblob.shift(2.47 * DOWN + 3.5 * RIGHT)
        bar_disapper_text2 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.2(ms)</b></span>',
                      0.4, GREY_A, 3.3 * DOWN + 3.9 * RIGHT)
        self.play(Transform(poly_flair, poly_textblob),FadeOut(poly), 
                  FadeOut(bar_disapper_text1), FadeIn(bar_disapper_text2),run_time=2)

        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2))

        cloud_text4 = """I have considerd Polarity for \nSentiment Analysis comparision."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.35, BLACK, 1.1 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text4))

        

        # # y_axis_label_name = currentTextPositionMarkup(r'<span font_family="monospace"><b>Time(milliseconds)</b></span>',
        # #               0.3, BLUE_D, 0.9 * DOWN + 1.1 * RIGHT)


        # # Vadar ---------------------------------------------------------------------------------------
        self.play(FadeOut(top_disapper_text), FadeOut(code_text1),FadeOut(code_text2))
        self.play(FadeOut(cloud_disapper_text4), FadeOut(cloud_disapper_text1))

        top_disapper_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>VADER NLP Library</b></span>',
                      0.6, PURPLE_A, 3.7 * UP + 0.6 * LEFT)

        cloud_disapper_text1 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>pip install vaderSentiment</b></span>',
                      0.35, BLACK, 2.2 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text1))


        vader_code = """from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer"""

        code_text1 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_code}</b></span>',
                      0.25, GREY_A, 1.7 * UP + 3.45 * LEFT)
        code_text1[0:4].set_color(ORANGE)
        code_text1[33:39].set_color(ORANGE)
        self.play(Write(code_text1))

        vader_code0 = """analyzer = SentimentIntensityAnalyzer()\n\ndef vader_sentiment(sentence):\n\n    vs = analyzer.polarity_scores(sentence)\n    print(f'Sentiment of above sentence is: {vs}')\n\nvader_sentiment(str1)"""

        code_text0 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_code0}</b></span>',
                      0.35, GREY_A, 0.05 * UP + 3.4 * LEFT)
        code_text0[37:40].set_color(ORANGE)
        code_text0[40:55].set_color(YELLOW_C)
        code_text0[103:108].set_color(BLUE_C)
        code_text0[109:137].set_color(GREEN_E)
        code_text0[142:143].set_color(GREEN_E)
        self.play(Write(code_text0), run_time=2)

        cloud_text2 = """VADER (Valence Aware Dictionary \nand sEntiment Reasoner) is a lexicon \nand rule-based sentiment analysis tool"""
        cloud_disapper_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text2}</b></span>',
                      0.3, BLACK, 1.5 * UP + 2.95 * RIGHT)
        self.play(Write(cloud_disapper_text2), run_time=3)


        cloud_text3 = """Vader default model is optimized \nfor social media data"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.55 * UP + 2.8 * RIGHT)
        self.play(Write(cloud_disapper_text3))

        fixed_text = currentTextPositionMarkup(r'<span font_family="monospace"><b>Output</b></span>',
                      0.4, TEAL_D, 2.14 * DOWN + 6.4 * LEFT)


        vader_code1 = """Sentiment of above sentence is:\n{'neg': 0.0, 'neu': 0.656, 'pos': 0.344, 'compound': 0.6361}"""

        code_text2 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{vader_code1}</b></span>',
                      0.3, GREY_A, 3 * DOWN + 3.4 * LEFT)
        self.play(Write(code_text2))

        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text2))


        cloud_text3 = """Classification - Positive, Negative, \nNeutral and compound.\n\nCompound score is the sum of all \nthe lexicon ratings [scale from +1 to -1]\n\npositive sentiment : >= 0.05\nneutral sentiment : > -0.05 and   0.05\nnegative sentiment :  = -0.05"""
        cloud_disapper_text3 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text3}</b></span>',
                      0.3, BLACK, 0.8 * UP + 3.1 * RIGHT)
        self.play(Write(cloud_disapper_text3), run_time = 3)


        cloud_disapper_text10 = currentTextPositionText(f'<',
                      0.34, BLACK, 0.1 * UP + 4.6 * RIGHT)

        cloud_disapper_text11 = currentTextPositionText(f'<',
                      0.34, BLACK, 0.15 * DOWN + 3.2 * RIGHT)


        poly_vader = BarChart([1.5],bar_names=["VADER"],
                         width=9, n_ticks=8,max_value=80, 
                         stroke_width=15,bar_colors=['#AD59B4'],
                         fill_opacity=1).scale(.6)
        bar_disapper_text3 = currentTextPositionMarkupWithout(r'<span font_family="monospace"><b>1.5(ms)</b></span>',
                      0.4, GREY_A, 3.3 * DOWN + 3.9 * RIGHT)
        poly_vader.shift(2.47 * DOWN + 3.5 * RIGHT)
        self.play(Transform(poly_textblob, poly_vader), FadeOut(poly_flair),
                  FadeOut(bar_disapper_text2), FadeIn(bar_disapper_text3) , run_time=2)

        self.play(FadeOut(cloud_disapper_text3), FadeOut(cloud_disapper_text10), FadeOut(cloud_disapper_text11))

        cloud_text4 = """I have considerd Compound score for \nSentiment Analysis comparision."""
        cloud_disapper_text4 = currentTextPositionMarkupWithout(f'<span font_family="monospace"><b>{cloud_text4}</b></span>',
                      0.35, BLACK, 1.1 * UP + 3 * RIGHT)
        self.play(Write(cloud_disapper_text4))
        self.wait(4)


        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(4)
