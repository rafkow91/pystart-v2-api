#!/bin/sh

if [ "$ENV_TYPE" = "dev" ]
then
    exec uvicorn main:app --reload --host 0.0.0.0
else
    exec uvicorn main:app --host 0.0.0.0
fi
