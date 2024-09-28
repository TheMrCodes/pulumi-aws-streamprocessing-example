import os
import pulumi
import pulumi_aws as aws
import dotenv
dotenv.load_dotenv()

PROJECT_ROLE = os.getenv("PROJECT_ROLE_ARN")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

# Define existing Project Role
role_info = aws.iam.get_role(name="LabRole")
PROJECT_ROLE_ARN = role_info.arn

# Create a Kinesis Data Stream
kinesis_stream = aws.kinesis.Stream(
    "turbine-data-stream", 
    stream_mode_details={
        "stream_mode": "ON_DEMAND"
    },
)

# Create an S3 bucket for Firehose to deliver data
bucket = aws.s3.Bucket("turbine-data-bucket")

# Create a Kinesis Data Firehose Delivery Stream
firehose = aws.kinesis.FirehoseDeliveryStream(
    "turbine-data-firehose",
    destination="extended_s3",
    extended_s3_configuration={
        "bucket_arn": bucket.arn,
        "role_arn": PROJECT_ROLE_ARN,
    },
    kinesis_source_configuration={
        "kinesis_stream_arn": kinesis_stream.arn,
        "role_arn": PROJECT_ROLE_ARN,
    },
)

# Create an SNS topic with the admin email as a subscriber
topic = aws.sns.Topic("turbine-data-topic")
email_subscription = aws.sns.TopicSubscription(
    "turbine-data-topic-subscription",
    topic=topic.arn,
    protocol="email",
    endpoint=ADMIN_EMAIL,
)


# Export the whole stack
pulumi.export("kinesis_stream_name", kinesis_stream.name)
pulumi.export("firehose_name", firehose.name)
pulumi.export("bucket_name", bucket.bucket)
pulumi.export("topic_name", topic.name)
