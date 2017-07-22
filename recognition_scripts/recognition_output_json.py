import scipy.misc
import warnings
import face_recognition.api as face_recognition


def test_image_output_json(image_to_check, known_names, known_face_encodings):
    unknown_image = face_recognition.load_image_file(image_to_check)

    # Scale down image if it's giant so things run a little faster
    if unknown_image.shape[1] > 1600:
        scale_factor = 1600.0 / unknown_image.shape[1]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            unknown_image = scipy.misc.imresize(unknown_image, scale_factor)

    unknown_encodings = face_recognition.face_encodings(unknown_image)

    output = list()

    for unknown_encoding in unknown_encodings:
        result = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

        if True in result:
            [output.append({'imagePath': image_to_check, 'name': name}) for is_match, name in zip(result, known_names) if is_match]
        else:
            [output.append({'imagePath': image_to_check, 'name': 'unknown_name'})]

    return output
