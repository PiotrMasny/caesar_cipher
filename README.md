# Caesar cipher app

## Overwiew
Caesar cipher app is a simply Python project that has four functionalities in menu:
- encoding
- deconding
- saving
- reading

## Encoding/decoding
Those two methods are similliary but both has key validation which means that user can type only non negative integers.

## Saving
Saving functionality starts working after first operation, such as encoding, after which the user can save that encoding or decode something else. All operations are saved in memory and if the user want to exit the app, the program will ask the user if he wants to save the unsaved history. Creates the ***history.json*** file if it doesn't exist.

## Reading
This method searches for the ***history.json*** file, where the saving module saves history, and prints it.
