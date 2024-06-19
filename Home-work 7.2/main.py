def correct_sentence(text):
    sentences = text.split('. ')
    corrected_sentences = []

    for sentence in sentences:
        if sentence:
            corrected_sentence = sentence[0].upper() + sentence[1:]
            if not corrected_sentence.endswith('.'):
                corrected_sentence += '.'
            corrected_sentences.append(corrected_sentence)

    return ' '.join(corrected_sentences)


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
