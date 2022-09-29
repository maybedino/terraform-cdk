# DOCS_BLOCK_START:assets
from constructs import Construct
import cdktf
import imports.aws as aws
import os

class MyStack(cdktf.TerraformStack):
    def __init__(self, scope: Construct, name: str):
        super().__init__(scope, name)

        aws.AwsProvider(self, 'aws', region='eu-central-1')

        bucket = aws.s3.S3Bucket(self, "bucket", bucket="demo")

        asset = cdktf.TerraformAsset(self, "lambda-asset",
                                     path=os.path.join(os.path.dirname(
                                         __file__), 'lambda'),
                                     type=cdktf.AssetType.ARCHIVE
                                     )

        aws.s3.S3BucketObject(self, "lambda-archive",
                              bucket=bucket.bucket,
                              key=asset.file_name,
                              source=asset.path
                              )
        x

app = cdktf.App()
MyStack(app, "demo")

app.synth()
# DOCS_BLOCK_END:assets
