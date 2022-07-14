import json

NEXTA = {"id": -1001413275904, "type" : "image"}
ZERKALO = {"id": -1001078868616, "type" : "image"}
ZERKALO_VYBORY_SMOTRI = {"id": -1001353067021, "type" : "image"}
CYNIC = {"id": -1001412170631, "type" : "text"}
ME = {"id": "me", "type" : "text"}
ZMAGARILLA = {"id": -1001435494534, "type" : "image"}
HABAROVSK = {"id" : -1001228741951, "type" : "image"}
REACTIONS = ["👍","👎","😢","🤬","😁","❤"]
REACTIONS_FULL = {'👍': 'Thumbs Up',
 '👎': 'Thumbs Down',
 '❤': 'Red Heart',
 '🔥': 'Fire',
 '🥰': 'Smiling Face with Hearts',
 '👏': 'Clapping Hands',
 '😁': 'Beaming Face',
 '🤔': 'Thinking Face',
 '🤯': 'Exploding Head',
 '😱': 'Screaming Face',
 '🤬': 'Face with Symbols on Mouth',
 '😢': 'Crying Face',
 '🎉': 'Party Popper',
 '🤩': 'Star-Struck',
 '🤮': 'Face Vomiting',
 '💩': 'Pile of Poo',
 '🙏': 'Folded Hands',
 '👌': 'Okay',
 '🕊': 'Dove of Peace',
 '🤡': 'Clown Face',
 '🥱': 'Yawning Face',
 '🥴': 'Woozy Face',
 '😍': 'Smiling Face with Heart Eyes',
 '🐳': 'Whale',
 '❤\u200d🔥': 'Heart on Fire',
 '🌚': 'New Moon Face',
 '🌭': 'Hot Dog',
 '💯': 'Hundred Points',
 '🤣': 'Rolling on the Floor Laughing',
 '😂': 'Face with Tears of Joy',
 '😭': 'Loudly Crying Face'}

class Channel:
    id : int
    __reactions : list
    def __init__(self, id):
        self.id = id
    def set_reactions(self, chat_info):
        self.__reactions = json.loads(chat_info)["full_chat"]["available_reactions"]
    def get_reactions(self):
        return self.__reactions
    reactions=property(get_reactions, set_reactions)    
