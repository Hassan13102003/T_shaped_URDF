import launch
from launch.substitutions import Command, LaunchConfiguration # <--- Fixed plural to singular
import launch_ros
import os

package_name='demo_robot'

urdfRelativePath='urdf/model.urdf'

rvizRelativePath='config/config.rviz'

def generate_launch_description():
    # 1. Define package name and URDF file name
    pkgPath = launch_ros.substitutions.FindPackageShare(package=package_name).find(package_name)
    
    # 2. Get the exact path to the URDF file in the install directory
    urdfModelPath = os.path.join(pkgPath, urdfRelativePath)
    rvizConfigPath = os.path.join(pkgPath, rvizRelativePath)

    print(urdfModelPath)
    
    # 3. Read the URDF file contents
    # <--- Fixed variable name from urdf_path to urdfModelPath
    with open(urdfModelPath, 'r') as infp:
        robot_desc = infp.read()

    params = {'robot_description': robot_desc}
    
    # 4. robot_state_publisher: publishes the robot's tf (transform) tree
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params], 
        arguments=[urdfModelPath]
    )
    
    # 5. joint_state_publisher_gui: provides a slider menu to manually move joints
    joint_state_publisher_gui_node = launch_ros.actions.Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui', # <--- Added missing comma
        arguments=[urdfModelPath],        # <--- Added missing comma
        condition=launch.conditions.IfCondition(LaunchConfiguration('gui')) # <--- Fixed to singular 
    )
    
    # 6. rviz2: launches the 3D visualization tool
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',                  # <--- Added missing comma
        arguments=['-d', rvizConfigPath]
    )
    
    # 7. Return the description to execute all nodes together
    return launch.LaunchDescription([ 
        launch.actions.DeclareLaunchArgument(
            name='gui', 
            default_value='True', 
            description='This is a flag for joint_state_publisher'
        ), 
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])