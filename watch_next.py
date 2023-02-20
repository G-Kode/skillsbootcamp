import spacy

nlp = spacy.load('en_core_web_md')

movie_list = [] # List which stores each line from the movie file.
similarity_list = [] # List which stores the similarity figures.

hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
    the Illuminati trick Hulk into a shuttle and launch him into space into a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

with open('movies.txt', 'r') as f: # Open the file in read mode
    file_lines = f.readlines() # Split each line of the file
    for line in file_lines:
        movie_list.append(line) # Add each seperated movie to the list.

# Function to find the most similar movie
def rec_movie():
    model_sentence = nlp(hulk)
    # Iterate through the movie list and find the similarity compared the the Hulk description.
    for description in movie_list:
        similarity = nlp(description).similarity(model_sentence)
        similarity_list.append(similarity) # Add each similarity to the list

    highest = similarity_list[0] # Initialize the highest similarity to the first figure within the list.

    # Iterate through the list of figures and find the largest number
    for position, similarity in enumerate(similarity_list):
        if similarity > highest:
            highest = similarity
            current_pos = position # Once the largest figure is found, store the curennt position within the list

    result = movie_list[current_pos].split(':') # Finds the matching movie with the highest similarity and splits the title and description.

    print(f'If you have watched Planet Hulk, you should watch {result[0]}next!') # Output the result

rec_movie()