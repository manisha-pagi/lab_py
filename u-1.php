
<?php

   $a=$_GET['v1'];
   $b=$_GET['v2'];
   
   function operation($a,$b)
   {
	    echo "Addtion of Value-1 & value-2 :".$a+$b;
		echo "<br>Subtrection of Value-1 & value-2 : ".$a-$b;
		echo "<br>Multiplication of Value-1 & value-2 : ".$a*$b;
		echo "<br>Divizion of Value-1 & value-2 : ".$a/$b;
		
   }
   operation($a,$b);
   
   


?>