#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Base  # Make sure Base is imported

# 1️⃣ Create engine and session
engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()

# 2️⃣ Optional: create tables if they don't exist
Base.metadata.create_all(engine)

# 3️⃣ Clear old data
session.query(Game).delete()
session.commit()

# 4️⃣ Add fixed games
fixed_games = [
    Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60),
    Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30),
    Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
]
session.add_all(fixed_games)
session.commit()

# 5️⃣ Add 50 random games using Faker
fake = Faker()
random_games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]
session.add_all(random_games)
session.commit()

print("Seeding complete!")
