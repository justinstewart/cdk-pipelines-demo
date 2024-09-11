# Python CDK Starter Kit
This is a base project for developing Python-based CDK applications. It's inspired by:

- [AWS CDK Best Practices](https://docs.aws.amazon.com/cdk/latest/guide/best-practices.html)
- [AWS Cross Account Deployment](https://aws.amazon.com/blogs/mt/cross-account-deployments-aws-control-tower-environment/)

The service it deploys is {service description here}.

A quick overview:
- Development Account: a dedicated account for a single developer or an entire team. You can deploy the API stack directly to this account for testing purposes.
- Operations Account: a dedicated account for CI/CD. This is where a CodePipeline will be deployed that is triggered by changes to the CDK app.
- Staging Account: a dedicated account for staging changes before they're deployed to production. The API is deployed here and a manual approval step is then triggered before you can move onto the...
- Production Account: the actual account your users and customers will be served from.

## Development
The following are required to run this project:

- [Python 3.10+]](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [Node.js 18.x](https://nodejs.org/en/download/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)

Installing dependencies:

```bash
poetry install
```
