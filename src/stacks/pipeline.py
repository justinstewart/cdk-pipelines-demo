import dataclasses

import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
    ManualApprovalStep,
)
from .api import ApiStack


@dataclasses.dataclass
class DeploymentEnvironment:
    name: str
    environment: cdk.Environment
    require_manual_approval: bool = False


class ApiDeploymentStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ApiStack(self, f"{construct_id}-api")


class PipelineStack(cdk.Stack):
    """
    The CodePipelineStack kicks off any time a change has been made
    to the AWS CDK app.
    """
    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            connection_arn: str,
            repo,
            branch,
            deployment_envs: list[DeploymentEnvironment],
            **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        synth_step = ShellStep(
            "Synth",
            input=CodePipelineSource.connection(
                repo, branch, connection_arn=connection_arn
            ),
            commands=[
                "npm install -g aws-cdk@2.158",
                "curl -sSL https://install.python-poetry.org | python3 -",
                "/root/.local/bin/poetry install",
                "/root/.local/bin/poetry run cdk synth",
            ],
            primary_output_directory="projects/base-cdk-python/cdk.out",
        )
        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="RootPipeline",
            synth=synth_step,
            cross_account_keys=True,
        )
        for deployment_env in deployment_envs:
            stage = pipeline.add_stage(
                ApiDeploymentStage(
                    self, f"{deployment_env.name}-stage", env=deployment_env.environment
                )
            )
            if deployment_env.require_manual_approval:
                stage.add_pre(
                    ManualApprovalStep(f"{deployment_env.name}-approval")
                )
