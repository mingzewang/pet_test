import os
import sys
import tarfile

import cv2 as cv
import numpy as np
import tensorflow as tf

from utils import  label_map_util
from utils import visualization_utils as vis_util

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = 'D:/tensorflow/handset/export/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('D:/tensorflow/handset/data', 'hand_label_map.pbtxt')

NUM_CLASSES = 3
detection_graph = tf.Graph()
capture = cv.VideoCapture(0)
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categorys = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categorys)


with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        while True:
            ret, image = capture.read()
            if ret is True:
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                image_np_expanded = np.expand_dims(image, axis=0)
                (boxes, scores, classes, num_detections) = sess.run([boxes, scores, classes, num_detections],
                                                                    feed_dict={image_tensor: image_np_expanded})
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    min_score_thresh=0.5,
                    use_normalized_coordinates=True,
                    line_thickness=4
                )
                c = cv.waitKey(5)
                if c == 27:  # ESC
                    break
                cv.imshow("Hand Gesture Demo", image)
            else:
                break
        cv.waitKey(0)
        cv.destroyAllWindows()