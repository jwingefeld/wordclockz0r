set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_executable(taskserver
	taskserver.cpp
	json_cst.cpp json_cst.hpp
	json_lex.cpp json_lex.hpp
	json_parse.cpp json_parse.hpp)

include_directories(.)

add_custom_command(
	OUTPUT json.ll
	COMMAND trees -l -o json.ll json.fparse
	MAIN_DEPENDENCY json.fparse)

add_custom_command(
	OUTPUT json.yy
	COMMAND trees -y -o json.yy json.fparse
	MAIN_DEPENDENCY json.fparse)

add_custom_command(
	OUTPUT json_parse.cpp
	COMMAND bison -o json_parse.cpp json.yy
	MAIN_DEPENDENCY json.yy)

add_custom_command(
	OUTPUT json_cst.hpp
	COMMAND trees -n taskserver -n cst -o json_cst.hpp json.yy
	MAIN_DEPENDENCY json.yy)

add_custom_command(
	OUTPUT json_cst.cpp
	COMMAND trees -n taskserver -n cst -c -o json_cst.cpp json.yy
	MAIN_DEPENDENCY json.yy)

add_custom_command(
	OUTPUT json_lex.cpp json_lex.hpp
	COMMAND flex -o json_lex.cpp --header-file=json_lex.hpp json.ll
	MAIN_DEPENDENCY json.ll)
