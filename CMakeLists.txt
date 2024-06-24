# ---------------------------------------------------------------------------------------
#                         Copyright (©) Carl Zeiss Meditec AG
#                               - All Rights Reserved -
#
#                     THIS IS UNPUBLISHED PROPRIETARY SOURCE CODE OF
#                                  CARL ZEISS MEDITEC AG
#
#                       This copyright notice does not evidence any
#                    actual or intended publication of such source code.
# ---------------------------------------------------------------------------------------

cmake_minimum_required(VERSION 3.21)
project(personal-finance VERSION 0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")

set(CMAKE_PREFIX_PATH "/lib/x86_64-linux-gnu/cmake" "${CMAKE_BINARY_DIR}/Debug/generators/" ${CMAKE_PREFIX_PATH})
# set(CMAKE_PREFIX_PATH "/home/sds/.conan2/p/qt0b8d5dc773b00/p/lib/cmake" ${CMAKE_PREFIX_PATH})


message(STATUS "SDSINGH: The value of CMAKE_PREFIX_PATH is: ${CMAKE_PREFIX_PATH}")
# message(FATAL_ERROR "Stopping execution after printing the variable value.")

set(QML_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/qml)
file(GLOB_RECURSE QML_SOURCE_FILES "${QML_SOURCE_DIR}/*.qml")

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

# Add the include directory
include_directories(${CMAKE_SOURCE_DIR}/include)

find_package(Qt6 COMPONENTS Core Quick Widgets Charts REQUIRED)
find_package(log4cplus REQUIRED)
# find_package(cpp-httplib REQUIRED)

# Add the source files
set(SOURCES
    ${PROJECT_SOURCE_DIR}/src/main.cpp
)

# Add the header files for MOC
# set(HEADERS
#     ${PROJECT_SOURCE_DIR}/include/Logger.h
#     ${PROJECT_SOURCE_DIR}/include/LoggingHelpers.h
# )

# Add the executable
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Core Qt6::Quick Qt6::Widgets Qt6::Charts log4cplus::log4cplus rt)

# Add custom target to copy QML files
add_custom_target(
  CopyQmlFilesOnBuild ALL
  COMMAND ${CMAKE_COMMAND} -E copy_directory ${QML_SOURCE_DIR}
          ${CMAKE_BINARY_DIR}/qml/
)

include_directories(${CMAKE_SOURCE_DIR}/include)

# Make sure the custom target runs before the main executable
add_dependencies(${PROJECT_NAME} CopyQmlFilesOnBuild)
