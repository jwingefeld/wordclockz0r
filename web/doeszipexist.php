<?php
    /*
     *  checks for a certain jobid if a zip file exists and the job is finished
     */
    
    //$jobid = "2c01e54add4cd4cfa70a";
    $jobid = $_POST['jobid'];
    
    $list = glob('../jobs/'.$jobid.'/*.zip');
    
    if(sizeof($list)>0)
    {
       $result = array("status"=>"OK","url"=>'../jobs/'.$jobid);
    } else {
       $result = array("status"=>"progress");
    }
    echo json_encode($result);
    
?>
