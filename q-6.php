<?php

$p_amount = 2500; 

$d_percent = 0;


if($p_amount > 2000) 
{
    $d_percent = 15;
} 

elseif($p_amount > 1000) 
{
    $d_percent = 10;
}

elseif($p_amount > 500)
{
    $d_percent = 5;
}

else
{
    $d_percent = 0;
	echo "Sorry ! That amount not give discount.";
}


$d_amount = ($p_amount * $d_percent) / 100;
$final_bill = $p_amount - $d_amount;


echo "Original Purchase Amount: " . $p_amount . "<br>";
echo "Discount amount: " . $d_percent . "%<br>";
echo "Total Bill Amount to Pay: " . $final_bill . "<br>";
?>