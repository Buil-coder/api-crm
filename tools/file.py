import datetime, os, environs, uuid, sys, uuid, datetime
from pathlib import Path

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class FILE:
    # Creado por Neil Yesikov Cuadros Miraval 👈(ﾟヮﾟ👈)
    # Esta clase es para las imagenes, videos y archivos subidos a
    # los modelos solo llamando a la clase y el metodo


    @classmethod
    def create_path(self, folder:str):
        """Crea una ruta como:``AÑO``/``MES``/``FOLDER`` """
        return str('{}{}/{}/'.format(
            datetime.datetime.now().year,
            str(datetime.datetime.now().month).rjust(2, '0'),
            folder,
        ))


    @classmethod
    def create_uuid_name(self, prefix:str, extension:str):
        """Crea un nuevo nombre de arcivos como:``UUID``.``EXTENSION`` """
        return str('{}{}.{}'.format(
            prefix,
            uuid.uuid4(),
            extension
        ))


    @classmethod
    def image_path(self, instance, filename):
        return '{}/{}'.format(
            self.create_path(folder='IMAGES'),
            self.create_uuid_name(prefix='IMAGE_', extension=filename.split('.')[-1])
        )


    @classmethod
    def video_path(self, instance, filename):
        return '{}/{}'.format(
            self.create_path(folder='VIDEOS'),
            self.create_uuid_name(prefix='VIDEO_', extension=filename.split('.')[-1])
        )


    @classmethod
    def file_path(self, instance, filename):
        return '{}/{}'.format(
            self.create_path(folder='FILES'),
            self.create_uuid_name(prefix='FILE_', extension=filename.split('.')[-1])
        )

    @classmethod
    def resize_constraints(self, width, height):
        """
            Retorna nuevas dimensiones para las imagenes basadas en el
            tamaño maximo establecido
        """
        max_size = 1000
        if width < max_size and height < max_size:
            return (width, height)

        if width > height:
            return (max_size, int((height * max_size) / width))
        return (int((width * max_size) / height), max_size)


    @classmethod
    def manage_image(self, image):
        default_extension = 'png'
        image_temporary = Image.open(image)
        output_iostream = BytesIO()

        image_temporary_resized = image_temporary.resize(
            self.resize_constraints(image_temporary.width ,image_temporary.height)
        )
        image_temporary.close()

        image_temporary_resized.save(
            output_iostream,
            format=default_extension,
            quality=100
        )
        output_iostream.seek(0)

        return InMemoryUploadedFile(
            output_iostream,
            "ImageField",
            self.create_uuid_name("IMAGE_", default_extension),
            default_extension,
            sys.getsizeof(output_iostream),
            None
        )