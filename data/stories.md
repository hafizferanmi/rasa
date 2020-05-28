## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## hungry local happy path
* greet
 - utter_greet
* mood_hungry
 - utter_which_dish
* select_local_dish
 - utter_which_local_dish
* select_which_local_dish
 - utter_order_completed
* goodbye
 - utter_goodbye

## hungry international happy path
* greet
 - utter_greet
* mood_hungry
 - utter_which_dish
* select_international_dish
 - utter_which_international_dish
* select_which_international_dish
 - utter_order_completed
* goodbye
 - utter_goodbye

## Election details submission
* register_for_election
  - user_details_form
  - form{"name": "user_details_form"}
  - form{"name": null}
  - utter_goodbye

## Request gadget
* buy_gadget
  - action_request_action

## tell name path
* tell_name
  <!-- - user_name_form -->

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
