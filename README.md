# How to run the program?

1. Use `python pre_processor.py` to generate the meta.json file
2. Use `python main.py` to run the actual code


## Approach

The dictionary file is a static file which is not likely to change as it just contains the set of valid english words.
So rather than traversing through the dictionary file every time to get the desired output, it is better to convert the
file to some other data structure that would be able to save some time when we try to lookup for the anagrams.
One of the suitable data structures for this task would be a `Map` which would provide faster lookup time.
The key would be the sorted word and the value can correspond to an array of actual words that consists of the same characters
as the key but can be in different order.
For simplicity, rather than using an array I used a string storing all the words as a comma-separated string itself as that
was the desired output.

### Example

We have a word `rreun` whose anagrams we would like to search
The key for this word would be `enrru` (After sort)
The value stored corresponding to this key would represent all the anagrams and would be like `rerun, runer`
