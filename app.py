import aws_cdk as cdk
from src.stacks.pipeline import PipelineStack, DeploymentEnvironment

CODESTAR_CONNECTION_ARN = "arn:aws:codestar-connections:us-east-2:730335243348:connection/db850af0-8994-4b59-b459-cbe0e2220ce9"  # noqa
OPERATIONS_US_EAST_2 = cdk.Environment(account="730335243348", region="us-east-2")
STAGING_US_EAST_2 = cdk.Environment(account="654654371827", region="us-east-2")
PRODUCTION_US_EAST_2 = cdk.Environment(account="851725358908", region="us-east-2")
GENERAL_ELECTRIC_US_WEST_2 = cdk.Environment(account="123456789012", region="us-west-2")


def main():
    app = cdk.App()
    PipelineStack(
        app,
        "CodePipelineDemo",
        connection_arn=CODESTAR_CONNECTION_ARN,
        repo="justinstewart/cdk-pipelines-demo",
        branch="main",
        deployment_envs=[
            DeploymentEnvironment(
                name="staging",
                environment=STAGING_US_EAST_2
            ),
            DeploymentEnvironment(
                name="production",
                environment=PRODUCTION_US_EAST_2,
                require_manual_approval=True
            ),
            DeploymentEnvironment(
                name="ge",
                environment=GENERAL_ELECTRIC_US_WEST_2,
                require_manual_approval=True
            )
        ],
        env=OPERATIONS_US_EAST_2,
    )
    app.synth()


if __name__ == "__main__":
    main()
