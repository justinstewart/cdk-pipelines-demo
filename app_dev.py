from aws_cdk import App

from src.stacks.dev import DevStack

from src.config import DEVELOPMENT_US_EAST_2


def main():
    app = App()
    DevStack(app, "DevStack", env=DEVELOPMENT_US_EAST_2)
    app.synth()


if __name__ == "__main__":
    main()
