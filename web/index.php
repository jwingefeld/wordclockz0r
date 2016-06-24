<?php require("config.inc.php"); ?>

<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The Wordclockz0r</title>
  <link rel="stylesheet/less" type="text/css" href="less/base.less">
  <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
  <script src="js/less.min.js" type="text/javascript"></script>
  <script src="js/jquery-1.10.2.js"></script>

</head>

<body>

<script src="js/script.js" type="text/javascript"></script>
<div class="content">
  <div class="progressbar">
    <span class="progress full" onclick="switchto(0);">Welcome</span><span class="progress"  onclick="switchto(1);">Font</span><span class="progress" onclick="switchto(2);">Features</span><span class="progress" onclick="switchto(3);">Size</span><span class="progress" onclick="switchto(4);">Done!</span>
  </div>
  <form id="contentform">
  	<div class="segments" id="segments">
      <div class="segmentwrapper">
    		<div id="welcome" class="segment">
          <span class="quote">Yo dawg. We heard you like generators<br />so we put a generator in your generator<br />so you can generate your wordclockgenerators</span>
          <input type="button" class="button" onclick="switchto(1);" value="ok, cool" />
        </div>
    		<div id="font" class="segment">
          <div class="title">Please select the font of your wordclock:</div>
          <?php
          for ($i=0;$i <= 5; $i++) {
            echo "<div class=\"option\"><label for=\"font-$i\"><img src=\"images/lang-$i.png\" /></label><br /><input type=\"radio\" name=\"font\" id=\"font-$i\" value=\"$i\"/><label for=\"font-$i\"></label><br /></div>";
          }
          ?>
        </div>
    		<div id="features" class="segment">
          <div class="title">Please select the features of your wordclock:</div>

          <?php
          $label="time";
          echo "<div class=\"option\"><label for=\"feature-$label\"><img src=\"images/feature-$label.png\" /></label><br /><input type=\"checkbox\" name=\"feature-$label\" id=\"feature-$label\" disabled=disabled selected=selected /><label for=\"feature-$label\"> Time</label><br /></div>";
          $label="date";
          echo "<div class=\"option\"><label for=\"feature-$label\"><img src=\"images/feature-$label.png\" /></label><br /><input type=\"checkbox\" name=\"feature-$label\" id=\"feature-$label\" disabled=disabled selected=selected /><label for=\"feature-$label\"> Date</label><br /></div>";
          $label="moonphase";
          echo "<div class=\"option\"><label for=\"feature-$label\"><img src=\"images/feature-$label.png\" /></label><br /><input type=\"checkbox\" name=\"feature-$label\" id=\"feature-$label\" disabled=disabled selected=selected /><label for=\"feature-$label\"> Moonphase</label><br /></div>";

           ?>
        </div>
    		<div id="size" class="segment">
          4
        </div>
    		<div id="summary" class="segment">
          5
        </div>
    	</div>
    </div>
  </form>
</div>
</body>
</html>
