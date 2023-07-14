# KUKA-YouBotPlatform-Seek_Thermal

## Description

KUKA-YouBotPlatform-Seek_Thermal — is a user space driver for the SEEK THERMAL COMPACT thermal imager built on libusb and libopencv.

Supported cameras:
* [Seek Thermal Compact](http://www.thermal.com/products/compact)


**NOTE. The library does not support the output of absolute temperature readings and is limited to the output of thermograms**


## Borrowing

The code is based on an idea from the following repository:
* https://github.com/coaco-robot/libseek-thermal

## Building

Dependencies:
* cmake
* libopencv-dev (>= 2.4)
* libusb-1.0-0-dev

NOTE: you can just "apt-get install" all of the above libraries

```
cd libseek-thermal
mkdir build
cd build
cmake ..
make
```

Install the shared library, headers and binaries files:

```
sudo make install
sudo ldconfig 
```

## Running examples

```
./examples/seek_viewer     # Getting a streaming image from a camera
./examples/seek_snapshot   # Getting a single image from a camera
```

### seek_viewer
seek_viewer — this is a software solution for permanently saving a thermogram in the process of work. The program supports image rotation, scaling and color matching using any of the OpenCV color maps.

```
seek_viewer --camtype=seekpro --colormap=11 --rotate=0                          # view color mapped thermal video
```

### seek_snapshot
seek_snapshot makes a single image. This is useful for integrating into shell scripts. The program supports rotation and color matching just like seek_viewer.

## Python_Seek_Thermal

Python_Seek_Thermal is a software solution that allows you to get an image from a thermal imager installed on a KUKA YouBot Platform robot using a stack (time, cv2, paramico)
NOTE: in the presented solution, the image is permanently saved on the robot because linux server does not allow media files to be displayed. In view of this, using the paramico library using ssh, the file is constantly taken from the robot to the user's PC.