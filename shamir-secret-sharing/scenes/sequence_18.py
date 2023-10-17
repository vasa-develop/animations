from manim import *

class Sequence18(Scene):
    
    def construct(self):

        question_1_a_text = MathTex(r"\textbf{1. Does this new form of arithmetic work for any}", color=RED).scale(1).to_edge(LEFT).shift(1.5*UP)
        question_1_b_text = MathTex(r"\textbf{modulo value?}", color=RED).scale(1).next_to(question_1_a_text, DOWN).to_edge(LEFT)
        question_1_group = VGroup(question_1_a_text, question_1_b_text)
        self.play(
            Write(question_1_group)
        )
        self.add(question_1_group)
        self.wait(0.5)

        question_2_a_text = MathTex(r"\textbf{2. What are finite fields and how modular arithmetic}", color=RED).scale(1).to_edge(LEFT).shift(DOWN)
        question_2_b_text = MathTex(r"\textbf{is related to it?}", color=RED).scale(1).next_to(question_2_a_text, DOWN).to_edge(LEFT)
        question_2_group = VGroup(question_2_a_text, question_2_b_text)
        self.play(
            Write(question_2_group)
        )
        self.add(question_2_group)
        self.wait(0.5)

        self.play(
            Indicate(question_2_group, scale_factor=1.01)
        )
        self.wait(0.5)

        question_group = VGroup(question_1_group, question_2_group)

        finite_field_text = MathTex(r"\textbf{Finite Fields}", color=BLUE).scale(2)

        self.play(
            TransformMatchingShapes(question_group, finite_field_text)
        )
        self.add(finite_field_text)
        self.remove(question_group)
        self.wait(0.5)

        rules_of_a_finite_field_text = MathTex(r"\textbf{Rules of a Finite Field}", color=BLUE).scale(1.5).to_edge(UP).shift(0.5*DOWN)

        rule_1_a_text = MathTex(r"\textbf{1. There is a specified number of elements.}", color=WHITE).scale(1).next_to(rules_of_a_finite_field_text, DOWN, buff=1).to_edge(LEFT)
        rule_1 = VGroup(rule_1_a_text)

        rule_2_a_text = MathTex(r"\textbf{2. Addition, subtraction, multiplication, and division}", color=WHITE).scale(1).next_to(rule_1, DOWN, buff=0.6).to_edge(LEFT)
        rule_2_b_text = MathTex(r"\textbf{operations (except 0) are closed within the field.}", color=WHITE).scale(1).next_to(rule_2_a_text, DOWN).to_edge(LEFT)
        rule_2 = VGroup(rule_2_a_text, rule_2_b_text)

        rule_3_a_text = MathTex(r"\textbf{3. There are unique additive and multiplicative}", color=WHITE).scale(1).next_to(rule_2, DOWN, buff=0.6).to_edge(LEFT)
        rule_3_b_text = MathTex(r"\textbf{identities.}", color=WHITE).scale(1).next_to(rule_3_a_text, DOWN).to_edge(LEFT)
        rule_3 = VGroup(rule_3_a_text, rule_3_b_text)

        self.play(
            TransformMatchingShapes(finite_field_text, rules_of_a_finite_field_text),
            Write(rule_1),
            Write(rule_2),
            Write(rule_3),
        )
        self.wait(0.5)
        
        rules_group = VGroup(rule_1, rule_2, rule_3)

        self.play(Indicate(rule_1, scale_factor=1.01, color=RED))
        self.wait(0.5)


        modulus_5_text = MathTex(r"\textbf{Modulus 5}", color=BLUE).scale(1.5).next_to(rules_of_a_finite_field_text, DOWN, buff=1)
        modulus_5_elements = MathTex(r"\textbf{\{0, 1, 2, 3, 4\}}", color=WHITE).scale(1).next_to(modulus_5_text, DOWN, buff=0.5)

        modulus_7_text = MathTex(r"\textbf{Modulus 7}", color=BLUE).scale(1.5).next_to(modulus_5_elements, DOWN, buff=1)
        modulus_7_elements = MathTex(r"\textbf{\{0, 1, 2, 3, 4, 5, 6\}}", color=WHITE).scale(1).next_to(modulus_7_text, DOWN, buff=0.5)


        rule_1_details = VGroup(
            modulus_5_text,
            modulus_5_elements,
            modulus_7_text,
            modulus_7_elements
        )

        self.play(
            rules_group.animate.set_opacity(0),
            FadeIn(rule_1_details)
        )
        self.add(rule_1_details)
        self.wait(0.5)

        self.play(
            Indicate(modulus_5_elements, scale_factor=1.01, color=YELLOW),
        )
        self.wait(0.5)
        
        self.play(
            Indicate(modulus_7_elements, scale_factor=1.01, color=YELLOW),
        )
        self.wait(0.5)

        self.play(
            rules_group.animate.set_opacity(1),
            FadeOut(rule_1_details)
        )
        self.wait(0.5)

        
        
        
        self.play(
            Indicate(rule_2, scale_factor=1.01, color=RED)
        )
        self.wait(0.5)
        
        modulus_5_text = MathTex(r"\textbf{Modulus 5}", color=BLUE).scale(1).next_to(rules_of_a_finite_field_text, DOWN, buff=1)
        modulus_5_elements = MathTex(r"\textbf{\{0, 1, 2, 3, 4\}}", color=WHITE).scale(1)
        operations = MathTex(r"(+,", r"-,", r"\times,", r"\div)", color=WHITE).scale(1)

        input_1_elements = modulus_5_elements.copy()
        input_operations = operations.copy().next_to(input_1_elements, DOWN)
        input_2_elements = modulus_5_elements.copy().next_to(input_operations, DOWN)
        output_elements = modulus_5_elements.copy().next_to(input_2_elements, DOWN, buff=1)
        arrow = Arrow(start=input_2_elements.get_bottom(), end=output_elements.get_top(), color=WHITE)

        modulus_5_closed_operations = VGroup(
            input_1_elements,
            input_operations,
            input_2_elements,
            output_elements,
            arrow
        ).next_to(modulus_5_text, DOWN, buff=0.6)
        
        rule_2_details = VGroup(
            modulus_5_text,
            modulus_5_closed_operations
        )

        self.play(
            rules_group.animate.set_opacity(0),
            FadeIn(rule_2_details)
        )
        self.wait(0.5)







        def mul_mod_6(x, y):
            return str((x * y) % 6)


        table_6 = Table(
            [[mul_mod_6(i, j) for j in range(6)] for i in range(6)],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}")],
            col_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}"), MathTex(r"\textbf{5}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        table_6.add_highlighted_cell((1,2), color=PURPLE)
        table_6.add_highlighted_cell((1,3), color=PURPLE)
        table_6.add_highlighted_cell((1,4), color=PURPLE)
        table_6.add_highlighted_cell((1,5), color=PURPLE)
        table_6.add_highlighted_cell((1,6), color=PURPLE)
        table_6.add_highlighted_cell((1,7), color=PURPLE)

        
        table_6.add_highlighted_cell((2,1), color=PURPLE)
        table_6.add_highlighted_cell((3,1), color=PURPLE)
        table_6.add_highlighted_cell((4,1), color=PURPLE)
        table_6.add_highlighted_cell((5,1), color=PURPLE)
        table_6.add_highlighted_cell((6,1), color=PURPLE)
        table_6.add_highlighted_cell((7,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(8):
            for j in range(8):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_6(i-2, j-2) == "1":
                        if i != 1 and j != 1:
                            table_6.add_highlighted_cell((i,j), color=GREEN)



        table_6.next_to(rules_of_a_finite_field_text, DOWN, buff=0.5)
        modulus_6_issue_1 = MathTex(r"\textbf{Multiplicative inverse (division) for 2, 3, and 4}", color=RED).scale(0.7).next_to(table_6, DOWN, buff=0.3)
        modulus_6_issue_2 = MathTex(r"\textbf{does not exist in Modulus 6, hence it cannot form a finite field}", color=RED).scale(0.7).next_to(modulus_6_issue_1, DOWN, buff=0.3)
        modulus_6_issue = VGroup(
            modulus_6_issue_1,
            modulus_6_issue_2
        )

        modulus_6_table = VGroup(
            table_6,
            modulus_6_issue
        )

        self.play(Transform(rule_2_details, modulus_6_table))
        self.add(modulus_6_table)
        self.remove(rule_2_details)
        self.wait(0.5)




        def mul_mod_5(x, y):
            return str((x * y) % 5)


        table_5 = Table(
            [[mul_mod_5(i, j) for j in range(5)] for i in range(5)],
            include_outer_lines=True,
            row_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}")],
            col_labels=[MathTex(r"\textbf{0}"), MathTex(r"\textbf{1}"), MathTex(r"\textbf{2}"), MathTex(r"\textbf{3}"), MathTex(r"\textbf{4}")],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.5)

        table_5.add_highlighted_cell((1,2), color=PURPLE)
        table_5.add_highlighted_cell((1,3), color=PURPLE)
        table_5.add_highlighted_cell((1,4), color=PURPLE)
        table_5.add_highlighted_cell((1,5), color=PURPLE)
        table_5.add_highlighted_cell((1,6), color=PURPLE)

        
        table_5.add_highlighted_cell((2,1), color=PURPLE)
        table_5.add_highlighted_cell((3,1), color=PURPLE)
        table_5.add_highlighted_cell((4,1), color=PURPLE)
        table_5.add_highlighted_cell((5,1), color=PURPLE)
        table_5.add_highlighted_cell((6,1), color=PURPLE)

        # color any cell with value 1 as green
        for i in range(7):
            for j in range(7):
                if i < 1 or j < 1:
                    continue
                else:
                    if mul_mod_5(i-2, j-2) == "1":
                        if i != 1 and j != 1:
                            table_5.add_highlighted_cell((i,j), color=GREEN)


        table_5.next_to(rules_of_a_finite_field_text, DOWN, buff=0.7)
        modulus_5_fact_1 = MathTex(r"\textbf{Multiplicative inverse (division) for all elements (except 0)}", color=GREEN).scale(0.7).next_to(table_6, DOWN, buff=0.2)
        modulus_5_fact_2 = MathTex(r"\textbf{exists in Modulus 5}", color=GREEN).scale(0.7).next_to(modulus_6_issue_1, DOWN, buff=0.3)
        modulus_5_fact = VGroup(
            modulus_5_fact_1,
            modulus_5_fact_2
        )

        modulus_5_table = VGroup(
            table_5,
            modulus_5_fact
        )

        self.play(Transform(modulus_6_table, modulus_5_table))
        self.add(modulus_5_table)
        self.remove(modulus_6_table)
        self.wait(0.5)


        self.play(
            rules_group.animate.set_opacity(1),
            FadeOut(modulus_5_table)
        )
        self.remove(modulus_5_table)
        self.wait(0.5)

        
        self.play(
            Indicate(rule_3, scale_factor=1.01, color=RED)
        )
        self.wait(0.5)






        addition_property_1 = MathTex(r"(a + b) + c \equiv a + (b + c)", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6)
        addition_property_2 = MathTex(r"a + b \equiv b + a", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(addition_property_1, DOWN, buff=0.2)
        addition_property_3 = MathTex(r"a \; (b + c) \equiv ab + ac", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(addition_property_2, DOWN, buff=0.2)
        addition_property_4 = MathTex(r"a + 0 \equiv a \equiv 0 + a", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(addition_property_3, DOWN, buff=0.2)
        addition_property_5 = MathTex(r"a + (-a) \equiv 0 \equiv (-a) + a", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(addition_property_4, DOWN, buff=0.2)

        addition_properties = VGroup(
            addition_property_1,
            addition_property_2,
            addition_property_3,
            addition_property_4,
            addition_property_5
        )


        multiplication_property_1 = MathTex(r"(ab)c \equiv a(bc)", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6)
        multiplication_property_2 = MathTex(r"ab \equiv ba", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(multiplication_property_1, DOWN, buff=0.2)
        multiplication_property_3 = MathTex(r"(a + b)c \equiv ac + bc", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(multiplication_property_2, DOWN, buff=0.2)
        multiplication_property_4 = MathTex(r"a \cdot 1 \equiv a \equiv 1 \cdot a", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(multiplication_property_3, DOWN, buff=0.2)
        multiplication_property_5 = MathTex(r"aa^{-1} \equiv 1 \equiv a^{-1}a; a \neq 0", r"\textbf{\; mod \;}", r"\textit{p}", color=WHITE).scale(0.6).next_to(multiplication_property_4, DOWN, buff=0.2)

        multiplication_properties = VGroup(
            multiplication_property_1,
            multiplication_property_2,
            multiplication_property_3,
            multiplication_property_4,
            multiplication_property_5
        )

        addition_text = MathTex(r"\textbf{Addition}", color=BLUE).scale(1.2).to_edge(UP).shift(3*LEFT)
        multiplication_text = MathTex(r"\textbf{Multiplication}", color=BLUE).scale(1.2).next_to(addition_text, RIGHT, buff=1)


        table = MobjectTable(
            [
                [addition_text.copy(),multiplication_text.copy()],
                [addition_properties.copy(),multiplication_properties.copy()],
            ]
        ).next_to(rules_of_a_finite_field_text, DOWN, buff=1)
        
        self.play(
            rules_group.animate.set_opacity(0),
            FadeIn(table)
        )

        self.wait(2)

        # fade out everything
        self.play(
            FadeOut(table),
            FadeOut(rules_of_a_finite_field_text)
        )

        recap_text = MathTex("Recap").set_color(WHITE).scale(1.2)
        self.play(Write(recap_text))
        self.add(recap_text)
        self.wait(0.5)
        
        self.play(FadeOut(recap_text))
        self.remove(recap_text)


        self.wait(2)
