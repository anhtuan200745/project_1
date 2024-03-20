import pydicom
import matplotlib.pyplot as plt


def display_dicom_image(dicom_file_path,new_image_name):

    dicom_data = pydicom.dcmread(dicom_file_path)
    pixel_data = dicom_data.pixel_array

    plt.imshow(pixel_data, cmap=plt.colormaps['gray'])
    plt.axis('off')
    plt.show()

    plt.imsave(new_image_name, pixel_data,cmap=plt.colormaps['gray'])


display_dicom_image('image-000001.dcm', 'image1.png')
