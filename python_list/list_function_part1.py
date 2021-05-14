from manim import *


class ListFunction(Scene):
    def construct(self):
        intro_text = Tex('Python offers the following list functions:')
        intro_text.shift(2 * UP)
        self.play(Write(intro_text))
        paragraph_1 = Paragraph("1. list.append()", "\n2. list.extend()", "\n3. list.insert()",
                                "\n4. list.remove() ", "\n5. list.pop() ", "\n6. list.clear()").scale(0.5)

        paragraph_2 = Paragraph("\n7. list.index()", "\n8. list.sort()", "\n9. list.count()",
                                "\n10. list.reverse()", "\n11. list.copy()", 
                                # "\n12. max(list"
                                ).scale(0.5)

        # paragraph_3 = Paragraph("\n13. min(list)", "\n14. len(list)", "\n15. cmp(list1, list2)").scale(0.5)

        paragraph_1.shift(0.5 * DOWN + 3 * LEFT)
        paragraph_2.shift(0.5 * DOWN + 1.2 * RIGHT)
        # paragraph_3.shift(0.5 * UP + 3.2 * RIGHT)
        # self.play(Write(paragraph_1))


        self.play(Write(paragraph_1))

        # self.play(Write(paragraph_2))
        paragraph_2.set_color(YELLOW)
        self.play(Write(paragraph_2))

        # self.play(Write(paragraph_3))
        # self.play(Write(paragraph_3))

        self.play(FadeOut(paragraph_2), FadeOut(intro_text),FadeOut(paragraph_1))

        part_text = Tex(r'Part 1').scale(2)
        part_text.shift(3 * UP)
        
        
        paragraph_1.scale(1)
        paragraph_1.shift(2 * RIGHT)
        self.add(paragraph_1)
        self.play(Write(part_text), Write(paragraph_1))

        self.play(FadeOut(paragraph_1), FadeOut(part_text))


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
            # self.play(Write(explain_filled_rect))
            # explain_filled_rect = explain_rect.copy()
            explain_filled_rect.set_fill(color_fill, 0.5)
            self.play(GrowFromCenter(explain_filled_rect, run_time=1))
            # Use stretch=True to preserve the dimension that is not modified
            # explain_filled_rect.set_height(1)
            # compress the definitions of your objects, this will make it easier to read them.
            explain_line_left, explain_line_bottom = [
                Line(
                    explain_filled_rect.get_corner(start),
                    explain_filled_rect.get_corner(end),
                    color=RED_A
                )
                for start, end in [(DL, UL), (DL, DR)]
            ]

            # self.play(FadeIn(explain_filled_rect))
            self.play(
                GrowFromEdge(explain_line_left, DOWN),
                GrowFromEdge(explain_line_bottom, LEFT)
            )

        # end first rectangle
        

        # create_rectange(12, 1, 1.9 * UP + 0.001 * RIGHT, DARK_GRAY)
        # create_rectange(6.6, 5.5, 1 * DOWN + 3.5 * LEFT, DARK_GRAY)
        # create_rectange(7.1, 5.5, 1 * DOWN + 3.5 * RIGHT, DARK_GRAY)

        def currentTextPositionTex(name, size_of_text, color_text, position):
            index_text = Tex(name,color=color_text).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text


        def currentTextPositionText(name, size_of_text, color_text, position):
            index_text = Text(name,color=color_text).scale(size_of_text)
            index_text.shift(position)
            self.play(Write(index_text))
            return index_text

        top_disapper_text = currentTextPositionTex(r"\\list.append(x) : Add an item to the end of the list.",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)

        create_rectange(12, 0.5, 3.2 * UP + 0.001 * RIGHT, BLACK)
        black_disappear_text = currentTextPositionText("Let's consider a list variable fruits", 0.5, WHITE, 3.18 * UP + 2 * LEFT)

        create_rectange(12, 0.8, 2.4 * UP + 0.001 * RIGHT, DARK_GRAY)
        # create_rectange(6.6, 5.5, 1 * DOWN + 3.5 * LEFT, DARK_GRAY)

        text_list = MathTex(
            "fruits = ",
            "[ ",
            " 'orange' " ,
             " , ",    
             " 'apple' " , " , "," 'pear' " , " , ", " 'banana'  " , ",", "'kiwi'", " ]"
        ).scale(0.8)

        text_list.shift( 2.4 * UP + LEFT)
        self.play(Write(text_list))


        # create_rectange(6.6, 5.5, 1 * DOWN + 3.5 * LEFT, DARK_GRAY)

        
        create_rectange(7.1, 5.5, 1 * DOWN + 3.5 * RIGHT, DARK_GRAY)

        random_text_1 = currentTextPositionText(">>>", 0.2, RED, 1.5 * UP + 0.2 * RIGHT)
        random_text_2 = currentTextPositionText(" fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']", 
                                                0.3, WHITE, 1.5 * UP + 3 * RIGHT)

        random_text_4 = currentTextPositionText(">>>", 0.2, RED, 1.2 * UP + 0.2 * RIGHT)
        random_text_3 = currentTextPositionText(" fruits.append('apple')", 
                                                0.3, WHITE, 1.2 * UP + 1.6 * RIGHT)

        self.play(FadeOut(black_disappear_text))
        black_disappear_text = currentTextPositionText("let’s extend the string by adding 'apple' to the list with the method append().", 
        	                                           0.4, WHITE, 3.18 * UP + 0.7 * LEFT)

        create_rectange(6.6, 5.5, 1 * DOWN + 3.5 * LEFT, DARK_GRAY)

        framebox1 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait(1)
        first_arrow = Arrow(2.15 * UP + 0.2 * LEFT,  0.7 * UP + 4.6 * LEFT)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("['orange', 'apple', 'pear', 'banana', 'kiwi'", 0.4, WHITE, 0.5 * UP + 4 * LEFT)
        random_text_6 = Text("]",color=WHITE).scale(0.4)
        random_text_6.shift(0.5 * UP + 1.2 * LEFT)
        self.play(Write(random_text_6))
        # random_text_6 = currentTextPositionText("]", 0.4, WHITE, 0.5 * UP + 1.2 * LEFT)
        
        self.play(FadeOut(black_disappear_text))
        black_disappear_text = currentTextPositionText("Using append() will increase the length of the list by 1.", 
        	                                           0.5, WHITE, 3.18 * UP + 1.2 * LEFT)

        second_arrow = CurvedArrow(1.1 * UP + 2.2 * RIGHT,  0.3 * UP + 0.4 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))
        random_text_6.shift(ORIGIN + 1 * RIGHT)


        random_text_7 = currentTextPositionText(", 'apple'", 0.4, WHITE, 0.5 * UP + 0.8 * LEFT)

        random_text_8 = currentTextPositionText(">>>", 0.2, RED, 0.9 * UP + 0.2 * RIGHT)
        random_text_9 = currentTextPositionText(" print(fruits)", 
                                                0.3, WHITE, 0.9 * UP + 1.1 * RIGHT)

        self.play(FadeOut(second_arrow))

        third_arrow = CurvedArrow( 0.3 * UP + 3.5 * LEFT,  0.6 * UP + ORIGIN, angle=1.23)
        self.play(ShowCreation(third_arrow))

        random_text_10 = currentTextPositionText("['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']", 
                                                0.3, WHITE, 0.6 * UP + 2.5 * RIGHT)


        # ---------------------------------------function extend() start-------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(framebox1), FadeOut(first_arrow), FadeOut(random_text_5), 
        	      FadeOut(random_text_6), FadeOut(random_text_7), FadeOut(third_arrow), FadeOut(black_disappear_text))
        top_disapper_text = currentTextPositionTex(r"\\list.extend(): Adds multiple elements to a list.",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)

        black_disappear_text = currentTextPositionText("The extend() method increases the length of the list by the number of elements", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        random_text_11 = currentTextPositionText(">>>", 0.2, RED, 0.3 * UP + 0.2 * RIGHT)
        random_text_12 = currentTextPositionText(" fruits.extend(['grape', 'apple'])", 
                                                0.3, WHITE, 0.3 * UP + 2 * RIGHT)

        framebox1 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )

        first_arrow = Arrow(2.15 * UP + 0.2 * LEFT,  0.7 * UP + 4.6 * LEFT)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("['orange', 'apple', 'pear', 'banana', 'kiwi'", 0.3, WHITE, 0.5 * UP + 4.5 * LEFT)
        random_text_6 = Text("]",color=WHITE).scale(0.3)
        random_text_6.shift(0.5 * UP + 2.3 * LEFT)
        self.play(Write(random_text_6))
        # random_text_6 = currentTextPositionText("]", 0.4, WHITE, 0.5 * UP + 1.2 * LEFT)
        

        second_arrow = CurvedArrow(0.2 * UP + 2.2 * RIGHT,  0.3 * UP + 1.5 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))
        random_text_6.shift(ORIGIN + 1.6 * RIGHT)

        random_text_7 = currentTextPositionText(" , 'grape', 'apple'", 0.3, WHITE, 0.5 * UP + 1.6 * LEFT)

        self.play(FadeOut(black_disappear_text))
        black_disappear_text = currentTextPositionText("to add multiple elements to the list, you can use extend() method", 
                                                       0.4, WHITE, 3.18 * UP + 0.7 * LEFT)
        

        random_text_13 = currentTextPositionText(">>>", 0.2, RED, ORIGIN + 0.2 * RIGHT)
        random_text_14 = currentTextPositionText(" print(fruits)", 
                                                0.3, WHITE, ORIGIN + 1.1 * RIGHT)

        self.play(FadeOut(second_arrow))

        third_arrow = CurvedArrow( 0.3 * UP + 3.5 * LEFT,  0.3 * DOWN  + ORIGIN, angle=1.23)
        self.play(ShowCreation(third_arrow))

        random_text_15 = currentTextPositionText("['orange', 'apple', 'pear', 'banana', 'kiwi', 'grape', 'apple']", 
                                                0.3, WHITE, 0.3 * DOWN + 2.9 * RIGHT)


        # ---------------------------------------function insert() start-------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(framebox1), FadeOut(first_arrow), FadeOut(random_text_5), 
        	      FadeOut(random_text_6), FadeOut(random_text_7), FadeOut(third_arrow), FadeOut(black_disappear_text))
        top_disapper_text = currentTextPositionTex(r"\\list.insert(): Insert an item at a given position.",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)


        black_disappear_text = currentTextPositionText("The first argument is the '2' index of the element before which to insert", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        currentTextPositionText('0',0.3,WHITE, 2.1 * UP + 2.8 * LEFT)
        currentTextPositionText('1',0.3,WHITE, 2.1 * UP + 1.2 * LEFT)
        currentTextPositionText('2',0.3,WHITE, 2.1 * UP + 0.1 * LEFT)
        currentTextPositionText('3',0.3,WHITE, 2.1 * UP + 1.4 * RIGHT)
        currentTextPositionText('4',0.3,WHITE, 2.1 * UP + 2.8 * RIGHT)


        random_text_16 = currentTextPositionText(">>>", 0.2, RED, 0.6 * DOWN + 0.2 * RIGHT)
        random_text_17 = currentTextPositionText(" fruits.insert(2, 'guava')", 
                                                0.3, WHITE, 0.6 * DOWN + 1.7 * RIGHT)

        self.play(FadeOut(black_disappear_text))
        black_disappear_text = currentTextPositionText("The second argument is the 'guava' item , which insert into fruits list", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        framebox1 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )

        first_arrow = Arrow(2.15 * UP + 0.2 * LEFT,  0.7 * UP + 4.6 * LEFT)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("['orange', 'apple', ", 0.3, WHITE, 0.5 * UP + 5.7 * LEFT)
        random_text_6 = Text("'pear', 'banana', 'kiwi']",color=WHITE).scale(0.3)
        random_text_6.shift(0.5 * UP + 3.5 * LEFT)
        self.play(Write(random_text_6))
        

        second_arrow = CurvedArrow(0.7 * DOWN + 2.4 * RIGHT,  0.3 * UP + 4.2 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))

        random_text_6.shift(ORIGIN + 0.8 * RIGHT)

        random_text_18 = currentTextPositionText("'guava', ", 0.3, WHITE, 0.5 * UP + 4.4 * LEFT)

        index_1 = currentTextPositionText('0',0.2,WHITE, 0.3 * UP + 6.1 * LEFT)
        index_2 = currentTextPositionText('1',0.2,WHITE, 0.3 * UP + 5.2 * LEFT)
        index_3 = currentTextPositionText('2',0.2,WHITE, 0.3 * UP + 4.4 * LEFT)
        index_4 = currentTextPositionText('3',0.2,WHITE, 0.3 * UP + 3.6 * LEFT)
        index_5 = currentTextPositionText('4',0.2,WHITE, 0.3 * UP + 2.7 * LEFT)
        index_6 = currentTextPositionText('5',0.2,WHITE, 0.3 * UP + 1.9 * LEFT)

        random_text_19 = currentTextPositionText(">>>", 0.2, RED, 0.9 * DOWN + 0.2 * RIGHT)
        random_text_20 = currentTextPositionText(" print(fruits)", 
                                                0.3, WHITE, 0.9 * DOWN + 1.1 * RIGHT)

        self.play(FadeOut(second_arrow))
        third_arrow = CurvedArrow( 0.3 * UP + 3.5 * LEFT,  1.2 * DOWN  + ORIGIN, angle=1.23)
        self.play(ShowCreation(third_arrow))


        random_text_21 = currentTextPositionText("['orange', 'apple', 'guava', 'pear', 'banana', 'kiwi', 'grape', 'apple']", 
        	                                     0.3, WHITE, 1.2 * DOWN + 3.4 * RIGHT)

        # ---------------------------------------function remove() start-------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(framebox1), FadeOut(first_arrow), FadeOut(random_text_5), 
        	      FadeOut(random_text_6), FadeOut(third_arrow),FadeOut(random_text_18), FadeOut(index_1), FadeOut(index_2), FadeOut(index_3), 
        	      FadeOut(index_4), FadeOut(index_5), FadeOut(index_6), FadeOut(black_disappear_text))

        top_disapper_text = currentTextPositionTex(r"\\list.remove(): Remove the item from the list",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)


        black_disappear_text = currentTextPositionText("Remove the first item from the list whose value is equal to 'banana'", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        random_text_22 = currentTextPositionText(">>>", 0.2, RED, 1.5 * DOWN + 0.2 * RIGHT)
        random_text_23 = currentTextPositionText("fruits.remove('banana')", 
                                                0.3, WHITE, 1.5 * DOWN + 1.7 * RIGHT)

        self.play(FadeOut(black_disappear_text))
        black_disappear_text = currentTextPositionText("It raises a ValueError if there is no such item.                  ", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        framebox1 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )

        first_arrow = Arrow(2.15 * UP + 0.2 * LEFT,  0.7 * UP + 4.6 * LEFT)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("['orange', 'apple', 'pear',  ", 0.3, WHITE, 0.5 * UP + 5.4 * LEFT)
        random_text_6 = currentTextPositionText(" 'banana', ", 0.3, WHITE, 0.5 * UP + 3.7 * LEFT)
        random_text_7 = currentTextPositionText(" 'kiwi']", 0.3, WHITE, 0.5 * UP + 2.9 * LEFT)

        second_arrow = CurvedArrow(1.6 * DOWN + 2.4 * RIGHT,  0.3 * UP + 3.9 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))

        self.play(FadeOut(random_text_6))
        random_text_7.shift( ORIGIN - 0.9 * RIGHT)

        index_1 = currentTextPositionText('0',0.3,WHITE, 0.3 * UP + 6.2 * LEFT)
        index_2 = currentTextPositionText('1',0.3,WHITE, 0.3 * UP + 5.3 * LEFT)
        index_3 = currentTextPositionText('2',0.3,WHITE, 0.3 * UP + 4.5 * LEFT)
        index_4 = currentTextPositionText('3',0.3,WHITE, 0.3 * UP + 3.8 * LEFT)

        random_text_24 = currentTextPositionText(">>>", 0.2, RED, 1.8 * DOWN + 0.2 * RIGHT)
        random_text_25 = currentTextPositionText(" print(fruits)", 
                                                0.3, WHITE, 1.8 * DOWN + 1.1 * RIGHT)

        self.play(FadeOut(second_arrow))

        third_arrow = CurvedArrow( 0.3 * UP + 4.6 * LEFT,  2.1 * DOWN + ORIGIN, angle=1.23)
        self.play(ShowCreation(third_arrow))

        random_text_26 = currentTextPositionText("['orange', 'apple', 'pear', 'kiwi']", 
                                                0.3, WHITE, 2.1 * DOWN + 1.7 * RIGHT)


        # ---------------------------------------function pop() start-------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(framebox1), FadeOut(first_arrow), FadeOut(random_text_5), 
        	      FadeOut(random_text_6), FadeOut(third_arrow),FadeOut(random_text_7), FadeOut(random_text_18), FadeOut(index_1), FadeOut(index_2), FadeOut(index_3), 
        	      FadeOut(index_4),FadeOut(black_disappear_text))


        top_disapper_text = currentTextPositionTex(r"\\list.pop(): Remove the list element at the given position",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)

        
        black_disappear_text = currentTextPositionText("fruits.pop() removes and returns the last item in the list.", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        random_text_27 = currentTextPositionText(">>>", 0.2, RED, 2.4 * DOWN + 0.2 * RIGHT)
        random_text_28 = currentTextPositionText("fruits.pop()", 
                                                0.3, WHITE, 2.4 * DOWN + 1 * RIGHT)


        framebox1 = SurroundingRectangle(text_list[10], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        curved_first = CurvedArrow(2.15 * UP + 2.4 * RIGHT,  2.7 * DOWN + ORIGIN, angle=2.5)
        self.play(ShowCreation(curved_first))
        random_text_29 = currentTextPositionText("'kiwi'", 
                                                0.3, WHITE, 2.7 * DOWN + 0.3 * RIGHT)

        random_text_30 = currentTextPositionText(">>>", 0.2, RED, 3 * DOWN + 0.2 * RIGHT)
        random_text_31 = currentTextPositionText("print(fruits)", 
                                                0.3, WHITE, 3 * DOWN + 1 * RIGHT)

        self.play(FadeOut(framebox1))


        framebox2 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox2),
        )
        first_arrow = Arrow(2.15 * UP + 0.2 * LEFT,  0.7 * UP + 4.6 * LEFT)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("['orange', 'apple', 'pear', 'banana'", 0.3, WHITE, 0.5 * UP + 5 * LEFT)
        random_text_6 = currentTextPositionText(" , 'kiwi' ", 0.3, WHITE, 0.5 * UP + 3 * LEFT)
        random_text_7 = currentTextPositionText(" ]", 0.3, WHITE, 0.5 * UP + 2.6 * LEFT)


        self.play(FadeOut(curved_first))
        second_arrow = CurvedArrow(2.4 * DOWN + ORIGIN,  0.3 * UP + 3 * LEFT, angle=-1.23)
        self.play(ShowCreation(second_arrow))

        self.play(FadeOut(random_text_6))
        random_text_7.shift( ORIGIN + 0.6 * LEFT)

        index_1 = currentTextPositionText('0',0.3,WHITE, 0.3 * UP + 6.2 * LEFT)
        index_2 = currentTextPositionText('1',0.3,WHITE, 0.3 * UP + 5.3 * LEFT)
        index_3 = currentTextPositionText('2',0.3,WHITE, 0.3 * UP + 4.5 * LEFT)
        index_4 = currentTextPositionText('3',0.3,WHITE, 0.3 * UP + 3.8 * LEFT)

        self.play(FadeOut(second_arrow))
        third_arrow = CurvedArrow( 0.3 * UP + 4.6 * LEFT,  3.3 * DOWN + ORIGIN, angle=1.23)
        self.play(ShowCreation(third_arrow))

        random_text_32 = currentTextPositionText("['orange', 'apple', 'pear', 'banana']", 
                                                0.3, WHITE, 3.3 * DOWN + 1.9 * RIGHT)

        # ---------------------------------------function clear() start-------------------------------------------------------

        self.play(FadeOut(top_disapper_text), FadeOut(framebox2), FadeOut(first_arrow), FadeOut(random_text_5), 
        	      FadeOut(random_text_6), FadeOut(third_arrow),FadeOut(random_text_7), 
        	      FadeOut(index_1), FadeOut(index_2), FadeOut(index_3), FadeOut(index_4), FadeOut(black_disappear_text))

        top_disapper_text = currentTextPositionTex(r"\\list.clear(): Remove all items from the list.",
                      0.8, YELLOW, 3.7 * UP + 1 * LEFT)

        black_disappear_text = currentTextPositionText(" clear() method is equivalent to del list[:].", 
                                                        0.4, WHITE, 3.18 * UP + 0.4 * LEFT)

        random_text_4 = currentTextPositionText(">>>", 0.2, RED, 1.5 * UP + 6.6 * LEFT)
        random_text_3 = currentTextPositionText("fruits.clear()", 
                                                0.3, WHITE, 1.5 * UP + 5.6 * LEFT)

        framebox2 = SurroundingRectangle(text_list[2:11], buff = .1)
        self.play(
            ShowCreation(framebox2),
        )
        first_arrow = CurvedArrow(2.15 * UP + 0.2 * LEFT,  0.3 * UP + 4.6 * LEFT, angle=-1.5)
        self.play(ShowCreation(first_arrow))
        random_text_5 = currentTextPositionText("[", 0.3, WHITE, 0.5 * UP + 6.4 * LEFT)
        random_text_6 = currentTextPositionText(" 'orange', 'apple', 'pear', 'banana', 'kiwi' ", 0.3, WHITE, 0.5 * UP + 4.3 * LEFT)
        random_text_7 = currentTextPositionText(" ]", 0.3, WHITE, 0.5 * UP + 2.1 * LEFT)

        second_arrow = Arrow(1.5 * UP + 5.8 * LEFT,  0.6 * UP + 4 * LEFT)
        self.play(ShowCreation(second_arrow))

        self.play(FadeOut(random_text_6), FadeOut(first_arrow))
        random_text_7.shift( ORIGIN - 4.2 * RIGHT)

        self.play(FadeOut(second_arrow))
        third_arrow = Arrow( 0.4 * UP + 6.3 * LEFT,  1.3 * UP + 6.6 * LEFT)
        self.play(ShowCreation(third_arrow))

        random_text_10 = currentTextPositionText("[ ]", 
                                                0.3, WHITE, 1.2 * UP + 6.6 * LEFT)




        self.wait(3)
