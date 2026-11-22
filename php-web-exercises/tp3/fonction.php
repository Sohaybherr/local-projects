<?php
function afficherDate($lang = "FR")
{
    $joursFR = [
        "Sunday" => "Dimanche",
        "Monday" => "Lundi",
        "Tuesday" => "Mardi",
        "Wednesday" => "Mercredi",
        "Thursday" => "Jeudi",
        "Friday" => "Vendredi",
        "Saturday" => "Samedi"
    ];

    $moisFR = [
        "January" => "Janvier",
        "February" => "Février",
        "March" => "Mars",
        "April" => "Avril",
        "May" => "Mai",
        "June" => "Juin",
        "July" => "Juillet",
        "August" => "Août",
        "September" => "Septembre",
        "October" => "Octobre",
        "November" => "Novembre",
        "December" => "Décembre"
    ];

    

    $jourAng = date("l");
    $moisAng = date("F");
    $jourNum = date("d");
    $annee = date("Y");

    if ($lang == "FR") {
        echo $joursFR[$jourAng] . " " . $jourNum . " " . $moisFR[$moisAng] . " " . $annee;
    } elseif ($lang == "EN") {
        echo $jourAng . " " . $jourNum . " " . $moisAng . " " . $annee;}
     else {
        echo date("d/m/Y");
    }
}
?>