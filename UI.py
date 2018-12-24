# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StyleTransfer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class UI(object):
    def __init__(self, title="title", width=1500, height=860):
        self.window = QMainWindow()
        self.title = title
        self.width = width
        self.height = height

        self.setupUi()
        self.window.show()

    def setupUi(self):
        self.window.setObjectName("self.window")
        self.window.resize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.transfer_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transfer_btn.sizePolicy().hasHeightForWidth())
        self.transfer_btn.setSizePolicy(sizePolicy)
        self.transfer_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.transfer_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.transfer_btn.setObjectName("transfer_btn")
        self.gridLayout_2.addWidget(self.transfer_btn, 1, 0, 1, 1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")

        self.segmentation_mask_view = QtWidgets.QLabel(self.centralwidget)
        self.segmentation_mask_view.setText("")
        self.segmentation_mask_view.setAlignment(QtCore.Qt.AlignCenter)
        self.segmentation_mask_view.setObjectName("segmentation_mask_view")
        self.gridLayout.addWidget(self.segmentation_mask_view, 5, 0, 2, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.original_browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.original_browse_btn.setObjectName("original_browse_btn")
        self.gridLayout.addWidget(self.original_browse_btn, 6, 1, 1, 1)

        self.stlye_browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stlye_browse_btn.setObjectName("stlye_browse_btn")
        self.gridLayout.addWidget(self.stlye_browse_btn, 6, 2, 1, 1)

        self.output_image_view = QtWidgets.QLabel(self.centralwidget)
        self.output_image_view.setText("")
        self.output_image_view.setAlignment(QtCore.Qt.AlignCenter)
        self.output_image_view.setObjectName("output_image_view")
        self.gridLayout.addWidget(self.output_image_view, 1, 3, 5, 1)

        self.style_image_view = QtWidgets.QLabel(self.centralwidget)
        self.style_image_view.setText("")
        self.style_image_view.setAlignment(QtCore.Qt.AlignCenter)
        self.style_image_view.setObjectName("style_image_view")
        self.gridLayout.addWidget(self.style_image_view, 1, 2, 5, 1)

        self.original_image_view = QtWidgets.QLabel(self.centralwidget)
        self.original_image_view.setText("")
        self.original_image_view.setAlignment(QtCore.Qt.AlignCenter)
        self.original_image_view.setObjectName("original_image_view")
        self.gridLayout.addWidget(self.original_image_view, 1, 1, 5, 1)

        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout.addWidget(self.export_btn, 6, 3, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.segmentation_mode_combo = QtWidgets.QComboBox(self.centralwidget)
        self.segmentation_mode_combo.setObjectName("segmentation_mode_combo")
        self.segmentation_mode_combo.addItems(["No segmentation", "Face Segmentation", "Edge Segmentation"])
        self.gridLayout.addWidget(self.segmentation_mode_combo, 0, 0, 1, 1)

        self.mask_c_input = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_c_input.setMaximumWidth(400)
        self.mask_c_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_c_input.setObjectName("mask_c_input")
        self.gridLayout.addWidget(self.mask_c_input, 1, 0, 1, 1)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(400, 350))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setObjectName("stackedWidget")

        self.no_segmentation_page = QtWidgets.QWidget()
        self.no_segmentation_page.setObjectName("no_segmentation_page")
        self.stackedWidget.addWidget(self.no_segmentation_page)
        # ====================================== face segmentation section ======================================
        self.face_segmentation_page = QtWidgets.QWidget()
        self.face_segmentation_page.setObjectName("face_segmentation_page")

        self.scale_factor_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.scale_factor_input.setGeometry(QtCore.QRect(10, 30, 170, 23))
        self.scale_factor_input.setAlignment(QtCore.Qt.AlignCenter)
        self.scale_factor_input.setObjectName("scale_factor_input")

        self.min_neighbours_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.min_neighbours_input.setGeometry(QtCore.QRect(200, 30, 170, 23))
        self.min_neighbours_input.setAlignment(QtCore.Qt.AlignCenter)
        self.min_neighbours_input.setObjectName("min_neighbours_input")

        self.label_7 = QtWidgets.QLabel(self.face_segmentation_page)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.face_segmentation_page)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.canny_sigma_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.canny_sigma_input.setGeometry(QtCore.QRect(10, 80, 170, 23))
        self.canny_sigma_input.setAlignment(QtCore.Qt.AlignCenter)
        self.canny_sigma_input.setObjectName("canny_sigma_input")

        self.mcv_gaussian_sigma_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.mcv_gaussian_sigma_input.setGeometry(QtCore.QRect(200, 80, 170, 23))
        self.mcv_gaussian_sigma_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_gaussian_sigma_input.setObjectName("mcv_gaussian_sigma_input")

        self.canny_low_threshold_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.canny_low_threshold_input.setGeometry(QtCore.QRect(10, 110, 170, 23))
        self.canny_low_threshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.canny_low_threshold_input.setObjectName("canny_low_threshold_input")

        self.canny_high_threshold_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.canny_high_threshold_input.setGeometry(QtCore.QRect(200, 110, 170, 23))
        self.canny_high_threshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.canny_high_threshold_input.setObjectName("canny_high_threshold_input")

        self.num_dialation_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.num_dialation_input.setGeometry(QtCore.QRect(10, 140, 170, 23))
        self.num_dialation_input.setAlignment(QtCore.Qt.AlignCenter)
        self.num_dialation_input.setObjectName("num_dialation_input")

        self.fs_mcv_c1_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_mcv_c1_input.setGeometry(QtCore.QRect(200, 140, 170, 23))
        self.fs_mcv_c1_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_mcv_c1_input.setObjectName("fs_mcv_c1_input")

        self.fs_mcv_c2_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_mcv_c2_input.setGeometry(QtCore.QRect(10, 170, 170, 23))
        self.fs_mcv_c2_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_mcv_c2_input.setObjectName("fs_mcv_c2_input")

        self.fs_mcv_threshold_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_mcv_threshold_input.setGeometry(QtCore.QRect(200, 200, 170, 23))
        self.fs_mcv_threshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_mcv_threshold_input.setObjectName("fs_mcv_threshold_input")

        self.fs_mcv_smoothing_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_mcv_smoothing_input.setGeometry(QtCore.QRect(10, 200, 170, 23))
        self.fs_mcv_smoothing_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_mcv_smoothing_input.setObjectName("fs_mcv_smoothing_input")

        self.fs_mcv_num_iter_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_mcv_num_iter_input.setGeometry(QtCore.QRect(200, 170, 170, 23))
        self.fs_mcv_num_iter_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_mcv_num_iter_input.setObjectName("fs_mcv_num_iter_input")

        self.fs_mcv_mode_combo = QtWidgets.QComboBox(self.face_segmentation_page)
        self.fs_mcv_mode_combo.setGeometry(QtCore.QRect(10, 230, 361, 23))
        self.fs_mcv_mode_combo.addItems(["edges (default)", "checkerboard", "circle", "original image gray scale", "other image (will be converted to gray scale and scaled to the size of the mask)"])
        self.fs_mcv_mode_combo.setObjectName("fs_mcv_mode_combo")

        self.label_9 = QtWidgets.QLabel(self.face_segmentation_page)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.grab_cut_mode_combo = QtWidgets.QComboBox(self.face_segmentation_page)
        self.grab_cut_mode_combo.setGeometry(QtCore.QRect(200, 280, 170, 23))
        self.grab_cut_mode_combo.addItems(["GC_INIT_WITH_MASK (default)", "GC_INIT_WITH_RECT", "GC_EVAL"])
        self.grab_cut_mode_combo.setObjectName("grab_cut_mode_combo")

        self.grab_cut_num_iter_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.grab_cut_num_iter_input.setGeometry(QtCore.QRect(10, 280, 170, 23))
        self.grab_cut_num_iter_input.setAlignment(QtCore.Qt.AlignCenter)
        self.grab_cut_num_iter_input.setObjectName("grab_cut_num_iter_input")

        self.fs_gaussian_sigma_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_gaussian_sigma_input.setGeometry(QtCore.QRect(10, 310, 110, 23))
        self.fs_gaussian_sigma_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_gaussian_sigma_input.setObjectName("fs_gaussian_sigma_input")

        self.model_size_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.model_size_input.setGeometry(QtCore.QRect(140, 310, 110, 23))
        self.model_size_input.setAlignment(QtCore.Qt.AlignCenter)
        self.model_size_input.setObjectName("model_size_input")

        self.fs_dialation_sigma_input = QtWidgets.QLineEdit(self.face_segmentation_page)
        self.fs_dialation_sigma_input.setGeometry(QtCore.QRect(270, 310, 110, 23))
        self.fs_dialation_sigma_input.setAlignment(QtCore.Qt.AlignCenter)
        self.fs_dialation_sigma_input.setObjectName("fs_dialation_sigma_input")
        self.stackedWidget.addWidget(self.face_segmentation_page)
        # ====================================== edge segmentation section ======================================
        self.edge_segmentation_page = QtWidgets.QWidget()
        self.edge_segmentation_page.setObjectName("edge_segmentation_page")

        self.edge_seg_algos = QtWidgets.QTabWidget(self.edge_segmentation_page)
        self.edge_seg_algos.setGeometry(QtCore.QRect(0, 40, 400, 311))
        self.edge_seg_algos.setMaximumSize(QtCore.QSize(400, 350))
        self.edge_seg_algos.setObjectName("edge_seg_algos")

        self.ch_tab = QtWidgets.QWidget()
        self.ch_tab.setObjectName("ch_tab")
        self.ch_ethreshold_input = QtWidgets.QLineEdit(self.ch_tab)
        self.ch_ethreshold_input.setGeometry(QtCore.QRect(70, 130, 250, 23))
        self.ch_ethreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ch_ethreshold_input.setObjectName("ch_ethreshold_input")
        self.edge_seg_algos.addTab(self.ch_tab, "")

        self.ws_tab = QtWidgets.QWidget()
        self.ws_tab.setObjectName("ws_tab")
        self.ws_ethreshold_input = QtWidgets.QLineEdit(self.ws_tab)
        self.ws_ethreshold_input.setGeometry(QtCore.QRect(70, 50, 240, 23))
        self.ws_ethreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ws_ethreshold_input.setObjectName("ws_ethreshold_input")

        self.ws_mdisk_size_input = QtWidgets.QLineEdit(self.ws_tab)
        self.ws_mdisk_size_input.setGeometry(QtCore.QRect(70, 90, 240, 23))
        self.ws_mdisk_size_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ws_mdisk_size_input.setObjectName("ws_mdisk_size_input")

        self.ws_mthreshold_input = QtWidgets.QLineEdit(self.ws_tab)
        self.ws_mthreshold_input.setGeometry(QtCore.QRect(70, 130, 240, 23))
        self.ws_mthreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ws_mthreshold_input.setObjectName("ws_mthreshold_input")

        self.ws_gdisk_size_input = QtWidgets.QLineEdit(self.ws_tab)
        self.ws_gdisk_size_input.setGeometry(QtCore.QRect(70, 170, 240, 23))
        self.ws_gdisk_size_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ws_gdisk_size_input.setObjectName("ws_gdisk_size_input")

        self.ws_glevel_threshold_input = QtWidgets.QLineEdit(self.ws_tab)
        self.ws_glevel_threshold_input.setGeometry(QtCore.QRect(70, 210, 240, 23))
        self.ws_glevel_threshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.ws_glevel_threshold_input.setObjectName("ws_glevel_threshold_input")
        self.edge_seg_algos.addTab(self.ws_tab, "")

        self.chws_tab = QtWidgets.QWidget()
        self.chws_tab.setObjectName("chws_tab")
        self.chws_ch_ethreshold_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_ch_ethreshold_input.setGeometry(QtCore.QRect(70, 30, 240, 23))
        self.chws_ch_ethreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_ch_ethreshold_input.setObjectName("chws_ch_ethreshold_input")

        self.chws_ws_ethreshold_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_ws_ethreshold_input.setGeometry(QtCore.QRect(70, 70, 240, 23))
        self.chws_ws_ethreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_ws_ethreshold_input.setObjectName("chws_ws_ethreshold_input")

        self.chws_mdisk_size_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_mdisk_size_input.setGeometry(QtCore.QRect(70, 110, 240, 23))
        self.chws_mdisk_size_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_mdisk_size_input.setObjectName("chws_mdisk_size_input")

        self.chws_mthreshold_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_mthreshold_input.setGeometry(QtCore.QRect(70, 150, 240, 23))
        self.chws_mthreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_mthreshold_input.setObjectName("chws_mthreshold_input")

        self.chws_gdisk_size_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_gdisk_size_input.setGeometry(QtCore.QRect(70, 190, 240, 23))
        self.chws_gdisk_size_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_gdisk_size_input.setObjectName("chws_gdisk_size_input")

        self.chws_glevel_threshold_input = QtWidgets.QLineEdit(self.chws_tab)
        self.chws_glevel_threshold_input.setGeometry(QtCore.QRect(70, 230, 240, 23))
        self.chws_glevel_threshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.chws_glevel_threshold_input.setObjectName("chws_glevel_threshold_input")
        self.edge_seg_algos.addTab(self.chws_tab, "")

        self.cv_tab = QtWidgets.QWidget()
        self.cv_tab.setObjectName("cv_tab")

        self.cv_ethreshold_input = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_ethreshold_input.setGeometry(QtCore.QRect(70, 10, 240, 23))
        self.cv_ethreshold_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_ethreshold_input.setObjectName("cv_ethreshold_input")

        self.cv_mu_input = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_mu_input.setGeometry(QtCore.QRect(70, 40, 240, 23))
        self.cv_mu_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_mu_input.setObjectName("cv_mu_input")

        self.cv_init_level_set_combo = QtWidgets.QComboBox(self.cv_tab)
        self.cv_init_level_set_combo.setGeometry(QtCore.QRect(70, 220, 240, 23))
        self.cv_init_level_set_combo.addItems(["checkerboard (default)", "disk", "small disk", "edges", "original image gray scale", "other image (will be converted to gray scale and scaled to the size of the mask)"])
        self.cv_init_level_set_combo.setObjectName("cv_init_level_set_combo")

        self.cv_lamda_1_imput = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_lamda_1_imput.setGeometry(QtCore.QRect(70, 70, 240, 23))
        self.cv_lamda_1_imput.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_lamda_1_imput.setObjectName("cv_lamda_1_imput")

        self.cv_lamda_2_imput = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_lamda_2_imput.setGeometry(QtCore.QRect(70, 100, 240, 23))
        self.cv_lamda_2_imput.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_lamda_2_imput.setObjectName("cv_lamda_2_imput")

        self.cv_tol_input = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_tol_input.setGeometry(QtCore.QRect(70, 130, 240, 23))
        self.cv_tol_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_tol_input.setObjectName("cv_tol_input")

        self.cv_max_iter_input = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_max_iter_input.setGeometry(QtCore.QRect(70, 160, 240, 23))
        self.cv_max_iter_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_max_iter_input.setObjectName("cv_max_iter_input")

        self.cv_dt_input = QtWidgets.QLineEdit(self.cv_tab)
        self.cv_dt_input.setGeometry(QtCore.QRect(70, 190, 240, 23))
        self.cv_dt_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cv_dt_input.setObjectName("cv_dt_input")

        self.cv_extended_output_check = QtWidgets.QCheckBox(self.cv_tab)
        self.cv_extended_output_check.setGeometry(QtCore.QRect(70, 250, 240, 21))
        self.cv_extended_output_check.setObjectName("cv_extended_output_check")
        self.edge_seg_algos.addTab(self.cv_tab, "")

        self.mcv_tab = QtWidgets.QWidget()
        self.mcv_tab.setObjectName("mcv_tab")
        self.mcv_init_level_set_combo = QtWidgets.QComboBox(self.mcv_tab)
        self.mcv_init_level_set_combo.setGeometry(QtCore.QRect(70, 130, 240, 23))
        self.mcv_init_level_set_combo.addItems(["edges (default)", "checkerboard", "circle", "original image gray scale", "other image (will be converted to gray scale and scaled to the size of the mask)"])
        self.mcv_init_level_set_combo.setObjectName("mcv_init_level_set_combo")

        self.mcv_c1_input = QtWidgets.QLineEdit(self.mcv_tab)
        self.mcv_c1_input.setGeometry(QtCore.QRect(70, 40, 240, 23))
        self.mcv_c1_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_c1_input.setObjectName("mcv_c1_input")

        self.mcv_c2_input = QtWidgets.QLineEdit(self.mcv_tab)
        self.mcv_c2_input.setGeometry(QtCore.QRect(70, 70, 240, 23))
        self.mcv_c2_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_c2_input.setObjectName("mcv_c2_input")

        self.mcv_max_iter_input = QtWidgets.QLineEdit(self.mcv_tab)
        self.mcv_max_iter_input.setGeometry(QtCore.QRect(70, 100, 240, 23))
        self.mcv_max_iter_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_max_iter_input.setObjectName("mcv_max_iter_input")

        self.mcv_smoothing_input = QtWidgets.QLineEdit(self.mcv_tab)
        self.mcv_smoothing_input.setGeometry(QtCore.QRect(70, 160, 240, 23))
        self.mcv_smoothing_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_smoothing_input.setObjectName("mcv_smoothing_input")

        self.mcv_sigma_input = QtWidgets.QLineEdit(self.mcv_tab)
        self.mcv_sigma_input.setGeometry(QtCore.QRect(70, 190, 240, 23))
        self.mcv_sigma_input.setAlignment(QtCore.Qt.AlignCenter)
        self.mcv_sigma_input.setObjectName("mcv_sigma_input")
        self.edge_seg_algos.addTab(self.mcv_tab, "")

        self.edge_strength_input = QtWidgets.QLineEdit(self.edge_segmentation_page)
        self.edge_strength_input.setGeometry(QtCore.QRect(10, 10, 160, 23))
        self.edge_strength_input.setAlignment(QtCore.Qt.AlignCenter)
        self.edge_strength_input.setObjectName("edge_strength_input")

        self.edge_coherence_input = QtWidgets.QLineEdit(self.edge_segmentation_page)
        self.edge_coherence_input.setGeometry(QtCore.QRect(200, 10, 160, 23))
        self.edge_coherence_input.setAlignment(QtCore.Qt.AlignCenter)
        self.edge_coherence_input.setObjectName("edge_coherence_input")

        self.stackedWidget.addWidget(self.edge_segmentation_page)
        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 1)
        # ---------------------------------------------------------------------------------------------
        self.get_mask_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_mask_btn.setObjectName("get_mask_btn")
        self.gridLayout.addWidget(self.get_mask_btn, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(self.window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(self.window)
        self.actionExit.setObjectName("actionExit")
        self.actionDocumentation = QtWidgets.QAction(self.window)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        self.edge_seg_algos.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("self.window", self.title))
        self.transfer_btn.setText(_translate("self.window", "Transfer"))
        self.label.setText(_translate("self.window", "Original"))
        self.label_2.setText(_translate("self.window", "Output"))
        self.label_3.setText(_translate("self.window", "Style"))
        self.original_browse_btn.setText(_translate("self.window", "Browse"))
        self.stlye_browse_btn.setText(_translate("self.window", "Browse"))
        self.export_btn.setText(_translate("self.window", "Export"))
        self.mask_c_input.setPlaceholderText(_translate("self.window", "c"))
        self.label_4.setText(_translate("self.window", "Segmentation Mask"))
        self.scale_factor_input.setPlaceholderText(_translate("self.window", "scale factor"))
        self.min_neighbours_input.setPlaceholderText(_translate("self.window", "min neighbours"))
        self.label_7.setText(_translate("self.window", "detect multi scale parameters"))
        self.label_8.setText(_translate("self.window", "segment edges parameters"))
        self.canny_sigma_input.setPlaceholderText(_translate("self.window", "canny_sigma"))
        self.mcv_gaussian_sigma_input.setPlaceholderText(_translate("self.window", "gaussian sigma"))
        self.canny_low_threshold_input.setPlaceholderText(_translate("self.window", "canny low threshold"))
        self.canny_high_threshold_input.setPlaceholderText(_translate("self.window", "canny high threshold"))
        self.num_dialation_input.setPlaceholderText(_translate("self.window", "number of dilations"))
        self.fs_mcv_c1_input.setPlaceholderText(_translate("self.window", "c1"))
        self.fs_mcv_c2_input.setPlaceholderText(_translate("self.window", "c2"))
        self.fs_mcv_threshold_input.setPlaceholderText(_translate("self.window", "chan vese threshold"))
        self.fs_mcv_smoothing_input.setPlaceholderText(_translate("self.window", "smoothing"))
        self.fs_mcv_num_iter_input.setPlaceholderText(_translate("self.window", "number of iterations"))
        self.label_9.setText(_translate("self.window", "Grab Cut and other parameters"))
        self.grab_cut_num_iter_input.setPlaceholderText(_translate("self.window", "grab cut iter count"))
        self.fs_gaussian_sigma_input.setPlaceholderText(_translate("self.window", "gaussian sigma"))
        self.model_size_input.setPlaceholderText(_translate("self.window", "model size"))
        self.fs_dialation_sigma_input.setPlaceholderText(_translate("self.window", "dialation sigma"))
        self.ch_ethreshold_input.setToolTip(_translate("self.window", "<html><head/><body><p>Threshold used to binarize edges to perform convex hull filling on them. Prefered values to be high range 0.65 to 0.85 is a good range. Very high values would lead to exclusion of all edges and may be a black mask with nothing filled at all. Low values would lead to inclusion of a lot of edges thus increases the chance of including noise and generally reduces the accuracy of the mask.</p></body></html>"))
        self.ch_ethreshold_input.setPlaceholderText(_translate("self.window", "edges threshold"))
        self.edge_seg_algos.setTabText(self.edge_seg_algos.indexOf(self.ch_tab), _translate("self.window", "Convex Hull"))
        self.ws_ethreshold_input.setToolTip(_translate("self.window", "<html><head/><body><p>Threshold used to binarize edges to perform watershed filling on them. Prefered lower values in the range of 0.15 to 0.35. As lower values mean including more edges and thus watershed is able to detect important regions and segment it. High regions would lead to less edges and the result may be a white mask that segment the entire image.</p></body></html>"))
        self.ws_ethreshold_input.setPlaceholderText(_translate("self.window", "edges threshold"))
        self.ws_mdisk_size_input.setPlaceholderText(_translate("self.window", "markers disk size"))
        self.ws_mthreshold_input.setPlaceholderText(_translate("self.window", "markers threshold"))
        self.ws_gdisk_size_input.setPlaceholderText(_translate("self.window", "gradient disk size"))
        self.ws_glevel_threshold_input.setPlaceholderText(_translate("self.window", "gray level threshold"))
        self.edge_seg_algos.setTabText(self.edge_seg_algos.indexOf(self.ws_tab), _translate("self.window", "Watershed"))
        self.chws_ch_ethreshold_input.setPlaceholderText(_translate("self.window", "convex hull edges threshold"))
        self.chws_ws_ethreshold_input.setPlaceholderText(_translate("self.window", "watershed edges threshold"))
        self.chws_mdisk_size_input.setPlaceholderText(_translate("self.window", "watershed markers disk size"))
        self.chws_mthreshold_input.setPlaceholderText(_translate("self.window", "watershed markers threshold"))
        self.chws_gdisk_size_input.setPlaceholderText(_translate("self.window", "watershed gradient disk size"))
        self.chws_glevel_threshold_input.setPlaceholderText(_translate("self.window", "watershed gray level threshold"))
        self.edge_seg_algos.setTabText(self.edge_seg_algos.indexOf(self.chws_tab), _translate("self.window", "ConvexHull*Watershed"))
        self.cv_ethreshold_input.setPlaceholderText(_translate("self.window", "edges threshold"))
        self.cv_mu_input.setPlaceholderText(_translate("self.window", "mu"))
        self.cv_lamda_1_imput.setPlaceholderText(_translate("self.window", "lamda 1"))
        self.cv_lamda_2_imput.setPlaceholderText(_translate("self.window", "lamda 2"))
        self.cv_tol_input.setPlaceholderText(_translate("self.window", "tol"))
        self.cv_max_iter_input.setPlaceholderText(_translate("self.window", "max_iter"))
        self.cv_dt_input.setPlaceholderText(_translate("self.window", "dt"))
        self.cv_extended_output_check.setText(_translate("self.window", "extended output"))
        self.edge_seg_algos.setTabText(self.edge_seg_algos.indexOf(self.cv_tab), _translate("self.window", "Chan Vese"))
        self.mcv_c1_input.setPlaceholderText(_translate("self.window", "c1"))
        self.mcv_c2_input.setPlaceholderText(_translate("self.window", "c2"))
        self.mcv_max_iter_input.setPlaceholderText(_translate("self.window", "max_iter"))
        self.mcv_smoothing_input.setPlaceholderText(_translate("self.window", "smoothing"))
        self.mcv_sigma_input.setPlaceholderText(_translate("self.window", "gaussian sigma"))
        self.edge_seg_algos.setTabText(self.edge_seg_algos.indexOf(self.mcv_tab), _translate("self.window", "Morphological Chan Vese"))
        self.edge_strength_input.setPlaceholderText(_translate("self.window", "strength threshold"))
        self.edge_coherence_input.setPlaceholderText(_translate("self.window", "coherence threshold"))
        self.get_mask_btn.setText(_translate("self.window", "Get Mask"))
        self.menuFile.setTitle(_translate("self.window", "File"))
        self.menuHelp.setTitle(_translate("self.window", "Help"))
        self.actionOpen.setText(_translate("self.window", "Open"))
        self.actionExit.setText(_translate("self.window", "Exit"))
        self.actionDocumentation.setText(_translate("self.window", "Documentation"))
