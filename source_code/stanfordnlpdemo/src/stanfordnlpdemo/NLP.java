//CIS 700 Term Project
//Saurabh Patel, Ojas Juneja, Ronak Bhuptani

package stanfordnlpdemo;

import java.util.Properties;

import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.neural.rnn.RNNCoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations.SentimentAnnotatedTree;
import edu.stanford.nlp.trees.Tree;
import edu.stanford.nlp.util.CoreMap;

public class NLP {
    static StanfordCoreNLP pipeline;

    public static void init() {
    	 Properties props = new Properties();
         props.put("annotators", "tokenize, ssplit, parse, sentiment");
         pipeline = new StanfordCoreNLP(props);
    }
    
    static void usingStanfordSentimentAnalysis() {
        String review = "An overly sentimental film with a somewhat "
                + "problematic message, but its sweetness and charm "
                + "are occasionally enough to approximate true depth "
                + "and grace. ";

        String sam = "Sam was an odd sort of fellow. Not prone to angry and "
                + "not prone to merriment. Overall, an odd fellow.";
        String mary = "Mary thought that custard pie was the best pie in the "
                + "world. However, she loathed chocolate pie.";
        Properties props = new Properties();
        props.put("annotators", "tokenize, ssplit, parse, sentiment");
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        Annotation annotation = new Annotation(review);
        pipeline.annotate(annotation);

        System.out.println("---sentimentText");
      
        String[] sentimentText = {"Very Negative", "Negative", "Neutral",
                "Positive", "Very Positive"};
        for (CoreMap sentence : annotation.get(
                CoreAnnotations.SentencesAnnotation.class)) {
            Tree tree = sentence.get(
                    SentimentAnnotatedTree.class);
            System.out.println("---Number of children: " + tree.numChildren());
            System.out.println("[" + tree.getChild(0) + "][" + tree.getChild(1) + "]");
            tree.printLocalTree();
            int score = RNNCoreAnnotations.getPredictedClass(tree);
            System.out.println(sentimentText[score]);
        }
    }

    public static int findSentiment(String tweet) {

    	 
        int mainSentiment = 0;
        if (tweet != null && tweet.length() > 0) {
            int longest = 0;
            Annotation annotation = pipeline.process(tweet);
            for (CoreMap sentence : annotation
                    .get(CoreAnnotations.SentencesAnnotation.class)) {
                Tree tree = sentence
                        .get(SentimentAnnotatedTree.class);
                int sentiment = RNNCoreAnnotations.getPredictedClass(tree);
                String partText = sentence.toString();
                if (partText.length() > longest) {
                    mainSentiment = sentiment;
                    longest = partText.length();
                }

            }
        }
      
        return mainSentiment;
    }
}