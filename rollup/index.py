from manim import *


def find_middle_anchor_option1(left_anchor, top_anchor):
    return [top_anchor[0], left_anchor[1], 0]


LINE_STROKE_WIDTH = 2.5


class Diagram(Scene):
    def construct(self):
        # Create 3 'tx' boxes
        boxes = VGroup(
            *[Square(side_length=0.7).round_corners(0.1).set_stroke(GREEN).set_fill(GREEN, opacity=0.3) for _ in range(3)])
        for i in range(3):
            boxes[i].add(Text('tx').scale(0.4))  # Increase text size
        boxes.arrange(DOWN, buff=0.3)
        boxes.to_edge(UL)  # Move to top side

        # Animate 'tx' boxes
        self.play(DrawBorderThenFill(boxes))

        sequencerText = Text('Sequencer').scale(0.4)
        sequencerText.next_to(boxes[0], RIGHT, buff=2)
        # sequencerText.to_edge(UP, buff=1)
        # Create 'Sequencer' box
        sequencer_box = SurroundingRectangle(
            sequencerText, color=GREEN, buff=0.2).round_corners(0.1).set_fill(GREEN, opacity=0.3)

        firstArrow = Arrow(boxes[0].get_right(),
                           sequencer_box.get_left(), buff=0,  stroke_width=LINE_STROKE_WIDTH)
        secondArrow = Elbow(color=WHITE).set_stroke(width=LINE_STROKE_WIDTH)
        secondArrow.set_points_as_corners(
            [boxes[1].get_right(), find_middle_anchor_option1(boxes[1].get_right(), firstArrow.get_center()), firstArrow.get_center()])
        thirdArrow = Elbow(color=WHITE).set_stroke(width=LINE_STROKE_WIDTH)
        thirdArrow.set_points_as_corners(
            [boxes[2].get_right(), find_middle_anchor_option1(boxes[2].get_right(), firstArrow.get_center()), firstArrow.get_center()])

        # Animate arrows and then 'Sequencer' box
        self.play(GrowArrow(firstArrow), DrawBorderThenFill(
            secondArrow), DrawBorderThenFill(thirdArrow))

        # Create arrows from 'tx' boxes to 'Sequencer' box

        self.play(AddTextLetterByLetter(sequencerText),
                  DrawBorderThenFill(sequencer_box))

        # Create 5 'tx' boxes
        tx_boxes = VGroup(
            *[Square().set_stroke(GREEN).set_height(0.5).set_width(0.5).set_fill(GREEN, opacity=0.5) for _ in range(5)])
        for i in range(5):
            tx_boxes[i].add(Text('tx').scale(0.4))  # Increase text size
        tx_boxes.arrange(RIGHT, buff=0)
        tx_boxes[0].round_corners([0.1, 0.1, 0, 0])
        tx_boxes[4].round_corners([0, 0, 0.1, 0.1])
        # Position 'tx' boxes to the right of 'Sequencer' box
        tx_boxes.next_to(sequencer_box, RIGHT, buff=4)

        # Create arrow from 'Sequencer' box to 'tx' boxes
        arrow_to_tx = Arrow(sequencer_box.get_right(),
                            tx_boxes[0].get_left(), buff=0, stroke_width=LINE_STROKE_WIDTH)

        self.play(GrowArrow(arrow_to_tx))
        sequencedTxText = Text('Sequenced tx').scale(0.4)
        sequencedTxText.next_to(tx_boxes, UP, buff=0.1)
        # Animate 'tx' boxes and arrow
        self.play(AddTextLetterByLetter(sequencedTxText),
                  DrawBorderThenFill(tx_boxes))

        stateTransitionFunctionText = Text(
            'State\nTransition\nFunction', should_center=True).scale(0.4)
        stateTransitionFunctionText.next_to(tx_boxes[4], DOWN, buff=1)
        # Create 'State Transition Function' box
        state_transition_box = SurroundingRectangle(
            stateTransitionFunctionText, buff=0.2).round_corners(0.1).set_stroke(GREEN).set_fill(GREEN, opacity=0.3)

        txsToStateTransitionArrow = Arrow(tx_boxes[4].get_bottom(),
                                          state_transition_box.get_top(), buff=0, stroke_width=LINE_STROKE_WIDTH)
        self.play(GrowArrow(txsToStateTransitionArrow))
        self.play(AddTextLetterByLetter(stateTransitionFunctionText),
                  DrawBorderThenFill(state_transition_box))

        stateText = Text(
            'State', should_center=True).scale(0.4)
        stateText.next_to(
            state_transition_box, RIGHT, buff=1)
        stateBox = SurroundingRectangle(
            stateText, buff=0.2).round_corners(0.1).set_stroke(GREEN).set_fill(GREEN, opacity=0.3)

        # stateBottomArrow = Elbow(color=WHITE)
        # stateBottomArrow.set_points_as_corners(
        #     [find_middle_anchor_option1(state_transition_box.get_bottom(), state_transition_box.get_right()), find_middle_anchor_option1(state_transition_box.get_bottom(), stateBox.get_bottom()), stateBox.get_bottom()])
        stateBottomArrow = CurvedArrow(find_middle_anchor_option1(state_transition_box.get_bottom(), state_transition_box.get_right(
        )),  stateBox.get_bottom(), angle=PI/3)
        stateTopArrow = CurvedArrow(stateBox.get_top(), find_middle_anchor_option1(state_transition_box.get_top(), state_transition_box.get_right(
        )), angle=PI/3)
        # stateBottomArrow1 = Line(find_middle_anchor_option1(state_transition_box.get_bottom(), state_transition_box.get_right(
        # )), find_middle_anchor_option1(state_transition_box.get_bottom(), stateBox.get_bottom()), buff=0)
        # stateBottomArrow2 = Arrow(find_middle_anchor_option1(
        #     state_transition_box.get_bottom(), stateBox.get_bottom()), stateBox.get_bottom(), buff=0, stroke_width=LINE_STROKE_WIDTH)

        # Create 'State' box

        # Create 3 'L2 block' boxes
        l2_boxes = VGroup(
            *[Square().set_stroke(GREEN).set_height(0.8).set_width(0.8).set_fill(GREEN, opacity=0.3) for _ in range(3)])
        for i in range(3):
            l2_boxes[i].add(Text('L2\nblock').scale(0.4))  # Increase text size
        l2_boxes.arrange(DOWN, buff=0)
        l2_boxes[0].round_corners([0.1, 0, 0, 0.1])
        l2_boxes[2].round_corners([0, 0.1, 0.1, 0])

        # Position 'L2 block' boxes below 'State Transition Function' box
        # Moved l2_boxes a little bit down
        l2_boxes.next_to(state_transition_box, DOWN, buff=1)

        # Create arrows from 'State Transition Function' box to 'L2 block' boxes
        # Attached arrows_to_l2 to the first box of l2_boxes
        stateToL2BoxArrow2 = Arrow(
            state_transition_box.get_bottom(), l2_boxes[0].get_top(), buff=0, stroke_width=LINE_STROKE_WIDTH)
        # Animate 'L2 block' boxes and arrows

        # self.play(DrawBorderThenFill(stateBottomArrow))

        self.play(DrawBorderThenFill(stateBottomArrow),
                  GrowArrow(stateToL2BoxArrow2))
        self.play(AddTextLetterByLetter(stateText),
                  DrawBorderThenFill(stateBox), DrawBorderThenFill(l2_boxes))

        sequencerText = Text('Sequencer feed\n(soft guarantee)').scale(0.4)

        arrow_to_txCenterPoint = arrow_to_tx.get_center()
        sequencerArrowStartPoint = [arrow_to_txCenterPoint[0] - (arrow_to_txCenterPoint[0] - arrow_to_tx.get_left()[
            0]) / 2, arrow_to_txCenterPoint[1], arrow_to_txCenterPoint[2]]
        sequencerText.shift(
            [sequencerArrowStartPoint[0], sequencerArrowStartPoint[1] - 1.5, sequencerArrowStartPoint[2]])
        arrowToSequencerText = Arrow(
            sequencerArrowStartPoint, sequencerText.get_top(), buff=0, stroke_width=LINE_STROKE_WIDTH)

        self.play(DrawBorderThenFill(stateTopArrow),
                  GrowArrow(arrowToSequencerText))
        self.play(AddTextLetterByLetter(sequencerText))
        batchAndCompressText = Text('Batch and\ncompress').scale(0.4)
        batchAndCompressTextArrowStartPoint = [arrow_to_txCenterPoint[0] + (arrow_to_txCenterPoint[0] - arrow_to_tx.get_left()[
            0]) / 2, arrow_to_txCenterPoint[1], arrow_to_txCenterPoint[2]]
        batchAndCompressText.shift(
            [batchAndCompressTextArrowStartPoint[0], batchAndCompressTextArrowStartPoint[1] - 2, batchAndCompressTextArrowStartPoint[2]])
        batchAndCompressbox = SurroundingRectangle(
            batchAndCompressText, buff=0.2).round_corners(0.1).set_stroke(GREEN).set_fill(GREEN, opacity=0.3)
        arrowToSequencerText = Arrow(
            batchAndCompressTextArrowStartPoint, batchAndCompressbox.get_top(), buff=0, stroke_width=LINE_STROKE_WIDTH)

        self.play(GrowArrow(arrowToSequencerText))
        self.play(AddTextLetterByLetter(batchAndCompressText),
                  DrawBorderThenFill(batchAndCompressbox))

        l1Rectangle = Rectangle(width=4, height=0.7, color=GREEN).round_corners(0.1).set_fill(GREEN, opacity=0.3).add(
            Text('L1 chain').scale(0.4))
        l1Rectangle.next_to(l2_boxes[2], LEFT, buff=2.6)

        arrowToSequencerText = Arrow(
            batchAndCompressbox.get_bottom(), [batchAndCompressbox.get_bottom()[0], l1Rectangle.get_top()[1], 0], buff=0, stroke_width=LINE_STROKE_WIDTH)
        self.play(
            GrowArrow(arrowToSequencerText))
        self.play(
            DrawBorderThenFill(l1Rectangle))
        l1GasCostText = Text('L1 gas cost\n(paid by sequencer)').scale(0.4)
        l1GasCostText.next_to(l1Rectangle, UP, buff=0.1)
        self.play(
            AddTextLetterByLetter(l1GasCostText))
        self.wait(10)
