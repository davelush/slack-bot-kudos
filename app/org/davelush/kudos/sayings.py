import random


class Sayings(object):

    @staticmethod
    def received_kudos_saying(user, amount):
        kudos_sayings = [f"Whoop whoop. You now have {amount} kudos {user}!",
                         f"You're flying to the moon {user} :rocket: :last_quarter_moon_with_face: You now have {amount} kudos",
                         f":fireball: {user} is on fire with {amount} kudos :fire:...... :fire_engine:",
                         f"Everyone knows you're a little :unicorn: {user} :unicorn: This puts you on {amount} kudos",
                         f"Who has {amount} kudos {user}? You do... You have {amount} kudos :star:"
                         ]
        return random.choice(kudos_sayings)

