#
-include GNUmakefile.local

#
NAME?=		monitoring-t2
NOW?=		$(shell date +%s)
ROLE?=		Role-Lambda-Montoring-T2

#
ifdef PROFILE
export AWS_DEFAULT_PROFILE=${PROFILE}
else
export AWS_DEFAULT_PROFILE=default
endif

ifdef REGION
export AWS_DEFAULT_REGION=${REGION}
else
export AWS_DEFAULT_REGION=us-west-2
endif

#
.DEFAULT_GOAL:=	${NAME}.zip
.PHONY:		clean setup-lambda setup-role

#
clean:
	rm -f -- "${NAME}.zip"
	rm -fr site-packages/

setup-lambda: ${NAME}.zip
	aws lambda create-function --function "${NAME}" --runtime python3.6 --role "arn:aws:iam::${ACCOUNT_ID}:role/${ROLE}" --handler "${NAME}.lambda_handler" --function-name "${NAME}" --zip-file "fileb://${NAME}.zip" --timeout 60 --memory-size 128 || true

setup-role:
	aws iam create-role --role-name "${ROLE}" --assume-role-policy-document '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}}' || true
	aws iam attach-role-policy --role-name "${ROLE}" --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole || true
	aws iam attach-role-policy --role-name "${ROLE}" --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess || true

site-packages: requirements.txt
	pip3 install -t site-packages/ -r requirements.txt

${NAME}.zip: ${NAME}.py site-packages
	zip -9 -q -r "${NAME}.zip" . -x '*.git*'
	( cd site-packages && zip -9 -q -r "../${NAME}.zip" * ) || true
