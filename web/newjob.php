<?php

    /*creates new directory in jobs and puts a JSON encoded .txt in it
     $features = array(
            "time"=>"test_time",
            "date"=>"2016-06-23",
            "language"=>"DE"
    );
    $case = "test";
    $email = "test@email.de";*/
    
    //grab variables from POST
    //echo $_POST['features'];
    $features = $_POST['features'];
    $case = $_POST['case'];
    $email = $_POST['email'];
    
    
    //generate a unique ID
    $uniqid2 =  openssl_random_pseudo_bytes(10);
    $newjobdir = bin2hex($uniqid2);
    
    if (!file_exists($newjobdir)) {
        mkdir('../jobs/'.$newjobdir, 0755, true);
        echo 'directory '.$newjobdir.' created';
        
    $arr = array($features,"case"=>$case,"email"=>$email);
    $jsonJobString = json_encode($arr);
    $file = $newjobdir.'/jobs.txt';
    file_put_contents('../jobs/'.$file, $jsonJobString);
    }
    echo "<br>\n";
    echo 'file '.$file.' created';
    
  
    
?>
