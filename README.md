## Simulation go1 quadropted robot in gazebo Ignition

### This builded and tested on ROS2 HUMBLE


### install dependenses:



### SETUP:

### install deps:
```bash
sudo apt install ros-humble-ign-ros2-control ros-humble-tf-transformations
```

```bash
mkdir -p go1_sim_py/src
cd go1_sim_py/src
git clone https://github.com/abutalipovvv/go1_sim_py.git .
cd ..
colcon build
```

### RUN SIMULATION

```bash
cd go1_sim_py
source install/local_setup.bash
ros2 launch go1_description go1_gazebo.launch.py
```


### move with teleop_twist_keyboard:

```bash
cd go1_sim_py
source install/local_setup.bash
ros2 launch go1_description go1_gazebo.launch.py
```

```bash
source install/local_setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```


## Credits

    mike4192: https://github.com/mike4192/spotMicro
    Unitree Robotics: https://github.com/unitreerobotics/a1_ros
    QUADRUPED ROBOTICS: https://quadruped.de
    lnotspotl : https://github.com/lnotspotl
