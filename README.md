# webapp-logging
Basic Web app and logs


## Web app

### Local dev
`python3 ./webapp/main.py`

### Local container
`pack build webapp --path ./webapp --builder gcr.io/buildpacks/builder:google-22`
`docker run --rm -p 8080:8080 webapp`

### Deploy to Cloud Run
gcloud run deploy weblogging --soruce ./webapps

## Deploy the function
gcloud functions deploy weblog-log-function \
    --source ./functions/log-pubsub \
     --runtime python311 \
     --trigger-topic weblog-log-ps \
     --entry-point hello_pubsub \
     --no-gen2