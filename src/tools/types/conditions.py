class Conditions:

    """
    Format: Wound State name: (Wound effect, Stabilization DV)
    """
    wound_states = {
        "Lightly Wounded": ("None", "DV10", None),
        "Seriously Wounded": ("-2 all actions", "DV13", None),
        "Mortally Wounded": ("-4 all actions, -6 MOVE (min 1), roll DS start of each turn, any ranged/melee attack = crit, and DSP +1", "DV15 to regain 1HP and become unconscious for 1 minute", None),
        "Dead": ("Death", None, None)
    }

    """
    Format: Injury: (Injury Effect, Quick Fix DV, Treatment DV)
    """
    body_critical_injuries = {
        "Dismembered Arm": ("Arm gone, DSP +1", "N/A", "Surgery DV17"),
        "Dismembered Hand": ("Hand gone, DSP +1", "N/A", "Surgery DV17"),
        "Collapsed Lung": ("-2 MOVE (min 1), DSP +1", "Paramedic DV15", "Surgery DV15"),
        "Broken Ribs": ("Move more than 4m/yds in turn = re-suffer critical injury bonus damage at end of turn", "Paramedic DV13", "Paramedic DV15 OR Surgery DV13"),
        "Broken Arm": ("Cannot use arm, drop any item", "Paramedic DV13", "Paramedic DV15 OR Surgery DV13"),
        "Foreign Object": ("Move more than 4m/yds in turn = re-suffer critical injury bonus damage at end of turn", "FirstAid OR Paramedic DV13", "Quick Fix removes permanently"),
        "Broken Leg": ("-4 MOVE (min 1)", "Paramedic DV13", "Paramedic DV15 OR Surgery DV13"),
        "Torn Muscle": ("-2 to Melee Attacks", "FirstAid OR Paramedic DV13", "Quick Fix removes permanently"),
        "Spinal Injury": ("Next turn: lose Action (can still MOVE), DSP +1", "Paramedic DV15", "Surgery DV15"),
        "Crushed Fingers": ("-4 to all Actions involving hand", "Paramedic DV13", "Surgery DV15"),
        "Dismembered Leg": ("Leg gone, -6 MOVE (min 1), cannot dodge, DSP +1", "N/A", "Surgery DV17")
    }

    """
    Format: Injury: (Injury Effect, Quick Fix DV, Treatment DV)
    """
    head_critical_injuries = {
        "Lost Eye": ("Eye gone, -4 to ranged attacks and perception checks involving vision, DSP +1", "N/A", "Surgery DV17"),
        "Brain Injury": ("-2 to all actions, DSP +1", "N/A", "Surgery DV17"),
        "Damaged Eye": ("-4 to ranged attacks and perception checks involving vision", "Paramedic DV15", "Surgery DV13"),
        "Concussion": ("-2 to all Actions", "FirstAid OR Paramedic DV13", "Quick Fix removes permanently"),
        "Broken Jaw": ("-4 to all speech-based Actions", "Paramedic DV13", "Paramedic OR Surgery DV13"),
        "Foreign Object": ("Move more than 4m/yds in turn = re-suffer critical injury bonus damage at end of turn", "FirstAid OR Paramedic DV13", "Quick Fix removes permanently"),
        "Whiplash": ("DSP +1", "Paramedic DV13", "Paramedic OR Surgery DV13"),
        "Cracked Skull": ("Headshot multiplier = 3x from 2x, DSP +1", "Paramedic DV15", "Paramedic OR Surgery DV15"),
        "Damaged Ear": ("Move more than 4m/yds in turn = no MOVE next turn, -2 to perception checks involving hearing", "Paramedic DV13", "Surgery DV13"),
        "Crushed Windpipe": ("Cannot speak, DSP +1", "N/A", "Surgery DV15"),
        "Lost Ear": ("Ear gone, move more than 4m/yds in turn = no MOVE next turn, -4 to perception checks involving hearing, DSP +1", "N/A", "Surgery DV17")
    }

    def get_all_conditions():
        combined = dict()
        combined.update(Conditions.wound_states)
        combined.update(Conditions.body_critical_injuries)
        combined.update(Conditions.head_critical_injuries)
        return combined
