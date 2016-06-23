<?php

    /*creates new directory in jobs and puts a JSON encoded .txt in it
     * it returns status success and the job id or an error
     *
     
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
    $frameSize = $_POST['frameSize'];
    $font = $_POST['font'];
    $email = $_POST['email'];
    
    
    //generate a unique ID
    $uniqid2 =  openssl_random_pseudo_bytes(10);
    $newjobdir = bin2hex($uniqid2);
    
    if (!file_exists($newjobdir)) {
        mkdir('../jobs/'.$newjobdir, 0755, true);
        //echo 'directory '.$newjobdir.' created';
        
    $arr = array($features,"frameSize"=>$frameSize,"font"=>$font,"email"=>$email);
    $jsonJobString = json_encode($arr);
    $file = $newjobdir.'/jobs.json';
    file_put_contents('../jobs/'.$file, $jsonJobString);
        
        $result = array("status"=>"success","jobid"=>$newjobdir);
        echo json_encode($result);
    //echo "<br>\n";
    //echo 'file '.$file.' created';
    } else {
        echo "error::jobid directory exists";
    }
  
    
?>
