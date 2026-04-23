import json
from Utils.Config import Config
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Players:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        print("Creating config.json...")
        Config.create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    # Player data
    high_id = 0
    low_id = 0
    token = "None"
    IsFacebookLinked = 0
    FacebookID = "None"
    FacebookToken = "None"
    box_id = 0
    map_id = 7
    slot_index = 0
    room_id = 0
    brawler_id = 0
    skin_id = 0

    # Socket
    ClientDict = {}

    # Brawler data
    skins_id = Skins.get_skins_id()
    brawlers_id = Characters.get_brawlers_id()
    card_skills_id = Cards.get_spg_id()
    card_unlock_id = Cards.get_brawler_unlock()

    # General player (Brawler, Currency, etc..)
    display_message = settings["PopUpMessage"]
    env = settings["Environment"]
    region = settings["Region"]
    UnlockType = settings['UnlockedBrawlersOption']
    BrawlersDict = json.loads(json.dumps(settings['UnlockedBrawler'][0]))
    BrawlersUnlockedState = {}

    if UnlockType == "All":
        for i in brawlers_id:
            BrawlersUnlockedState[str(i)] = 1
    elif UnlockType == "SpecifiedOnly":
        index = 0
        for brawlers_name in BrawlersDict:
            BrawlersUnlockedState[str(index)] = BrawlersDict[brawlers_name]
            if index == 34:
                index += 3
            elif index == 32:
                index += 2
            else:
                index += 1
    elif UnlockType == "StarterOnly":
        starter = [0, 1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
        for i in brawlers_id:
            if i in starter:
                BrawlersUnlockedState[str(i)] = 1
            else:
                BrawlersUnlockedState[str(i)] = 0

    brawler_power_level = settings['BrawlerPowerLevel']
    brawler_trophies_for_rank = settings['BrawlerTrophiesForRank']
    brawler_trophies = settings['BrawlerTrophies']
    brawler_upgrade_points = settings['BrawlerUpgradePoints']
    brawlers_spg_unlock = {}
    gadget = 255
    starpower = 76

    brawlers_trophies = {}
    for id in brawlers_id:
        brawlers_trophies.update({f'{id}': brawler_trophies_for_rank})

    brawlers_skins = {}
    for id in brawlers_id:
        brawlers_skins.update({f'{id}': 0})

    name = "Guest"
    player_experience = 0
    profile_icon = 0
    name_color = 0
    do_not_distrub = 0
    brawl_boxes = settings['BrawlBoxTokens']
    big_boxes = settings['BigBoxTokens']
    star_points = settings['Starpoints']
    highest_trophies = 0
    trophies = settings['Trophies']
    solo_wins = 0
    duo_wins = 0
    ThreeVSThree_wins = 0
    tokensdoubler = 0
    player_tokens = 0
    gems = settings['Gems']
    gold = settings['Gold']
    tickets = settings['Tickets']
    exp_points = settings['ExperiencePoints']
    theme_id = 41000000 + settings['ThemeID']
    content_creator = settings['SupportedContentCreator']
    tokens = 0

    # Alliances
    club_high_id = 0
    club_low_id = 0
    club_role = 0

    # Message stuff...
    update_url = settings['UpdateUrl']
    patch_url = settings['PatchUrl']
    patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")
    maintenance_time = 0

    err_code = 7
    maintenance = False
    patch = False

    if settings['Patch']:
        error_code = 7
        patch = True

    if settings['Maintenance']:
        err_code = 10
        maintenance = True
        maintenance_time = settings['MaintenanceTime']

    # Chat data
    message_tick = 0
    bot_message_tick = 0

    brawlers_trophies_in_rank = {}
    brawlers_upgradium = {}
    Brawler_level = {}

    for id in brawlers_id:
        brawlers_trophies_in_rank[str(id)] = brawler_trophies_for_rank
        brawlers_upgradium[str(id)] = brawler_upgrade_points
        Brawler_level[str(id)] = brawler_power_level

    # Friendly game (Teams, info, result)
    battle_result = 0
    game_type = 0
    use_gadget = 1
    rank = 0
    team = 0
    isReady = 0
    shouldRedirect = settings['RedirectFromOnlineToOfflineGame']
    bot1 = 0
    bot1_n = None
    bot2 = 0
    bot2_n = None
    bot3 = 0
    bot3_n = None
    bot4 = 0
    bot4_n = None
    bot5 = 0
    bot5_n = None

    # === ДРУЗЬЯ ===
    friends_list = []
    incoming_requests = []
    outgoing_requests = []

    def CreateNewBrawlersList():
        Players.BrawlersUnlockedState = {}
        for id in Players.brawlers_id:
            if id == 0:
                Players.BrawlersUnlockedState[str(id)] = 1
            else:
                Players.BrawlersUnlockedState[str(id)] = 0
        return Players.BrawlersUnlockedState

    def __init__(self, device):
        self.device = device
