#manage.py

import sys, os
from flask.cli import FlaskGroup
from app import create_app


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('train_model')
def train_model():
    #TODO: create cli to train model
    pass
    
if __name__ == "__main__":
    cli()   