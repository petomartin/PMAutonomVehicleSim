options = {
    map_frame = "map",
    tracking_frame = "base_link",
    published_frame = "base_link",
    odom_frame = "odom",
    provide_odom_frame = false,
    use_odometry = false,
    use_nav_sat = false,
    use_landmarks = false,
    num_laser_scans = 1,
    num_multi_echo_laser_scans = 0,
    num_subdivisions_per_laser_scan = 1,
    num_point_clouds = 0,
    rangefinder_sampling_ratio = 1.0,
    odometry_sampling_ratio = 1.0,
    fixed_frame_pose_sampling_ratio = 1.0,
    imu_sampling_ratio = 0, -- 1 ha az IMU használva van
    landmarks_sampling_ratio = 1.0,
  }
  
  TRAJECTORY_BUILDER_2D.use_imu_data = false
  TRAJECTORY_BUILDER_2D.min_range = 0.1
  TRAJECTORY_BUILDER_2D.max_range = 10.0
  TRAJECTORY_BUILDER_2D.missing_data_ray_length = 5.0
  TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true
  TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.linear_search_window = 0.1
  TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.angular_search_window = math.rad(20.)
  
  POSE_GRAPH.constraint_builder.min_score = 0.65
  POSE_GRAPH.constraint_builder.global_localization_min_score = 0.7
  
  return options
  