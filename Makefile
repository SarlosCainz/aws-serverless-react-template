.PHONY: deploy deploy_lambda deploy_ui build_ui

deploy: deploy_ui deploy_lambda

deploy_lambda:
	sls deploy --stage dev
deploy_ui: build_ui
	cd ui/dist &&  aws s3 sync --delete . s3://aws-serverless-react-template/html/
build_ui:
	cd ui && npm run build
