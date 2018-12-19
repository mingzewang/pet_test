import cv2 as cv
import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

root_dir = "D:/hand_data/VOC2012/JPEGImages/"


def change_to_jpg():
    files = os.listdir(root_dir)
    for img_file in files:
        if os.path.isfile(os.path.join(root_dir, img_file)):
            image_path = os.path.join(root_dir, img_file)
            print(image_path)
            image = cv.imread(image_path)
            print(image_path.replace("png","jpg"))
            cv.imwrite(image_path.replace("png","jpg"), image)


def xml_modification():
    ann_dir = "D:/hand_data/VOC2012/Annotations/"
    files = os.listdir(ann_dir)
    for xml_file in files:
        if os.path.isfile(os.path.join(ann_dir, xml_file)):
            xml_path = os.path.join(ann_dir, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # changing a field text
            for elem in root.iter('folder'):
                elem.text = 'voc2012'

            for elem in root.iter('name'):
                name = elem.text
                elem.text = name.replace(" ", "")

            for elem in root.iter('filename'):
                filename = elem.text
                filename = filename.replace("png", "jpg")
                elem.text = filename

            for elem in root.iter('path'):
                path = elem.text
                path = path.replace("png", "jpg")
                path = path.replace("D:\gloomyfish\pupil", "D:\hand_data\VOC2012\JPEGImages")
                elem.text = path

            tree.write(xml_path)
            print("processed xml : %s" % (xml_path))


def generate_classes_text():
    print("start to generate classes text...")
    ann_dir = "D:/hand_data/VOC2012/Annotations/"

    handone_train = open("D:/hand_data/VOC2012/ImageSets/Main/handone_train.txt", 'w')
    handone_val = open("D:/hand_data/VOC2012/ImageSets/Main/handone_val.txt", 'w')

    handfive_train = open("D:/hand_data/VOC2012/ImageSets/Main/handfive_train.txt", 'w')
    handfive_val = open("D:/hand_data/VOC2012/ImageSets/Main/handfive_val.txt", 'w')

    handtwo_train = open("D:/hand_data/VOC2012/ImageSets/Main/handtwo_train.txt", 'w')
    handtwo_val = open("D:/hand_data/VOC2012/ImageSets/Main/handtwo_val.txt", 'w')

    files = os.listdir(ann_dir)
    for xml_file in files:
        if os.path.isfile(os.path.join(ann_dir, xml_file)):
            xml_path = os.path.join(ann_dir, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            for elem in root.iter('filename'):
                filename = elem.text
            for elem in root.iter('name'):
                name = elem.text

            if name == "handone":
                handone_train.write(filename.replace(".jpg", " ") + str(1) + "\n")
                handone_val.write(filename.replace(".jpg", " ") + str(1) + "\n")

                handfive_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handfive_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")

                handtwo_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handtwo_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")
            if name == "handtwo":
                handone_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handone_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")

                handfive_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handfive_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")

                handtwo_train.write(filename.replace(".jpg", " ") + str(1) + "\n")
                handtwo_val.write(filename.replace(".jpg", " ") + str(1) + "\n")

            if name == "handfive":
                handone_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handone_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")

                handfive_train.write(filename.replace(".jpg", " ") + str(1) + "\n")
                handfive_val.write(filename.replace(".jpg", " ") + str(1) + "\n")

                handtwo_train.write(filename.replace(".jpg", " ") + str(-1) + "\n")
                handtwo_val.write(filename.replace(".jpg", " ") + str(-1) + "\n")

    handone_train.close()
    handone_val.close()
    handfive_train.close()
    handfive_val.close()
    handtwo_train.close()
    handtwo_val.close()


xml_modification()