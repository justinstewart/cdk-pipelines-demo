from pathlib import Path


from aws_cdk import (
    aws_ecs as ecs,
    aws_ecr_assets as ecr_assets,
    aws_ecs_patterns as ecs_patterns
)
from constructs import Construct


class Api(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Image
        directory = Path(__file__).parent.parent / "assets" / "api-image"
        asset = ecr_assets.DockerImageAsset(
            self,
            "ApiImage",
            directory=str(directory),
        )
        image = ecs.ContainerImage.from_docker_image_asset(asset)

        # Fargate Service
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "Service",
            cpu=512,
            memory_limit_mib=1024,
            task_image_options={
                "image": image,
            },
        )
