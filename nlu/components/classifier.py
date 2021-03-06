from nlu.pipe_components import SparkNLUComponent
class Classifier(SparkNLUComponent):
    def __init__(self, component_name='sentiment_dl', language='en', component_type='classifier', get_default=True ,model = None,sparknlp_reference =''):
        if 'e2e' in component_name or 'toxic' in component_name :
            component_name='multi_classifier'
            SparkNLUComponent.__init__(self, component_name, component_type)
        elif 'classifierdl' in sparknlp_reference.split('_')[0] and get_default==False :
            component_name='classifier_dl'
            SparkNLUComponent.__init__(self, 'classifier_dl', component_type)
        elif 'sentimentdl' in sparknlp_reference.split('_')[0]:
            SparkNLUComponent.__init__(self, 'sentiment_dl', component_type)
            component_name='sentiment'
        elif 'vivekn' in component_name or 'vivekn' in sparknlp_reference :
            component_name='vivekn_sentiment'
            SparkNLUComponent.__init__(self, component_name, component_type)
        elif 'wiki_' in component_name or 'wiki_' in sparknlp_reference :
            component_name='language_detector'
            SparkNLUComponent.__init__(self, component_name, component_type)


        else : SparkNLUComponent.__init__(self, component_name, component_type)

        
        if model != None : self.model = model
        else :
            if 'sentiment' in component_name and 'vivekn' not in component_name:
                from nlu import SentimentDl
                if get_default : self.model = SentimentDl.get_default_model()
                else : self.model = SentimentDl.get_pretrained_model(sparknlp_reference,language)
            elif 'vivekn' in component_name:
                from nlu import ViveknSentiment
                if get_default : self.model = ViveknSentiment.get_default_model()
                else : self.model = ViveknSentiment.get_pretrained_model(sparknlp_reference, language)
            elif 'ner' in component_name or 'ner.dl' in component_name:
                from nlu import NERDL
                if get_default : self.model = NERDL.get_default_model()
                else : self.model = NERDL.get_pretrained_model(sparknlp_reference,language)
            elif 'ner.crf' in component_name:
                from nlu import NERDLCRF
                if get_default : self.model = NERDLCRF.get_default_model()
                else : self.model = NERDLCRF.get_pretrained_model(sparknlp_reference,language)
            elif 'multi_classifier' in component_name:
                from nlu import MultiClassifier
                if get_default : self.model = MultiClassifier.get_default_model()
                else : self.model = MultiClassifier.get_pretrained_model(sparknlp_reference,language)

                if 'toxic' in sparknlp_reference:
                    self.model.setOutputCol("toxic")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('toxic')
                    self.component_info.name ='toxic'


                if 'e2e' in sparknlp_reference:
                    self.model.setOutputCol("e2e")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('e2e')
                    self.component_info.name ='e2e'

            elif ('classifier_dl' in component_name or component_name=='toxic') and not 'multi' in component_name:
                from nlu import ClassifierDl
                if get_default : self.model = ClassifierDl.get_default_model()
                else : self.model = ClassifierDl.get_pretrained_model(sparknlp_reference,language)



                if 'emotion' in sparknlp_reference:
                    self.model.setOutputCol("emotion")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('emotion')
                    self.component_info.name ='emotion'



                if 'trec' in sparknlp_reference:
                    self.model.setOutputCol("question")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('question')
                    self.component_info.name ='question'

                if 'fakenews' in sparknlp_reference:
                    self.model.setOutputCol("fake")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('fake')
                    self.component_info.name ='fake'


                if 'sarcasm' in sparknlp_reference:
                    self.model.setOutputCol("sarcasm")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('sarcasm')
                    self.component_info.name ='sarcasm'

                if 'spam' in sparknlp_reference:
                    self.model.setOutputCol("spam")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('spam')
                    self.component_info.name ='spam'

                if 'cyberbullying' in sparknlp_reference:
                    self.model.setOutputCol("cyberbullying")
                    self.component_info.spark_output_column_names.remove('category')
                    self.component_info.spark_output_column_names.append('cyberbullying')
                    self.component_info.name ='cyberbullying'



            elif 'language_detector' in component_name:
                from nlu import LanguageDetector
                if get_default : self.model = LanguageDetector.get_default_model()
                else: self.model = LanguageDetector.get_pretrained_model(sparknlp_reference, language)
            elif 'pos' in component_name:
                from nlu import PartOfSpeechJsl
                if get_default : self.model = PartOfSpeechJsl.get_default_model()
                else : self.model = PartOfSpeechJsl.get_pretrained_model(sparknlp_reference,language)
            elif 'yake' in component_name:
                from nlu import Yake
                self.model  = Yake.get_default_model()
