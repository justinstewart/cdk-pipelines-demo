from aws_cdk import App, Environment

from src.stacks.api import ApiStack

DEVELOPMENT_US_EAST_2 = Environment(
    account="058264246364", region="us-east-2"
)


def main():
    app = App()
    ApiStack(app, "DevStack", env=DEVELOPMENT_US_EAST_2)
    app.synth()


if __name__ == "__main__":
    main()
