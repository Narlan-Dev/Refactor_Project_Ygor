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
        background-color: #00bfff96;
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
        background-color: #333;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(105, 105, 105, 0.397);
    }
"""

button_style = """
    QPushButton {
        background-color: #00bfff;
        color: white;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #00bfff96;
    }
"""

list_widget_style = """
    QListWidget {
        background-color: transparent;  /* Match the sidebar's color */
        color: white;
        padding: 0px;  /* Remove padding */
        border: none;  /* Remove border */
        font-size: 18px;
    }
    QListWidget::item {
        padding: 15px;
    }
    QListWidget::item:selected {
        background-color: #00bfff;
        color: white;
    }
"""
