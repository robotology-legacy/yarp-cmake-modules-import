#!/usr/bin/python
import os

#         folder/filename                                                       new folder                      new filename
files = [["conf/FindCFW2CANAPI.cmake",                                          "keep/find-modules",            "FindCFW2CANAPI.cmake"],
         ["conf/FindDRAGONFLYAPI.cmake",                                        "keep/find-modules",            "FindDRAGONFLYAPI.cmake"],
         ["conf/FindESDCANAPI.cmake",                                           "keep/find-modules",            "FindESDCANAPI.cmake"],
         ["conf/FindGLUT.cmake",                                                "keep/find-modules",            "FindGLUT.cmake"],
         ["conf/FindIPOPT.cmake",                                               "keep/find-modules",            "FindIPOPT.cmake"],
         ["conf/FindIPP.cmake",                                                 "keep/find-modules",            "FindIPP.cmake"],
         ["conf/FindODE.cmake",                                                 "keep/find-modules",            "FindODE.cmake"],
         ["conf/FindOpenGL.cmake",                                              "keep/find-modules",            "FindOpenGL.cmake"],
         ["conf/FindPLXCANAPI.cmake",                                           "keep/find-modules",            "FindPLXCANAPI.cmake"],
         ["conf/FindQt3.cmake",                                                 "keep/find-modules",            "FindQt3.cmake"],
         ["conf/FindQtOpenGL.cmake",                                            "keep/find-modules",            "FindQtOpenGL.cmake"],
         ["conf/FindQwt.cmake",                                                 "keep/find-modules",            "FindQwt.cmake"],
         ["conf/FindSIFTGPU.cmake",                                             "keep/find-modules",            "FindSIFTGPU.cmake"],

         ["conf/FindGtkMM.cmake",                                               "keep/deprecated",              "FindGtkMM.cmake"],
         ["conf/FindGtkMMUnix.cmake",                                           "keep/deprecated",              "FindGtkMMUnix.cmake"],
         ["conf/FindGtkMMWin32.cmake",                                          "keep/deprecated",              "FindGtkMMWin32.cmake"],
         ["conf/FindGtkMMWin32-new.cmake",                                      "keep/deprecated",              "FindGtkMMWin32.cmake"]]


for file in files:
  if not os.access(file[1], os.R_OK):
    os.makedirs(file[1])
  if os.access(file[0], os.R_OK):
    os.rename(file[0], file[1]+"/"+file[2])
