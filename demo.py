import cv2
from PIL import Image
import face_recognition

vidcap = cv2.VideoCapture("security_cam_feed.MOV")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Face Detection Result.avi', fourcc, 20.0, (1280, 720))
count = 0
while count < 1060:
    ret,frame = vidcap.read()
    resized_image = cv2.resize(frame, (1280,720))
    # cv2.imwrite("frame%d.jpg" % count, resized_image);

    # Load the jpg file into a numpy array
    #image = face_recognition.load_image_file("frame%d.jpg" % count)

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(resized_image)
    
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location

        cv2.rectangle(resized_image, (left, top), (right, bottom), (0, 255, 0), 2)

    # You can access the actual face itself like this:
    face_image = resized_image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    
    known_names = ["asmita", "brandy", "Derek_leung", "ming", "namita", "sharif", "victoria"]
    for known_name in known_names:
    	known_face_image = face_recognition.load_image_file("static/images/faces/known/{}.jpg".format(known_name))
        
    #cv2.imshow('security footage',resized_image)
    out.write(resized_image)
    percent = count / 10.6
    print("Writing to video: {}% done".format(percent), end='\r')
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
vidcap.release()
cv2.destroyAllWindows()
print("Face Detection Result.avi has been written successfully.")
