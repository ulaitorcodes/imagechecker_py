from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
import cv2
import numpy as np

class ImageView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the uploaded image file
        image_file = request.data.get('image_file')

        # OpenCV for image recognition (you may need to adjust this based on your specific requirements)
        # Here, we're using a simple example of computing the hash of the image
        img = cv2.imread(image_file.temporary_file_path())
        img_hash = cv2.hash(img, cv2.HASH_SHA256)

        # Check if an image with the same hash already exists in the database
        if Image.objects.filter(image_hash=img_hash).exists():
            return Response({'error': 'Duplicate image. The same image cannot be uploaded twice.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the image to the database
        image = Image.objects.create(image_file=image_file, image_hash=img_hash)
        serializer = ImageSerializer(image)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
