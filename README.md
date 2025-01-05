
# LOG8415 - Assignment 1: Load Balancer Deployment

This project focuses on deploying a load balancer using AWS services to manage traffic across multiple EC2 instances running a FastAPI application.

## Objectives

- **Deploy** EC2 instances in two clusters: `t2.micro` and `t2.large`.
- **Implement** a FastAPI application on each instance to handle incoming requests.
- **Configure** an Application Load Balancer (ALB) to distribute traffic between the clusters.
- **Set up** routing rules based on URL paths for each cluster.
- **Perform** performance tests using a benchmarking script.

## Project Structure

- `src/`: Contains the Python scripts for deploying resources and running benchmarks.
- `images/`: Includes diagrams and screenshots related to the project setup.
- `README.md`: This file, providing an overview of the project.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Prerequisites

Ensure you have the following installed:

- Python 3.8
- AWS CLI configured with appropriate permissions
- Boto3 library for AWS interactions

Install the required Python packages:

```bash
pip install -r requirements.txt
