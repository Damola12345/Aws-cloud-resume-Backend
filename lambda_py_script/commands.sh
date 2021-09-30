#create an s3 bucket
aws s3 mb s3://damolacodelambdapyscript

#package 
sam package --s3-bucket damolacodelambdapyscript --template-file template.yml                                                  

# deploy
sam deploy --template-file deploy.yml --stack-name counter --capabilities CAPABILITY_IAM 