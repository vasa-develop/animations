from manim import *

class DiscreteFunction(Scene):
    def construct(self):
        # Define the coordinate pairs
        coordinates = [(1, 0), (2, 1), (3, 4)]
        
        # Create the coordinate pairs as a list of Tex objects
        coordinate_pairs = VGroup(*[
            Tex(f"{y}, x = {x}")
            for x, y in coordinates
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Create a big left curly brace
        left_brace = Brace(coordinate_pairs, direction=LEFT)
        
        # Group the curly brace and coordinate pairs
        function_representation = VGroup(
            left_brace,
            coordinate_pairs
        )
        
        # Display the function representation
        self.play(Write(function_representation))
        
        self.wait()
