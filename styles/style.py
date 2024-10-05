main_window_style = """
    QWidget {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
    }
    QLabel {
        color: rgba(255, 255, 255, 0.7);
        font-size: 14px;
    }
    QLineEdit {
        background-color: #333;
        color: white;
        border: 1px solid rgba(105, 105, 105, 0.397);
        padding: 10px;
        border-radius: 10px;
    }
    QPushButton {
        background-color: #00bfff;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #1c86e2;
    }
"""

card_style = """
    QFrame {
        background-color: #1a1a1a;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
"""

sidebar_style = """
    QWidget {
        background-color: #1a1a1a;
    }
"""

label_style = """
    QLabel {
        color: white;
        font-size: 18px;
        background-color: #444;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
    }
"""

button_style =  """
    QPushButton {
        background-color: #1e90ff;
        color: white;
        padding: 12px 24px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: bold;
        min-width: 120px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    QPushButton:hover {
        background-color: #1c86e2;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }
    QPushButton:pressed {
        background-color: #1b75d1;
    }
"""

list_widget_style = """
    QListWidget {
        background-color: transparent;
        color: white;
        padding: 0px;
        border: none;
        font-size: 18px;
    }

    QListWidget::item {
        padding: 15px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-left: 5px;
    }

    QListWidget::item:selected {
        background-color: #1c86e2;
        color: white;
        border-radius: 8px;
        outline: none;
    }

    QListWidget::item:focus {
        outline: none;
    }

    QListWidget::item:hover {
        background-color: rgba(28, 134, 226, 0.5);
        color: white;
        transition: background-color 0.3s ease;
    }

    QListWidget::item:selected:hover {
        background-color: #1a75d1;
    }
"""
