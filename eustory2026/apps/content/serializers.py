import os
import requests
from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import ContentBlock, Source

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'
        extra_kwargs = {
            'author': {'read_only': True},  # Author will be set automatically by the view
            'image_url': {'write_only': True}  # This field is only for input
        }
    

    
    def validate(self, data):
        # If it's an image content type, require either image file or image_url
        if data.get('content_type') == 'image':
            if not data.get('image') and not data.get('image_url'):
                raise serializers.ValidationError(
                    "Les images nécessitent soit un fichier téléchargé, soit une URL d'image."
                )
        return data
    
    def create(self, validated_data):
        image_url = validated_data.pop('image_url', None)
        
        # If we have an image URL, download the image and save it locally
        if image_url and validated_data.get('content_type') == 'image':
            try:
                # Download the image
                response = requests.get(image_url, stream=True)
                response.raise_for_status()
                
                # Create a file-like object using tempfile
                from tempfile import NamedTemporaryFile as TempFile
                img_temp = TempFile()
                for chunk in response.iter_content(chunk_size=8192):
                    img_temp.write(chunk)
                img_temp.flush()
                
                # Get the filename from the URL
                filename = os.path.basename(image_url) or f"downloaded_image_{ContentBlock.objects.count() + 1}.jpg"
                
                # Create the content file from the temporary file
                img_temp.seek(0)  # Reset file pointer to beginning
                content_file = ContentFile(img_temp.read(), name=filename)
                
                # Save the image to the model
                content_block = ContentBlock.objects.create(image=content_file, image_url=image_url, **validated_data)
                
                # Debug: log the final image URL
                print(f"Image saved. Local path: {content_block.image.url if content_block.image else 'None'}")
                
                # Close and cleanup the temporary file
                img_temp.close()
                
            except requests.exceptions.SSLError as e:
                # Handle SSL certificate errors specifically
                content_block = ContentBlock.objects.create(image_url=image_url, **validated_data)
                error_msg = f"SSL Certificate Error: Failed to download image from {image_url}. The URL might be invalid or the site uses an untrusted certificate."
                print(error_msg)
                # Store the error in the text field for debugging
                if not validated_data.get('text'):
                    content_block.text = f"[IMAGE DOWNLOAD ERROR] {error_msg}"
                    content_block.save()
            except requests.exceptions.RequestException as e:
                # Handle other request errors (404, timeout, etc.)
                content_block = ContentBlock.objects.create(image_url=image_url, **validated_data)
                error_msg = f"Download Error: Failed to download image from {image_url}. Error: {str(e)}"
                print(error_msg)
                if not validated_data.get('text'):
                    content_block.text = f"[IMAGE DOWNLOAD ERROR] {error_msg}"
                    content_block.save()
            except Exception as e:
                # Handle any other unexpected errors
                content_block = ContentBlock.objects.create(image_url=image_url, **validated_data)
                error_msg = f"Unexpected Error: Failed to download image from {image_url}. Error: {str(e)}"
                print(error_msg)
                if not validated_data.get('text'):
                    content_block.text = f"[IMAGE DOWNLOAD ERROR] {error_msg}"
                    content_block.save()
        else:
            # Normal creation for non-image content
            content_block = ContentBlock.objects.create(**validated_data)
        
        return content_block
    
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'