# Pairwise comparision

Official github of the paper "Monocular Depth Estimation of Old Photos via Collaboration of Monocular and Stereo Networks", IEEE Access, Ju Ho Kim, Kwang-Lim Ko, Le Thanh Ha, and Seung-Won Jung


# Requirements

This code is implemented with Python 3.6 (Anaconda)

```
open3d==0.12.0
numpy
screeninfo
opencv-python
```


# Old Photo Dataset

The dataset was crawled old photos from onlie library.
[Library of congress](https://www.loc.gov/pictures/)

[Old Photo Restoration](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life) was used for dataset. 


# Folder Description

```
old_depth     : depth result images
old_xyz       : xyzrgb.txt files
original_old  : original(before restoration) images
restored_old  : restored(after restoration) images
```


# GUI example

<img src="https://github.com/rmawngh/Old-Photo-3D/blob/main/Pairwise_comparison/gui_example.png">
