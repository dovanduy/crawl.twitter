import twitter4j.*;
import twitter4j.auth.RequestToken;
import twitter4j.conf.ConfigurationBuilder;

import java.util.List;

public class GetTweets {
    public static void main(String[] args) {
        ConfigurationBuilder cb = new ConfigurationBuilder(); 
        TwitterFactory tf = new TwitterFactory(cb.build()); 
        Twitter twitter = tf.getInstance(); 

        // security credentials have been configured in file 
        // twitter4j.properties under current directory.
        
        // System.out.println("connected"); 

        // List<Status> ss = null; 
        // try {
        //    ss = twitter.getUserTimeline(); 

        //      System.out.println("Get user timeline:" ); 
        // for(Status s : ss) {
        //  System.out.println(s.getUser().getName() + ":" + s.getText()); 
        //     }
        // } catch (TwitterException e) {
        //    System.out.println("Get timeline: " + e + " Status Code: " + e.getStatusCode()); 
        // }

        // search tweets. 
        try {
            String qstr1 = "obama OR president OR american OR america OR says OR country OR russia OR pope OR island OR failed OR honduras OR talks OR george OR us OR usa OR syria OR strike OR attack"; 
            String qstr2 = "am OR still OR doing OR sleep OR so OR going OR tired OR bed OR awake OR supposed OR hell OR asleep OR early OR sleeping OR sleepy OR wondering OR ugh";
            String qstr3 = "haha OR lol OR :) OR funny OR :p OR omg OR hahaha OR yeah OR too OR yes OR thats OR ha OR wow OR cool OR lmao OR though OR kinda OR hilarious OR totally";
            String qstr4 = "can OR make OR help OR if OR someone OR tell OR me OR them OR anyone OR use OR makes OR any OR sense OR trying OR explain OR without OR smile OR laugh";
            String qstr5 = "la OR el OR en OR y OR del OR los OR con OR las OR se OR por OR para OR un OR al OR es OR una OR su OR mais OR este OR nuevo OR hoy"; 

            String qstrprivacy = "fuck OR sex OR sexy OR sexual OR alcohol OR wine OR beer OR drug OR drunk OR smoking OR marijuana"; 
            String qstr6 = "phone number OR address"; 
            String qstr7 = "drink OR drunk"; 
            String qstr8 = "#mh370 OR #MH370 OR MH370 OR mh370 OR malaysia airlines OR MH370 Flight Incident"; 
            String qstr9 = "#mh370 OR #MH370 OR MH370 OR mh370 "; 
            Query q = null; 
            q = new Query(qstr9); 
            // Query q = new Query(""); 
            q.setLang("en"); // only get english tweets. 
            QueryResult r = twitter.search(q); 

            for(Status s : r.getTweets()) {
                
                System.out.println(s.getUser().getScreenName() + "\t" + 
                                   s.getGeoLocation() + "\t" + 
                                   //s.getGeoLocation().getLatitude() + "\t" + 
                                   //s.getGeoLocation().getLongitude() + "\t" + 
                                   s.getCreatedAt() + "\t" + s.getText()); 
            }

        } catch (Exception e) {
            System.err.println("Error search tweets:" + e); 
        }
    }
}
