# Old Photo Dataset

This is the implementation of the paper "Monocular Depth Estimation of Old Photos via Collaboration of Monocular and Stereo Networks", IEEE Access, Ju Ho Kim, Kwang-Lim Ko, Le Thanh Ha, and Seung-Won Jung


# Folder Description

```
Old_photo_dataset         : Description of the dataset.
Pairwise_comparison       : Description of the pairwise comparison tool.
Main_Code                 : Main Code
image                     : Sample images
```

# Dataset Description

The dataset was crawled old photos from onlie library.
[Library of congress](https://www.loc.gov/pictures/)

We select 5 collection

Collection | Number of images
---- | ----
[Abdul Hamid II Collection](https://www.loc.gov/pictures/collection/ahii/) | 1774 images
<br>
[Carpenter Collection](https://www.loc.gov/pictures/collection/ffcarp/) | 1657 images
<br>
[Grabil Collection](https://www.loc.gov/pictures/collection/grabill/) | 248 images
<br>
[Lawrence & Houseworth Collection](https://www.loc.gov/pictures/collection/lawhou/) | 792 images
<br>
[Genthe Collection](https://www.loc.gov/pictures/collection/agc/) - [Travel views of Japan and Korea](https://www.loc.gov/pictures/search/?q=Travel+views+of+Japan+and+Korea&sp=1&st=gallery) | 613 images
<br>
Total 5084 images

We use Old Photo Restoration technique [Bringing-Old-Photos](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life)

###### Before Old Photo Restoration:
<p align="center">
<img src="https://github.com/rmawngh/Old-Photo-3D/blob/main/image/old_photo_example.jpg">
</p>

###### After Old Photo Restoration:
<p align="center">
<img src="https://github.com/rmawngh/Old-Photo-3D/blob/main/image/restorated_old_photo_example.jpg">
</p>


## Acknowledgments
[Library of congress](https://www.loc.gov/pictures/)
