from manim import *

class SecretSharing(Scene):
    def construct(self):
        # Introduction
        intro_text = Text("Imagine you have a secret...")
        self.play(Write(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        # Distributing the secret
        distribute_text = Text("You want to distribute it among 'k' friends...")
        self.play(Write(distribute_text))
        self.wait(1)
        self.play(FadeOut(distribute_text))

        # Recovery by n friends
        recovery_text = Text("Such that any 'n' of them can recover it.")
        self.play(Write(recovery_text))
        self.wait(1)
        self.play(FadeOut(recovery_text))

        # Representing the secret on a graph
        graph_text = Text("Represent the secret as a point on a graph...")
        self.play(Write(graph_text))
        graph = NumberPlane()
        secret_point = Dot(point=[0, 3, 0], color=RED)
        secret_label = Text("Secret").next_to(secret_point, UP)
        self.play(Create(graph), GrowFromCenter(secret_point), Write(secret_label))
        self.wait(1)
        self.play(FadeOut(graph_text))

        # Introducing randomness with n-1 points
        randomness_text = Text("Add 'n-1' random points for randomness...")
        self.play(Write(randomness_text))
        random_points = [Dot(point=[i, np.random.randint(1, 5), 0]) for i in range(1, 4)]
        self.play(*[GrowFromCenter(dot) for dot in random_points])
        self.wait(1)
        self.play(FadeOut(randomness_text))

        # Distributing k shares
        shares_text = Text("Choose 'k' shares from this chart...")
        self.play(Write(shares_text))
        shares = VGroup(secret_point, *random_points)
        self.play(shares.animate.shift(LEFT*3))
        self.wait(1)
        self.play(FadeOut(shares_text))

        # Friends coming together
        friends_text = Text("Any 'n' friends can recover the secret curve...")
        self.play(Write(friends_text))
        curve = VMobject()
        curve.set_points_as_corners([dot.get_center() for dot in shares])
        self.play(Create(curve))
        self.wait(1)
        self.play(FadeOut(friends_text))

        # Recovering the original secret
        recover_text = Text("And use it to recover the original secret at f(0).")
        self.play(Write(recover_text))
        self.wait(2)
        self.play(FadeOut(recover_text), FadeOut(curve), FadeOut(graph), FadeOut(shares))

