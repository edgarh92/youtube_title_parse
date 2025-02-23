# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import MetaTestSequence

tests = [
    {
        "input": "clipping. - Inside Out [OFFICIAL VIDEO]",
        "expected": ["clipping.", "Inside Out"],
    },
    {
        "input": "King Tuff - Black Moon Spell [OFFICIAL VIDEO]",
        "expected": ["King Tuff", "Black Moon Spell"],
    },
    {
        "input": "Sleater-Kinney - Bury Our Friends (feat. Miranda July)",
        "expected": ["Sleater-Kinney", "Bury Our Friends"],
    },
    {
        "input": "Pissed Jeans - Boring Girls [OFFICIAL VIDEO]",
        "expected": ["Pissed Jeans", "Boring Girls"],
    },
    {
        "input": "Father John Misty - Chateau Lobby #4 (in C for Two Virgins) [OFFICIAL VIDEO]",
        "expected": ["Father John Misty", "Chateau Lobby"],
    },
    {
        "input": "Chad VanGaalen - Monster [OFFICIAL VIDEO]",
        "expected": ["Chad VanGaalen", "Monster"],
    },
    {
        "input": "Luluc - Tangled Heart  [OFFICIAL VIDEO]",
        "expected": ["Luluc", "Tangled Heart"],
    },
    {
        "input": "J Mascis - Every Morning [OFFICIAL VIDEO]",
        "expected": ["J Mascis", "Every Morning"],
    },
    {
        "input": "THEESatisfaction - Recognition  (not the video)",
        "expected": ["THEESatisfaction", "Recognition"],
    },
    {
        "input": "Goat - Hide from the Sun [OFFICIAL VIDEO]",
        "expected": ["Goat", "Hide from the Sun"],
    },
    {
        "input": "Shabazz Palaces - Motion Sickness [OFFICIAL VIDEO]",
        "expected": ["Shabazz Palaces", "Motion Sickness"],
    },
    {
        "input": "The Afghan Whigs - Lost in the Woods [OFFICIAL VIDEO]",
        "expected": ["The Afghan Whigs", "Lost in the Woods"],
    },
    {
        "input": "The Head and the Heart - Another Story [OFFICIAL VIDEO]",
        "expected": ["The Head and the Heart", "Another Story"],
    },
    {
        "input": "Washed Out - Weightless [OFFICIAL VIDEO]",
        "expected": ["Washed Out", "Weightless"],
    },
    {
        "input": "Deaf Wish - Cool Comment [OFFICIAL VIDEO]",
        "expected": ["Deaf Wish", "Cool Comment"],
    },
    {
        "input": "Father John Misty - Bored In The USA",
        "expected": ["Father John Misty", "Bored In The USA"],
    },
    {
        "input": "Flake Music - Spanway Hits  (not the video)",
        "expected": ["Flake Music", "Spanway Hits"],
    },
    {
        "input": "Sleater-Kinney - Surface Envy",
        "expected": ["Sleater-Kinney", "Surface Envy"],
    },
    {
        "input": "clipping. - Get Up [OFFICIAL VIDEO]",
        "expected": ["clipping.", "Get Up"],
    },
    {"input": "King Tuff - Headbanger", "expected": ["King Tuff", "Headbanger"]},
    {
        "input": "Shabazz Palaces - #CAKE [OFFICIAL VIDEO]",
        "expected": ["Shabazz Palaces", "#CAKE"],
    },
    {
        "input": "The Afghan Whigs - Every Little Thing She Does is Magic (cover of The Police)",
        "expected": [
            "The Afghan Whigs",
            "Every Little Thing She Does is Magic",
        ],
    },
    {
        "input": "Mirel Wagner - The Dirt [OFFICIAL VIDEO]",
        "expected": ["Mirel Wagner", "The Dirt"],
    },
    {
        "input": "Avi Buffalo - Memories of You (not the video)",
        "expected": ["Avi Buffalo", "Memories of You"],
    },
    {"input": "Goat - Words (not the video)", "expected": ["Goat", "Words"]},
    {
        "input": "clipping. - Story 2 [OFFICIAL VIDEO]",
        "expected": ["clipping.", "Story 2"],
    },
    {
        "input": "Shabazz Palaces - #CAKE (Animal Collective Premature Deflirt Mix)",
        "expected": [
            "Shabazz Palaces",
            "#CAKE",
        ],
    },
    {
        "input": "Shorts Test - CAKE #Shorts",
        "expected": [
            "Shorts Test",
            "CAKE",
        ],
    },
    {"input": "Flake Music - The Shins", "expected": ["Flake Music", "The Shins"]},
    {
        "input": "J Mascis - Wide Awake (not the video)",
        "expected": ["J Mascis", "Wide Awake"],
    },
    {
        "input": "The Head and the Heart - Let's Be Still [OFFICIAL VIDEO]",
        "expected": ["The Head and the Heart", "Let's Be Still"],
    },
    {
        "input": "Luluc - Small Window [OFFICIAL VIDEO]",
        "expected": ["Luluc", "Small Window"],
    },
    {
        "input": "Lyla Foy - Honeymoon [OFFICIAL VIDEO]",
        "expected": ["Lyla Foy", "Honeymoon"],
    },
    {
        "input": "Avi Buffalo - So What [OFFICIAL VIDEO]",
        "expected": ["Avi Buffalo", "So What"],
    },
    {
        "input": "clipping. - Body & Blood [CENSORED VERSION of OFFICIAL VIDEO]",
        "expected": ["clipping.", "Body & Blood"],
    },
    {
        "input": "King Tuff - Eyes of the Muse (not the video)",
        "expected": ["King Tuff", "Eyes of the Muse"],
    },
    {"input": "Deaf Wish - St Vincent's", "expected": ["Deaf Wish", "St Vincent's"]},
    {
        "input": "The Afghan Whigs - Matamoros [OFFICIAL VIDEO]",
        "expected": ["The Afghan Whigs", "Matamoros"],
    },
    {
        "input": "Dum Dum Girls - Too True To Be Good [OFFICIAL VIDEO]",
        "expected": ["Dum Dum Girls", "Too True To Be Good"],
    },
    {
        "input": "J Mascis - Fade Into You (a Mazzy Star cover)",
        "expected": ["J Mascis", "Fade Into You"],
    },
    {
        "input": "Shabazz Palaces - Forerunner Foray",
        "expected": ["Shabazz Palaces", "Forerunner Foray"],
    },
    {
        "input": "Lee Bains III & The Glory Fires - The Company Man [OFFICIAL VIDEO]",
        "expected": ["Lee Bains III & The Glory Fires", "The Company Man"],
    },
    {
        "input": "The Postal Service - Nothing Better [LIVE]",
        "expected": ["The Postal Service", "Nothing Better"],
    },
    {
        "input": "Rose Windows - There is a Light [OFFICIAL VIDEO]",
        "expected": ["Rose Windows", "There is a Light"],
    },
    {
        "input": "Mirel Wagner - Oak Tree [OFFICIAL VIDEO]",
        "expected": ["Mirel Wagner", "Oak Tree"],
    },
    {
        "input": "clipping. - Work Work (feat. Cocc Pistol Cree) [OFFICIAL VIDEO]",
        "expected": ["clipping.", "Work Work"],
    },
    {
        "input": "Dum Dum Girls - Rimbaud Eyes [OFFICIAL VIDEO]",
        "expected": ["Dum Dum Girls", "Rimbaud Eyes"],
    },
    {
        "input": "The Head and the Heart - Summertime [OFFICIAL VIDEO]",
        "expected": ["The Head and the Heart", "Summertime"],
    },
    {
        "input": "Shabazz Palaces - They Come In Gold (not the video)",
        "expected": ["Shabazz Palaces", "They Come In Gold"],
    },
    {
        "input": "Lee Bains III & The Glory Fires - The Weeds Downtown (not the video)",
        "expected": ["Lee Bains III & The Glory Fires", "The Weeds Downtown"],
    },
    {
        "input": "Constantines - Young Lions (not the video)",
        "expected": ["Constantines", "Young Lions"],
    },
    {
        "input": "The Afghan Whigs - The Lottery (not the video)",
        "expected": ["The Afghan Whigs", "The Lottery"],
    },
    {"input": "Luluc - Without a Face", "expected": ["Luluc", "Without a Face"]},
    {
        "input": "Lyla Foy - Feather Tongue [OFFICIAL VIDEO]",
        "expected": ["Lyla Foy", "Feather Tongue"],
    },
    {
        "input": "Dum Dum Girls -  Are You Okay? [OFFICIAL SHORT FILM VIDEO]",
        "expected": ["Dum Dum Girls", "Are You Okay?"],
    },
    {
        "input": "THUMPERS - Lungs (Originally Performed by Chvrches) [not the video]",
        "expected": ["THUMPERS", "Lungs"],
    },
    {
        "input": "Washed Out - All I Know [Moby Remix] (not the video)",
        "expected": ["Washed Out", "All I Know"],
    },
    {
        "input": "Goat - Dreambuilding (not the video)",
        "expected": ["Goat", "Dreambuilding"],
    },
    {
        "input": "Lee Bains III & The Glory Fires - The Company Man (not the video)",
        "expected": ["Lee Bains III & The Glory Fires", "The Company Man"],
    },
    {
        "input": "The Afghan Whigs - Algiers [OFFICIAL VIDEO]",
        "expected": ["The Afghan Whigs", "Algiers"],
    },
    {
        "input": 'Shearwater - Black Is The Color  (from the "Colors" episode of Radiolab)',
        "expected": [
            "Shearwater",
            'Black Is The Color',
        ],
        "skip": True,
    },
    {
        "input": "The Notwist - Kong [OFFICIAL VIDEO]",
        "expected": ["The Notwist", "Kong"],
    },
    {
        "input": "Death Vessel - Mercury Dime [OFFICIAL VIDEO]",
        "expected": ["Death Vessel", "Mercury Dime"],
    },
    {
        "input": "The Ruby Suns - Desert Of Pop [OFFICIAL VIDEO]",
        "expected": ["The Ruby Suns", "Desert Of Pop"],
    },
    {
        "input": "THUMPERS - Unkinder (A Tougher Love) [OFFICIAL VIDEO]",
        "expected": ["THUMPERS", "Unkinder"],
    },
    {
        "input": "Chad VanGaalen - Where Are You?",
        "expected": ["Chad VanGaalen", "Where Are You?"],
    },
    {
        "input": "Mogwai - The Lord Is Out Of Control [OFFICIAL VIDEO]",
        "expected": ["Mogwai", "The Lord Is Out Of Control"],
    },
    {
        "input": "Lyla Foy -  Impossible [OFFICIAL PERFORMANCE VIDEO]",
        "expected": ["Lyla Foy", "Impossible"],
    },
    {
        "input": "Death Vessel - Ilsa Drown (feat. Jónsi) [not the video]",
        "expected": ["Death Vessel", "Ilsa Drown"],
    },
    {
        "input": "The Notwist - Close To The Glass (not the video)",
        "expected": ["The Notwist", "Close To The Glass"],
    },
    {
        "input": "Dum Dum Girls - Lost Boys And Girls Club [OFFICIAL VIDEO]",
        "expected": ["Dum Dum Girls", "Lost Boys And Girls Club"],
    },
]


class TestSequence(with_metaclass(MetaTestSequence, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
