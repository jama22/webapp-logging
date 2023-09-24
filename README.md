# webapp-logging
Basic Web app and logs

## Deploying the web app
gcloud run deploy weblogging --soruce ./webapps

## Deploy the function
gcloud functions deploy weblog-log-function \
    --source ./functions/log-pubsub \
     --runtime python311 \
     --trigger-topic weblog-log-ps \
     --entry-point hello_pubsub \
     --no-gen2