
from django.views.generic import TemplateView
import boto3

from datetime import datetime, timezone

from s3_app.models import Farmer_image


class Farmer_Image(TemplateView):
    template_name = 'farmer.html'


    today = datetime.now(timezone.utc)

    s3 = boto3.client('s3', region_name = 'ap-south-1',
                      aws_access_key_id='AKIASR7S365YF66LBQ65',
                      aws_secret_access_key='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'
                      )

    objects = s3.list_objects(Bucket='gisfy-stage', Prefix='CustomData/')

    for o in objects["Contents"]:

        if o["LastModified"] != today:
            a = []
            a.append(o["Key"] + " " + str(o["LastModified"]))
            print(o["Key"] + " " + str(o["LastModified"]))
            img=Farmer_image()
            img.image_name=o["Key"]
            img.date_time= str(o["LastModified"])
            # img.save()







