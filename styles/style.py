card_style = """
    QWidget {
        background-color: #2C3E99;
        border-radius: 20px;
    }
    QLabel {
        font-family: 'Inter';
        font-size: 20px;
        color: #f2f1f1;
    }
    QLineEdit {
        background-color: #f2f1f1;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid lightgray;
        font-size: 16px;
        font-family: 'Inter';
        qproperty-alignment: AlignCenter;
    }
    QPushButton {
        background-color: #f2f1f1;
        border-radius: 15px;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
        font-family: 'Inter';
        width: 150px;
        color: #7D7D7D;
    }
    QPushButton:hover {
        background-color: lightgray;
    }
"""

title_layout_style= """
    QLabel {
        font-family: 'Inter';
        font-size: 30px;
        color: #f2f1f1;
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

arrow_button_style = """
    QPushButton {
        background-color: #1e90ff;
        color: white;
        padding: 12px 24px;
        border-radius: 10px;
        font-size: 24px;
        font-weight: bold;
        min-width: 50px;
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

main_window_style = """
    QMainWindow, QWidget {
        background-color: #2A2E83;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    QPushButton {
        background-color: transparent;
        color: white;
        text-align: left;
        padding: 15px 20px;
        border: none;
        font-size: 16px;
        font-weight: 500;
    }
    QPushButton:hover {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    QPushButton:pressed {
        background-color: rgba(255, 255, 255, 0.1);
    }
    QPushButton[selected="true"] {
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        font-weight: bold;
    }
    #sidebar {
        background-color: #343AEB;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
        padding-top: 20px;
    }
    #content {
        background-color: #2A2E83;
        border-top-right-radius: 20px;
        border-bottom-right-radius: 20px;
    }
    QLabel#sidebar-title {
        background-color: none;
        font-size: 24px;
        font-weight: 600;
        padding: 10px;
        text-align: center;
    }
    #steps {    
        font-size: 22px;
        font-family: 'Segoe UI', sans-serif;
        color: white;
        padding: 10px;
        background-color: #3B48C2;
        border-radius: 5px;
    }
    QPushButton#nav-button {
        font-size: 24px;
        padding: 10px;
        background-color: #2A2E83;
        border-radius: 5px;
        color: white;
    }
    #nav-button:hover {
        background-color: #3B48C2;
    }
    #return-button {
        background-color: #4C5CD2;
        border-radius: 8px;
        padding: 15px;
        font-size: 16px;
        color: white;
        margin: 20px;
    }
    #return-button:hover {
        background-color: #3B48C2;
    }
    QPushButton#return-button {
        font-weight: 500;
    }
"""
