## MacOS OpenCV install
> <code>cd opencv </code>

> <code>mkdir build </code>

> <code>cd build </code>

## CONTRIB OpenCV
> <code>cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ../</code>

## Logs OpenCV
+ Interpreter:                 <code>/usr/local/bin/python3</code> (ver 3.11.5)
+ Libraries:                   <code>/usr/local/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib</code> (ver 3.11.5)
+ numpy:                       <code>/usr/local/lib/python3.11/site-packages/numpy/core/include</code> (ver 1.26.0)
+ install path:                <code>lib/python3.11/site-packages/cv2/python-3.11</code>


## Logs OpenCV Contrib
* To be built: <code>aruco bgsegm bioinspired calib3d ccalib core datasets dnn dnn_objdetect dnn_superres dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc intensity_transform line_descriptor mcc ml objdetect optflow phase_unwrapping photo plot python3 quality rapid reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking ts video videoio videostab wechat_qrcode xfeatures2d ximgproc xobjdetect xphoto</code>
* Disabled: <code>world</code>
* Disabled by dependency: -    
* Unavailable: <code>alphamat cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev cvv freetype hdf java julia matlab ovis python2 sfm viz</code>

> <code>make </code>

> <code>make install </code>