from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_tell_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('fullname')
        print('Name gotten', name)
        print('last message',tracker.latest_message)
        # text = 'Your name is {}. Is that right?'.format(name)
        text = 'Your name has been taken down, we will get back to you soon.'

        dispatcher.utter_message(text=text)
        return []

class DeviceAction(Action):

    def name(self) -> Text:
        return "action_request_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gadget = tracker.get_slot('gadget')
        print('Getting ', gadget)
        print('--------------------------------------')

        if gadget == 'phone':
          text = 'We have iPhone, Infinix, Tecno, Nokia in store, which do you like?'
        elif gadget == 'laptop':
          text = 'We have Dell, Samsung, Toshiba, Lg in store, which do you like?'
        else:
          text = 'Nice device you just selected'

        dispatcher.utter_message(text=text)
        return []

class NameForm(FormAction):

    def name(self) -> Text:
        return "user_details_form"

    @staticmethod
    def required_slots(tracker):
        return ['full_name', 'user_email', 'local_govt']
    
    def slot_mappings(self):
      return {
        'full_name': [ self.from_text(intent='name_entry') ],
        'user_email': [self.from_text(intent='email_entry') ]
        # '': [self.from_text(intent='name_entry') ],
        # 'full_name': [ self.from_entity(entity='name', intent='name_entry') ],
        # 'user_email': [ self.from_entity(entity='email', intent='email_entry') ],
        # 'local_govt': [ self.from_entity(entity='local_govt', intent='local_govt_entry') ]
      }
    
    def submit(self, dispatcher, tracker, domain):
      # text = 'Form is properly submitted'
      name = tracker.get_slot('full_name')
      print('name', name)
      email = tracker.get_slot('user_email')
      print('Email', email)
      local_govt = tracker.get_slot('local_govt')
      print ('Local govt', local_govt)
      text = 'Your name {}, and your email address is {}, and local is {}'.format(name, email, local_govt)
      dispatcher.utter_message(text=text)
      return []
