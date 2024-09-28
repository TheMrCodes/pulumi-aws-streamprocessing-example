# Stream Processing Project

This project is a minimal AWS Python Pulumi program for stream processing. It sets up AWS resources such as Kinesis Data Streams, S3 buckets, and SNS topics.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.6+](https://www.python.org/downloads/)
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Setup

1. **Clone the repository:**

    ```sh
    git clone git@github.com:TheMrCodes/pulumi-aws-streamprocessing-example.git
    cd streamprocessing
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install .
    ```

4. **Configure AWS CLI:**

    Ensure your AWS CLI is configured with the necessary permissions to create resources. You can configure it using:

    ```sh
    aws configure
    ```

## Pulumi Configuration

1. **Login to Pulumi:**

    ```sh
    pulumi login --local
    ```

2. **Install Pulumi dependencies:**

    ```sh
    pulumi plugin install
    ```

3. **Configure Pulumi stack:**

    ```sh
    pulumi stack init streamprocessing
    ```

4. **Set AWS region:**

    ```sh
    pulumi config set aws:region <your-aws-region>
    ```

## Deploying the Infrastructure

1. **Preview the changes:**

    ```sh
    pulumi preview
    ```

2. **Deploy the stack:**

    ```sh
    pulumi up
    ```

    Confirm the deployment by typing `yes` when prompted.

## Cleaning Up

To destroy the resources created by Pulumi, run:

```sh
pulumi destroy
```
