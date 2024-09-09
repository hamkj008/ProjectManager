import pytest
from unittest.mock import patch, MagicMock, Mock
from Views.AboutView import AboutView


# ========================================================================================

@pytest.fixture
def aboutView(viewControllerMock):
    
    qssControllerMock = MagicMock()
    qssControllerMock.getStandardStyle.return_value = "background-color: green;"
    viewControllerMock.qssController = qssControllerMock
    
    aboutView = AboutView(viewControllerMock, "1")
    aboutView.setStyleSheet = MagicMock()
    
    return aboutView

# ========================================================================================

def test_init(setupApp, aboutView, viewControllerMock):
    
    # Check constructor assignment
    assert aboutView.viewController == viewControllerMock
    
    # Check Style
    assert aboutView.viewController.qssController.getStandardStyle() == "background-color: green;"
        
    aboutView.setStyle()

    aboutView.setStyleSheet.assert_called_once()
    aboutView.setStyleSheet.assert_called_with("background-color: green;")
    
    # Check version number assigned
    versionText = aboutView.window.VersionDataLabel.text()
    assert versionText == "1"
    
# ========================================================================================
    
def test_signals(setupApp, aboutView):
    
    closeMock = Mock()

    aboutView.window.CloseBtn.clicked.connect(closeMock)
    
    # Simulate emission
    aboutView.window.CloseBtn.click()
    
    closeMock.assert_called_once()


# ========================================================================================
    

