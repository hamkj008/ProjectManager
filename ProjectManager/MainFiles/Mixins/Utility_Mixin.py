


class Interaction_Mixin:

    # ========================================================================================

    def hoverEnter(self, labelList, descriptionLabel, text, event):

        descriptionLabel.setText(text)

        for label in labelList:
            label.setStyleSheet(self.viewController.qssController.modeHoverEnterStyle)

    # ========================================================================================

    def hoverLeave(self, labelList, descriptionLabel, event): 

        descriptionLabel.setText("")

        for label in labelList:
            label.setStyleSheet(self.viewController.qssController.modeHoverLeaveStyle)

    # ========================================================================================