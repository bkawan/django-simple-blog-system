import uuid
import os


def get_image_path(instance, filename):
    """Store image in the directory of it's class name."""
    class_name = instance.__class__.__name__
    image_directory = 'uploads/images/{}'.format(class_name)
    extension = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), extension)
    return os.path.join(image_directory, filename)


def get_file_path(instance, filename):
    """Store file in the directory of it's class name."""
    class_name = instance.__class__.__name__
    file_directory = 'uploads/files/{}'.format(class_name)
    extension = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), extension)
    return os.path.join(file_directory, filename)
