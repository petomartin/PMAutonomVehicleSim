-- Defináljuk a szenzorok pluginjait
local back_camera_sensor = {
    frameName = "back_camera_frame",
    topicName = "/back_camera/image_raw",
    output_type = "sensor_msgs/Image"
  }
  
  local back_left_far_sonar_sensor = {
    frameName = "back_left_far_sonar_frame",
    topicName = "/back_left_far_sonar/scan",
    output_type = "sensor_msgs/PointCloud2"
  }

  local back_left_middle_sonar_sensor = {
    frameName = "back_left_middle_sonar_frame",
    topicName = "/back_left_middle_sonar/scan",
    output_type = "sensor_msgs/PointCloud2"
}

  local center_laser_sensor = {
    frameName = "center_laser_frame",
    topicName = "/center_laser_controller/out",  -- Ezt kell javítani
    output_type = "sensor_msgs/LaserScan"
  }
  
  -- További szenzor pluginok...
  
  -- Függvény a szenzorok inicializálásához
  function initSensors()
    -- Kamera plugin inicializálása
    gazebo_ros_camera.loadCamera(back_camera_sensor.frameName, back_camera_sensor.topicName, back_camera_sensor.output_type)
  
    -- Sonar plugin inicializálása
    gazebo_ros_ray_sensor.loadRaySensor(back_left_far_sonar_sensor.frameName, back_left_far_sonar_sensor.topicName, back_left_far_sonar_sensor.output_type)
    gazebo_ros_ray_sensor.loadRaySensor(back_left_middle_sonar_sensor.frameName, back_left_middle_sonar_sensor.topicName, back_left_middle_sonar_sensor.output_type)
    gazebo_ros_ray_sensor.loadRaySensor(center_laser_sensor.frameName, center_laser_sensor.topicName, center_laser_sensor.output_type)


    -- További szenzorok inicializálása...
  end
  
  -- A szimuláció elindulásakor hívjuk meg az initSensors függvényt
  function OnStart()
    initSensors()
  end
  
  -- Regisztráljuk az OnStart eseményt
  gz.registerEvent("onStart", OnStart)
  