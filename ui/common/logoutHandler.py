"""
Logout Handler for managing logout functionality across the application
"""

from PyQt5.QtWidgets import QMessageBox
# Đảm bảo import đúng cho các hằng số QObject và pyqtSignal
from PyQt5.QtCore import pyqtSignal, QObject


class LogoutHandler(QObject):
    """
    Signal để thông báo khi người dùng đăng xuất
    """
    logout_requested = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def request_logout(self, window=None):
        """
        Xử lý yêu cầu đăng xuất, hiển thị hộp thoại xác nhận và đóng cửa sổ.

        Args:
            window: Cửa sổ hiện tại (dùng để hiển thị xác nhận)
        """
        if window:
            reply = QMessageBox.question(
                window,
                "Xác nhận đăng xuất",
                "Bạn có chắc chắn muốn đăng xuất?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # Đóng cửa sổ hiện tại
                window.close()
                # Phát tín hiệu đăng xuất
                self.logout_requested.emit()
        else:
            # Nếu không có cửa sổ, phát tín hiệu đăng xuất trực tiếp
            self.logout_requested.emit()

    def confirm_logout(self, window=None):
        """
        Yêu cầu xác nhận trước khi đăng xuất, trả về True/False
        """
        if window:
            reply = QMessageBox.question(
                window,
                "Đăng xuất",
                "Bạn muốn đăng xuất khỏi hệ thống?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            return reply == QMessageBox.Yes
        return True