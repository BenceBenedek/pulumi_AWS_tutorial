"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)

bucketList = ["Raw-bucket", "Trusted-bucket", "Cleansed-bucket"]

for item in bucketList:

    bucket = s3.Bucket(item)

    # Export the name of the bucket
    pulumi.export('bucket_name', bucket.id)
