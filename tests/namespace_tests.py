import unittest
from tests.test_utils import get_sample_pdf_with_labels, get_sample_pdf, get_sample_sdf, get_sample_pdf_with_extra_cols, get_sample_pdf_with_no_text_col ,get_sample_spark_dataframe
from nlu import *


class TestNameSpace(unittest.TestCase):

    def test_tokenize(self):
        df = nlu.load('en.tokenize').predict('What a wonderful day!')
        
        print(df)

        df = nlu.load('tokenize').predict('What a wonderful day!')
        print(df)
        

    def test_pos(self):
        df = nlu.load('en.pos').predict('What is this')
        print(df)

        df = nlu.load('pos').predict('What a wonderful day!')
        print(df)
    # 
    # def test_embed(self):
    #     # df = nlu.load('en.embed').predict('What a wonderful day!')
    #     #
    #     # print(df)
    # 
    #     df = nlu.load('embed').predict('What a wonderful day!')
    #     print(df)
    #     
    # 
    # def test_embed_glove(self):
    #     df = nlu.load('en.embed.glove').predict('What a wonderful day!')
    #     
    #     print(df)
    # 
    #     df = nlu.load('embed.glove').predict('What a wonderful day!')
    #     print(df)
    #     df = nlu.load('glove').predict('What a wonderful day!')
    #     print(df)
    # 




    def test_sentiment(self):
        df = nlu.load('en.sentiment.vivekn').predict('What a wonderful day!')

        print(df)


        df = nlu.load('en.sentiment').predict('What a wonderful day!')


        print(df)

        df = nlu.load('sentiment').predict('What a wonderful day!')
        print(df)
        

    def test_emotion(self):
        df = nlu.load('en.classify.emotion').predict('What a wonderful day!')
        
        print(df) #todo, add Alias for datasets? aka just'emotion'



    def test_spell(self):

        df = nlu.load('en.spell').predict(get_sample_pdf())

        print(df)

        df = nlu.load('spell').predict('What a wonderful day!')
        print(df)
        
    #
    def test_dependency(self): # IINFITIE LOOP RISKY
        df = nlu.load('dep', verbose=True).predict('What a wonderful day!')

        print(df)

        # df = nlu.load('en.dep').predict('What a wonderful day!')
        # print(df)

    # 
    def test_dependency_untyped(self): # IINFITIE LOOP RISKY
        df = nlu.load('dep.untyped', verbose=True).predict('What a wonderful day!')

        print(df)
        # 
    #     # df = nlu.load('en.dep.untyped').predict('What a wonderful day!')
    #     # print(df)

    # 
    def test_bert(self):
        df = nlu.load('bert').predict('What a wonderful day!')

        print(df)

    #     df = nlu.load('en.bert').predict('What a wonderful day!')
    #     print(df)

    def test_lang(self):
        df = nlu.load('lang', verbose=True).predict('What a wonderful day!')
        print(df)
        print(df.columns)
        print(df['language_de'])
        print(df['language_fr'])
        print(len(df['language_de'][0]))
        # df = nlu.load('xx.classify.lang').predict('What a wonderful day!')
        # print(df)
        # df = nlu.load('classify.lang').predict('What a wonderful day!')
        # print(df)
        # print(df)


    def test_explain(self):
        df = nlu.load('en.explain').predict('What a wonderful day!')
        print(df)
        df = nlu.load('explain').predict('What a wonderful day!')
        print(df)

    def test_ner_pipe(self):
        df = nlu.load('en.ner').predict('What a wonderful day!')

        print(df)

        df = nlu.load('ner').predict('What a wonderful day!')
        print(df)

    def test_ner_models(self):
        # THIS IS STILL A PIPE!
        df = nlu.load('en.ner.onto').predict('What a wonderful day! Arnold schwanenegger is the Terminator and he wants to get to the American chopper')
        print(df)
        # THIS IS ACTUALLY A MODEL!
        df = nlu.load('en.ner.onto.glove_6B_300d').predict('What a wonderful day!')
        print(df)


    def test_match(self):
        df = nlu.load('match.datetime').predict('What a wonderful day!')
        print(df)
        df = nlu.load('en.match.datetime').predict('What a wonderful day!')
        print(df)

    def test_clean_stop(self):
        # df = nlu.load('clean.stop').predict('What a wonderful day!')
        # print(df)
        df = nlu.load('en.clean.stop').predict('What a wonderful day!')
        print(df)


    def test_spell(self):
        df = nlu.load('spell').predict('What a wonderful day!')

        print(df)

        df = nlu.load('en.spell').predict('What a wonderful day!')

        print(df)

    # def test_all_spell(self):
        # df = nlu.load('en.spell.symmetric').predict('What a wonderful day!')
        #
        # print(df)
        #
        # df = nlu.load('en.spell.context').predict('What a wonderful day!')

        # print(df)
        # df = nlu.load('en.spell.norvig').predict('What a wonderful day!')
        # 
        # print(df)
        # df = nlu.load('spell').predict('What a wonderful day!')
        # 
        # print(df)
        # 
        # df = nlu.load('en.spell').predict('What a wonderful day!')
        # 
        # print(df)

    # def test_biobert(self):
    #     df = nlu.load('biobert').predict('What a wonderful day!')
    # 
    #     print(df)
    # 
    #     df = nlu.load('en.embed.biobert').predict('What a wonderful day!')
    #     print(df)
    # 
    # def test_elmo(self):
    #     df = nlu.load('en.embed.elmo').predict('What a wonderful day!')
    #     print(df)
    #     df = nlu.load('elmo').predict('What a wonderful day!')
    #     print(df)
    # 
    # def test_use(self):
    #     df = nlu.load('en.embed.use').predict('What a wonderful day!')
    # 
    #     print(df)
    # 
    #     df = nlu.load('use').predict('What a wonderful day!')
    #     print(df)
    # 
    # def test_albert(self):
    #     df = nlu.load('en.embed.albert').predict('What a wonderful day!')
    # 
    #     print(df)
    # 
    #     df = nlu.load('albert').predict('What a wonderful day!')
    #     print(df)
    # 
    # def test_xlnet(self):
    #     df = nlu.load('en.embed.xlnet').predict('What a wonderful day!')
    # 
    #     print(df)
    # 
    #     df = nlu.load('xlnet').predict('What a wonderful day!')
    #     print(df)

    def test_lemma(self):
        df = nlu.load('lemma').predict('What a wonderful day!')

        print(df)
        df = nlu.load('en.lemma').predict('What a wonderful day!')

        print(df)

    # def test_norm(self):
    #     df = nlu.load('lemma').predict('What a wonderful day!')
    #
    #     print(df)
    #     df = nlu.load('en.lemma').predict('What a wonderful day!')
    #
    #     print(df)
    # 
    # def test_use(self):
    #     df = nlu.load('en.embed_sentence.use').predict('What a wonderful day!')
    #     print(df)
    # 
    # def test_glove(self):
    #     df = nlu.load('nl.ner.wikiner.glove_6B_300').predict('What a wonderful day!')
    # 
    #     print(df)

    def test_sentence_detector(self):
        df = nlu.load('sentence_detector', verbose=True).predict('What a wonderful day! Tomorrow will be even better!')

        print(df)

    def test_stopwords(self):
        df = nlu.load('match.chunk').predict('What a wonderful day!')
        print(df)

    def test_classify_lang(self):
        df = nlu.load('xx.classify.wiki_7').predict('What a wonderful day!')
        print(df)

    def test_sentiment_on_datasets(self):
        df = nlu.load('sentiment.twitter').predict('What a wonderful day!')
        print(df)
        # df = nlu.load('sentiment.imdb').predict('What a wonderful day!')
        # print(df)

    def test_multiple_nlu_references(self):
        # df = nlu.load('elmo bert').predict('What a wonderful day!')
        df = nlu.load('elmo').predict('What a wonderful day!')

        print(df)
        # df = nlu.load('sentiment.imdb').predict('What a wonderful day!')
        # print(df)
        
    def test_sentiment_output(self):
        res = nlu.load('sentiment',verbose=True).predict('Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')
        
        print(res)
        print(res['sentiment'])

        print(res.dtypes)
        
    def test_pdf_column_prediction(self):
        pdf = get_sample_pdf()
        res = nlu.load('sentiment',verbose=True).predict(pdf['text'], output_level='sentence')
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')

        print(res)
        print(res['sentiment'])

        print(res.dtypes)

    def test_pdf_prediction_with_additional_cols(self):
        # TODO case if input column names overlap with output column names not handeld!
        pdf = get_sample_pdf_with_extra_cols()
        res = nlu.load('pos',verbose=True).predict(pdf)
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')

        print(res)
        print(res['pos'])

        print(res.dtypes)

    def test_bad_data_input(self):
        pdf = get_sample_pdf_with_no_text_col()
        res = nlu.load('sentiment',verbose=True).predict(pdf, output_level='sentence')
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')

        print(res)


    def test_spark_dataframe_input(self):
        sdf = get_sample_spark_dataframe()
        res = nlu.load('sentiment',verbose=True).predict(sdf, output_level='sentence')
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')

        print(res)

    def test_bad_component_reference(self):
        sdf = get_sample_spark_dataframe()
        res = nlu.load('asdasj.asdas',verbose=True).predict(sdf, output_level='sentence')
        # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')

        print(res)

    def test_stem(self):
        pdf = get_sample_pdf()
        res = nlu.load('stem',verbose=True).predict(pdf )
        print(res)
        res = nlu.load('en.stem',verbose=True).predict(pdf)
        print(res)

    def test_norm(self):
        pdf = get_sample_pdf()
        res = nlu.load('norm',verbose=True).predict(pdf, output_positions=True )
        print(res)
        # res = nlu.load('en.norm',verbose=True).predict(pdf)
        # print(res)

    def test_chunk(self):
        pdf = get_sample_pdf()
        res = nlu.load('chunk',verbose=True).predict(pdf )
        print(res)
        res = nlu.load('en.chunk',verbose=True).predict(pdf)
        print(res)

    def test_ngram(self):
        pdf = get_sample_pdf()
        # res = nlu.load('ngram',verbose=True).predict(pdf )
        pipe = nlu.load('ngram',verbose=True)
        # print(res['ngrams'])
        print("PIPE", pipe)
        res = nlu.load('en.ngram',verbose=True).predict(pdf)
        print(res['ngrams'])
    

    def test_chunk_embeds(self):
        pdf = get_sample_pdf()
        res = nlu.load('embed_chunk',verbose=True).predict("What a wondful day!" )
        print(res)
        res = nlu.load('en.embed_chunk',verbose=True).predict(pdf)
        print(res)

    def test_regex_matcher(self):
        pdf = get_sample_pdf()
        res = nlu.load('match.regex',verbose=True).predict(pdf )
        print(res)

    def test_text_matcher(self):
        pdf = get_sample_pdf()
        res = nlu.load('match.text',verbose=True).predict(pdf )
        print(res)

    def test_auto_sentence_embed_bert(self): # TODO 
        pdf = get_sample_pdf()
        res = nlu.load('embed_sentence.bert',verbose=True).predict(pdf )
        print(res)

    def test_auto_sentence_embed_elmo(self): # TODO  
        pdf = get_sample_pdf()
        res = nlu.load('embed_sentence.elmo',verbose=True).predict(pdf )
        print(res)
        
        
    # def test_bad_pandas_column_datatype(self):
    #     sdf = get_sample_spark_dataframe()
    #     res = nlu.load('asdasj.asdas',verbose=True).predict(sdf, output_level='sentence')
    #     # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')
    # 
    #     print(res)
    # 
    # def test_bad_pandas_dataframe_datatype(self):
    #     sdf = get_sample_spark_dataframe()
    #     res = nlu.load('asdasj.asdas',verbose=True).predict(sdf, output_level='sentence')
    #     # res = nlu.load('bert',verbose=True).predict('@Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.', output_level='sentence')
    # 
    #     print(res)

if __name__ == '__main__':
    unittest.main()

