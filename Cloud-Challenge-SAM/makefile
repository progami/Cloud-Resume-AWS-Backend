.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec Jarrar --no-session -- sam deploy

deploy-site:
	aws-vault exec Jarrar --no-session -- aws s3 sync ./resume-site s3://my-fantastic-website1337

invoke-put:
	sam build && aws-vault exec Jarrar --no-session -- sam local invoke PutFunction

invoke-get:
	sam build && aws-vault exec Jarrar --no-session -- sam local invoke GetFunction
