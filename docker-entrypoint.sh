#!/bin/sh

if [ "$ENV_TYPE" = "dev" ]
then
    exec uvicorn pyrometheus.main:app --reload --host 0.0.0.0
else
    exec uvicorn pyrometheus.main:app --host 0.0.0.0
fi
