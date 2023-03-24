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
