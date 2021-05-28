# resume_serverless
Serverless resume project inspired by the resume challange.

https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resume-in-azure


In order to finalize SAM deployment, the id and hits values must be initialized in DynamoDB for the Lambda function to be operational.

aws dynamodb put-item --table-name test --item '{\"id\":{\"N\":\"0\"},\"hits\": {\"N\":\"0\"}}'