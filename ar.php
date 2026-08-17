<?php
// 1:IndexedArray
echo "<fontcolor="green"><i>:Indexed Array</i></font><br>"."<br>";
    $a=array(0,1,2,3,4);
	echo $a[2];
	echo "<br><br>";
//2:Associative Array
echo "<fontcolor="green"><i>2:Associative Array</i></font>"."<br>";
     $a=array("zero"=>0,"one"=>1,"two"=>2,"three"=>3,"four"=>4);
     echo $a["two"];
	 echo "<br><br>";
//3:Associative Array
echo "<fontcolor="green"><i>3:Associative Array</i></font>"."<br>";
    $a=array("tokyo"=>"japan","Mexico City"=>"Mexico","New York"=>"USA","Mubai"=>"India",
	"Seoal"=>"Korea","Shanghai"=>"China","Lagos"=>"Nigeria","Buenos Aires"=>"Argentina","Cairo"=>"Egypt",
	"London"=>"England"); 
	foreach($a as $city=>$country)
	{
		echo $city."is in".$country."<br>";
	}
	  echo "<br><br>";
//4:Index/Numeric Array
echo "<fontcolor="green"><i>4:Index/Numeric Array</i></font>"."<br>";
    $a =array("atmiya","Christ","DDIT","ROLLWALA","Marwadi","RK");
	foreach($a as $collage)
	{
		echo "<li>$collage </li>";
	}
	 echo "<br><br>";
//5:Normal Array
echo "<fontcolor="green"><i>5:Normal Array</i></font>"."<br>";
	 $color=array("white","green","red");
	 sort($color);
	 foreach($color as $c)
	 {
		 echo "<li>$c</li>";
	 }
	 echo "<br><br>";
	 
//6:MultiDimensional Array
echo "<fontcolor="green"><i>6:MultiDimensional Array</i></font>"."<br>";
    $marks=array("Bipin"=>array("maths"=>45,"physics"=>40,"Chemistry"=>42),
	         "Ravi"=>array("maths"=>40,"physics"=>40,"Chemistry"=>40),
			 "Amit"=>array("maths"=>50,"physics"=>45,"Chemistry"=>48)
	         );
	echo "Marks for Bipin in Maths:";
    echo $marks['Bipin']['maths']."<br>";	
	echo "Marks for Ravi in physics:";
    echo $marks['Ravi']['physics']."<br>";
	echo "Marks for Amit in :";
    echo $marks['Amit']['Chemistry']."<br>";
	
	echo "<pre>";
	print_r($marks);
			 
?>