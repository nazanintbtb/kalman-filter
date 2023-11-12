# kalman-filter
It is an optimal linear estimation method.
# application
When we need to measure a parameter, but we cannot measure it directly. Therefore, we measure the required parameter indirectly using other parameters.
For example, we have a furnace with a very high temperature, and we cannot place a temperature sensor inside the furnace. So, we place the sensor at the boundary of the furnace inside an insulator to measure the temperature, but the measured temperature is much lower than the temperature inside the furnace. Therefore, using parameters such as external temperature calculated by the sensor and the amount of fuel we input into the furnace, we estimate the temperature inside the furnace (Kalman filter is a method used for estimation).
We measure the value of a parameter from different sources because the desired parameter is contaminated with noise, and its value deviates from reality.
For example, measuring moving speed.
To measure speed, we can use tools such as GPS (provides absolute location), odometer (provides relative displacement), and IMU (provides acceleration information). It is evident that these parameters can be used to calculate speed, but the problem is that these tools may not provide accurate values. For example, GPS may not work properly inside a tunnel and introduce noise. Therefore, the accurate speed value may not be calculated. Here, the Kalman filter can help us in optimal estimation.
# output of kalman filter without fault 
![kalman](https://github.com/nazanintbtb/kalman-filter/assets/88847995/66094063-0edf-4d91-9863-13bfecfba798)


