import warnings, os
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from imageai.Classification import ImageClassification
def load():
    executionpath = os.getcwd()
    global detection
    detection = ImageClassification()
    
    detection.setModelTypeAsInceptionV3()
    detection.setModelPath(executionpath + '/models/inception_v3_weights_tf_dim_ordering_tf_kernels.h5')
    detection.loadModel()

def classifier(image_arg):
    
    detections, percentageprob = detection.classifyImage(image_arg,result_count=1)

    # for Index in range(len(detections)):
    #     print(detections[Index],':',percentageprob[Index])
    output = { detections[0] : percentageprob[0] }
    return output
