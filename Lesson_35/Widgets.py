from PyQt5 import QtWidgets, QtCore
import datetime

QtWidgets.QWidget
## Labels
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QFrame -> QtWidgets.QLabel
## Qlabel

## Buttons
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractButton -> QtWidgets.QPushButton

## RadioButton
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractButton -> QtWidgets.QRadioButton
## CheckBox
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractButton -> QtWidgets.QCheckBox
## LineEdit
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QLineEdit
# cursorPositionChanged
# editingFinished
# returnPressed
# selectionChanged
# textChanged
# textEdited
# DateTimeEdit
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSpinBox -> QtWidgets.QDateTimeEdit
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSpinBox -> QtWidgets.QDateTimeEdit ->
QtWidgets.QTimeEdit
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSpinBox -> QtWidgets.QDateTimeEdit ->
QtWidgets.QDateEdit
# TextEdit
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QFrame -> QtWidgets.QAbstractScrollArea ->
QtWidgets.QTextEdit

# TextBrowser
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QFrame -> QtWidgets.QAbstractScrollArea ->
QtWidgets.QTextEdit -> QtWidgets.QTextBrowser

# SpinBox
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSpinBox -> QtWidgets.QSpinBox
# DoubleSpinBox
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSpinBox -> QtWidgets.QDoubleSpinBox
# CalendarWidget
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QCalendarWidget
# LCDNumber
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QFrame -> QtWidgets.QLCDNumber
# ProgressBar
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QProgressBar
# Slider
QtCore.QObject -> QtWidgets.QAbstractSlider -> QtWidgets.QSlider
# Dial
QtCore.QObject -> QtWidgets.QAbstractSlider -> QtWidgets.QDial
# ScrollBar
QtCore.QObject -> QtWidgets.QWidget -> QtWidgets.QAbstractSlider -> QtWidgets.QScrollBar
