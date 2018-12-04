# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 18))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPrepocess = QtWidgets.QMenu(self.menubar)
        self.menuPrepocess.setObjectName("menuPrepocess")
        self.menuTrain = QtWidgets.QMenu(self.menubar)
        self.menuTrain.setObjectName("menuTrain")
        self.menuClassify = QtWidgets.QMenu(self.menubar)
        self.menuClassify.setObjectName("menuClassify")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSampleProduce = QtWidgets.QMenu(self.menubar)
        self.menuSampleProduce.setObjectName("menuSampleProduce")
        self.menuPostproc = QtWidgets.QMenu(self.menubar)
        self.menuPostproc.setObjectName("menuPostproc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLabel_check = QtWidgets.QAction(MainWindow)
        self.actionLabel_check.setObjectName("actionLabel_check")
        self.actionImage_strech = QtWidgets.QAction(MainWindow)
        self.actionImage_strech.setObjectName("actionImage_strech")
        self.actionSampleGenCommon = QtWidgets.QAction(MainWindow)
        self.actionSampleGenCommon.setObjectName("actionSampleGenCommon")
        self.actionCombineSingleModelReults = QtWidgets.QAction(MainWindow)
        self.actionCombineSingleModelReults.setText("Combine multiclass")
        self.actionCombineSingleModelReults.setObjectName("actionCombineSingleModelReults")
        self.action_VoteMultiModelResults = QtWidgets.QAction(MainWindow)
        self.action_VoteMultiModelResults.setText("Vote Results")
        self.action_VoteMultiModelResults.setObjectName("action_VoteMultiModelResults")
        self.actionAccuracyEvaluation = QtWidgets.QAction(MainWindow)
        self.actionAccuracyEvaluation.setText("Accuracy Evaluate")
        self.actionAccuracyEvaluation.setObjectName("actionAccuracyEvaluation")
        self.actionSampleGenByCV2 = QtWidgets.QAction(MainWindow)
        self.actionSampleGenByCV2.setObjectName("actionSampleGenByCV2")
        self.actionImage_Clip = QtWidgets.QAction(MainWindow)
        self.actionImage_Clip.setObjectName("actionImage_Clip")
        self.actionMismatch_Analyze = QtWidgets.QAction(MainWindow)
        self.actionMismatch_Analyze.setObjectName("actionMismatch_Analyze")
        self.actionTrain_Binary_Jaccard = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Jaccard.setObjectName("actionTrain_Binary_Jaccard")
        self.actionTrain_Binary_JaccCross = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_JaccCross.setObjectName("actionTrain_Binary_JaccCross")
        self.actionTrain_Binary_Cross_entropy = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Cross_entropy.setObjectName("actionTrain_Binary_Cross_entropy")
        self.actionTrain_Multiclass = QtWidgets.QAction(MainWindow)
        self.actionTrain_Multiclass.setObjectName("actionTrain_Multiclass")
        self.actionTrain_Binary_Onehot_Cross = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Onehot_Cross.setObjectName("actionTrain_Binary_Onehot_Cross")
        self.actionPredict_Binary_Single = QtWidgets.QAction(MainWindow)
        self.actionPredict_Binary_Single.setObjectName("actionPredict_Binary_Single")
        self.actionPredict_Multiclass_Single = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass_Single.setObjectName("actionPredict_Multiclass_Single")
        self.actionPredict_Binary_Batch = QtWidgets.QAction(MainWindow)
        self.actionPredict_Binary_Batch.setObjectName("actionPredict_Binary_Batch")
        self.actionPredict_Multiclass_Batch = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass_Batch.setObjectName("actionPredict_Multiclass_Batch")
        self.actionPredict_Multiclass = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass.setObjectName("actionPredict_Multiclass")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTrain_Binary_new = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_new.setObjectName("actionTrain_Binary_new")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuPrepocess.addAction(self.actionLabel_check)
        self.menuPrepocess.addAction(self.actionImage_strech)
        self.menuPrepocess.addAction(self.actionImage_Clip)
        self.menuTrain.addAction(self.actionTrain_Binary_Jaccard)
        self.menuTrain.addAction(self.actionTrain_Binary_JaccCross)
        self.menuTrain.addAction(self.actionTrain_Binary_Cross_entropy)
        self.menuTrain.addAction(self.actionTrain_Binary_Onehot_Cross)
        self.menuTrain.addAction(self.actionTrain_Multiclass)
        self.menuTrain.addAction(self.actionTrain_Binary_new)
        self.menuClassify.addAction(self.actionPredict_Binary_Single)
        self.menuClassify.addAction(self.actionPredict_Binary_Batch)
        self.menuClassify.addAction(self.actionPredict_Multiclass_Single)
        self.menuClassify.addAction(self.actionPredict_Multiclass_Batch)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSampleProduce.addAction(self.actionSampleGenCommon)
        self.menuPostproc.addAction(self.actionCombineSingleModelReults)
        self.menuPostproc.addAction(self.action_VoteMultiModelResults)
        self.menuPostproc.addAction(self.actionAccuracyEvaluation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPrepocess.menuAction())
        self.menubar.addAction(self.menuSampleProduce.menuAction())
        self.menubar.addAction(self.menuTrain.menuAction())
        self.menubar.addAction(self.menuClassify.menuAction())
        self.menubar.addAction(self.menuPostproc.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionLabel_check.triggered.connect(MainWindow.for_action_label_check)
        self.actionImage_strech.triggered.connect(MainWindow.for_action_image_stretch)
        self.actionImage_Clip.triggered.connect(MainWindow.slot_actiong_image_clip)
        self.actionSampleGenCommon.triggered.connect(MainWindow.slot_action_sampleGenCommon)
        self.actionTrain_Binary_JaccCross.triggered.connect(MainWindow.slot_action_trainBinaryJaccCross)
        self.actionTrain_Binary_Cross_entropy.triggered.connect(MainWindow.slot_action_trainBinaryCrossentropy)
        self.actionTrain_Binary_Jaccard.triggered.connect(MainWindow.slot_action_trainBinaryJaccard)
        self.actionTrain_Binary_Onehot_Cross.triggered.connect(MainWindow.slot_action_trainBinaryOnehot)
        self.actionTrain_Multiclass.triggered.connect(MainWindow.slot_action_trainMulticlass)
        self.actionPredict_Binary_Single.triggered.connect(MainWindow.slot_action_predictBinarySingleImg)
        self.actionPredict_Multiclass_Single.triggered.connect(MainWindow.slot_action_predictMulticlassSingleImg)
        self.actionPredict_Binary_Batch.triggered.connect(MainWindow.slot_action_predictBinaryBatch)
        self.actionPredict_Multiclass_Batch.triggered.connect(MainWindow.slot_action_predictMulticlassBatch)
        self.actionCombineSingleModelReults.triggered.connect(MainWindow.slot_action_combineMulticlassFromSingleModel)
        self.action_VoteMultiModelResults.triggered.connect(MainWindow.slot_action_VoteMultimodleResults)
        self.actionAccuracyEvaluation.triggered.connect(MainWindow.slot_action_accuracyEvaluate)
        self.actionOpen.triggered.connect(MainWindow.slot_open_show)
        self.actionAbout.triggered.connect(MainWindow.slot_action_about)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionTrain_Binary_new.triggered.connect(MainWindow.slot_action_trainBinaryNew)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RS Imagery Deep Learning Process System"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPrepocess.setTitle(_translate("MainWindow", "PreProcess"))
        self.menuTrain.setTitle(_translate("MainWindow", "Train"))
        self.menuClassify.setTitle(_translate("MainWindow", "Classify"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSampleProduce.setTitle(_translate("MainWindow", "Sample"))
        self.menuPostproc.setTitle(_translate("MainWindow", "Postprocess"))
        self.actionLabel_check.setText(_translate("MainWindow", "Label Check"))
        self.actionImage_strech.setText(_translate("MainWindow", "Image Stretch"))
        self.actionSampleGenCommon.setText(_translate("MainWindow", "Sample Generate"))
        self.actionSampleGenByCV2.setText(_translate("MainWindow", "SampleGenByCV2"))
        self.actionImage_Clip.setText(_translate("MainWindow", "Image Clip"))
        self.actionMismatch_Analyze.setText(_translate("MainWindow", "Mismatch Analyze"))
        self.actionTrain_Binary_Jaccard.setText(_translate("MainWindow", "Train Binary Jaccard"))
        self.actionTrain_Binary_JaccCross.setText(_translate("MainWindow", "Train Binary JaccCross"))
        self.actionTrain_Binary_Cross_entropy.setText(_translate("MainWindow", "Train Binary Cross-entropy"))
        self.actionTrain_Multiclass.setText(_translate("MainWindow", "Train Multiclass"))
        self.actionTrain_Binary_Onehot_Cross.setText(_translate("MainWindow", "Train Binary Onehot Cross"))
        self.actionPredict_Binary_Single.setText(_translate("MainWindow", "Predict Binary Single"))
        self.actionPredict_Multiclass_Single.setText(_translate("MainWindow", "Predict Multiclass Single"))
        self.actionPredict_Binary_Batch.setText(_translate("MainWindow", "Predict Binary Batch"))
        self.actionPredict_Multiclass_Batch.setText(_translate("MainWindow", "Predict Multiclass Batch"))
        self.actionPredict_Multiclass.setText(_translate("MainWindow", "Predict Multiclass"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open Raster"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTrain_Binary_new.setText(_translate("MainWindow", "Train Binary new"))

