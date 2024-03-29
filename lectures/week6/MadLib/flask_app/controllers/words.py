from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.word import *
import random

nouns = Noun.getAll()
nounPlurals = Nounplural.getAll()
foods = Food.getAll()
verbs = Verb.getAll()
verbings = Verbing.getAll()
verbpasts = Verbpast.getAll()
adjectives = Adjective.getAll()
shapes = Shape.getAll()
names = Name.getAll()
numbers = Number.getAll()
liquids = Liquid.getAll()
rooms = Room.getAll()
birds = Bird.getAll()
bodyparts = Bodypart.getAll()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/madLib01/')
def madLib01():
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounPlurRand01 = random.choice(nounPlurals)
    verbRand01 = random.choice(verbs)
    verbingRand01 = random.choice(verbings)
    verbingRand02 = random.choice(verbings)
    verbpastRand01 = random.choice(verbpasts)
    adjectRand01 = random.choice(adjectives)
    adjectRand02 = random.choice(adjectives)
    nameRand01 = random.choice(names)
    liquidRand01 = random.choice(liquids)
    roomRand01 = random.choice(rooms)
    birdRand01 = random.choice(birds)
    bodyRand01 = random.choice(bodyparts)
    return render_template('lib01.html',adjective01=adjectRand01, adjective02=adjectRand02, bird=birdRand01, room=roomRand01, verb01=verbpastRand01, verb02=verbRand01, name=nameRand01, noun01=nounRand01, liquid=liquidRand01, verb03=verbingRand01, body=bodyRand01, noun02=nounPlurRand01, verb04=verbingRand02, noun03=nounRand02)

@app.route('/madLib02/')
def madLib02():
    foodRand01 = random.choice(foods)
    foodRand02 = random.choice(foods)
    foodRand03 = random.choice(foods)
    nameRand01 = random.choice(names)
    adjectRand01 = random.choice(adjectives)
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounRand03 = random.choice(nouns)
    nounRand04 = random.choice(nouns)
    verbingRand01 = random.choice(verbs)
    verbingRand02 = random.choice(verbs)
    verbingRand03 = random.choice(verbs)
    return render_template('lib02.html', food01=foodRand01, food02=foodRand02, food03=foodRand03, name=nameRand01, adjective=adjectRand01, noun01=nounRand01, noun02=nounRand02, noun03=nounRand03, noun04=nounRand04, verb01=verbingRand01, verb02=verbingRand02, verb03=verbingRand03)

@app.route('/madLib03/')
def madLib03():
    adjectRand01 = random.choice(adjectives)
    adjectRand02 = random.choice(adjectives)
    adjectRand03 = random.choice(adjectives)
    adjectRand04 = random.choice(adjectives)
    nameRand01 = random.choice(names)
    nounRand01 = random.choice(nouns)
    nounRand02 = random.choice(nouns)
    nounRand03 = random.choice(nouns)
    nounPlurRand01 = random.choice(nounPlurals)
    foodRand01 = random.choice(foods)
    foodRand02 = random.choice(foods)
    shapeRand01 = random.choice(shapes)
    numRand01 = random.choice(numbers)
    numRand02 = random.choice(numbers)
    return render_template('lib03.html', adjective01=adjectRand01, adjective02=adjectRand02, adjective03=adjectRand03, adjective04=adjectRand04, name=nameRand01, noun01=nounRand01, noun02=nounRand02, noun03=nounRand03, noun04=nounPlurRand01, food01=foodRand01, food02=foodRand02, shape=shapeRand01, num01=numRand01, num02=numRand02)