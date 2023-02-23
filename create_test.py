import insightface
import numpy as np
import PIL.Image
def img_test(img):
    ar = []
    rows = ['100' , '200' , '300' , '10001' , '10002' , '4000' , '20001' , '20002' , '30002']
    for row in rows:
        img_sample = "./templates/img/"
        img_sample = img_sample + str(row)
        img_sample = img_sample + ".jpg"


        def read_image(file_path):
            image = PIL.Image.open(file_path).convert("RGB")
            image = np.array(image)
            image = image[:, :, [2, 1, 0]]  # RGB to BGR
            return image


        # REF: https://github.com/deepinsight/insightface/blob/f474870cc5b124749d482cf175818413a9fe12cd/python-package/insightface/model_zoo/arcface_onnx.py#L70
        def compute_sim(feat1, feat2):
            return np.dot(feat1, feat2) / (np.linalg.norm(feat1) * np.linalg.norm(feat2))


        face_analysis = insightface.app.FaceAnalysis()
        face_analysis.prepare(ctx_id=0, det_size=(640, 640))

        image1 = read_image(img)
        faces1 = face_analysis.get(image1)
        embedding1 = faces1[0].embedding

        image2 = read_image(img_sample)
        faces2 = face_analysis.get(image2)
        for val in faces2:
            embedding2 = val.embedding

            if compute_sim(embedding1, embedding2) >= 0.3:
                val = "./img/" + str(row) + ".jpg"
                ar.append(val)
    return ar
