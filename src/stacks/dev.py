from aws_cdk import Stack
from constructs import Construct

from ..constructs.api import Api


class DevStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        Api(self, "Api")
