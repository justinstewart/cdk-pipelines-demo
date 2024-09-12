bootstrap-dev:
	npx cdk bootstrap --profile ${AWS_PROFILE_DEV} "aws://${AWS_ACCOUNT_ID_DEV}/${AWS_PRIMARY_REGION_DEV}"

bootstrap-operations:
	aws sso login --profile ${AWS_PROFILE_OPERATIONS}
	npx cdk bootstrap --profile ${AWS_PROFILE_OPERATIONS} "aws://${AWS_ACCOUNT_ID_OPERATIONS}/${AWS_PRIMARY_REGION_OPERATIONS}"

bootstrap-staging:
	aws sso login --profile ${AWS_PROFILE_STAGING}
	npx cdk bootstrap --profile ${AWS_PROFILE_STAGING} "aws://${AWS_ACCOUNT_ID_STAGING}/${AWS_PRIMARY_REGION_STAGING}" --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess" --trust ${AWS_ACCOUNT_ID_OPERATIONS}

bootstrap-production:
	aws sso login --profile ${AWS_PROFILE_PRODUCTION}
	npx cdk bootstrap --profile ${AWS_PROFILE_PRODUCTION} "aws://${AWS_ACCOUNT_ID_PRODUCTION}/${AWS_PRIMARY_REGION_PRODUCTION}" --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess" --trust ${AWS_ACCOUNT_ID_OPERATIONS}

install:
	poetry install
	cd src/assets/api-image && poetry install

deploy:
	npx cdk@2.158 deploy -a "poetry run python app.py" --profile sandbox-operations

deploy-dev:
	npx cdk@2.158 deploy --profile sandbox-dev -a "poetry run python app_dev.py"

diff-dev:
	npx cdk@2.158 diff --profile sandbox-dev -a "poetry run python app_dev.py"

test:
	cd src/assets/api-image && poetry run pytest
