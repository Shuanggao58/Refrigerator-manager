cmake_minimum_required(VERSION 3.10.2)

project(demo)

set(OpenCV_DIR "/home/concefly/Project/opencv-exp/opencv-3.4.12/_output/share/O$

find_package( OpenCV REQUIRED )

message("WARNING" "OpenCV_INCLUDE_DIRS:" ${OpenCV_INCLUDE_DIRS})
message("WARNING" "OpenCV_LIBS:" ${OpenCV_LIBS})

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(demo main.cpp)
target_link_libraries(demo ${OpenCV_LIBS})