
player = None
monsters = []
projectiles = []


def run_monsters():
    for m in monsters:
        m.act()


def run_projectiles():
    for p in projectiles:
        p.act()

