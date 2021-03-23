<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Massimo Vassalli">

    <title>Nanoengineering for Mechanobiology 2018</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts for this template -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Cabin:700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <!-- Custom styles for this template -->
    <link href="css/program.css" rel="stylesheet">

  </head>
<?php
    function speach($time,$name,$title){
        echo '<tr><td width="200">'.$time.'</td><td width="300">'.$name.'</td><td class="text-left">'.$title.'</td></tr>';
        echo '<tr><td></td><td>Question time</td><td></td></tr>';
    }
    function coffee($time,$type = 'coffee'){
        $name = 'Coffee break';
        if ($type=='lunch'){
            $name='Lunch';
        }else if($type=='poster'){
            $name='POSTER session';
        }
        echo '<tr><td>'.$time.'</td><td class="coffee">'.$name.'</td><td></td></tr>';
    }
    function block($time,$name,$where='Cassiopea Room'){
          //echo '<div class="row"><div class="col-lg-1 time">'.$time.'</div><div class="col-lg-3 coffee">'.$name.'</div><div class="col-lg-8 title">'.$where.'</div></div>';          
        echo '<tr> <td class="time" width="200">'.$time.'</td><td class="name coffee">'.$name.'</td><td class="where" width="200">'.$where.'</td> </tr>';
    }
    function blocktitle($title){
        echo '<tr> <th colspan="3" class="text-center table-secondary">'.$title.'</th> </tr>';
    }
    function blockhead($time,$name,$where){
        echo '<table class="table table-bordered"><thead><tr>';
        echo '<tr> <th class="text-center">'.$time.'</th><th class="text-center">'.$name.'</th><th class="text-center">'.$where.'</th> </tr>';
        echo '</tr></thead><tbody>';
    }
    function blockfooter(){
        echo '</tbody></table>';
    }
      
?>
  <body id="page-top">
<div class="container text-center">
      
      <h1>Nanoengineering for Mechanobiology</h1>
      <h3>Camogli, March 25-28 2018</h3>
      
      
      <h2>Meeting program</h2>
      
    
        
      <?php 
        
        blockhead('Time','Activity','Location');
        
        blocktitle('Sunday 25/03/2018');
        block('19:00-20:00','Welcome cocktail');
        block('> 20:00','Free time for dinner and leisure','');
        
        blocktitle('Monday 26/03/2018');
        block('8:30-9:00','Registration','Cassiopea anteroom');
        block('9:00-13:00','Session 1');
        block('13:00-14:00','Lunch','Restaurant');
        block('14:00-15:00','Poster session','Syrius Room');
        block('15:00-19:00','Session 2');
        block('> 19:00','Free time for dinner and leisure','');
        
        blocktitle('Tuesday 27/03/2018');
        block('9:00-13:00','Session 3');
        block('13:00-14:00','Lunch','Restaurant');
        block('14:00-15:00','Poster session','Syrius Room');
        block('15:00-19:00','Session 4');
        block('> 19:00','Free time for dinner and leisure','');

        blocktitle('Wednesday 28/03/2018');
        block('9:00-13:00','Session 5');
        block('13:00-14:00','Lunch','Restaurant');
    
        blockfooter();
      ?>
        
      <h2>Scientific Program</h2>
    
<?php 
      blockhead('Time','Speaker','Title');
        
      blocktitle('Session 1: Monday 26/03/2018 9:00-13:00');
      speach('9:00-9:30','Aldo Ferrari and Massimo Vassalli','Introduction');
      $json = file_get_contents('http://n4m2018.mechanobiology.eu/webservices/json.php?session=1');
      $jsonlist = json_decode ($json,true)['data']; 
      $time = array(0=>'9:30-10:00',1=>'10:15-10:35',3=>'11:15-11:45',4=>'12:00-12:20',5=>'12:30-12:50');
      for($y = 0; $y <= 5; $y++){        
        if ($y != 2){
            $author = $jsonlist[$y]['author'];
            $title = $jsonlist[$y]['title'];
            //$abstract = $jsonlist[$y]['abstract'];
            speach($time[$y],$author,$title);
            if ($y==1){
                coffee('10:45-11:15');               
            }
        }
      }
      
      $time = array('morning'=>array(0=>'9:00-9:30',1=>'9:45-10:05',2=>'10:15-10:35',3=>'10:45-11:15',4=>'11:15-11:45',5=>'12:00-12:20',6=>'12:30-12:50'),
      'afternoon' => array(0=>'15:00-15:30',1=>'15:45-16:05',2=>'16:15-16:35',3=>'16:45-17:15',4=>'17:15-17:45',5=>'18:00-18:20',6=>'18:30-18:50'));
      $timing=['morning'=>'9:00-13:00','afternoon'=>'15:00-19:00'];
      
      //session2
      $half='afternoon';
      $session=2;
      blocktitle( 'Session 2: Monday 26/03/2018 '.$timing[$half]);
      $json = file_get_contents('http://n4m2018.mechanobiology.eu/webservices/json.php?session='.$session);
      $jsonlist = json_decode ($json,true)['data']; 
      $now = $time[$half];
	  $h=0;
      for($y = 0; $y <= 6; $y++){        
        if ($y==3){
            coffee($now[$y]);
        }else{
            $author = $jsonlist[$h]['author'];
            $title = $jsonlist[$h]['title'];
            speach($now[$y],$author,$title);
			$h+=1;
        }
      }
      
      //session3
      $half='morning';
      $date = 'Tuesday 27/03/2018';
      $session=3;
      blocktitle('Session '.$session.': '.$date.' '.$timing[$half]);
      $json = file_get_contents('http://n4m2018.mechanobiology.eu/webservices/json.php?session='.$session);
      $jsonlist = json_decode ($json,true)['data']; 
      $now = $time[$half];
	  $h=0;
      for($y = 0; $y <= 6; $y++){        
        if ($y==3){
            coffee($now[$y]);
        }else{
            $author = $jsonlist[$h]['author'];
            $title = $jsonlist[$h]['title'];
            speach($now[$y],$author,$title);
			$h+=1;
        }
      }
      
      //session4
      $half='afternoon';
      $date = 'Tuesday 27/03/2018';
      $session=4;
      blocktitle( 'Session '.$session.': '.$date.' '.$timing[$half]);
      $json = file_get_contents('http://n4m2018.mechanobiology.eu/webservices/json.php?session='.$session);
      $jsonlist = json_decode ($json,true)['data']; 
      $now = $time[$half];
	  $h=0;
      for($y = 0; $y <= 6; $y++){        
        if ($y==3){
            coffee($now[$y]);
        }else{
            $author = $jsonlist[$h]['author'];
            $title = $jsonlist[$h]['title'];
            speach($now[$y],$author,$title);
			$h+=1;
        }
      }
      
      //session4
      $half='morning';
      $date = 'Wednesday 28/03/2018';
      $session=5;
      blocktitle( 'Session '.$session.': '.$date.' '.$timing[$half]);
      $json = file_get_contents('http://n4m2018.mechanobiology.eu/webservices/json.php?session='.$session);
      $jsonlist = json_decode ($json,true)['data']; 
      $now = $time[$half];
	  $h=0;
      for($y = 0; $y <= 6; $y++){        
        if ($y==3){
            coffee($now[$y]);
        }else{
            $author = $jsonlist[$h]['author'];
            $title = $jsonlist[$h]['title'];
            speach($now[$y],$author,$title);
			$h+=1;
        }
      }
    
      blockfooter();
?>
    
    
    
      <h2>Oral contributions</h2>
      
<?php      
$db = new SQLite3('dbAbstract.sqlite');
$results = $db->query("SELECT * FROM abstracts where Contribution='T' order by Lastname");      
while ($row = $results->fetchArray()) {
    echo '<h3 class="abstitle">'.$row['Title'].'</h3>';
    echo '<div class="absauthor">'.$row['Firstname'].' '.$row['Lastname'].'</div>';
    echo '<div class="absaffiliation">'.$row['Deparment'].', '.$row['Institution'].', '.$row['City'].' ('.$row['Country'].')</div>';
    echo '<div class="absmail">'.$row['Email'].'</div>';
    echo '<div class="abstract">'.$row['Abstract'].'</div>';
}
echo '<h2>Poster contributions</h2>';

$results = $db->query("SELECT * FROM abstracts where Contribution='P' order by Lastname");      
while ($row = $results->fetchArray()) {
    echo '<h3 class="abstitle">'.$row['Title'].'</h3>';
    echo '<div class="absauthor">'.$row['Firstname'].' '.$row['Lastname'].'</div>';
    echo '<div class="absaffiliation">'.$row['Deparment'].', '.$row['Institution'].', '.$row['City'].' ('.$row['Country'].')</div>';
    echo '<div class="absmail">'.$row['Email'].'</div>';
    echo '<div class="abstract">'.$row['Abstract'].'</div>';
}    
?>
      
    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/popper/popper.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for this template -->
    <script src="js/grayscale.min.js"></script>
      </div>
  </body>

</html>
