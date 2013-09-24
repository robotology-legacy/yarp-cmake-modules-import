#!/usr/bin/python
import os

#         folder/filename                                                       new folder                              new filename
files = [
         ["conf/FindACE.cmake",                                                 "keep/find-modules",                    "FindACE.cmake"],
         ["conf/FindAce.cmake",                                                 "keep/find-modules",                    "FindACE.cmake"],
         ["conf/FindAtlas.cmake",                                               "keep/find-modules",                    "FindAtlas.cmake"],
         ["conf/FindFFMPEG.cmake",                                              "keep/find-modules",                    "FindFFMPEG.cmake"],
         ["conf/FindGooCanvas.cmake",                                           "keep/find-modules",                    "FindGooCanvas.cmake"],
         ["conf/FindGooCanvasMM.cmake",                                         "keep/find-modules",                    "FindGooCanvasMM.cmake"],
         ["conf/FindGSL.cmake",                                                 "keep/find-modules",                    "FindGSL.cmake"],
         ["conf/FindGtkDatabox.cmake",                                          "keep/find-modules",                    "FindGtkDatabox.cmake"],
         ["src/yarpscope/cmake/FindGtkDatabox.cmake",                           "keep/find-modules",                    "FindGtkDatabox.cmake"],
         ["conf/FindGtkDataboxMM.cmake",                                        "keep/find-modules",                    "FindGtkDataboxMM.cmake"],
         ["src/yarpscope/cmake/FindGtkDataboxMM.cmake",                         "keep/find-modules",                    "FindGtkDataboxMM.cmake"],
         ["conf/FindOpenCV.cmake",                                              "keep/find-modules",                    "FindOpenCV.cmake"],
         ["conf/FindOpenCV-yarp.cmake",                                         "keep/find-modules",                    "FindOpenCV.cmake"],
         ["conf/FindPortAudio.cmake",                                           "keep/find-modules",                    "FindPortAudio.cmake"],
         ["conf/FindSQLite.cmake",                                              "keep/find-modules",                    "FindSQLite.cmake"],
         ["conf/FindTinyXML.cmake",                                             "keep/find-modules",                    "FindTinyXML.cmake"],

         ["conf/MacroStandardFindModule.cmake",                                 "keep/modules",                         "MacroStandardFindModule.cmake"],
         ["conf/MacroExtractVersion.cmake",                                     "keep/modules",                         "MacroExtractVersion.cmake"],
         ["conf/YarpAceCheck.cmake",                                            "keep/modules",                         "ACECheck.cmake"],
         ["conf/ace_hash_test.cpp",                                             "keep/modules",                         "ace_hash_test.cpp"],
         ["conf/ace_test.cpp",                                                  "keep/modules",                         "ace_test.cpp"],
         ["conf/YarpCheckStructHasMember.cmake"                                 "keep/modules",                         "CheckCXXStructHasMember.cmake"],
         ["conf/YarpCheckTypeSize.cmake"                                        "keep/modules",                         "CheckCXXTypeSize.cmake"],
         ["conf/YarpCMakeWorkarounds.cmake"                                     "keep/modules",                         "CMakeWorkarounds.cmake"],
         ["conf/YARPUninstall.cmake"                                            "keep/modules",                         "Uninstall.cmake"],
         ["conf/template/YARPConfigUninstall.cmake.in"                          "keep/modules",                         "ConfigUninstall.cmake.in"],
         ["conf/template/YarpCheckTypeSize.cxx.in"                              "keep/modules",                         "YarpCheckTypeSize.cxx.in"],

         ["conf/cmake-2.8.12/Copyright.txt",                                    "keep/cmake-next",                      "Copyright.txt"],
         ["conf/cmake-2.8.12/Modules/CMakeParseArguments.cmake",                "keep/cmake-next/Modules",              "CMakeParseArguments.cmake"],
         ["conf/cmake-2.8.12/Modules/FindFreetype.cmake",                       "keep/cmake-next/Modules",              "FindFreetype.cmake"],
         ["conf/cmake-2.8.12/Modules/FindGTK2.cmake",                           "keep/cmake-next/Modules",              "FindGTK2.cmake"],
         ["conf/cmake-2.8.12/Modules/FindPackageHandleStandardArgs.cmake",      "keep/cmake-next/Modules",              "FindPackageHandleStandardArgs.cmake"],
         ["conf/cmake-2.8.12/Modules/FindPackageMessage.cmake",                 "keep/cmake-next/Modules",              "FindPackageMessage.cmake"],
         ["conf/cmake-2.8.12/Modules/SelectLibraryConfigurations.cmake",        "keep/cmake-next/Modules",              "SelectLibraryConfigurations.cmake"],

         ["conf/cmake-2.8.13/Copyright.txt",                                    "keep/cmake-next",                      "Copyright.txt"],
         ["conf/cmake-2.8.13/Modules/CMakeParseArguments.cmake",                "keep/cmake-next/Modules",              "CMakeParseArguments.cmake"],
         ["conf/cmake-2.8.13/Modules/FindFreetype.cmake",                       "keep/cmake-next/Modules",              "FindFreetype.cmake"],
         ["conf/cmake-2.8.13/Modules/FindGTK2.cmake",                           "keep/cmake-next/Modules",              "FindGTK2.cmake"],
         ["conf/cmake-2.8.13/Modules/FindPackageHandleStandardArgs.cmake",      "keep/cmake-next/Modules",              "FindPackageHandleStandardArgs.cmake"],
         ["conf/cmake-2.8.13/Modules/FindPackageMessage.cmake",                 "keep/cmake-next/Modules",              "FindPackageMessage.cmake"],
         ["conf/cmake-2.8.13/Modules/SelectLibraryConfigurations.cmake",        "keep/cmake-next/Modules",              "SelectLibraryConfigurations.cmake"],

         ["conf/FindGthread.cmake",                                             "keep/deprecated",                "FindGthread.cmake"],
         ["conf/deprecated/FindGthread.cmake",                                  "keep/deprecated",                "FindGthread.cmake"],
         ["conf/FindGtkMM.cmake",                                               "keep/deprecated",                "FindGtkMM.cmake"],
         ["conf/deprecated/FindGtkMM.cmake",                                    "keep/deprecated",                "FindGtkMM.cmake"],
         ["conf/FindGtkMMUnix.cmake",                                           "keep/deprecated",                "FindGtkMMUnix.cmake"],
         ["conf/deprecated/FindGtkMMUnix.cmake",                                "keep/deprecated",                "FindGtkMMUnix.cmake"],
         ["conf/FindGtkMMWin32.cmake",                                          "keep/deprecated",                "FindGtkMMWin32.cmake"],
         ["conf/FindGtkmmWin32.cmake",                                          "keep/deprecated",                "FindGtkMMWin32.cmake"],
         ["conf/deprecated/FindGtkMMWin32.cmake",                               "keep/deprecated",                "FindGtkMMWin32.cmake"],
         ["conf/FindGtkPlus.cmake",                                             "keep/deprecated",                "FindGtkPlus.cmake"],
         ["conf/deprecated/FindGtkPlus.cmake",                                  "keep/deprecated",                "FindGtkPlus.cmake"],
         ["conf/FindGtkWin32.cmake",                                            "keep/deprecated",                "FindGtkWin32.cmake"],
         ["conf/deprecated/FindGtkWin32.cmake",                                 "keep/deprecated",                "FindGtkWin32.cmake"],
         ["conf/FindBoost.cmake",                                               "keep/deprecated",                "FindBoost.cmake"],
         ["conf/FindYarp1.cmake",                                               "keep/deprecated",                "FindYarp1.cmake"]]


for file in files:
  if not os.access(file[1], os.R_OK):
    os.makedirs(file[1])
  if os.access(file[0], os.R_OK):
    os.rename(file[0], file[1]+"/"+file[2])
