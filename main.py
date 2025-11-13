from retinaface import RetinaFace
import matplotlib.pyplot as plt
from deepface import DeepFace

faces = RetinaFace.extract_faces(img_path = "7.jpeg", align = True)
for face in faces:
  plt.imshow(face)
  plt.show()

obj = DeepFace.verify("4.jpeg", "7.jpeg"
          , model_name = 'ArcFace', detector_backend = 'retinaface')
print(obj["verified"])