import random


class Sayings(object):

    @staticmethod
    def received_kudos_saying(user, amount):
        kudos_sayings = [f"Whoop whoop. You now have {amount} kudos {user}!",
                         f"You're flying to the moon {user} :rocket: :last_quarter_moon_with_face: You now have {amount} kudos",
                         f":fireball: {user} is on fire with {amount} kudos :fire:...... :fire_engine:",
                         f"Everyone knows you're a little unicorn :unicorn: {user} :unicorn: This puts you on {amount} kudos",
                         f"Who has {amount} kudos {user}? You do... You have {amount} kudos :star:",
                         f":trophy: :trophy: :chicken: :knife_fork_plate: Winner winner chicken dinner :trophy: :trophy: :chicken: :knife_fork_plate: {user} has {amount} kudos",
                         f":dart: That's band on target {user} :dart: You now have {amount} kudos",
                         f":fishing_pole_and_fish: Have you been fishing for compliments {user}? :fishing_pole_and_fish: Well it worked! You have {amount} kudos",
                         f":church: :raised_hands: All praise {user} :raised_hands: :church: You have {amount} kudos",
                         f":hypnotoad: Hypnotoad says `all praise` {user}... `Give them more kudos` :hypnotoad: You now have {amount} kudos",
                         f"You're in pole position {user} :racing_car::racing_car::racing_car::racing_car::racing_car: You have {amount} kudos",
                         f":gem: :gem: You little diamond {user} :gem: :gem: You now have {amount} kudos",
                         ]
        return random.choice(kudos_sayings)

