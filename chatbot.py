from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot('Buddy',
             logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. ',
                     'maximum_similarity_threshold': 1.0
                 }
             ],
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])
def trainbot(bot):
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train('chatterbot.corpus.english')

