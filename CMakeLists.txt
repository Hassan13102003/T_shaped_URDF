cmake_minimum_required(VERSION 3.8)
project(demo_robot)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# Install URDF, launch, and any other configuration directories
# (Other find_package calls and rules above...)

# --- 1. Testing Block (Default from ros2 pkg create) ---
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# --- 2. Install Block (What you added) ---
install(
  DIRECTORY 
    urdf
    launch
  DESTINATION share/${PROJECT_NAME}
)

# --- 3. Ament Package (MUST BE THE LAST LINE) ---
ament_package()